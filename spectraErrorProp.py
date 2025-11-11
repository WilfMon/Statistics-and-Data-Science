import numpy as np

P = np.array([380, 602.5, 1325, 1859])
P_err = np.array([3, 1.5, 3, 0.5])
b = -1478
b_err = 2.4
a = 4.2773
a_err = 0.0041

covab = -9.7857e-03

pba = - ( P - b ) / a ** 2
print(pba)

err = np.sqrt( (P_err ** 2) * (1 / a) ** 2 + (b_err ** 2) * (-1 / a) ** 2 + (a_err ** 2) * pba  ** 2 + 2 * covab * (pba / a))

print(err)

wavelength = (P - b) / a

print(wavelength)