
# -*- coding: utf-8 -*-

# pyinstaller --onefile --icon=instar.ico --add-binary "chromedriver.exe";"." instarbot.py

from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys, os
from random import randint

import io
with io.open("tag.txt", "r", encoding="utf-8") as my_file:
    user_tags = my_file.read()

with io.open("id.txt", "r", encoding="utf-8") as for_id:
    user_id = for_id.read()

with io.open("pw.txt", "r", encoding="utf-8") as for_pw:
    user_pw = for_pw.read()

tags = (user_tags.split(','))

URL = "http://www.instagram.com/"
EXPLORE = "explore/tags/"

COUNT = 0
LIMIT = 200
DELAY = 80
RANDOM_MIN = 1
RANDOM_MAX = 30

# 로그인
def user_login(ID, PW):
    id_input = driver.find_element_by_name('username')
    id_input.click() 
    id_input.send_keys(ID)
    pw_input = driver.find_element_by_name('password')
    pw_input.click()
    pw_input.send_keys(PW)
    login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login_btn.click()

# 로그인시 나타나는 팝업 지우기
def close_popup():
    save_user_popup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    save_user_popup.send_keys(Keys.ENTER)
    notice_popup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    notice_popup.send_keys(Keys.ENTER)

# 태그 검색하기
def search_tags(keyword):
    driver.get(URL + EXPLORE + keyword)


# 다음 피드로 화살표
def next_feed():
    nextFeed = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
    nextFeed.click()

# 좋아요 누르기!!
def click_like_btn():
    like_list = driver.find_elements_by_xpath('//article//section/span/button')
    likeBtnTxt = driver.find_elements_by_class_name('_8-yf5 ')
    like_pass = False

    global COUNT

    for i in range ( len ( likeBtnTxt ) ) :
        if likeBtnTxt[i].get_attribute("fill") == '#ed4956':
            like_pass = True
            print ("Pass like")
            COUNT -= 1
            break

    like_list = driver.find_elements_by_xpath('//article//section/span/button')
    if like_pass == False :
        try:
            time.sleep(1)
            like_list[0].click()
            time_random_wait = randint(RANDOM_MIN, RANDOM_MAX)

            print(str(COUNT) + "회 좋아요 중")
            print(str(time_random_wait + int(DELAY)) + "초 후 다음 피드로 넘어갑니다.")

            time.sleep(time_random_wait + int(DELAY))  # 작업마다 딜레이
        except:
            COUNT -= 1
            print('좋아요 버튼을 못찾았습니다.')
            hard_work()
    else:
        print('pass')

# 열일해라!! 원하는 만큼 좋아요!
def hard_work():
    for a in range(int(LIKE_COUNT)):
        global COUNT
        
        if COUNT >= int(LIMIT):
            print("끝!")
            break
        
        COUNT += 1

        click_like_btn()
        next_feed()
        

# 게시글 누르고 좋아요 작업 시작하기
def select_board_and_like(recent):
    if recent == False:  # 인기 게시글
        feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
        feed.send_keys(Keys.ENTER)
    else: # 최근 게시글
        feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a')
        feed.send_keys(Keys.ENTER)
    hard_work()

# 시작해라 인스타봇
def start_instar_bot():
    for i in range(len(tags)):
        global COUNT
        if COUNT >= int(LIMIT):
            print("좋아요 작업 종료!")
            break
        search_tags(tags[i])
        time.sleep(2)
        select_board_and_like(True)  # True면 최근 게시글들만, False면 인기게시글들 부터 작업 시작

        if tags[i] == tags[-1]:
            print('태그를 모두 돌아 처음부터 다시 시작합니다.')
            start_instar_bot()
            break


def go_instar():
    global driver
    if  getattr(sys, 'frozen', False): 
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver")
        driver = webdriver.Chrome(chromedriver_path)
    else:
        driver = webdriver.Chrome("./chromedriver")
    driver.get(URL)
    driver.implicitly_wait(10)
    user_login(ID, PW)
    close_popup()
    time.sleep(2)
    start_instar_bot()



win = Tk() 
win.geometry('440x520') 
win.title('instarBot ver 1.0') 

label_id = Label(win ,text="아이디")
label_id.pack()
input_id = Entry(win)
input_id.focus()
input_id.insert(0, user_id)
input_id.pack()

label_pw = Label(win ,text="비밀번호")
label_pw.pack()
input_pw = Entry(win)
input_pw.insert(0, user_pw)
input_pw.pack()

label_like = Label(win ,text="태그당 좋아요 개수 설정")
label_like.pack()
input_like = Entry(win, width=8)
input_like.insert(0, "10")
input_like.pack()

label_limit = Label(win ,text="좋아요 제한 개수 설정")
label_limit.pack()
input_limit = Entry(win, width=8)
input_limit.insert(0, LIMIT)
input_limit.pack()

label_delay = Label(win ,text="딜레이 설정")
label_delay.pack()
input_delay = Entry(win, width=8)
input_delay.insert(0, DELAY)
input_delay.pack()

label_random = Label(win ,text="랜덤 딜레이 설정, 위에는 최소, 아래는 최대")
label_random.pack()
input_random_min = Entry(win, width=4)
input_random_max = Entry(win, width=4)
input_random_min.insert(0, RANDOM_MIN)
input_random_max.insert(0, RANDOM_MAX)
input_random_min.pack()
input_random_max.pack()

label_tag = Label(win ,text="시행할 태그 목록입니다. tag.txt에서 수정하는 걸 추천해요.")
label_tag.pack()
input_tag = Text(win, width=20, height=10, highlightbackground = "black", highlightcolor= "black")
input_tag.insert("current", user_tags)
input_tag.pack()

btn = Button(win)
btn.config(width=20, height=10)
btn.config(text = "클릭해서 좋아요 시작")

def ent_p():
    global ID
    ID = input_id.get()
    
    global PW
    PW = input_pw.get()
    
    global LIKE_COUNT
    LIKE_COUNT = input_like.get()

    global LIMIT
    LIMIT = input_limit.get()

    global DELAY
    DELAY = input_delay.get()
    
    global tags
    tags = input_tag.get("1.0", "end").split(",")

    global RANDOM_MIN
    RANDOM_MIN= int(input_random_min.get())
    
    global RANDOM_MAX
    RANDOM_MAX = int(input_random_max.get())

    go_instar()

btn.config(command= ent_p)
btn.pack()

win.mainloop() 
