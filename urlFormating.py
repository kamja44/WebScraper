websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://youtube.com",
)
# website 변수는 차례대로 각 사이클에서 list 안의 item으로 바뀐다.
for website in websites:
    if not website.startswith("https://"):  # website가 https://로 시작하지 않을 때
        # if website.startswith("https://") == False와 동일한 코드
        website = f"https://{website}"
    print(website)
