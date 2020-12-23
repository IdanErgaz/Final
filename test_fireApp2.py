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



def test_library():
    driver.find_element_by_xpath("//*[@id='ember12']").click()
    # driver.find_element_by_xpath("//*[@id='ember12']").click()#click on library at navbar menu
    # wait=WebDriverWait(driver, 10)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/h1")))#wait for the main title to be shown

    element = driver.find_element_by_xpath("/html/body/main/div[2]/div[12]/div/div[2]")#scroll to the relevent element
    driver.execute_script("arguments[0].scrollIntoView();", element)

    # wait.until(EC.visibility_of_element_located(element))
    # driver.find_element_by_xpath("/html/body/main/div[2]/div[12]/div/div[3]/span[2]/button").click()
    # driver.save_screenshot("E:\\TestFiles\\screen13.png")

    # wait.until(EC.alert_is_present())
    # alertText=driver.switch_to_alert().text
    # assert alertText=="Are you sure?"
    # driver.switch_to_alert().accept()

