from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
article_count.click() # click link

# vid 391
from selenium.webdriver.common.keys import Keys

search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

driver.quit()

# fake signup
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
first_name.send_keys("Foo")
last_name.send_keys("Bar")
email.send_keys("foobar@email.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()