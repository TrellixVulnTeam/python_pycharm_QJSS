# -*-coding:utf-8 -*-
import pandas as pd

def read_excel(file, **kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file, **kwargs)
        data_dict = data.to_dict('records')
    finally:
        return data_dict

if __name__ == '__main__':
    sheet1 = read_excel('交付记录02.xlsx')
    sheet2 = read_excel('交付记录02.xlsx', sheet_name ='Sheet2')
    print(sheet1)
    print(sheet2)