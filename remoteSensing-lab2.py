import matplotlib.pyplot as plt
import numpy as np
import glob

fileNames = glob.glob(r'vertical_radiance\*.asc')

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
        wavelength.append(float(arg[0]))
        control_rad.append(float(arg[1]))
        object_rad.append(float(arg[2]))
        reflectance.append(float(arg[3]))

    wavelength = np.array(wavelength); control_rad = np.array(control_rad)
    object_rad = np.array(object_rad); reflectance = np.array(reflectance)

#plt.axis('equal')
plt.plot(wavelength, object_rad, 'r-')
plt.show()





