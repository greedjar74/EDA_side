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
#data1 = pd.read_csv('/Users/kimhongseok/EDA_side/data/1.csv', encoding='cp949')
#data2 = pd.read_csv('/Users/kimhongseok/EDA_side/data/2.csv', encoding='cp949')
data3 = pd.read_csv('/Users/kimhongseok/EDA_side/data/3.csv', encoding='cp949')

#data1_shape = data1.shape
#data2_shape = data2.shape
data3_shape = data3.shape

# col 확인
#print(get_cols(data1))
#print(get_cols(data2))
print(get_cols(data3))
print()

# 데이터타입, 결측치 등을 확인
#print(data1.info())
#print()
#print(data2.info())
#print()
print(data3.info())
print()

print(set(data3['등급'].to_list()))
print()