# Recipe Recommendation and Shopping List Generator

#### Video Demo:  https://youtu.be/bfiLyTeuGV0

#### Description:
The **Recipe Recommendation and Shopping List Generator** is a command-line Python application designed to suggest recipes based on user preferences, dietary restrictions, and cuisine preferences. This program also provides a shopping list of ingredients required for any selected recipe, helping users plan their meals more efficiently.

### Project Overview
The project consists of three main parts:

1. Recipe Selection: The app recommends a recipe based on dietary preferences and preferred cuisine, using a built-in list of sample recipes.
2. Shopping List Generation: For each recipe, the program generates a simple shopping list of ingredients needed.
3. Recipe Filtering: Recipes are filtered based on user input for dietary restrictions (e.g., vegetarian, vegan, non-vegetarian) and desired cuisine (e.g., Italian, Asian).

### File Descriptions
- project.py: This is the main file containing the core logic of the application. It includes:
  - `main`: The entry point for the program, guiding users through recipe selection and shopping list generation.
  - `get_recipe`: A function that suggests a recipe based on user input for dietary preference and cuisine.
  - `generate_shopping_list`: This function creates a shopping list for a given recipe’s ingredients.
  - `filter_recipes`: Filters recipes from a predefined list based on dietary and cuisine choices.
- test_project.py: Contains the unit tests for the core functions in `project.py`. Each test validates the functionality of the respective functions using `pytest`.
- requirements.txt: Lists `pytest` as a dependency for testing the project.


