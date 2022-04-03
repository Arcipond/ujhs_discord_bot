from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import re

class mealfind:
    def __init__(self):
        data_meal = ""

    def find(self): #day[0-6] = [월-일]
        date = datetime.today().strftime("%Y%m%d")[2:]
        url = "https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=3fb2d090f9c746e694d7a9097c466af2&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7531047&MLSV_YMD="
        url += str(date)

        html = requests.get(url)
        soup = bs(html.text, 'html.parser')
        make = soup.findAll('ddish_nm')

        data_meal = []
        p=re.compile('[ a-zA-Z가-힗()]+')
        q=re.compile('[0-9]|[.]')

        for i in range(2):
            if(i+1 > len(make)):
                data_meal.append("None")
            else:
                t_list=make[i].text.split('<br/>')
                temp_save=[]
                for j in t_list:
                    temp_save.append([''.join(p.findall(j)),''.join(q.findall(j))])
                data_meal.append(temp_save)

        return data_meal