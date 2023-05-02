
from selenium import webdriver
from selenium.webdriver.common.by import By


# 웹드라이버 경로
Chrome = webdriver.Chrome()

# 대학교 온라인 수업 홈페이지
Chrome.get("https://eclass.kbu.ac.kr/")

# ID 값들중 input-username이라는 id 가져오기
id = Chrome.find_element(By.ID, "input-username")
# 학번 id 값 받기
id.send_keys(input("학번을 입력해주세요: "))

# ID 값들중 input-username이라는 id 가져오기
pwd = Chrome.find_element(By.ID, "input-password")
# 비번 값 받기
pwd.send_keys(input("비밀번호를 입력해주세요: "))

# loginbutton 이름 클릭
login = Chrome.find_element(By.XPATH, "//*[@name='loginbutton']")
login.click()

# 로그인 성공

# Class들중 my-course-lists coursemos-layout-0의 이름을 가진 ul 리스트 가져오기
list1 = Chrome.find_elements(By.XPATH, "//*[@class='my-course-lists coursemos-layout-0']/li")



