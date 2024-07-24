spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list =[]
    for spicy_food in spicy_foods:
        names_list.append(spicy_food['name'])
    
    return names_list

def get_spiciest_foods(spicy_foods):
    spiciest_food_list = []
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5: 
            spiciest_food_list.append(spicy_food)
    
    return spiciest_food_list
def print_spicy_foods(spicy_foods):
    
    for spicy_food in spicy_foods:
        print(f"{spicy_food.get('name')} ({spicy_food['cuisine']}) | Heat Level: { '🌶'*spicy_food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food['cuisine'] == cuisine:
            return spicy_food
        

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    counter = 0
    for food in spicy_foods:
        counter += food['heat_level']
    return counter/len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
