from selenium import webdriver  # webdriver <- python에서 website 실행
from selenium.webdriver.chrome.options import Options


options = Options()
# Relipt에서 실행시키기 위한 코드
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
browser.get("https://kr.indeed.com/jobs?q=python&limit=50")
print(browser.page_source)
