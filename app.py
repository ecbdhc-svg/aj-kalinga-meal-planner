import streamlit as st
import random
import pandas as pd

# FOOD LISTS

breakfast_carbs = ["Pandesal", "garlic rice", "white rice"]
breakfast_proteins = ["Egg",
    "Steamed Pork Siomai",
    "Chicken Sopas",
    "Pork Tapa", "Scrambled egg with tomato and onion", "Paksiw na GG with talong and ampalaya",
    "Tuna Sisig", "Ginisang Luncheon Meat at Kalabasa",
    "Tortang Dilis", "Pancit Canton Guisado",
    "Ginisang Sayote w/ Corned Beef"]

carbs = ["Rice", "pancit"]

proteins = {
     "Chicken Adobo": {"veg": []},
    "Tinolang Manok": {"veg": ["Sayote"]},
    "Ginisang Monggo": {"veg": ["Malunggay"]},
    "Tortang Talong": {"veg": ["Talong"]},
    "Paksiw na Isda": {"veg": []},
    "Chicken Pastel": {"veg": []}, "Tortang Giniling": {"veg": []}, "Nilagang Baboy": {"veg": []}, "Almondigas soup w/ patola": {"veg": []},
    "Ginisang munggo": {"veg": []}, "Chicken Afritada": {"veg": []}, "Buttered Chicken": {"veg": []}, "Laing": {"veg": []}, "Sinigang na baboy": {"veg": []},
    "Kinamatisang manok and petchay": {"veg": []}, "Sweet and Sour meatballs": {"veg": []}, "Pork Caldereta": {"veg": []}, "Pork Afritada": {"veg": []},
    "Escabecheng Tilapia": {"veg": []}, "Adobong Baboy with beans": {"veg": []}, "Sinigang na bangus": {"veg": []},
    "Chicken Caldereta": {"veg": []}, "Pininyahang manok": {"veg": []}, "Fish fillet with sauce": {"veg": []}, "Tofu and kangkong in oyster sauce": {"veg": []},
    "Pork Hamonado": {"veg": []}, "Chicken Inasal": {"veg": []}, "Tochong bangus": {"veg": []}, "Pritong Tilapia": {"veg": []}, "Beef Bulalo": {"veg": []}, "Chicken Ala King": {"veg": []},
    "Kinamatisang Baboy": {"veg": []}, "Miswa sa baboy": {"veg": []}, "Paksiw na baboy": {"veg": []}, "Braised Pork Belly": {"veg": []}, "Pork Chop Steak": {"veg": []},
    "Pata sa Bitswelas": {"veg": []}, "Pork Asado": {"veg": []}, "Pork Igado": {"veg": []}, "Tokwat Baboy": {"veg": []}, "Chicken sa miswa": {"veg": []},
    "Pocherong Manok": {"veg": []}, "Chicken Bistek": {"veg": []}, "Kung Pao Chicken": {"veg": []}, "Kinamatisang Manok": {"veg": []}, "Chicken Curry": {"veg": []},
    "Chicken Mechado": {"veg": ["potato", "carrots"]}}

vegetables = ["Ginisang Kangkong",
"Blanched Pechay",
"Inihaw na Talong",
"Ginisang Sayote",
"Ginisang Kalabasa",
"Ginisang Repolyo",
"Ginisang Sitaw",
"Ginisang Ampalaya",
"Pipino Salad",
"Ginisang Patola",
"Ginisang Upo",
"Ginisang Labanos",
"Ginisang Sigarilyas",
"Ginisang Puso ng Saging",
"Ginisang Malunggay",
"Ginisang Mustasa",
"Steamed Okra",
"Ginisang Kamote Tops"]

fruits = {
    "Banana": {"season": "all"},
    "Mango": {"season": "summer"},
    "Papaya": {"season": "all"},
    "Apple slices": {"season": "all"},
     "Oranges": {"season": "all"}
}
# FUNCTIONS

def get_seasonal_fruits(season):
    available = []
    for fruit, info in fruits.items():
        if info["season"] == season or info["season"] == "all":
            available.append(fruit)
    return available


def get_valid_vegetables(ulam):
    used = proteins[ulam]["veg"]
    valid = []
    for veg in vegetables:
        if veg not in used:
            valid.append(veg)
    return valid


def generate_breakfast():
    carb = random.choice(breakfast_carbs)
    protein = random.choice(breakfast_proteins)
    return carb + " + " + protein


def generate_lunch(season, used_ulam):

    available_ulam = []

    for ulam in proteins:
        if ulam not in used_ulam:
            available_ulam.append(ulam)

    if len(available_ulam) == 0:
        used_ulam.clear()
        available_ulam = list(proteins.keys())

    ulam = random.choice(available_ulam)
    used_ulam.append(ulam)

    carb = random.choice(carbs)
    veg = random.choice(get_valid_vegetables(ulam))
    fruit = random.choice(get_seasonal_fruits(season))

    return carb + " + " + ulam + " + " + veg + " + " + fruit


def generate_dinner(used_ulam):

    available_ulam = []

    for ulam in proteins:
        if ulam not in used_ulam:
            available_ulam.append(ulam)

    if len(available_ulam) == 0:
        used_ulam.clear()
        available_ulam = list(proteins.keys())

    ulam = random.choice(available_ulam)
    used_ulam.append(ulam)

    carb = random.choice(carbs)
    veg = random.choice(vegetables)
    return carb + " + " + veg + " + " + ulam


def generate_plan(days, season):

    used_ulam = []
    data = []

    for day in range(days):

        breakfast = generate_breakfast()
        lunch = generate_lunch(season, used_ulam)
        dinner = generate_dinner(used_ulam)

        data.append({
            "Day": day + 1,
            "Breakfast": breakfast,
            "Lunch": lunch,
            "Dinner": dinner
        })

    return pd.DataFrame(data)


# STREAMLIT INTERFACE

st.title("AJ Kalinga Meal Planner")

season = st.selectbox(
    "Select Season",
    ["summer", "rainy", "all"]
)

days = st.slider(
    "Number of Days",
    7, 30, 30
)

if st.button("Generate Meal Plan"):

    df = generate_plan(days, season)

    st.dataframe(df)