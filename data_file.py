import xlwt, random
from xlwt import Workbook

day = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
capacity = (10,8) 
start_time_hr = (8,9)
start_time_min = range(0,60)
columns = ("Day", "Start Time", "Auto Capacity", "Class")

wb = Workbook()
sheet1 = wb.add_sheet("Sheet1",cell_overwrite_ok=True)

for i in range(4):
     sheet1.write(0,i,columns[i])

for i in range(1,102):
     sheet1.write(i,0,random.choice(day))
     temp = str(random.choice(start_time_hr))+":"+str(random.choice(start_time_min))
     sheet1.write(i,1,temp)
     sheet1.write(i,2,random.choice(capacity))

wb.save('test_data.xls')
