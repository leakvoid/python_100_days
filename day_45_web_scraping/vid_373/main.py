from bs4 import BeautifulSoup
import lxml

DIR_PATH = "day_45_web_scraping/vid_373/"

with open(DIR_PATH + "website.html", "r") as f:
    contents = f.read()

# soup = BeautifulSoup(contents, 'html.parser') # alternative parser
soup = BeautifulSoup(contents, 'lxml')
print("TITLE: ", soup.title)
print("TITLE.NAME: ", soup.title.name)
print("TITLE.STRING: ", soup.title.string)
print("PRETTIFY: ", soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print("ALL LINKS: ", all_anchor_tags)

for tag in all_anchor_tags:
    print("LINK TEXT: ", tag.getText())
    print("REF: ", tag.get("href"))

heading = soup.find(name="h1", id="name") # find first by id
print("BY ID: ", heading)

section_heading = soup.find(name="h3", class_="heading") # find first by class
print("BY CLASS: ", section_heading)

company_url = soup.select_one(selector="p a")
print("p a: ", company_url)

name = soup.select_one(selector="#name")
print("#name: ", name)

headings = soup.select(".heading")
print(".heading: ", headings)