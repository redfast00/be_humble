from config import recipients
from send_mail import send_mail
from humblebundle import get_free_game_names


if __name__ == '__main__':
    free_games = get_free_game_names()
    if free_games:
        with open('email_template.txt') as infile:
            content = infile.read()
        games = '\n'.join(free_games)
        send_mail(recipients, content.format(games=games))
