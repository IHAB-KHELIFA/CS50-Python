import json
import random

# Sample data for recipes
sample_recipes = [
    {
        "name": "Spaghetti Carbonara",
        "ingredients": ["spaghetti", "eggs", "parmesan", "bacon", "pepper"],
        "diet": "non-vegetarian",
        "cuisine": "Italian"
    },
    {
        "name": "Avocado Toast",
        "ingredients": ["bread", "avocado", "salt", "pepper"],
        "diet": "vegetarian",
        "cuisine": "American"
    },
    {
        "name": "Vegetable Stir Fry",
        "ingredients": ["broccoli", "carrot", "bell pepper", "soy sauce", "ginger"],
        "diet": "vegan",
        "cuisine": "Asian"
    }
]

def main():
    print("Welcome to the Recipe Recommendation and Shopping List Generator!")
    preferences = input("Enter dietary preference (vegetarian, vegan, non-vegetarian): ").strip().lower()
    cuisine = input("Enter preferred cuisine (e.g., Italian, Asian): ").strip().lower()

    recipe = get_recipe(preferences, cuisine)
    if recipe:
        print(f"Recommended Recipe: {recipe['name']}")
        print("Ingredients needed:", ", ".join(recipe["ingredients"]))
        if input("Do you want to generate a shopping list for this recipe? (y/n): ").lower() == 'y':
            shopping_list = generate_shopping_list(recipe["ingredients"])
            print("Shopping List:", shopping_list)
    else:
        print("No recipe matches your preferences.")

def get_recipe(preferences, cuisine):
    """Returns a recipe matching the user's preferences and cuisine."""
    filtered_recipes = filter_recipes(preferences, cuisine)
    if filtered_recipes:
        return random.choice(filtered_recipes)
    return None

def generate_shopping_list(ingredients):
    """Generates a shopping list of ingredients for the selected recipe."""
    return {ingredient: 1 for ingredient in ingredients}  # Each item once for simplicity

def filter_recipes(preferences, cuisine):
    """Filters recipes based on dietary preference and cuisine."""
    return [
        recipe for recipe in sample_recipes
        if recipe["diet"] == preferences and recipe["cuisine"].lower() == cuisine.lower()
    ]

if __name__ == "__main__":
    main()

