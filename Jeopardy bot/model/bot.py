import os
import discord
import asyncio
import textwrap
from dotenv import load_dotenv

import check_answer
from user import User
from leaderboard import show_leaderboard, recent_answers, lifetime_leaderboard

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.u = {}
        self.q = {}

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('---------')
        await client.change_presence(status=discord.Status.online, activity=discord.Game('This. Is. Jeopardy!'))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        # Loads the user's record from the user table
        if message.content.startswith('$load'):
            try:
                await message.channel.send('Loading new questions')
                self.u[message.author.id] = User(message.author.id, message.author.name)
                self.u[message.author.id].get_record()
            except:
                await message.channel.send('Error loading clue data')

        # Asks the next question for the user, gathers the answer, then updates all info
        if message.content.startswith('$ask'):
            def check_wager(m):
                return m.author == message.author and not message.content.startswith('$')

            # if Final Jeopardy clue, get wager
            try:
                self.q[message.author.id] = self.u[message.author.id].get_question
                if self.q[message.author.id][3] == 'Final Jeopardy!':
                    await message.channel.send(f'Final Jeopardy Category: ||{self.q[message.author.id][4]}||')
                    await message.channel.send(f'Your current show winnings are: {self.u[message.author.id].show_winnings}')
                    await message.channel.send('Place your wager now')

                    while True:
                        wager = await self.wait_for('message', check=check_wager)
                        try:
                            if 0 <= int(wager.content) <= max(int(self.u[message.author.id].show_winnings), 1000):
                                break
                            else:
                                await message.channel.send('Invalid wager, try again')
                        except ValueError:
                            await message.channel.send('Invalid, your wager should be an integer, try again')
                    winnings = int(wager.content)
                    await message.channel.send('Your Final Jeopardy clue:')

                # For non-Final Jeopardy clues, display the category and dollar amount
                else:
                    await message.channel.send(f'Category: ||{self.q[message.author.id][4]}||')
                    await message.channel.send(f'Dollar amount: {self.q[message.author.id][5]}')
                    winnings = int(self.q[message.author.id][5].replace('$', '').replace(',', ''))

                # The question being asked here
                await message.channel.send(f'||{self.q[message.author.id][6]}||')

                # Setting the correct answer, then taking the guess and comparing
                answer = self.q[message.author.id][7]
                try:
                    await asyncio.sleep(0.5)
                    guess = await self.wait_for('message', timeout=30.0, check=check_wager)
                    await asyncio.sleep(0.5)
                    await message.channel.purge(limit=1)
                except asyncio.TimeoutError:
                    if self.q[message.author.id][3] != 'Final Jeopardy!':
                        self.u[message.author.id].update_record(question=self.q[message.author.id][6], answer=answer, guess="No guess",
                                                                clue_id=self.q[message.author.id][0], show_id=self.q[message.author.id][1],
                                                                jep_round=self.q[message.author.id][3], cash=0)
                    else:
                        self.u[message.author.id].update_record(question=self.q[message.author.id][6], answer=answer, guess="No guess",
                                                                clue_id=self.q[message.author.id][0], show_id=self.q[message.author.id][1],
                                                                jep_round=self.q[message.author.id][3], cash=-winnings)
                    return await message.channel.send(f"Time's up, the correct answer is ||{answer}||")

                # Allow user to skip the question for no gain or loss without waiting the 2 minutes
                if guess.content in ['skip', 'pass', '$skip', '$pass'] and self.q[message.author.id][3] != 'Final Jeopardy!':
                    self.u[message.author.id].update_record(question=self.q[message.author.id][6], answer=answer, guess="No guess",
                                                            clue_id=self.q[message.author.id][0], show_id=self.q[message.author.id][1],
                                                            jep_round=self.q[message.author.id][3], cash=0)
                    return await message.channel.send(f"Question skipped, the correct answer is ||{answer}||")

                # Answer validation if answered and not skipped
                else:
                    result = check_answer.validation(guess.content, answer, self.q[message.author.id][3])

                    if result:
                        await message.channel.send('Correct!')
                        r, warn = check_answer.check_prefix(guess.content, self.q[message.author.id][3])
                        if warn:
                            await message.channel.send('You did not answer in the form of a question, this is only allowed in the Jeopardy! round')
                        self.u[message.author.id].update_record(question=self.q[message.author.id][6], answer=answer, guess=guess.content,
                                                                clue_id=self.q[message.author.id][0], show_id=self.q[message.author.id][1],
                                                                jep_round=self.q[message.author.id][3], cash=winnings)
                    else:
                        await message.channel.send(f'Wrong, the correct answer is ||{answer}||')
                        self.u[message.author.id].update_record(question=self.q[message.author.id][6], answer=answer, guess=guess.content,
                                                                clue_id=self.q[message.author.id][0], show_id=self.q[message.author.id][1],
                                                                jep_round=self.q[message.author.id][3], cash=-winnings)

                if self.q[message.author.id][3] == 'Final Jeopardy!':
                    await message.channel.send("Show complete, here's how you did: ")
                    await message.channel.send(f"""```{show_leaderboard(self.u[message.author.id].get_user_id)}```""")

            except KeyError:
                await message.channel.send('Please use $load to load your user data first')

        # Allows the user to check their winnings
        if message.content.startswith('$winnings'):
            try:
                await message.channel.send(f'Total lifetime winnings for {self.u[message.author.id].discord_name}: {self.u[message.author.id].winnings}')
                await message.channel.send(f'Current show winnings for {self.u[message.author.id].discord_name}: {self.u[message.author.id].show_winnings}')
            except KeyError:
                await message.channel.send('Please use $load to load your user data first')

        # Check a show leaderboard, add number after $show to display a specific show
        if message.content.startswith('$show'):
            try:
                await message.channel.send(f"""```{show_leaderboard(self.u[message.author.id].get_user_id, 
                                                                    message.content.split(' ')[1])}```""")
            except IndexError:
                await message.channel.send(f"""```{show_leaderboard(self.u[message.author.id].get_user_id)}```""")
            except KeyError:
                await message.channel.send('Please use $load to load your user data first')

        # Display lifetime winnings leaderboard
        if message.content.startswith('$overall'):
            await message.channel.send(f"""```{lifetime_leaderboard()}```""")

        # Check recent answers, add number after $recent to display that many
        if message.content.startswith('$recent'):
            try:
                await client.get_user(message.author.id).send(f"""```{recent_answers(self.u[message.author.id].get_user_id, 
                                                                                     message.content.split(' ')[1])}```""")
            except IndexError:
                await client.get_user(message.author.id).send(
                    f"""```{recent_answers(self.u[message.author.id].get_user_id)}```""")
            except KeyError:
                await message.channel.send('Please use $load to load your user data first')

        # Check best/worst show
        if message.content.startswith('$best'):
            try:
                await message.channel.send(f"""```{self.u[message.author.id].best_show}```""")

            except KeyError:
                await message.channel.send('Please use $load to load your user data first')

        if message.content.startswith('$worst'):
            try:
                await message.channel.send(f"""```{self.u[message.author.id].worst_show}```""")

            except KeyError:
                await message.channel.send('Please use $load to load your user data first')

        # Sends me a DM if a user disputes their answer
        if message.content.startswith('$dispute'):
            try:
                try:
                    await message.channel.send('Your last response will be sent for manual review')
                    await client.get_user(261512986949058560).send(f'Clue disputed by {message.author.name} - '
                                                                   f'clue id {self.u[message.author.id].day - 1}')
                except:
                    await message.channel.send("Looks like you've got nothing to dispute")
            except KeyError:
                await message.channel.send('Please use $load to load your user data first')

        # Lists all commands
        if message.content.startswith('$help'):
            await message.channel.send(textwrap.dedent("""
            List of commands: 
            $load - Loads user data, use this to load your session
            $ask - Asks a question, you only have 120 seconds to answer so be ready!
            $winnings - Check your winnings, both lifetime and for the show
            $overall - Check lifetime winnings of all players
            $show # - Check leaderboard for a specific show number. Leave blank for your most recent show.
            $recent # - Get table of recent # answers (max of 10)
            $best - Check your best show
            $worst - Check your worst show
            $dispute - If you think your answer should be correct, this will trigger a manual review
            Tips:
            If you don't know the answer, you can respond with skip or pass to move on
            When answering a question with a number, type the number rather than the word
            For example, use 10 rather than Ten
            Remember, always answer in the form of a question!
            """))

        # Debug
        if message.content.startswith('$test'):
            await message.channel.send("Hello")


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
