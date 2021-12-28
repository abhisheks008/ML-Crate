from fuzzywuzzy import fuzz


def validation(g, a, r):
    while g:
        g = str(g).lower()
        a = str(a).lower()
        g, a = clean_chars(g, a)
        g, warn = check_prefix(g, r)
        a = split_answer(a)
        if not final_check(g, a):
            return False
        return True
    return False


def check_prefix(g, r):
    prefix = ['what is ', 'who is ', 'where is ', 'what are ', 'who are ', 'where are ']
    for ans in prefix:
        if g.lower().startswith(ans):
            return g.replace(ans, ''), False
    if r == 'Jeopardy!':
        return g, True
    else:
        return False, False


def clean_chars(g, a):
    g = g.translate({ord(i): None for i in "\"?!@#$%^&*()-_=+/\\[]{};:`~"})
    a = a.replace('&', 'and')
    a = a.replace(' acceptable)', '')
    a = a.replace(' accepted)', '')
    a = a.translate({ord(i): None for i in "\"?!@#$%^&*)-_=+\\[]{};:`~"})
    return g, a


def split_answer(a):
    if '(' in a:
        a = a.split('(')
    elif '/' in a:
        a = a.split('/')
    return a


def final_check(g, a):
    if isinstance(g, bool):
        return False
    elif isinstance(a, list):
        for ans in a:
            if fuzz.ratio(g.strip(), ans.strip()) > 80 or fuzz.token_set_ratio(g.strip(), ans.strip()) > 90:
                return True
    elif isinstance(g, bool):
        return False
    else:
        if fuzz.ratio(g.strip(), a.strip()) > 80 or fuzz.token_set_ratio(g.strip(), a.strip()) > 90:
            return True
    return False
