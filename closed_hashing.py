import math

# Розміри хеш-таблиць
M_DIV = 13
M_MUL = 16

# Константа методу множення
A = 0.6180339887

# Послідовність слів варіанта №15
WORDS = [
    "ХТО", "ГРОШИМА", "ВЕЛИЧАЄТЬСЯ",
    "ТОЙ", "БЕЗ", "ДУШІ", "ЗОСТАЧАЄТЬСЯ"
]

# Український алфавіт
ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

# Словник порядкових номерів літер
LETTER_POSITIONS = {
    char: i + 1 for i, char in enumerate(ALPHABET)
}


def calculate_key(word):
    """
    Обчислення числового ключа слова.
    K = сума порядкових номерів літер.
    """
    key = 0

    for char in word.upper():
        key += LETTER_POSITIONS.get(char, 0)

    return key


def division_hash(key):
    """Метод ділення: h(K) = K mod 13."""
    return key % M_DIV


def multiplication_hash(key):
    """
    Метод множення:
    h(K) = floor(16 * (KA mod 1)).
    """
    fractional_part = (key * A) % 1
    return math.floor(M_MUL * fractional_part)


def build_closed_hash_table(words, m, hash_function):
    """
    Побудова закритої хеш-таблиці
    з використанням лінійного пробування.
    """
    # Ініціалізація порожніх комірок
    hash_table = [None] * m

    # Обробка кожного слова
    for word in words:

        # Обчислення числового ключа
        key = calculate_key(word)

        # Визначення початкової адреси
        start_address = hash_function(key)

        # Лінійне пробування
        for i in range(m):

            # Обчислення поточної адреси
            address = (start_address + i) % m

            # Перевірка вільної комірки
            if hash_table[address] is None:

                # Вставлення слова
                hash_table[address] = word
                break

        else:
            # Якщо всі комірки зайняті
            print(f"Помилка: таблиця заповнена. "
                  f"Не вдалося додати: {word}")

    return hash_table


def display_hash_table(table, method):
    """Виведення закритої хеш-таблиці."""
    print(f"\n--- {method} ---")
    print("Індекс | Слово")
    print("-------|----------------")

    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")


# Побудова таблиці методом ділення
table_div = build_closed_hash_table(
    WORDS, M_DIV, division_hash
)

display_hash_table(
    table_div, "Метод ділення (M=13)"
)

# Побудова таблиці методом множення
table_mul = build_closed_hash_table(
    WORDS, M_MUL, multiplication_hash
)

display_hash_table(
    table_mul, "Метод множення (M=16)"
)
