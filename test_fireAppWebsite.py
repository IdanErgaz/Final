
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest
# import PyExecJS
def test_setup():
    global driver
    driver= webdriver.Chrome(executable_path="C:\\Projects\\Automation\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://library-app.firebaseapp.com/")
    wait = WebDriverWait(driver, 10)
    element= wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/section/h1")))

def test_validateThe_H1():
    title=driver.find_element_by_xpath("/html/body/main/section/p[2]").text
    assert (title=="Don't forget to check out other menu points as well. ;)")


def test_ValidatePlaceHolder():
    wait=WebDriverWait(driver, 10)
    element= wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ember26']")))
    place=element.get_attribute("placeholder")
    assert place=="Please type a fake e-mail address."


def test_validateButton():
    current=driver.find_element_by_css_selector(".btn.btn-primary.btn").text
    assert current=="Request invitation"

def test_setEmailAndClick():
    driver.find_element_by_id("ember26").send_keys("blabla@walla.com")
    # button= driver.find_element_by_css_selector(".btn.btn-primary.btn")
    wait=WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn"))).click()

def test_selectFromList():
# ddl=Select(driver.find_element_by_xpath("//*[@id='ember23']/a"))
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(".dropdown-toggle.nav-link").click()
    driver.save_screenshot("E:\\TestFiles\\screen01.png")
    wait=WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-item.ember-view"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/h1")))
    assert (driver.find_element(By.XPATH, "/html/body/main/h1")).text == "Invitations"


def test_scrollTo():
    # scrool to ELEMENT
    element = driver.find_element_by_xpath("/html/body/main/table/tbody/tr[20]/th")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.implicitly_wait(2000)
    driver.save_screenshot("E:\\TestFiles\\screen11.png")

def test_hoverStyle():
    home=driver.find_element_by_xpath("//*[@id='ember10']")
    ActionChains(driver).move_to_element(home).perform()
    driver.save_screenshot("E:\\TestFiles\\screen12.png")



def test_teardown():
    driver.quit()
