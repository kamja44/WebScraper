from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from save_file import save_to_file
keyword = input("What do you want to Search for?")


indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr # 리스트끼리 더하기

save_to_file(keyword, jobs)