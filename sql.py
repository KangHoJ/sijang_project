import pymysql
from sqlalchemy import create_engine
from dataload import main_load
from env import settings

df , etc_lst = main_load()

def db_import():
    print('데이터 : ',df)
    print('분류 안된 정보 : ',etc_lst)
    host = settings.DATABASE_CONFIG['host']
    port = settings.DATABASE_CONFIG['port']
    user = settings.DATABASE_CONFIG['user']
    password = settings.DATABASE_CONFIG['password']
    database = settings.DATABASE_CONFIG['database']

    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
    conn = engine.connect()
    print('연결 성공')
    df.to_sql(name='sijang3', con=conn, if_exists='replace', index=False) # 새로운 db 데이터 
    print("새로운 db 데이터 넣기 성공.")
    df.to_sql(name='sijang4', con=conn, if_exists='append', index=False) # Append new data
    print("새로운 데이터 넣기 성공.")
    

if __name__ == "__main__":
    db_import()