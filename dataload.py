import requests
import pandas as pd
from preporcessing import category , get_category_list
from dotenv import load_dotenv
from datetime import datetime
import requests
import os
import pandas as pd
import os
load_dotenv('env/key.env')
key1 = os.getenv('API_KEY')
key2 = os.getenv('key')
id = os.getenv('id')

#API 요청을 자동화하여 데이터 가져오기
def get_data(start, end):
    url = f'http://openapi.seoul.go.kr:8088/{key1}/json/GarakGradePrice/{start}/{end}/'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data['GarakGradePrice']['row'])


def main_load():
    df = pd.DataFrame()
    for i in range(1, 3000, 1000):
        data = get_data(i, i + 999)
        df = pd.concat([df, data])

    # df = df[~((df['MAXPRICE']==0) & (df['MAXPRICE']==0) & (df['MAXPRICE']==0))] # 최고가 0인것들 제외(이상치)
    df['단위당 평균 가격'] = (df['AVGPRICE'] / df['UNITQTY']).astype('int')# kg당 평균 가격 구하기
    df['category'] = df['PUMNAME'].apply(category) # category 칼럼 만들기
    df.reset_index(drop=True, inplace=True)
    etc_lst = get_category_list(df)
    return df , etc_lst  
    

def Data_load2():
    basic_data = []
    country_data = []
    for action in ['dailySalesList', 'dailyCountyList']:
        if action == 'dailySalesList':
            url = f'http://www.kamis.or.kr/service/price/xml.do?action={action}&p_cert_key={key2}&p_cert_id={id}&p_returntype=json'
            response = requests.get(url)
            data = response.json()
            basic_data.extend(data['price'])
        else:
            for county in [1101,2100,2200,2300,2401,2501,2601,3111,3211,3311,3511,3711,3911,3113,3613,3714,3814,3145]:
                url = f'http://www.kamis.or.kr/service/price/xml.do?action={action}&p_cert_key={key2}&p_cert_id={id}&p_returntype=json&p_countycode={county}'
                response = requests.get(url)
                data = response.json()
                country_data.extend(data['price'])
    basic_data = pd.DataFrame(basic_data)
    country_data = pd.DataFrame(country_data)
    country_data['value'] = pd.to_numeric(country_data['value'])
    country_data.drop(['county_code','product_cls_code','category_code','productName'],axis=1,inplace=True)
    return basic_data , country_data


if __name__ == "__main__":
    main_load()
    Data_load2()
    

