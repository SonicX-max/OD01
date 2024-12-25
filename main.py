# Алгоритм для проверки, является ли строка палиндромом:
# 1. Запрос строки от пользователя:
#    - Получить ввод от пользователя.
# 2. Подготовка строки:
#    - Удалить из строки все символы, кроме букв и цифр.
#    - Привести все символы к нижнему регистру для игнорирования регистра.
# 3. Сравнение:
#    - Сравнить строку с её перевёрнутой версией.
#    - Если строка совпадает с перевёрнутой, значит это палиндром.
# 4. Вывод результата:
#    - Вывести сообщение, является ли строка палиндромом или нет.

def is_palindrome(s):
    """
    Функция для проверки, является ли строка палиндромом.

    :param s: Строка для проверки
    :return: True, если строка является палиндромом, иначе False
    """

    clean_s = ''.join(char.lower() for char in s if char.isalnum())

    return clean_s == clean_s[::-1]


if __name__ == "__main__":
    user_input = input("Введите строку для проверки: ")

    if is_palindrome(user_input):
        print("Введённая строка является палиндромом.")
    else:
        print("Введённая строка не является палиндромом.")