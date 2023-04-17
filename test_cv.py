"""
Business Card Test
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_title_validation(browser):
    
    url = "https://qagu.ru/"
    browser.get(url=url)

    title = browser.find_element(By.CLASS_NAME, value="title")

    assert title.text == 'QA-Engineer', "Unexpected title"