import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\\Projects\\Automation\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://demo.automationtesting.in/Windows.html")
    driver.implicitly_wait(2000)


def test_currentWindow():
    currentWindow=driver.current_window_handle
    currenthandles=driver.window_handles
    print("current window:", currentWindow, "numebr of handles:", len(currenthandles))

def test_click():
    driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
    handles=driver.window_handles
    print("the handles are:", handles)
    print(driver.current_window_handle)
    driver.close()
    driver.switch_to.window(handles[1])

def test_scrol2MoreNews():
    element=driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/a/div/b")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.save_screenshot("E:\TestFiles\MoreNews.png")


def test_teardown():
    driver.quit()
# def testClick():
#     driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click();
#
#     handles=driver.window_handles  #All handles values of open browser windows
#     print (handles )
#     print("totla windows number:", len(handles))
    # for handle in handles:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     if driver.title =="Frames & windows":
#         driver.close() #close ONLY parent window
#     moreNews = driver.find_element_by_xpath("/html/body/div[4]/div[4]/a/div")
#     driver.execute_script("arguments[0].scrollIntoView();", moreNews)
#     moreNews.click()
# driver.quit()

