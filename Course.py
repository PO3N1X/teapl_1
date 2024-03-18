import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' + \
                         '121.0.0.0 Safari/537.36'}

def get_course(link):
    full_page = requests.get(link, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    course = convert[0].text
    qwe = course.find(',')
    course = course[0:qwe] + '.' + course[qwe + 1:]
    return float(course)
