import random


# WHERE I PROGRAM WHAT THE BOT WILL SAY
def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'hey (with rizz)'

    if p_message == '!rizz':
        lst = ["If I said you had a good body would you hold it against me?",
               "Are you tired? Because you’ve been running through my mind all day.",
               "Are you a cake, Because I want a piece of that.",
               "Are you a bank loan? Well, you’ve certainly got my interest.",
               "On a scale of 1 to 10, you’re a 9 and I’m the 1 you lack."]

        return random.choice(lst)

    if message == '!roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return 'Here are a list of my commands: \n!rizz \n!hello \n!roll \nuse \'?\' prefix to recieve message privately'


def handle_response(user_message):
    return None