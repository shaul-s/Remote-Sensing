import matplotlib as plt
import numpy as np


try:
    raw_data = open(r'C:\Users\Saul\OneDrive - Technion\סמסטר 5\חישה\מעבדה 2\הארה אנכית\alon_0000.asc', 'r', encoding='utf8')
except:
    print('Could not open file')
    quit()

data = raw_data.readlines()

print(data[0])


#if __name__ == "__main__":
