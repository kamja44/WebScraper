from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't Request Page")
else:
    # response.text <- 소스코드를 text로 가져오고 BeautifulSoup를 이용하여 html로 변환
    soup = BeautifulSoup(response.text, "html.parser")
    # 소스코드(HTML)에서 ul 찾기
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    # job_list 안의 모든 li 찾기(하위의 li태그도 모두 찾는다)
    # jobs = job_list.find_all("li")
    # job_list 안의 즉, ul태그의 자식 li 태그만 찾는다. reqursive=False옵션을 사용해서 지정 가능하다.
    jobs = job_list.find_all("li", recursive=False)
    # print(len(jobs)) # <- 몇개의 데이터를 검색하는지 확인
    # for job in jobs:
