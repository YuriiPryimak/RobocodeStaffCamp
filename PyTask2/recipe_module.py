
from typing import Dict, List, Union
from collections import OrderedDict

def get_recipe(dish_name: str) -> OrderedDict:
    recipes = {
        "борщ": {
            "інгредієнти": ["буряк", "капуста", "картопля", "морква", "цибуля", "часник", "м'ясо", "сметана"],
            "кроки": ["Підготувати інгредієнти", "Зварити м'ясо", "Додати овочі", "Готувати до готовності"]
        },
        "омлет": {
            "інгредієнти": ["яйця", "молоко", "сіль", "масло"],
            "кроки": ["Збити яйця з молоком", "Розігріти сковороду", "Вилити суміш на сковороду", "Готувати до готовності"]
        }
    }
    return OrderedDict(recipes.get(dish_name.lower(), {}))

def determine_difficulty(recipe: Dict[str, List[str]]) -> int:
    try:
        num_ingredients = len(recipe.get("інгредієнти", []))
        num_steps = len(recipe.get("кроки", []))
        total = num_ingredients + num_steps

        if total <= 5:
            return 1  # легко
        elif total <= 8:
            return 2  # середнє
        else:
            return 3  # складно
    except Exception as e:
        print(f"Error determining difficulty: {e}")
        return -1

def can_cook(user_ingredients: List[str], recipe: Dict[str, List[str]]) -> bool:
    try:
        required_ingredients = set(recipe.get("інгредієнти", []))
        user_ingredients_set = set(user_ingredients)
        return required_ingredients.issubset(user_ingredients_set)
    except Exception as e:
        print(f"Error checking if can cook: {e}")
        return False
