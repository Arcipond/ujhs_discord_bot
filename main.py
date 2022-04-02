import discord
import requests
from bs4 import BeautifulSoup as bs4
import datetime

today = datetime.datetime.now()
date = today.strftime('%Y%m%d')[2:]
xml = "https://open.neis.go.kr/hub/mealServiceDietInfo?ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7531047&KEY=3fb2d090f9c746e694d7a9097c466af2&MLSV_YMD="+date

xml = requests.get(req_url)
soup = bs4(xml.text,'xml.parser')

food = soup.find('DDISH_NM')