import matplotlib.pyplot as plt
import numpy as np
import glob


fileNames = glob.glob(r'D:\One Drive - Technion\OneDrive - Technion\סמסטר 5\חישה\מעבדה 2\הארה אנכית\*.asc')

for file in fileNames:
    try :
        raw_data = open(str(file), 'r', encoding='utf8')
    except :
        print('Could not open file')
        quit()
    data = raw_data.readlines()

    wavelength = []
    control_rad = []
    object_rad = []
    reflectance = []

    for j in range(12, len(data)):
        arg = data[j].split()
        wavelength.append(arg[0])
        control_rad.append(arg[1])
        object_rad.append(arg[2])
        reflectance.append(arg[3])

    #wavelength = np.array(wavelength); control_rad = np.array(control_rad)
    #object_rad = np.array(object_rad); reflectance = np.array(reflectance)

plt.axis('equal')
plt.plot(wavelength, object_rad)
plt.show()





