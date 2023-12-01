import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test__product_view_sku():
    """
    Test case WERT-1
    """
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") 
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions") 
	
		
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url = "https://testqastudio.me/"
    driver.get(url=url)
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему,
    # чтобы просмотреть детали
    element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11340"]')
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = driver.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'BFB9ZOK210', "Unexpected sku"