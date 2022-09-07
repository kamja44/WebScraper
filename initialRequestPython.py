from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"
response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    # print(response.text)  # 웹 사이트의 HTML 코드를 볼 수 있다.
    soup = BeautifulSoup(response.text, "html.parser")
    # class_ == class # class는 예약어이기에 class_로 사용
    jobs = print(soup.find_all("section", class_="jobs"))


# def say_hello(name, age):
#     print(f"Hello {name} you are {age} years old")


# position arguments <- argument의 위치를 알고있다. 즉, 자리에 기반하여 argument를 보낸다.
# say_hello("kamja", 20)
# keyword arguments <- argumet의 이름에 값을 정해준다. arguemnt의 자리가 바뀌어도 상관없다.
# say_hello(age=20, name="kamja")
