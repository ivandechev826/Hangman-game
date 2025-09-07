import random

def read_words_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file]
        return words
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

def random_word(words):
    if not words:
        return None
    return random.choice(words)

def display_game(word, guessed_letters, attempts_left):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    print(displayed_word)
    print(f"Осталось попыток: {attempts_left}")

def play():
    filename = "words.txt"
    words = read_words_from_file(filename)

    if not words:
        print("Список слов пуст.")
        return

    word_to_guess = random_word(words)
    if not word_to_guess:
        print("Не удалось выбрать случайное слово.")
        return

    guessed_letters = set()
    attempts_left = 10

    print("Добро пожаловать в игру 'Виселица'!")

    while attempts_left > 0:
        display_game(word_to_guess, guessed_letters, attempts_left)

        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Вводить можно только одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже угадывали эту букву.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Верно!")
            all_guessed = True
            for letter in word_to_guess:
                if letter not in guessed_letters:
                    all_guessed = False
                    break
            if all_guessed:
                print("\nПоздравляем, вы угадали слово!:", word_to_guess)
                display_game(word_to_guess, guessed_letters, attempts_left)
                break
        else:
            print("Неверно!")
            attempts_left -= 1

    if attempts_left == 0:
        print("\nВы проиграли! Загаданное слово было:", word_to_guess)

def main():
    while True:
        play()
        play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if play_again == 'да':
           main()
        else:
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    try:
        with open("words.txt", "x", encoding="utf-8") as f:
            f.write("собака\n")
            f.write("кот\n")
            f.write("пайтон\n")
            f.write("самолет\n")
            f.write("игра\n")
            f.write("машина\n")
            f.write("яблоко\n")
            f.write("программирование\n")
            f.write("висельница\n")
            f.write("человек\n")
    except FileExistsError:
        print("Файл words.txt уже существует.")
    main()
