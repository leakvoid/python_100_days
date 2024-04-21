import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

links = soup.select('.titleline')#soup.find_all(name='span', class_='titleline')
text_list = []
link_list = []
for link in links:
    first_link = link.select_one('a')
    text_list.append(first_link.getText())
    link_list.append(first_link.get("href"))

scores = soup.select('.subtext')
score_list = []
for score in scores:
    s = score.find(class_="score")
    if not s:
        score_list.append(0)
    else:
        score_list.append( int(s.getText().split(" ")[0]) )

max_score_idx = 0
for idx in range(1, len(score_list)):
    if score_list[idx] > score_list[max_score_idx]:
        max_score_idx = idx

print(f"Max score article: {text_list[max_score_idx]}, link: {link_list[max_score_idx]}, score: {score_list[max_score_idx]}")

# Some website/robots.txt