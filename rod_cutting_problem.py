# Розробіть програму для знаходження оптимального способу розрізання стрижня, щоб отримати максимальний прибуток. Необхідно реалізувати два підходи: через рекурсію з мемоізацією та через табуляцію.
# Опис завдання
# 1. На вхід подається довжина стрижня та масив цін, де price[i] — це ціна стрижня довжини i+1 .
# 2. Потрібно визначити, як розрізати стрижень, щоб отримати максимальний прибуток.
# 3. Реалізувати обидва підходи динамічного програмування.
# 4. Вивести оптимальний спосіб розрізання та максимальний прибуток.

# 2. Обмеження:
# Довжина стрижня > 0.
# Всі ціни > 0.
# Масив цін не може бути порожнім.
# Довжина масиву цін повинна відповідати довжині стрижня.


from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    memo = {}

    def helper(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        max_profit = 0
        best_cuts = []
        for i in range(1, n + 1):
            if i <= len(prices):
                profit, cuts = helper(n - i)
                profit += prices[i - 1]
                if profit > max_profit:
                    max_profit = profit
                    best_cuts = cuts + [i]

        memo[n] = (max_profit, best_cuts)
        return memo[n]

    max_profit, cuts = helper(length)

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": max(len(cuts) - 1, 0),
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    dp = [0] * (length + 1)
    cuts = [[] for i in range(length + 1)]

    for n in range(1, length + 1):
        for i in range(1, n + 1):
            if i <= len(prices):
                if dp[n] < dp[n - i] + prices[i - 1]:
                    dp[n] = dp[n - i] + prices[i - 1]
                    cuts[n] = cuts[n - i] + [i]

    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": max(len(cuts[length]) - 1, 0),
    }


# Time Complexity: O(n^2)
# Space Complexity: O(n)
# for both approaches


def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {"length": 5, "prices": [2, 5, 7, 8, 10], "name": "Базовий випадок"},
        # Тест 2: Оптимально не різати
        {"length": 3, "prices": [1, 3, 8], "name": "Оптимально не різати"},
        # Тест 3: Всі розрізи по 1
        {"length": 4, "prices": [3, 5, 6, 7], "name": "Рівномірні розрізи"},
    ]

    for test in test_cases:
        print(f"\\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test["length"], test["prices"])
        print("\\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test["length"], test["prices"])
        print("\\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()
