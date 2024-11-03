class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, ingredients, instructions):
        recipe = Recipe(name, ingredients, instructions)
        self.recipes.append(recipe)
        print(f"Recipe '{name}' added.")

    def view_recipes(self):
        if not self.recipes:
            print("No recipes available.")
        else:
            for recipe in self.recipes:
                print(f"Recipe: {recipe.name}")

    def search_recipe(self, name):
        found_recipes = [recipe for recipe in self.recipes if name.lower() in recipe.name.lower()]
        if found_recipes:
            for recipe in found_recipes:
                print(f"Recipe: {recipe.name}")
                print("Ingredients:", recipe.ingredients)
                print("Instructions:", recipe.instructions)
                print()
        else:
            print("No recipes found.")

def main():
    recipe_manager = RecipeManager()

    while True:
        print("\nRecipe Manager Menu:")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipe")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma separated): ")
            instructions = input("Enter cooking instructions: ")
            recipe_manager.add_recipe(name, ingredients.split(','), instructions)
        elif choice == '2':
            recipe_manager.view_recipes()
        elif choice == '3':
            name = input("Enter recipe name to search: ")
            recipe_manager.search_recipe(name)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
