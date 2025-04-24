## 💻 Amazon Laptop Scraper

This project is a simple web scraper built using Python and Selenium to extract laptop information from [Amazon.in](https://www.amazon.in). It collects data such as laptop names, prices, reviews, and product links, and stores the output in a CSV file for further analysis.

### 📂 Features
- Scrapes data across multiple Amazon search result pages
- Extracts:
  - Laptop names
  - Prices
  - Number of reviews
  - Product links
- Saves the data to a CSV file using Pandas

### 🛠️ Requirements
- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- Selenium
- Pandas

### 🔧 Installation
```bash
pip install selenium pandas
```

Make sure ChromeDriver is installed and its path is set in your system environment variables.

### 🚀 Usage
Run the script:
```bash
python Amazon.py
```
The data will be saved to:
```
D:\pycharm projects\PythonProject1\.venv\Live_laptop.csv
```

