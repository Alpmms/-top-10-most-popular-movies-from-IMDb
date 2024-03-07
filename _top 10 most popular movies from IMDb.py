#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install requests beautifulsoup4


# In[5]:


import requests
from bs4 import BeautifulSoup

def get_top_movies():
    url = "https://www.imdb.com/chart/top/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    movies = []
    for i, movie_row in enumerate(soup.select("tbody tr")):
        if i < 10:
            title = movie_row.select_one("td.titleColumn").text.strip()
            year = int(movie_row.select_one("span.secondaryInfo").text.strip("()"))
            rating = float(movie_row.select_one("td.imdbRating strong").text)
            movies.append({"title": title, "year": year, "rating": rating})
        else:
            break

    return movies

def print_top_movies(movies):
    print("Top 10 Movies on IMDb:")
    for i, movie in enumerate(movies):
        print(f"{i+1}. {movie['title']} ({movie['year']}) - IMDb Rating: {movie['rating']}")

if __name__ == "__main__":
    top_movies = get_top_movies()
    print_top_movies(top_movies)


# In[ ]:




