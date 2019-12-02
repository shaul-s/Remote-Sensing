import matplotlib.pyplot as plt
import numpy as np
import glob

fileNames = glob.glob(r'vertical_radiance\*.asc')

for idx, file in enumerate(fileNames[::3]):
    try:
        raw_data = open(str(file), 'r', encoding='utf8')
    except:
        print('Could not open file')
        quit()
    data = raw_data.readlines()

    wavelength1 = []; wavelength2 = []; wavelength3 = []
    control_rad1 = []; control_rad2 = []; control_rad3 = []
    object_rad1 = []; object_rad2 = []; object_rad3 = []
    reflectance1 = []; reflectance2 = []; reflectance3 = []

    for j in range(12, len(data), 3):
        arg1 = data[j].split()
        arg2 = data[j+1].split()
        arg3 = data[j+2].split()
        wavelength1.append(float(arg1[0])); wavelength2.append(float(arg2[0])); wavelength3.append(float(arg3[0]))
        control_rad1.append(float(arg1[1])); control_rad2.append(float(arg2[1])); control_rad3.append(float(arg3[1]))
        object_rad1.append(float(arg1[2])); object_rad2.append(float(arg2[2])); object_rad3.append(float(arg3[2]))
        reflectance1.append(float(arg1[3])); reflectance2.append(float(arg2[3])); reflectance3.append(float(arg3[3]))

    #wavelength = np.array(wavelength); control_rad = np.array(control_rad)
    #object_rad = np.array(object_rad); reflectance = np.array(reflectance)
    plt.title(file)
    plt.xlabel('Wavelength')
    plt.ylabel('Reflectance')
    plt.plot(wavelength1, reflectance1, 'r-', label='1'); plt.plot(wavelength2, reflectance2, 'g-', label='2'); plt.plot(wavelength3, reflectance3, 'b-', label='3')
    plt.legend()
    plt.show()






