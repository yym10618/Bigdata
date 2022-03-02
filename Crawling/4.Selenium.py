"""
날짜 : 2022/03/02
이름 : 양용민
내용 : 파이썬 Selenium 가상 브라우저 크롤링 실습

selenium 패키지 설치
 - 가상 브라우저를 조작하기 위한 파이썬 패키지
 - pip3 install selenium
"""

from selenium import  webdriver
from selenium.webdriver.common.by import By

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
browser.get('http://naver.com')

# 로그인 클릭
tag_a_login = browser.find_element(By.CSS_SELECTOR, '#account > a')
tag_a_login.click()

# 아이디 비밀번호 입력
tag_input_id = browser.find_element(By.CSS_SELECTOR, '#id')
tag_input_pw = browser.find_element(By.CSS_SELECTOR, '#pw')
tag_input_id.send_keys('abcd')
tag_input_pw.send_keys('1234')

# 로그인 클릭
tag_input_login = browser.find_element(By.CSS_SELECTOR, '#log\.login')
tag_input_login.click()