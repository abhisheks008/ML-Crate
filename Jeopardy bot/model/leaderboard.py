import sqlite3
import pandas as pd


def lifetime_leaderboard():
    with sqlite3.connect('jepbot.db') as conn:
        cur = conn.cursor()

        lb = cur.execute('''SELECT name, questions_answered, lifetime_winnings FROM user 
                            ORDER BY lifetime_winnings DESC''')

    df = pd.DataFrame(lb.fetchall(), columns=['Name', 'Questions Answered', 'Winnings']).set_index('Name')
    return df


def show_leaderboard(uid, show_num=0):
    try:
        show_num = int(show_num)
    except ValueError:
        return 'Invalid show number'
    if show_num < 0:
        return 'Invalid show number'

    with sqlite3.connect('jepbot.db') as conn:
        cur = conn.cursor()

        def most_recent_show(user):
            mrs = cur.execute(f'SELECT max(show_id) FROM show WHERE user_id = {user}')
            return mrs.fetchone()[0]

        show = cur.execute(f'''SELECT s.show_id, u.name, s.amount_won FROM show as s 
                            INNER JOIN user as u ON s.user_id = u.user_id 
                            WHERE s.show_id = {show_num if show_num > 0 else most_recent_show(uid)}''')

    # Create df to output table of players
    df = pd.DataFrame(show.fetchall(), columns=['Show', 'Player', 'Winnings']).set_index('Player')
    df.sort_values(by=['Winnings'], ascending=False, inplace=True)

    if df.empty:
        return 'No data for that show'
    else:
        return df


def recent_answers(uid, num=10):
    try:
        num = int(num)
        if num > 10:
            num = 10
    except ValueError:
        return 'Invalid number'
    if num < 1:
        return 'Invalid number'

    with sqlite3.connect('jepbot.db') as conn:
        cur = conn.cursor()

        recent = cur.execute(f'''SELECT show_id, question, answer, guess, answered_correctly, winnings_change 
                                FROM transactions WHERE user_id = {uid} ORDER BY transaction_id DESC LIMIT {num}''')

    pd.set_option('max_columns', None)
    pd.set_option('max_row', None)
    df = pd.DataFrame(recent.fetchall(), columns=['Show', 'Question', 'Answer', 'Your Guess', 'Correct Guess?', 'Winnings Change'])

    return df
