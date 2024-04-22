# EDA_side
# 미친 윤성

# project 목표
csv형태의 파일을 읽어서 데이터 전처리 후 예측모델 생성

# 구현 기능
## 1. 크롤링 - 옵션
- 사용자가 입력한 검색어 혹은 링크를 사용하여 관련 csv파일 다운로드

## 2. EDA
- 사용자에게 미리 데이터의 형태를 보여주고 상호작용한다.
    - df.info() 등으로 데이터 확인
    - 사용자로부터 결측치의 범위 등을 입력받을 수 있게 한다.
    - 결측치, 이상치 대체값의 경우 평균, 최빈값 등을 추천하고 하나 고를 수 있게 하는 것도 좋을듯
- 데이터 전처리
- 결측치, 이상치 처리
    - 수치형 변수 결측치 : 특정 영역을 벗어나거나 데이터가 없는 경우 평균 등의 값으로 채워넣는다.
    - 문자형 변수 결측치 : 값이 없는 경우 혹은 '없음'과 같은 경우 특정 문자를 채워넣는다.
- 최대, 최소 등 데이터 요약
- 상관계수가 큰 변수, 결과에 영향을 많이 주는 변수 등을 찾는다

## 3. 예측모델 생성 - 옵션
- 사용자가 선택한 변수를 예측하는 다중선형회귀모델 생성

## 4. backend
- fastAPI를 사용하여 backend구현

## 5. frontend
- 구현된 기능들을 출력

## 6. Publish
- AWS EC2를 통해 외부에서 접속가능하게 만든다.