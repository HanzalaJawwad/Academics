import pandas as pd
import numpy as np
from minisom import MiniSom
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('exp4&5_data.csv')
X = data.values

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

som = MiniSom(x=5, y=5, input_len=2, sigma=1.0, learning_rate=0.5, random_seed=0)
som.train_random(X_scaled, 100)

plt.figure(figsize=(7, 7))
for i, x in enumerate(X_scaled):
    w = som.winner(x)
    plt.plot(w[0] + 0.5, w[1] + 0.5, 'o', markerfacecolor='C0', markeredgecolor='k', markersize=12)
    plt.text(w[0] + 0.5, w[1] + 0.5, str(i), color='white', ha='center', va='center')

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.title('Self-Organizing Map (SOM) Clustering')
plt.grid(True)
plt.show()
