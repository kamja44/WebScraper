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
