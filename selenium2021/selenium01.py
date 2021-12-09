from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chromedriver.exe를 실행 폴더와 같은 경로에 둠
driver = webdriver.Chrome()
url = "https://google.com"
driver.get(url)

# 클래스 값 - gLFyf
driver.find_element(By.CSS_SELECTOR, '.gLFyf').send_keys('파이썬') # 검색어 입력
#driver.find_element(By.CSS_SELECTOR, '.gLFyf').send_keys(Keys.ENTER) # 엔터
#첫번째 검색 사이트
#driver.find_element(By.CSS_SELECTOR, '.LC20lb').click()

#두번째 검색사이트 - 리스트 이므로 elements로 찾음
#driver.find_elements(By.CSS_SELECTOR, '.LC20lb')[1].click()
