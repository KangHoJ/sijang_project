import psycopg2
from sqlalchemy import create_engine
from dataload import main_load , Data_load2
from env import settings
# from model import model_process

api_df , etc_lst = main_load()
# final_df = model_process()
basic_df , country_df = Data_load2()

def db_import():
    print('<데이터> : ',api_df)
    print('분류 안된 정보 : ',etc_lst)
    # print('<최종 데이터> :',final_df)
    host = settings.DATABASE_CONFIG['host']
    port = settings.DATABASE_CONFIG['port']
    user = settings.DATABASE_CONFIG['user']
    password = settings.DATABASE_CONFIG['password']
    database = settings.DATABASE_CONFIG['database']

    conn_str = f"host={host} port={port} dbname={database} user={user} password={password}"

    try:
        # PostgreSQL에 연결
        conn = psycopg2.connect(conn_str)
        print('연결 성공')
        # 데이터베이스에 엔진 생성
        engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
        # 데이터를 데이터베이스에 넣기
        api_df.to_sql(name='new_sijang_data', con=engine, if_exists='replace', index=False) # 새로운 db 데이터 
        print("새로운 db 데이터 넣기 성공.")
        api_df.to_sql(name='acc_sijang_data', con=engine, if_exists='append', index=False) # Append new data
        print("새로운 데이터 넣기 성공.")
        print('--------'*15)
        print(basic_df)
        print(country_df)
        basic_df.to_sql(name='test1', con=engine, if_exists='replace', index=False) # 새로운 db 데이터 
        print("새로운 db 데이터 넣기 성공.")
        country_df.to_sql(name='test2', con=engine, if_exists='append', index=False) # Append new data
        print("새로운 데이터 넣기 성공.")

    except Exception as e:
        print("데이터를 데이터베이스에 쓰는 중 에러 발생:", e)

    finally:
        # 연결 닫기
        if conn is not None:
            conn.close()
            print("연결 닫힘")


if __name__ == "__main__":
    db_import()