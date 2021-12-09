from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "http://ecos.bok.or.kr/jsp/vis/keystat/#/key"
driver.get(url)


excel_download = driver.find_element(By.TAG_NAME, 'img[alt="download"]')
excel_download.click()