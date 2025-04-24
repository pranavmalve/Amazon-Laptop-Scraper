from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Setup Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Lists to store extracted data
laptop_names = []
laptop_prices = []
laptop_reviews = []
laptop_links = []

# Loop through Amazon pages
for page in range(1, 3):
    url = f"https://www.amazon.in/s?k=laptop&page={page}"
    driver.get(url)
    time.sleep(3)

    all_products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

    for product in all_products:
        # Name
        try:
            name = product.find_element(By.XPATH, ".//h2/span").text
        except:
            name = "N/A"
        laptop_names.append(name)

        # Price
        try:
            price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        except:
            price = "N/A"
        laptop_prices.append(price)

        # Review Count
        try:
            review = product.find_element(By.XPATH, ".//span[@class='a-size-base s-underline-text']").text
        except:
            review = "0"
        laptop_reviews.append(review)

        # Product Link
        try:
            link = product.find_element(By.XPATH, ".//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']").get_attribute("href")
        except:
            link = "N/A"
        laptop_links.append(link)

# Close the driver
driver.quit()

# Save to CSV
df = pd.DataFrame({
    'laptop_names': laptop_names,
    'laptop_prices': laptop_prices,
    'laptop_reviews': laptop_reviews,
    'laptop_links': laptop_links
})
df.to_csv(r"D:\pycharm projects\PythonProject1\.venv\Live_laptop.csv", index=False)
