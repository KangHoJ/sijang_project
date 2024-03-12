from dataload import main_load
from sql import db_import
import pandas as pd

df = main_load() # api로 호출되고 , 전처리된 데이터 불러오기 

if __name__ == "__main__":
    db_import() # db로 넣기