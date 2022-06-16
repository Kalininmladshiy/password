import string
import urwid
from functools import reduce


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(map(str.isdigit, password))


def has_letters(password):
    return any(map(str.isalpha, password))


def has_upper_letters(password):
    return any(map(str.isupper, password))


def has_lower_letters(password):
    return any(map(str.islower, password))


def has_simbols(password):
    punctuation = string.punctuation + ' '
    return any(map(lambda x: x in punctuation, password))


def reiting_password(password, *args):
    reiting = reduce(
        lambda z, y: z + y,
        map(lambda x: 0 if not x(password) else 2, args),
        0,
    )
    return reiting


def on_ask_change(edit, new_edit_text):
        reply.set_text(
            "Рейтинг вашего пароля: %s" % reiting_password(
                new_edit_text,
                is_very_long,
                has_digit,
                has_letters,
                has_upper_letters,
                has_lower_letters,
                has_simbols,
            )
        )


if __name__ == '__main__':
    ask = urwid.Edit('Введите ваш пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
