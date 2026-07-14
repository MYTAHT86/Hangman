import random
def start_game():
    def five_mistakes_left():
        ris = [
        " __________",
        "|          ",
        "|          ",
        "|          ",
        "|          ",
        "|          ",
    ]
        return "\n".join(ris)


    def four_mistakes_left():
        ris = [
        " __________",
        "|     О/   ",
        "|          ",
        "|          ",
        "|          ",
        "|          ",
    ]
        return "\n".join(ris)


    def three_mistakes_left():
        ris = [
        " __________",
        "|     О/   ",
        "|     |    ",
        "|          ",
        "|          ",
        "|          ",
    ]
        return "\n".join(ris)


    def two_mistakes_left():
        ris = [
        " __________",
        "|     О/   ",
        "|     |    ",
        "|    /|\\  ",
        "|          ",
        "|          ",
    ]
        return "\n".join(ris)


    def one_mistakes_left():
        ris = [
        " __________",
        "|     О/   ",
        "|     |    ",
        "|    /|\\  ",
        "|     |    ",
        "|          ",
    ]
        return "\n".join(ris)
    def zero_mistakes_left():
        ris = [
        " __________",
        "|     О/   ",
        "|     |    ",
        "|    /|\\  ",
        "|     |    ",
        "|    / \\  ",
    ]
        return "\n".join(ris)

    dict_mistakes = {
    5: five_mistakes_left(),
    4: four_mistakes_left(),
    3: three_mistakes_left(),
    2: two_mistakes_left(),
    1: one_mistakes_left(),
    0: zero_mistakes_left()
}
    with open("dict.txt", encoding="utf-8") as file:
        word = random.choice(file.readlines()).rstrip()
    user_word = '_' * len(word)
    tries = 5
    used_letters = []
    print(user_word)
    print()
    print("Введите букву")
    while user_word != word and tries != -1:
        letter = input().lower()
        if letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" and letter in word:
            cur_li = [c for c in word]
            cur_user = [c for c in user_word]
            for i in range(len(cur_li)):
                if cur_li[i] == letter:
                    cur_user[i] = letter
                    user_word = "".join(cur_user)
            print(user_word)
            print()
        elif letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" and letter not in word:
            if letter in used_letters:
                print("Данная буква уже вводилась")
                continue
            print()
            print(f"Введенной буквы в слове нет. У вас осталось {tries} попыток")
            print(user_word)
            print(dict_mistakes[tries])
            print()
            used_letters.append(letter)
            tries -= 1
        elif letter not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
            print('Введите букву из кириллицы')
    if tries == -1:
        print()
        print(f"Вы проиграли, загаданное слово {word}. Хотите попробовать еще раз? Введите N для Новой игры и E для выхода")
        return
    else:
        print("Вы победили! Хотите попробовать еще раз? Введите N для Новой игры и E для выхода")
        return
    
print("Добро пожаловать в игру Виселица. Нажмите N для старта игры")
while True:
    start_button = input()
    if start_button in ('n', 'N', 'Т', 'т'):
        start_game()
        break
    else:
        print("Введен неверный символ, попробуйте еще раз")
while True:
    button = input()
    if button in ('n', 'N', 'Т', 'т'):
        start_game()
    elif button in ('e', 'E', 'У', 'у'):
        print('Игра завершена')
        break
    else:
        print('Введен неверный символ, попробуйте еще раз')
