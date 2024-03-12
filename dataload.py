import requests
import pandas as pd
from preporcessing import category , get_category_list
from dotenv import load_dotenv
import os
load_dotenv('env/key.env')
key = os.getenv('API_KEY')


#API 요청을 자동화하여 데이터 가져오기
def get_data(start, end):
    url = f'http://openapi.seoul.go.kr:8088/{key}/json/GarakGradePrice/{start}/{end}/'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data['GarakGradePrice']['row'])


def main_load():
    df = pd.DataFrame()
    for i in range(1, 3000, 1000):
        data = get_data(i, i + 999)
        df = pd.concat([df, data])

    df = df[~((df['MAXPRICE']==0) & (df['MAXPRICE']==0) & (df['MAXPRICE']==0))] # 최고가 0인것들 제외(이상치)
    df['kg당 평균 가격'] = (df['AVGPRICE'] / df['UNITQTY']).astype('int')# kg당 평균 가격 구하기
    df['category'] = df['PUMNAME'].apply(category) # category 칼럼 만들기
    df.reset_index(drop=True, inplace=True)
    etc_lst = get_category_list(df)
    return df , etc_lst  
    
if __name__ == "__main__":
    main_load()
    

