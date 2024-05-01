import pandas as pd

from fastapi import APIRouter
from sqlalchemy.orm import Session

router = APIRouter(prefix='')

@router.get('/data_info')
def data_info(data_path):
    print(data_path)
    data = pd.read_csv('/Users/kimhongseok/EDA_side/data/3.csv', encoding='cp949')
    print(data.info)

@router.get('/EDA_setting')
def EDA_setting():
    