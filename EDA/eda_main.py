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

datad_shape = data.shape

# col 확인 -> 사용자로부터 예측 모델의 결과 변수를 선택할 수 있게 한다.
print(get_cols(data))
print()
target = input("결과 변수를 선택하세요 : ")

# 데이터타입, 결측치 등을 확인 -> 사용자로부터 결측치의 범위 등을 어떻게 처리할지 선택할 수 있게 한다.
print(data.info())
print()

# 숫자형 데이터에 대한 정보
print(data.describe())
# 문자형 데이터에 대한 정보
print(set(data['등급'].to_list()))
print()