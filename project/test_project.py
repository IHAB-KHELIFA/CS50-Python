from project import get_recipe, generate_shopping_list, filter_recipes

def test_get_recipe():
    recipe = get_recipe("vegetarian", "American")
    assert recipe is not None
    assert recipe["name"] == "Avocado Toast"

def test_generate_shopping_list():
    ingredients = ["bread", "avocado", "salt", "pepper"]
    shopping_list = generate_shopping_list(ingredients)
    assert isinstance(shopping_list, dict)
    assert shopping_list["bread"] == 1
    assert len(shopping_list) == len(ingredients)

def test_filter_recipes():
    filtered = filter_recipes("vegan", "Asian")
    assert len(filtered) == 1
    assert filtered[0]["name"] == "Vegetable Stir Fry"
