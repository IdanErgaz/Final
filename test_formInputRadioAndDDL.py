import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

#Navigate to page
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\\Projects\\Automation\\Drivers\\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

def test_login():
    current=driver.find_element_by_id("logInPanelHeading").text
    assert "LOGIN Panel"==current
    print("Title of Login panel CAN BE SEEN!")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[2]/div[2]/div[1]/aside/fieldset/fieldset[2]/div[2]/div[1]/div[1]/div/label/span[1]")))
    # element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/div/div[1]/h1")))
    EC.text_to_be_present_in_element((By.XPATH, "//*[@id='content']/div/div[1]/h1"),"Dashboard title to display")

def test_hover():
    admin =driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
    configuration= driver.find_element_by_css_selector("#menu_admin_Configuration")
    modules= driver.find_element_by_id("menu_admin_viewModules")
    action=ActionChains(driver)
    action.move_to_element(admin).move_to_element(configuration).move_to_element(modules).click().perform()
    time.sleep(2)


def test_checkbox():
    leaveModule=driver.find_element_by_css_selector("#moduleConfig_leave").is_selected()
    if leaveModule!=False:
        print("Problem is detected, the leave module IS checked !!!")
        driver.save_screenshot("E:\\TestFiles\\image.png")
    time.sleep(1)
    driver.find_element_by_id("btnSave").click()
    driver.find_element_by_css_selector("#moduleConfig_leave").click()
    print("Assert2")
    time.sleep(2)
    assert (driver.find_element_by_css_selector("#moduleConfig_leave").is_selected())==True
    driver.find_element_by_id("btnSave").click()
    expected="Successfully Saved"
    curruent=driver.find_element_by_xpath("//*[@id='saveFormDiv']/div[2]/div").text
    assert curruent == expected, "The messge is not shown!!!"
    print("Restore settings!!!")
    driver.find_element_by_id("btnSave").click()
    driver.find_element_by_css_selector("#moduleConfig_leave").click()
    time.sleep(1)
    driver.find_element_by_id("btnSave").click()

    #Fill in all data

def test_fillBoxes():#fill boxes data, select checkbox and radio options, upload a file
    driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
    driver.find_element_by_id("RESULT_TextField-1").send_keys("Bob")
    driver.find_element_by_id("RESULT_TextField-2").send_keys("Marly")

def test_selectGender():    #Update tomorrow!!!!
    gender=driver.find_element_by_css_selector("#RESULT_RadioButton-7_0").is_selected()
    print("The male STATUS IS :", gender)
    time.sleep(2)
    if gender==False:
        driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()
        time.sleep(3)
        print("new gender status:", gender)



def test_selectDay(): #Update tomorrow!!!!
    ThursdayStatus=driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[5]/td/label").is_selected()
    if ThursdayStatus==False:
        driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[5]/td/label").click()

def test_righClickAndAlertHandling():
    driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
    button=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
    action=ActionChains(driver)
    action.context_click(button).perform()#Perform right click
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/ul/li[3]").click()#click on copy option
    driver.implicitly_wait(5)
    driver.switch_to.alert.text=="clicked: copy"
    driver.switch_to.alert.accept()
    driver.save_screenshot("E:\\TestFiles\\image.png")



def test_dragAndDrop():
    driver.get("https://testautomationpractice.blogspot.com/%22")
    driver.implicitly_wait(3)
    source=driver.find_element_by_xpath("//*[@id='gallery']/li[1]/img")
    dest=driver.find_element_by_xpath("//*[@id='trash']")
    action=ActionChains(driver)
    action.drag_and_drop(source, dest).perform()
    driver.find_element_by_xpath("//*[@id='trash']/ul/li/img").click()#click on image from recycle section

def test_datePicker():
    print("date picker!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def test_UrlAndTitle():
    url=driver.current_url
    title=driver.title
    print("url:", url, "and title:", title)

def test_teardown():
    print("Finish testing!!!")
    driver.quit()
