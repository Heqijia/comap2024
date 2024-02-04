import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/result_momemtum.csv')
df2 = pd.read_csv('./data/momentum_factor.csv')
df3 = pd.read_csv('./data/Wimbledon_featured_matches.csv')

p1_momentum = pd.Series(np.zeros(df.shape[0]), name='p1_momentum')
p2_momentum = pd.Series(np.zeros(df.shape[0]), name='p2_momentum')

server = df3['server']
victor = df2['victor']

for i in range(df.shape[0]):
    p1_current = df.iloc[i-1]['p1_current']
    p2_current = df.iloc[i-1]['p2_current']
    
    p1_mark = df.iloc[i]['mark_1']
    p2_mark = df.iloc[i]['mark_2']
    p1_win_factor = df.iloc[i]['p1_win_factor']
    p2_win_factor = df.iloc[i]['p2_win_factor']
    
    p1_momentum[i] = p1_current * p1_win_factor * p1_mark + p1_current + p1_win_factor + p1_mark
    p2_momentum[i] = p2_current * p2_win_factor * p2_mark + p2_current + p2_win_factor + p2_mark
df = pd.concat([df, p1_momentum, p2_momentum], axis=1)

accuracy = 0
for i in range(300):
    if (p1_momentum[i] - p2_momentum[i]) * (victor[i] - 1.5) > 0:
        accuracy += 1
accuracy /= 300

print('Accuracy:', accuracy) 
plt.plot(p1_momentum[:300], label='p1_momentum')
plt.plot(p2_momentum[:300], label='p2_momentum')   
plt.plot(p1_momentum[:300] - p2_momentum[:300], label='p1_momentum - p2_momentum')
plt.plot(victor[:300] - 1.5, label='victor')

plt.xlabel('Index')
plt.ylabel('Momentum')
plt.title('Momentum of p1 and p2')
plt.legend()

plt.show()
    
