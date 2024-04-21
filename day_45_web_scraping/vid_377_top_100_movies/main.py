import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

print(soup.prettify())

movies = soup.find_all(name="h3", class_='listicleItem_listicle-item__title__BfenH')

movie_list = [movie.getText() for movie in movies]
movie_list = movie_list[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")