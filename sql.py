import pymysql
from sqlalchemy import create_engine
from dataload import main_load

df = main_load()

def db_import():
    host = 'localhost'
    port = 3306
    user = ''
    password = ''
    database = ''

    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
    conn = engine.connect()
    print('연결 성공')
    df.to_sql(name='sijang3', con=conn, if_exists='replace', index=False) # 새로운 db 데이터 
    print("새로운 db 데이터 넣기 성공.")
    df.to_sql(name='sijang4', con=conn, if_exists='replace', index=False) # Append new data
    print("새로운 데이터 넣기 성공.")
    

if __name__ == "__main__":
    db_import()