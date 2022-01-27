from bs4 import BeautifulSoup
import requests
user = input("What job would you want? ")
url = f"https://ca.indeed.com/jobs?q={user}&l=Cambridge,%20ON&vjk=33efd0c38300448e&advn=4811491706743809"
get = requests.get(url).text
soup = BeautifulSoup(get,"html.parser")

titles = soup.find_all("div",attrs={"class": "heading4 color-text-primary singleLineTitle tapItem-gutter"})
titles_2 = soup.find_all("div",attrs={"class": "heading6 company_location tapItem-gutter companyInfo"})
titles_3 = soup.find_all("div",attrs={"class": "salary-snippet"})

for title_3 in titles_3[:3]:
    for title_2 in titles_2[:3]:
        for title in titles[:3]:
            print(f"\nName: {title.text}"
                  f"\nCompany Name: {title_2.text}"
                  f"\nSalary: {title_3.text}")
            print("==================================================================")