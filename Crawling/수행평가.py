from datetime import datetime
import os.path
from selenium import  webdriver
from selenium.webdriver.common.by import By

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 기상청 날씨누리 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 파일 디렉터리 생성
dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)

# 파일 생성 및 데이터 파싱
fname = "{:Weather_%Y-%m-%d-%H-%M.csv}".format(datetime.now())
file = open(dir+'/'+fname, 'w', encoding='utf-8')

trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')
for tr in trs:
    t1 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(1) > a').text
    t2 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
    t3 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
    t4 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
    t5 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
    t6 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
    t7 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(7)').text
    t8 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text
    t9 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(9)').text
    t10 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(10)').text
    t11 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(11)').text
    t12 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(12)').text
    t13 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(13)').text
    t14 = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(14)').text

    file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},\n'.format(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14))

file.close()
print('데이터 수집 완료...')


