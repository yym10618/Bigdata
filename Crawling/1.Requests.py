"""
날짜 : 2022/02/28
이름 : 양용민
내용 : 파이썬 HTML 페이지 요청 실습

# 패키지 설치 : Terminal -> pip3 install requests입력
"""

import requests as req

# 페이지 요청하기
html = req.get('http://naver.com').text
print(html)

print('-'*20)

test = req.get('http://chhak.or.kr/test.html').text
print(test)