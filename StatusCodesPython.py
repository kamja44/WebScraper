from requests import get
websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://youtube.com",
)

resulte = {

}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    # print(response)
    # print(response.status_code)
    if response.status_code >= 500:
        resulte[website] = "SERVER ERROR"
    elif response.status_code >= 400:
        resulte[website] = "USER ERROR"
    elif response.status_code >= 300:
        resulte[website] = "REDIRECT"
    elif response.status_code >= 200:
        resulte[website] = "OK"
    elif response.status_code >= 100:
        resulte[website] = "WAIT"

print(resulte)
