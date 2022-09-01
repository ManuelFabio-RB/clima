from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:/Users\manub\Documents/7mo Semestre\PACS\chromedriver_win32/chromedriver.exe")
driver.get("https://www.clima.com")

driver.find_element(By.XPATH, "//a[contains(@href, \'https://www.clima.com/mexico\')]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id=\'term\']").send_keys("Querétaro")
time.sleep(2)

driver.find_element(By.XPATH, "//span[contains(text(),'Querétaro, Estado de Querétaro de Art')]").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Por horas").click()
time.sleep(2)


