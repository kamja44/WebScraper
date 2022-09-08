from requests import get
from bs4 import BeautifulSoup  # beautifulSoup Document 참고


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        # print(response.text)  # 웹 사이트의 HTML 코드를 볼 수 있다.
        soup = BeautifulSoup(response.text, "html.parser")
        # class_ == class # class는 예약어이기에 class_로 사용
        jobs = soup.find_all("section", class_="jobs")
        # print(len(jobs))
        for job_section in jobs:
            job_posts = job_section.find_all("li")
            job_posts.pop(-1)  # list에서 마지막 항목 <li class="view-all"> 제거
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor["href"]
                company, kind, region = anchor.find_all(
                    "span", class_="company")  # 리스트의 구조와 길이를 알고있을 때 사용가능
                # 리스트에서 오브젝트처럼 추출.py 참고
                title = anchor.find("span", class_="title")
                job_data = {
                    "link": f"https://weworkremotely.com{link}",
                    "company": company.string.replace(","," "),
                    "region": region.string.replace(",", " "),
                    "position": title.string.replace(","," "),
                }
                results.append(job_data)
    return results
