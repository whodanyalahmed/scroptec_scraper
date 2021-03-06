from requests import get
from bs4 import BeautifulSoup


def MakeSoup(data):
    soup = BeautifulSoup(data,'lxml')
    return soup


html = get("https://www.scorptec.com.au/product/cases/all-cases").text
soup = MakeSoup(html)
raw_data = soup.find_all("div",attrs={'class':'inner-detail'})

Desc_soup = MakeSoup(str(raw_data))
desc = Desc_soup.find_all("div",attrs={"class":'desc'})
print(desc)