import random


def make_dictionary() -> str:
    with open("Dict.txt", encoding="utf-8") as file:
        return file.readlines()


def start_game(dictionary: list[str]) -> None:
    word = make_word(dictionary)
    run_game(word, tries)


def run_game(word: str, tries: int) -> None:
    user_word = "_" * len(word)
    used_wrong_letters = set()
    used_correct_letters = set()
    print()
    print(user_word)
    while user_word != word and tries != 0:
        print()
        print("Введите букву")
        letter = input().lower()
        user_word, tries, step_result = check_letter(
            letter, word, user_word, used_wrong_letters, used_correct_letters, tries
        )
        print_step_result(
            user_word, used_wrong_letters, used_correct_letters, tries, step_result
        )
    check_result(word, user_word, tries)


def make_word(dictionary: list) -> str:
    return random.choice(dictionary).rstrip()


def check_letter(
    letter: str,
    word: str,
    user_word: str,
    used__wrong_letters: set[str],
    used_correct_letters: set[str],
    tries: int,
) -> tuple[str, int]:
    if (
        letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        and letter in word
        and len(letter) == 1
        and letter != ""
    ):
        temporary_word_list = [c for c in word]
        temporary_user_word_list = [c for c in user_word]
        for i in range(len(temporary_word_list)):
            if temporary_word_list[i] == letter:
                temporary_user_word_list[i] = letter
                user_word = "".join(temporary_user_word_list)
                used_correct_letters.add(letter)
        step_result = 1
        return user_word, tries, step_result
    elif (
        letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        and letter not in word
        and len(letter) == 1
        and letter != ""
    ):
        if letter in used__wrong_letters:
            step_result = 2
            return user_word, tries, step_result
        step_result = 3
        used__wrong_letters.add(letter)
        tries -= 1
        return user_word, tries, step_result
    elif (
        letter not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        or len(letter) != 1
        or letter == ""
    ):
        step_result = 4
        return user_word, tries, step_result


def print_step_result(
    user_word: str,
    used_wrong_letters: set[str],
    used_correct_letters: set[str],
    tries: int,
    step_result: int,
) -> None:
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
    if step_result == 1:
        print()
        print(user_word)
        print(f"Неверные буквы: {', '.join(used_wrong_letters)}")
        print(f"Корректные буквы: {', '.join(used_correct_letters)}")
        return
    elif step_result == 2:
        print()
        print("Данная буква уже вводилась")
        return
    elif step_result == 3:
        print()
        print(f"Введенной буквы в слове нет. У вас осталось {tries} попыток")
        print(user_word)
        print(*mistakes[tries], sep="\n")
        print()
        print(f"Неверные буквы: {', '.join(used_wrong_letters)}")
        print(f"Корректные буквы: {', '.join(used_correct_letters)}")
        return
    elif step_result == 4:
        print()
        print("Введите букву из кириллицы")
        return


def check_result(word: str, user_word: str, tries: int) -> None:
    if user_word == word:
        print()
        print(f"Вы победили! Правильное слово - {word}")
    else:
        print()
        print(f"Вы проиграли! Правильное слово - {word}")
    return


if __name__ == "__main__":

    while True:
        dictionary = make_dictionary()
        tries = 6
        print("Для запуска новой игры нажмите N или E для выхода")
        button = input()
        if button in ("n", "N", "Т", "т"):
            start_game(dictionary)
        elif button in ("e", "E", "У", "у"):
            print("Игра завершена")
            break
        else:
            print("Введен неверный символ, попробуйте еще раз")
