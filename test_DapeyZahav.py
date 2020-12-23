import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium.webdriver.support.wait import WebDriverWait
import uuid



def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\\Projects\\Automation\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get("https://www.d.co.il/")
    print("Opening website pahe...")

def test_clickFlower():
    driver.find_element_by_css_selector("[data-statistics-label='col3-row1']").click()
    #wait for element
    # title=driver.find_element_by_css_selector("#search_results_main_title")
    # print(title)
    wait = WebDriverWait(driver, 5)
    mainTitle = wait.until(ec.presence_of_element_located((By.ID, "search_results_main_title")))

def test_selectArea():
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[3]/div/main/aside[1]/div/div[3]/div[1]/div[2]/ul/li[4]/label/a/span").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[3]/div/main/aside[1]/div/div[3]/div[2]/div[2]/ul/li[4]/label/a/div").click()
    driver.save_screenshot("E:\\TestFiles\\image1.png")
    unique_filename = str(uuid.uuid4())

    driver.find_element(By.XPATH, "//*[@id='sorter_ranking']/a").click()
    driver.save_screenshot("E:\\TestFiles\\"+unique_filename+".png")
    # current =(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[3]/div/main/section/article[1]/div[1]/h3/a").text)
    # expected ="פרחי ספיר"
    #



def test_scrollDown():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    unique_filename = str(uuid.uuid4())

    driver.save_screenshot("E:\\TestFiles\\"+ unique_filename+".png")
    wait=WebDriverWait(driver, 20)
    # button =wait.until(ec.element_to_be_clickable(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[4]'))
    # button.click()
    driver.find_element(By.CSS_SELECTOR, ".up_to_top").click()
    # botton.click()
    print("clicking the up button!!!")


def test_runQuery():
    driver.find_element_by_css_selector("#query").send_keys("אינסטלטור בתל אביב")
    driver.find_element(By.XPATH, "//*[@id='searchTopForm']/input[2]").click()
    print("Search by query")
    time.sleep(4)
    # driver.find_element(By.ID, "search_results_main_title").click()

    current= driver.find_element(By.ID, "search_results_main_title").text
    assert "אינסטלטור בתל אביב"==current
    unique_filename = str(uuid.uuid4())
    driver.save_screenshot("E:\\TestFiles\\" + unique_filename + ".png")


def test_teardown():
    print("Finish testing, Closing the page!")
    driver.quit()

