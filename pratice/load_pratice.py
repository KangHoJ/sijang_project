from dotenv import load_dotenv
from datetime import datetime
import requests
import os
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px

'''
dailyPriceByCategoryList : 도소매 가격정보
p_product_cls_code : 01소매 , 02도매
p_regday : 날짜
p_item_category_code : (100:식량작물, 200:채소류, 300:특용작물, 400:과일류, 500:축산물, 600:수산물)
'''
key = os.getenv('key')
id = os.getenv('id')
# def DSomea_data_load(): # 일일 소,도매가 불러오기
#     today_date = datetime.now().strftime('%Y-%m-%d') # 오늘날짜
#     domea_data = []
#     somea_data = []
#     for category_code in ['01', '02']: # 도소매
#         for a in ['100', '200', '300', '400', '500', '600']: # 모든 분류다
#             url = f'http://www.kamis.or.kr/service/price/xml.do?action=dailyPriceByCategoryList&p_product_cls_code={category_code}&p_regday={today_date}&p_item_category_code={a}&p_cert_key={key}&p_cert_id={id}&p_returntype=json'
#             response = requests.get(url)
#             data = response.json()
#             if category_code == '02':
#                 domea_data.extend(data['data']['item'])
#             else:
#                 somea_data.extend(data['data']['item'])
#     return pd.DataFrame(domea_data) , pd.DataFrame(somea_data) 


# domea_df, somea_df = DSomea_data_load()
# print(domea_df,somea_df)

'''
(1101:서울, 2100:부산, 2200:대구, 2300:인천, 2401:광주, 2501:대전, 
2601:울산, 3111:수원, 3211:춘천, 3311:청주, 3511:전주, 3711:포항, 3911:제주, 
3113:의정부, 3613:순천, 3714:안동, 3814:창원, 3145:용인) 도매가격 선택가능 지역 
(1101:서울, 2100:부산, 2200:대구, 2401:광주, 2501:대전)
'''
def Data_load2():
    basic_data = []
    country_data = []
    for action in ['dailySalesList', 'dailyCountyList']:
        if action == 'dailySalesList':
            url = f'http://www.kamis.or.kr/service/price/xml.do?action={action}&p_cert_key={key}&p_cert_id={id}&p_returntype=json'
            response = requests.get(url)
            data = response.json()
            basic_data.extend(data['price'])
        else:
            for county in [1101,2100,2200,2300,2401,2501,2601,3111,3211,3311,3511,3711,3911,3113,3613,3714,3814,3145]:
                url = f'http://www.kamis.or.kr/service/price/xml.do?action={action}&p_cert_key={key}&p_cert_id={id}&p_returntype=json&p_countycode={county}'
                response = requests.get(url)
                data = response.json()
                country_data.extend(data['price'])
        
    return pd.DataFrame(basic_data) , pd.DataFrame(country_data) 

basic_data, country_data = Data_load2()
# print(basic_data,country_data)

country_data['value'] = pd.to_numeric(country_data['value'])
top_index = country_data.groupby('category_name')['value'].nlargest(5).index.values
number_list = []
for category_name, value in top_index:
    number_list.append(int(value))
category_cheaper_data = country_data.loc[number_list]
print(category_cheaper_data)

fruit = category_cheaper_data[category_cheaper_data['category_name']=='과일류']
su = category_cheaper_data[category_cheaper_data['category_name']=='수산물']
sik = category_cheaper_data[category_cheaper_data['category_name']=='식량작물']
food = category_cheaper_data[category_cheaper_data['category_name']=='식품']
vegetable = category_cheaper_data[category_cheaper_data['category_name']=='채소류']
livestock  = category_cheaper_data[category_cheaper_data['category_name']=='축산물']
special = category_cheaper_data[category_cheaper_data['category_name']=='특용작물']

# category_name = st.selectbox('카테고리 선택', category_cheaper_data['category_name'])
# selected_data = category_cheaper_data[category_cheaper_data['category_name'] == category_name]
# fig = px.bar(selected_data, x="item_name", y="value")
# st.plotly_chart(fig)