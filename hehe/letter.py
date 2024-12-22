import pandas as pd
import matplotlib.pyplot as plt

for i in range(1,101):
    data=pd.read_csv('C:/Code C/Python_Hash/pieces_of_letter/piece_'+str(i)+'.csv')
    temp_x = data.iloc[:, 0].to_numpy()
    temp_y = data.iloc[:, 1].to_numpy()
    plt.scatter(temp_x,temp_y)

plt.title('Biểu đồ Scatter từ CSV')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()

