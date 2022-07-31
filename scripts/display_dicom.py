import pydicom as pdicom
import matplotlib.pyplot as plt
img=pdicom.dcmread('sample.DCM')
plt.imshow(img.pixel_array[0])
plt.show()