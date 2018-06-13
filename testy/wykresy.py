import math
import matplotlib.pyplot as plt
from xlrd import open_workbook

def readXLS():

    wb = open_workbook('20171116.xlsx')
    for s in wb.sheets():
        print ('Sheet:',s.name)
        values = []
        for row in range(s.nrows):
            col_value = []
            for col in range(s.ncols):
                value  = (s.cell(row,col).value)
                try : value= int(value) #value = str(int(value))
                except : pass
                col_value.append(value)
            values.append(col_value)
        print(values)



readXLS()



# plt.plot(tzew, czas2)
#
# plt.xlabel("temp. zew. ")
# plt.ylabel("czas [min]")
# plt.title("Krzywa grzewcza")
# plt.grid()
# plt.show()
