from io import BytesIO
from PIL import Image, ImageTk
import requests
import tkinter as tk
import webbrowser

BUTTON_CLICK_SOUND = r"assets\frame0\clicks.mp3"
WINDOW_TITLE = "Recipe App"
RECIPE_IMAGE_WIDTH = 350
RECIPE_IMAGE_HEIGHT = 300

class RecipeApp(object):

    def __init__(self, recipe_app_key):
        self.recipe_app_key = recipe_app_key
        self.window = tk.Tk()
       
        # Auto resize geometry
        self.window.geometry("")
        self.window.configure(bg="#9ddfd3")
        self.window.title(WINDOW_TITLE)

        self.search_label = tk.Label(self.window, text="Search Recipe", bg="#ea86b6")
        self.search_label.grid(column=0, row=0, padx=5)

        self.search_entry = tk.Entry(master=self.window, width=40)
        self.search_entry.grid(column=1, row=0, padx=5, pady=10)

        self.search_button = tk.Button(self.window, text="Search", highlightbackground="#ea86b6",
            command=self.__run_search_query)
        self.search_button.grid(column=2, row=0, padx=5)

    def __run_search_query(self):
        query = self.search_entry.get()
        recipe = self.__get_recipe(query)

        if recipe:
            recipe_image = recipe['image']
            # Safely access 'sourceUrl' using .get()
            recipe_url = recipe.get('sourceUrl', "")  # Default to an empty string if not found
        else:
            # Recipe not found
            recipe_image = "https://www.mageworx.com/blog/wp-content/uploads/2012/06/Page-Not-Found-13.jpg"
            recipe_url = ""

        self.__show_image(recipe_image)
        self.__get_ingredients(recipe)

        def __open_link():
            if recipe_url:  # Open link only if it's not empty
                webbrowser.open(recipe_url)

        
        if recipe_url:
            self.recipe_button = tk.Button(self.window, text="Recipe Link", highlightbackground="#ea86b6",
                                           command=__open_link)
            self.recipe_button.grid(column=1, row=7, pady=10)
        else:
           
            self.recipe_button = tk.Label(self.window, text="No recipe link available", bg="#ea86b6")
            self.recipe_button.grid(column=1, row=7, pady=10)

    def __get_recipe(self, query):
        # URL for the Spoonacular recipe search API
        url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}https://api.spoonacular.com/recipes/complexSearch?query=burger&cuisine=italian&excludeCuisine=greek&diet=vegetarian&intolerances=gluten&equipment=pan&includeIngredients=tomato,cheese&excludeIngredients=eggs&type=main course&instructionsRequired=true&fillIngredients=false&addRecipeInformation=false&addRecipeNutrition=false&author=coffeebean&tags=ipsum ea proident amet occaecat&recipeBoxId=2468&titleMatch=Crock Pot&maxReadyTime=20&ignorePantry=false&sort=calories&sortDirection=asc&minCarbs=10&maxCarbs=100&minProtein=10&maxProtein=100&minCalories=50&maxCalories=800&minFat=1&maxFat=100&minAlcohol=0&maxAlcohol=100&minCaffeine=0&maxCaffeine=100&minCopper=0&maxCopper=100&minCalcium=0&maxCalcium=100&minCholine=0&maxCholine=100&minCholesterol=0&maxCholesterol=100&minFluoride=0&maxFluoride=100&minSaturatedFat=0&maxSaturatedFat=100&minVitaminA=0&maxVitaminA=100&minVitaminC=0&maxVitaminC=100&minVitaminD=0&maxVitaminD=100&minVitaminE=0&maxVitaminE=100&minVitaminK=0&maxVitaminK=100&minVitaminB1=0&maxVitaminB1=100&minVitaminB2=0&maxVitaminB2=100&minVitaminB5=0&maxVitaminB5=100&minVitaminB3=0&maxVitaminB3=100&minVitaminB6=0&maxVitaminB6=100&minVitaminB12=0&maxVitaminB12=100&minFiber=0&maxFiber=100&minFolate=0&maxFolate=100&minFolicAcid=0&maxFolicAcid=100&minIodine=0&maxIodine=100&minIron=0&maxIron=100&minMagnesium=0&maxMagnesium=100&minManganese=0&maxManganese=100&minPhosphorus=0&maxPhosphorus=100&minPotassium=0&maxPotassium=100&minSelenium=0&maxSelenium=100&minSodium=0&maxSodium=100&minSugar=0&maxSugar=100&minZinc=0&maxZinc=100&offset=606&number=10&limitLicense=true &apiKey={self.recipe_app_key}"
        
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # If we have search results, return the first one
            if data.get('results'):
                return data['results'][0]  # Return the first recipe result
        return None
    
    def __show_image(self, image_url):
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((RECIPE_IMAGE_WIDTH, RECIPE_IMAGE_HEIGHT))
        image = ImageTk.PhotoImage(img)

        holder = tk.Label(self.window, image=image)
        holder.photo = image
        holder.grid(column=1, row=6, pady=10)

    def __get_ingredients(self, recipe):
        ingredients_text = tk.Text(master=self.window, height=15, width=50, bg="#ffdada")
        ingredients_text.grid(column=1, row=4, pady=10)
        ingredients_text.delete("1.0", tk.END)

        if recipe is None:
            ingredients_text.insert(tk.END, "No Recipe found for search criteria")
            return

        ingredients_text.insert(tk.END, "\n" + recipe['title'] + "\n")
        # For the ingredients, we use the `extendedIngredients` field
        if 'extendedIngredients' in recipe:
            for ingredient in recipe['extendedIngredients']:
                ingredients_text.insert(tk.END, "\n- " + ingredient['name'])

    def run_app(self):
        self.window.mainloop()

# Create App and run the app
if __name__ == "__main__":
    recipe_app_key = "8b4d854f3bb446afa28109f20019f126" 

    recipe_app = RecipeApp(recipe_app_key)
    recipe_app.run_app()
