import xlrd
import xlwt
import numpy as np
import xlsxwriter

#读数据
data1 = xlrd.open_workbook('E:\桌面\第三个工作\LAGCN-master\LAGCN-master\data/m_d.xlsx')
table1 = data1.sheets()[0]
row1 = table1.nrows
col1 = table1.ncols
book1 = xlwt.Workbook()
sheet1 = book1.add_sheet('test', cell_overwrite_ok=True)


d_n = []
for i in range(0,591):
    tmp_sum = 0
    for j in range(0,853):
        tmp_sum = tmp_sum + table1.cell(j,i).value
        # d_n[i] = sum(table1.cell(i,j).value)
    d_n.append(tmp_sum)


count = np.zeros((2, int(max(d_n))), dtype=int)
count[0,:] = np.array(range(1, 375))
for i in range(len(d_n)):
    index = int(d_n[i])
    count[1, index-1] = count[1, index-1] + 1

workbook = xlsxwriter.Workbook('E:\桌面/degree_m.xlsx')
worksheet = workbook.add_worksheet('sheet1')
for i in range(0,374):
    for j in range(0,2):
        worksheet.write(j, i, count[j][i])
workbook.close()


