import requests
import re

def parse():
    page = requests.get('http://www.caiga.ru/common/AirInter/series_notam/')
    return list(set(links(page.text)))

def links(pageText):
    return re.findall(r'(?<=clicks.php\?uri=).*?(?=&)', pageText)