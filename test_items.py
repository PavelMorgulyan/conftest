import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_check_basket_button_exists(browser): # language
    button = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    print(button)
    
    assert button, "No basket button in website"
    
