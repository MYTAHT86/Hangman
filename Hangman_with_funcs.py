import random


def start_game():
    word = make_word()
    run_game(word)


def run_game(word):
    user_word = "_" * len(word)
    tries = 5
    used_letters = []
    print()
    print(user_word)
    while user_word != word and tries != -1:
        print()
        print("Введите букву")
        letter = input().lower()
        user_word, tries = check_letter(letter, word, user_word, used_letters, tries)
    check_result(word, user_word, tries)


def make_word():
    with open("dict.txt", encoding="utf-8") as file:
        return random.choice(file.readlines()).rstrip()


def check_letter(letter, word, user_word, used_letters, tries):
    mistakes = [
        [
            " __________",
            "|     О/   ",
            "|     |    ",
            "|    /|\\  ",
            "|     |    ",
            "|    / \\  ",
        ],
        [
            " __________",
            "|     О/   ",
            "|     |    ",
            "|    /|\\  ",
            "|     |    ",
            "|          ",
        ],
        [
            " __________",
            "|     О/   ",
            "|     |    ",
            "|    /|\\  ",
            "|          ",
            "|          ",
        ],
        [
            " __________",
            "|     О/   ",
            "|     |    ",
            "|          ",
            "|          ",
            "|          ",
        ],
        [
            " __________",
            "|     О/   ",
            "|          ",
            "|          ",
            "|          ",
            "|          ",
        ],
        [
            " __________",
            "|          ",
            "|          ",
            "|          ",
            "|          ",
            "|          ",
        ],
    ]
    if letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" and letter in word:
        cur_li = [c for c in word]
        cur_user = [c for c in user_word]
        for i in range(len(cur_li)):
            if cur_li[i] == letter:
                cur_user[i] = letter
                user_word = "".join(cur_user)
        print()
        print(user_word)
        print(f"Неверные буквы: {used_letters}")
        return user_word, tries
    elif letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" and letter not in word:
        if letter in used_letters:
            print()
            print("Данная буква уже вводилась")
            return user_word, tries
        print()
        print(f"Введенной буквы в слове нет. У вас осталось {tries} попыток")
        print(user_word)
        print(*mistakes[tries], sep="\n")
        print()
        used_letters.append(letter)
        print(f"Неверные буквы: {used_letters}")
        tries -= 1
        return user_word, tries
    elif letter not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        print()
        print("Введите букву из кириллицы")
        return user_word, tries


def check_result(word, user_word, tries):
    if user_word == word:
        print()
        print(f"Вы победили! Правильное слово - {word}")
    else:
        print()
        print(f"Вы проиграли! Правильное слово - {word}")
    return


while True:
    print("Для запуска новой игры нажмите N или E для выхода")
    button = input()
    if button in ("n", "N", "Т", "т"):
        start_game()
    elif button in ("e", "E", "У", "у"):
        print("Игра завершена")
        break
    else:
        print("Введен неверный символ, попробуйте еще раз")
