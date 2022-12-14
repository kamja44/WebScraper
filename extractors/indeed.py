from requests import get
from bs4 import BeautifulSoup


def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request page")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("ul", class_="pagination-list")
        if pagination == None:
            return 1  # pagination이 없으면 페이지 1개만 스크래핑한다.
        pages = pagination.find_all("li", recursive=False)
        count = len(pages)
        if count >= 5:
            return 5
        else:
            return count


get_page_count("python")


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs&start=0"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("requesting", final_url)
        response = get(final_url)

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
            for job in jobs:
                # find는 찾은 element를 반환하거나 None를 반환한다. 즉, mosaic-zone이 없어야 찾는 데이터
                zone = job.find("div", class_="mosaic-zone")
                if zone == None:
                    print("job li")
                    # h2 = job.find("h2", class_="jobTitle")
                    # a = h2.find("a")
                    # 위의 h2와 a를 select문을 이용하여 한 문장으로 사용 가능
                    # anchor = job.select("h2 a")
                    anchor = job.select_one("h2 a")
                    title = anchor["aria-label"]
                    link = anchor["href"]
                    company = job.find("span", class_="companyName")
                    location = job.find("div", class_="companyLocation")
                    job_data = {
                        "link": f"https://kr/indeed.com{link}",
                        "company": company.string.replace(",", " "),
                        "location": location.string.replace(",", " "),
                        "position": title.replace(","," "),
                    }
                    results.append(job_data)
            # for result in results:
            #     print(result, "//////\n//////")
                # else:
                #     print("mosaic li")
    return results
