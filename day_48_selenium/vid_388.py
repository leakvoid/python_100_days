from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price a-text-price")
# print("PRICE:", price_dollar)

driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")
print("SEARCH BAR: ", search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print("BUTTON: ", button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print("DOCUMENTATION: ", documentation_link.text)

f_link = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/div/p/small/span[2]/a") # inspect -> right click -> copy -> xpath
print("F LINK: ", f_link.text)

driver.quit()