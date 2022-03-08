from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import logging
import time
from pymongo import MongoClient as mongo

# MongoDB 접속
conn = mongo('mongodb://yym10618:1234@192.168.56.101:27017')
db = conn.get_database('NaverMovie')
collection = db.get_collection('review')

# 로거생성
logger = logging.getLogger('movie_logger')
logger.setLevel(logging.INFO)

# 로거 포맷설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 로그 핸들러
log_handler = logging.FileHandler('./movie_review.log')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

# 가상 브라우저 실행(헤드리스 모드)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)")

rank = 1
page = 1

while True:
    browser = webdriver.Chrome('./chromedriver.exe', options=options)
    logger.info('가상 브라우저 실행...')

    # 네이버 영화 랭킹 이동
    browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&page=%d' % page)
    logger.info('네이버 영화 랭킹 {}페이지 이동...'.format(page))

    # 영화 제목 클릭
    tag_a_titles = browser.find_elements(By.CSS_SELECTOR, '#old_content > table > tbody > tr > td.title > div > a')
    logger.info('{}-{}영화 제목 클릭... :'.format(rank, tag_a_titles[rank - 1].text))
    tag_a_titles[rank-1].click()


    # 영화 평점 클릭
    tag_a_tab5 = browser.find_element(By.CSS_SELECTOR, "#movieEndTabMenu > li > a[title='평점']")
    tag_a_tab5.click()
    logger.info('영화 평점 클릭...')

    # 영화 제목 수집
    title = browser.find_element(By.CSS_SELECTOR, '#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text
    logger.info('영화 제목 수집 : %s' %title)

    # 현재 가상 브라우저의 제어를 영화 리뷰 iframe으로 전환
    browser.switch_to.frame('pointAfterListIframe')
    logger.info('iframe으로 전환...')

    # 영화 리뷰 출력
    count = 1
    while True:
        tag_lis = browser.find_elements(By.CSS_SELECTOR, 'body > div > div > div.score_result > ul > li')
        for li in tag_lis:
            score = li.find_element(By.CSS_SELECTOR, '.star_score > em').text
            reple = li.find_element(By.CSS_SELECTOR, '.score_reple > p > span:last-child').text

            print('{},{},{},{}'.format(count, title, reple, score))

            # MongoDB로 Insert
            #collection.insert_one({'count':count, 'title':title, 'reple':reple, 'score':score})
            logger.info('{},{}'.format(count, title))
            count += 1

        # 다음 페이지 버튼클릭
        try:
            tag_a_next = browser.find_element(By.CSS_SELECTOR, 'body > div > div > div.paging > div > a.pg_next')
            tag_a_next.click()
            logger.info('다음 페이지 클릭...')
        except:
            logger.error('{} 수집완료...'.format(title))
            #browser.close()
            browser.quit()
            break


    # 다음 순위 영화
    rank += 1

    if rank > page * 50:
        # 랭킹 페이지 다음버튼 클릭
        page += 1

        if page > 40:
            # 최종 종료
            break

# MongoDB 종료
conn.close()

logger.info('크롤링 종료...')