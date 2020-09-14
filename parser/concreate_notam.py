import requests
import re
from types.Notamn import Notamn

def parse(url):
    page = requests.get(url)
    return notamns(page.text) #TODO: разбить контент на одельные нотамы

# Регексы:
# (\W|\w)*?(?=\(.*?[NOT].*?) - захватывает UHMD, UHMM, etc.
# (\W|\w)*?(?=\<br\>\s\<br\>) - нужно очистить от <br>
def notamns(pageText):
   return ''