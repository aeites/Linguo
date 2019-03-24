from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initiate driver and define wait between actions
link = "https://sentence.yourdictionary.com/"
driver = webdriver.Chrome()
driver.get(link)

#wait = WebDriverWait(driver, 1000)

driver.find_element_by_xpath("//*[@id=\"yd_search_bar\"]").send_keys("jobs")

