import pandas as pd

practice = pd.DataFrame({'날짜':[], '운동':[], '양':[]})
practice.loc[0] = ['2021-3-1', '달리기', 0.5]
practice.loc[1] = ['2021-3-2', '걷기', 1]
practice.loc[2] = ['2021-3-2', '달리기', 1]
practice.loc[3] = ['2021-3-3', '계단오르기', 0.5]
print(practice)

# 데이터 프레임을 csv 파일로 저장
practice.to_csv("./data/practice1.csv")

# 데이터 프레임을 excel 파일로 저장
# pip install openpyxl
practice.to_excel("./data/practice2.xlsx")

practice.plot()