import pandas as pd
import numpy as np

# col을 추출하는 함수
def get_cols(data):
    col_list = data.columns.tolist()
    return col_list

def get_missing_value(data):
    is_null = data.isnull()
    return is_null.sum()


# 데이터 읽어오기
data = pd.read_csv('/Users/kimhongseok/EDA_side/data/3.csv', encoding='cp949')

data_shape = data.shape
print(data_shape)

col_list = data.columns
print(col_list)

for col in col_list:
    col_type = type(data[col][0])
    
    # 데이터의 형태가 수치형인지 확인하여 서로 다르게 데이터를 보여준다. -> 구현방법 연구
    if col_type == '<class \'str\'>': # 문자형인 경우
        print(set(data[col].to_list()))

    else : # 수치형인 경우
        print(col, col_type)
        print(data[col].describe(), end='\n\n') # describe()를 통해 데이터의 요약본을 보여준다.