import os
import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_KEY = os.getenv("API_KEY")
API_BASE_URL = "https://api.spoonacular.com"

def get_recipes(ingredients: list) -> dict:
    # Use global variable as st.button onclick doesn't return data
    global recipes_data
    recipes_data = []
    # Prepare ingredient list for api request
    ingredient_list = ingredients.split(',')
    ingredients_url_parameters = ',+'.join(ingredient_list)
    # Get recipes from findByIngredients api endpoint
    response = requests.get(f"{API_BASE_URL}/recipes/findByIngredients?apiKey={API_KEY}&ingredients={ingredients_url_parameters}")
    # Return result as dict if http status 200
    if response.status_code == 200:
        recipes_data = response.json()
    else:
        recipes_data = "Something went wrong."

def format_amount_number(amount: float) -> str:
    amount = round(amount,2)
    if amount == int(amount):
        return str(int(amount))
    else:
        return str(amount)

def create_ingredients_dataframe(people_count: int, recipe: list):
    data = {}
    for ingredient in recipe["usedIngredients"]:
        name = ingredient['originalName']
        data[name] = people_count * ingredient['amount']

    for ingredient in recipe["missedIngredients"]:
        name = ingredient['originalName']
        data[name] = people_count * ingredient['amount']
    
    # Erstelle das Kuchendiagramm
    fig = px.pie(values=list(data.values()), names=list(data.keys()), title='Ingredients Distribution')
    st.plotly_chart(fig)

# Setup page
st.set_page_config(page_title="Recipe Finder", page_icon="🍽️")
st.title("Recipe Finder")
st.write("""Discover delicious recipes based on the ingredients you have on
            hand! Simply enter your ingredients and find suitable recipes for
            your next meal.""")

# Ingredients and people Input and search button
st.subheader("Input Ingredients separated by
