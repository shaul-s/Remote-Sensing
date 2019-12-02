import matplotlib.pyplot as plt
import numpy as np
import glob


"""
getting the data from vertical light source
"""
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
    reflectance_avg = []
    reflectance_std = []
    reflectance_neg = []

    for j in range(12, len(data), 3):
        arg1 = data[j].split()
        arg2 = data[j+1].split()
        arg3 = data[j+2].split()
        wavelength1.append(float(arg1[0])); wavelength2.append(float(arg2[0])); wavelength3.append(float(arg3[0]))
        control_rad1.append(float(arg1[1])); control_rad2.append(float(arg2[1])); control_rad3.append(float(arg3[1]))
        object_rad1.append(float(arg1[2])); object_rad2.append(float(arg2[2])); object_rad3.append(float(arg3[2]))
        reflectance1.append(float(arg1[3])); reflectance2.append(float(arg2[3])); reflectance3.append(float(arg3[3]))
        ref_mes = []
        ref_mes.append(float(arg1[3])); ref_mes.append(float(arg2[3])); ref_mes.append(float(arg3[3]))
        reflectance_avg.append(np.average(ref_mes))
        reflectance_std.append(np.std(ref_mes))
        reflectance_neg.append(np.max(ref_mes) - np.min(ref_mes))

    """
    plotting
    """
    plt.figure(num=None, figsize=(9, 7), dpi=150, facecolor='w', edgecolor='k')
    plt.ylim(-50, 150)
    plt.title(file)
    plt.grid()
    plt.xlabel('Wavelength[nm]')
    plt.ylabel('Reflectance[%]')
    plt.plot(wavelength1, reflectance1, 'r-', label='1')
    plt.plot(wavelength2, reflectance2, 'g-', label='2')
    plt.plot(wavelength3, reflectance3, 'b-', label='3')
    plt.savefig("vertical_spectral_reflectance" + str(idx) + ".png", format="PNG", dpi=150)
    plt.cla()

    plt.ylim(-50, 150)
    plt.title('Average Reflectance ' + file)
    plt.grid()
    plt.xlabel('Wavelength[nm]')
    plt.ylabel('Reflectance[%]')
    plt.plot(wavelength1, reflectance_avg, 'k')
    plt.savefig("vertical_spectral_reflectance_avg" + str(idx) + ".png", format="PNG", dpi=150)
    plt.cla()

    plt.ylim(-50, 150)
    plt.title('Standard Deviation - Reflectance ' + file)
    plt.grid()
    plt.xlabel('Wavelength[nm]')
    plt.ylabel('Reflectance[%]')
    plt.plot(wavelength1, reflectance_std, 'k')
    plt.savefig("vertical_spectral_reflectance_std" + str(idx) + ".png", format="PNG", dpi=150)
    plt.cla()

    plt.ylim(-50, 150)
    plt.title('(Max Obs - Min Obs) - Reflectance ' + file)
    plt.grid()
    plt.xlabel('Wavelength[nm]')
    plt.ylabel('Reflectance[%]')
    plt.plot(wavelength1, reflectance_neg, 'k')
    plt.savefig("vertical_spectral_reflectance_neg" + str(idx) + ".png", format="PNG", dpi=150)
    plt.cla()

"""
getting the data from 30 degree light source
"""
fileNames = glob.glob(r'30_angle_radiance\*.asc')

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
    reflectance_avg = []
    reflectance_std = []
    reflectance_neg = []

    for j in range(12, len(data), 3):
        arg1 = data[j].split()
        arg2 = data[j+1].split()
        arg3 = data[j+2].split()
        wavelength1.append(float(arg1[0])); wavelength2.append(float(arg2[0])); wavelength3.append(float(arg3[0]))
        control_rad1.append(float(arg1[1])); control_rad2.append(float(arg2[1])); control_rad3.append(float(arg3[1]))
        object_rad1.append(float(arg1[2])); object_rad2.append(float(arg2[2])); object_rad3.append(float(arg3[2]))
        reflectance1.append(float(arg1[3])); reflectance2.append(float(arg2[3])); reflectance3.append(float(arg3[3]))
        ref_mes = []
        ref_mes.append(float(arg1[3])); ref_mes.append(float(arg2[3])); ref_mes.append(float(arg3[3]))
        reflectance_avg.append(np.average(ref_mes))
        reflectance_std.append(np.std(ref_mes))
        reflectance_neg.append(np.max(ref_mes) - np.min(ref_mes))

    """
    plotting
    """
    plt.figure(num=None, figsize=(9, 7), dpi=150, facecolor='w', edgecolor='k')
    plt.ylim(-50, 150)
    plt.title(file)
    plt.grid()
    plt.xlabel('Wavelength[nm]')
    plt.ylabel('Reflectance[%]')
    plt.plot(wavelength1, reflectance1, 'r-', label='1')
    plt.plot(wavelength2, reflectance2, 'g-', label='2')
    plt.plot(wavelength3, reflectance3, 'b-', label='3')
    plt.savefig("30deg_spectral_reflectance" + str(idx) + ".png", format="PNG", dpi=150)
    plt.cla()

    plt.ylim(-50, 150)
    plt.title('Average Reflectance ' + file)
    plt.grid()
    plt.xlabel('Wavelength[nm]')
    plt.ylabel('Reflectance[%]')
    plt.plot(wavelength1, reflectance_avg, 'k')
    plt.savefig("30deg_spectral_reflectance_avg" + str(idx) + ".png", format="PNG", dpi=150)
    plt.cla()

    plt.ylim(-50, 150)
    plt.title('Standard Deviation - Reflectance ' + file)
    plt.grid()
    plt.xlabel('Wavelength[nm]')
    plt.ylabel('Reflectance[%]')
    plt.plot(wavelength1, reflectance_std, 'k')
    plt.savefig("30deg_spectral_reflectance_std" + str(idx) + ".png", format="PNG", dpi=150)
    plt.cla()

    plt.ylim(-50, 150)
    plt.title('(Max Obs - Min Obs) - Reflectance ' + file)
    plt.grid()
    plt.xlabel('Wavelength[nm]')
    plt.ylabel('Reflectance[%]')
    plt.plot(wavelength1, reflectance_neg, 'k')
    plt.savefig("30deg_spectral_reflectance_neg" + str(idx) + ".png", format="PNG", dpi=150)
    plt.cla()




