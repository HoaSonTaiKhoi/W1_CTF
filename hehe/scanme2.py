
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('C:/Code C/Python_Hash/Testing_Dataset.csv')
temp_x = data.iloc[:, 115].to_numpy()
print(len(temp_x))
matrix = np.reshape(temp_x, (int(np.sqrt(len(temp_x))), int(np.sqrt(len(temp_x)))))
plt.imshow(matrix, cmap='gray')
plt.axis('off')
plt.show()