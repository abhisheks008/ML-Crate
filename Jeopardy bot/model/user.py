import sqlite3
import pandas as pd
class User:
    def __init__(self, ident, discord_name):
        self.id = ident
        self.userdb = None
        self.day = None
        self.winnings = None
        self.show_winnings = None
        self.discord_name = discord_name

    def get_record(self):
        with sqlite3.connect('jepbot.db') as conn:
            cur = conn.cursor()
            cur.row_factory = lambda cursor, row: row[0]
            if self.id not in cur.execute("SELECT discord_id FROM user").fetchall():
                self.day = 1
                self.winnings = 0
                self.show_winnings = 0
                self.new_user()
            else:
                self.day = cur.execute(f"SELECT questions_answered FROM user WHERE discord_id = {self.id}").fetchone()
                self.winnings = cur.execute(f"SELECT lifetime_winnings FROM user WHERE discord_id = {self.id}").fetchone()
                self.show_winnings = cur.execute(f"SELECT show_winnings FROM user WHERE discord_id = {self.id}").fetchone()

    def new_user(self):
        with sqlite3.connect('jepbot.db') as conn:
            nu = (self.id, self.discord_name, 1, 0, 0)
            conn.cursor().execute("""INSERT INTO user(discord_id, name, questions_answered, lifetime_winnings, show_winnings)
                VALUES(?, ?, ?, ?, ?);""", nu)

    def update_record(self, question=None, answer=None, guess=None, clue_id=None, show_id=None, jep_round=None, cash=0):
        self.day = self.day + 1
        self.winnings = self.winnings + cash
        self.show_winnings = self.show_winnings + cash
        correct = True if cash > 0 else False
        with sqlite3.connect('jepbot.db') as conn:
            cur = conn.cursor()

            # Update user table with result of question
            cur.execute(f"UPDATE user SET questions_answered = {self.day} WHERE discord_id = {self.id}")
            cur.execute(f"UPDATE user SET lifetime_winnings = {self.winnings} WHERE discord_id = {self.id}")
            cur.execute(f"UPDATE user SET show_winnings = {self.show_winnings} WHERE discord_id = {self.id}")

            # Add entry to transactions table from question asked
            if clue_id is not None and show_id is not None:
                transact = (self.get_user_id, clue_id, show_id, correct, cash, question, answer, guess)
                cur.execute("""INSERT INTO transactions(user_id, clue_id, show_id, answered_correctly, winnings_change, question, answer, guess)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", transact)

            # If it was a final jeopardy clue, update the show table and reset show_winnings
            if jep_round == 'Final Jeopardy!':
                show_add = (show_id, self.get_user_id, self.show_winnings)
                cur.execute("""INSERT INTO show(show_id, user_id, amount_won)
                    VALUES(?, ?, ?);""", show_add)
                self.show_winnings = 0
                cur.execute(f"UPDATE user SET show_winnings = {self.show_winnings} WHERE discord_id = {self.id}")

    @property
    def print_record(self):
        return [self.id, self.day, self.winnings]

    @property
    def get_user_id(self):
        with sqlite3.connect('jepbot.db') as conn:
            user_id = conn.cursor().execute(f"SELECT user_id FROM user WHERE discord_id = {self.id}").fetchone()[0]
        return user_id

    @property
    def get_question(self):
        with sqlite3.connect('jepbot.db') as conn:
            q = list(conn.cursor().execute(f"SELECT * FROM clues WHERE clue_id = {self.day}").fetchall()[0])
        return q

    @property
    def best_show(self):
        with sqlite3.connect('jepbot.db') as conn:
            winnings = conn.cursor().execute(f"""SELECT show_id, amount_won FROM show 
                                                WHERE user_id = {self.get_user_id} ORDER BY amount_won DESC LIMIT 1""")

        df = pd.DataFrame(winnings.fetchall(), columns=['Show', 'Amount Won']).set_index('Show')
        if df.empty:
            return 'No shows completed'
        else:
            return df

    @property
    def worst_show(self):
        with sqlite3.connect('jepbot.db') as conn:
            winnings = conn.cursor().execute(f"""SELECT show_id, amount_won FROM show 
                                                WHERE user_id = {self.get_user_id} ORDER BY amount_won LIMIT 1""")

        df = pd.DataFrame(winnings.fetchall(), columns=['Show', 'Amount Won']).set_index('Show')
        if df.empty:
            return 'No shows completed'
        else:
            return df
