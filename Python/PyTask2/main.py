
from recipe_module import get_recipe, determine_difficulty, can_cook

def main():
    # 1. Отримуємо рецепт
    dish_name = input("Введіть назву страви: ")
    recipe = get_recipe(dish_name)

    if not recipe:
        print(f"Рецепт для страви '{dish_name}' не знайдено.")
        return

    print(f"Рецепт для '{dish_name}': {recipe}")

    # 2. Визначаємо складність приготування
    difficulty = determine_difficulty(recipe)
    if difficulty == -1:
        print("Не вдалося визначити складність приготування.")
    else:
        difficulty_levels = {1: "легко", 2: "середнє", 3: "складно"}
        print(f"Складність приготування: {difficulty_levels.get(difficulty, 'невідомо')}")

    # 3. Перевіряємо чи може користувач приготувати страву
    user_ingredients = input("Введіть інгредієнти через кому: ").split(", ")
    if can_cook(user_ingredients, recipe):
        print(f"Ви можете приготувати '{dish_name}'.")
    else:
        print(f"Ви не можете приготувати '{dish_name}'.")

if __name__ == "__main__":
    main()
