# def fibonacci_numbers_up_to(n):
#     fib_nums = [0, 1]
#     while True:
#         next_fib = fib_nums[-1] + fib_nums[-2]
#         if next_fib > n:
#             break
#         fib_nums.append(next_fib)
#     return set(fib_nums)
#
# def main():
#     import statistics
#
#     # Зчитування вводу від користувача
#     numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
#
#     if not numbers:
#         print("Введено порожній набір чисел.")
#         return
#
#     # 1. Знаходимо середнє арифметичне і число, найближче до нього
#     avg = statistics.mean(numbers)
#     closest_num = min(numbers, key=lambda x: abs(x - avg))
#     probability = numbers.count(closest_num) / len(numbers)
#     print(f"Середнє арифметичне: {avg}")
#     print(f"Число, найближче до середнього: {closest_num}")
#     print(f"Ймовірність отримання числа, найближчого до середнього: {probability:.2%}")
#
#     # 2. Видаляємо числа, які збігаються з числами Фібоначчі
#     max_num = max(numbers)
#     fib_numbers = fibonacci_numbers_up_to(max_num)
#     numbers = [num for num in numbers if num not in fib_numbers]
#     print(f"Набір після видалення чисел Фібоначчі: {numbers}")
#
#     # 3. Видаляємо дублікати чисел, які кратні найменшому числу
#     if numbers:
#         min_num = min(numbers)
#         unique_numbers = []
#         seen_multiples = set()
#
#         for num in numbers:
#             if num % min_num == 0:
#                 if num not in seen_multiples:
#                     unique_numbers.append(num)
#                     seen_multiples.add(num)
#             else:
#                 unique_numbers.append(num)
#
#         numbers = unique_numbers
#         print(f"Набір після видалення дублікатів чисел, кратних найменшому: {numbers}")
#
# if __name__ == "__main__":
#     main()

