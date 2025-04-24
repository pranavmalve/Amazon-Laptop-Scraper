from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
laptop_names = []
laptop_prices = []
laptop_reviews= []
laptop_links = []


for page in range(1, 3):
    url = f"https://www.amazon.in/s?k=laptop&page={page}"
    driver.get(url)
    time.sleep(3)
    all_products = driver.find_elements(By.XPATH, "//div[@data-component-type = 's-search-result']")

    for product in all_products:
        names = product.find_elements(By.XPATH,".//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']/span")
        for name in names :
            laptop_names.append(name.text)

        prices = product.find_elements(By.XPATH,".//span[@class='a-price-whole']")
        for price in prices:
            laptop_prices.append(price.text)

        try :
            if len(product.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']"))>0:
                reviews = product.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")
                for review in reviews:
                    laptop_reviews.append(review.text)
            else:
                laptop_reviews.append("0")
        except:
            pass

        links = product.find_elements(By.XPATH, ".//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
        for link in links:
            laptop_links.append(link.get_attribute("href"))


# Save to CSV using pandas
import pandas as pd
df = pd.DataFrame(zip(laptop_names,laptop_prices,laptop_reviews,laptop_links),columns=['laptop_names','laptop_prices','laptop_reviews','laptop_links'])
df.to_csv(r"D:\pycharm projects\PythonProject1\.venv\Live_laptop.csv", index=False)




