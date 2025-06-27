from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_add_elements(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='addElement()']"))
    )
    for _ in range(3):
        add_button.click()

    delete_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually"))
    )
    assert len(delete_buttons) == 3

def test_remove_elements(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='addElement()']"))
    )
    for _ in range(3):
        add_button.click()

    delete_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually"))
    )
    delete_buttons[0].click()

    delete_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually"))
    )
    assert len(delete_buttons) == 2

def test_remove_all_elements(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='addElement()']"))
    )
    for _ in range(3):
        add_button.click()

    delete_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually"))
    )
    for btn in delete_buttons:
        btn.click()

    # Wait until no delete buttons remain
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "added-manually"))
    )
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    assert len(delete_buttons) == 0
