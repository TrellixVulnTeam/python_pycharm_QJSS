import openpyxl

if __name__ == '__main__':
    path = 'D:/钉钉文件/部门与角色导入用户(30)个.xlsx'
    # 读取excel文件
    workbook = openpyxl.load_workbook(path)
    # 读取所有sheet(表)
    sheet = workbook.sheetnames
    # 获取某个sheet
    sheet = workbook[sheet[0]]
    # 获取某个cell的值
    cell_val = sheet.cell(row=1, column=1).value
    print(cell_val)