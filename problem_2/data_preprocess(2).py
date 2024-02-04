import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/Wimbledon_featured_matches.csv')
performance = pd.read_csv('./data/performance_final.csv')

match_info = df.iloc[:, 0:4]
match_background = df.iloc[:, 4:13]
match_serve = df.iloc[:, 13:15]
match_result = df.iloc[:, 15:20]
match_comment = df.iloc[:, 20:]                                                                              

score_mapping = {'0': 0, '15': 1, '30': 2, '40': 3, 'AD': 4}

for i in range(match_background.shape[0]):
    p1_score = match_background.iloc[i]['p1_score']
    p2_score = match_background.iloc[i]['p2_score']

    if p1_score in score_mapping:
        match_background.at[i, 'p1_score'] = score_mapping[p1_score]
    if p2_score in score_mapping:
        match_background.at[i, 'p2_score'] = score_mapping[p2_score]

p1_score = match_background.iloc[:]['p1_score'].astype(int)
p2_score = match_background.iloc[:]['p2_score'].astype(int)
p1_games = match_background.iloc[:]['p1_games'].astype(int)
p2_games = match_background.iloc[:]['p2_games'].astype(int)
p1_sets = match_background.iloc[:]['p1_sets'].astype(int)
p2_sets = match_background.iloc[:]['p2_sets'].astype(int)

p1_score_win = pd.Series(np.zeros(match_background.shape[0]), name='p1_score_win')
p2_score_win = pd.Series(np.zeros(match_background.shape[0]), name='p2_score_win')
p1_games_win = pd.Series(np.zeros(match_background.shape[0]), name='p1_games_win')
p2_games_win = pd.Series(np.zeros(match_background.shape[0]), name='p2_games_win')
for i in range(match_background.shape[0]):
    if i == 0:
        p1_score_win[i] = 0
        p2_score_win[i] = 0
        p1_games_win[i] = 0
        p2_games_win[i] = 0
    else:
        if (p1_score[i] - p1_score[i - 1] == 1):
            p1_score_win[i] = p1_score_win[i - 1] + 1 if p1_score_win[i-1] >= 0 else 0
        else:
            p1_score_win[i] = p1_score_win[i - 1] - 1 if p1_score_win[i-1] <= 0 else 0
        if (p2_score[i] - p2_score[i - 1] == 1):
            p2_score_win[i] = p2_score_win[i - 1] + 1 if p2_score_win[i-1] >= 0 else 0
        else:
            p2_score_win[i] = p2_score_win[i - 1] - 1 if p2_score_win[i-1] <= 0 else 0
        if (p1_score[i] == 0 and p2_score[i] == 0):
            if (p1_games[i] - p1_games[i - 1] == 1):
                p1_games_win[i] = p1_games_win[i - 1] + 1 if p1_games_win[i-1] >= 0 else 0
            else:
                p1_games_win[i] = p1_games_win[i - 1] - 1 if p1_games_win[i-1] <= 0 else 0
            if (p2_games[i] - p2_games[i - 1] == 1):
                p2_games_win[i] = p2_games_win[i - 1] + 1 if p2_games_win[i-1] >= 0 else 0
            else:
                p2_games_win[i] = p2_games_win[i - 1] - 1 if p2_games_win[i-1] <= 0 else 0
        else:
            p1_games_win[i] = p1_games_win[i - 1]
            p2_games_win[i] = p1_games_win[i - 1]
        
# base mark
p1_base_mark = 50 * (p1_score + 1) / 5 \
                + 30 * (p1_games + 1) / 7 \
                + 20 * (p1_sets + 1) / 3
                
p2_base_mark = 50 * (p2_score + 1) / 5 \
                + 30 * (p2_games + 1) / 7 \
                + 20 * (p2_sets + 1) / 3
                
# advanced factor
p1_score_factor = np.array([0.5 * 0.1 * (i - k) if (i - k) > 2 or (i - k) < -2 else 0 for i, k in zip(p1_score, p2_score)])
p1_games_factor = np.array([0.3 * 0.1 * (i - k) if (i - k) > 2 or (i - k) < -2 else 0 for i, k in zip(p1_games, p2_games)])
p1_sets_factor = np.array([0.2 * 0.1 * (i - k) for i, k in zip(p1_sets, p2_sets)])

p2_score_factor = np.array([0.5 * 0.1 * (i - k) if (i - k) > 2 or (i - k) < -2 else 0 for i, k in zip(p2_score, p1_score)])
p2_games_factor = np.array([0.3 * 0.1 * (i - k) if (i - k) > 2 or (i - k) < -2 else 0 for i, k in zip(p2_games, p1_games)])
p2_sets_factor = np.array([0.2 * 0.1 * (i - k) for i, k in zip(p2_sets, p1_sets)])

p1_advanced_factor = p1_score_factor + p1_games_factor + p1_sets_factor
p2_advanced_factor = p2_score_factor + p2_games_factor + p2_sets_factor
                    
# win factor
p1_win_factor = 0.7 * 0.2 * p1_score_win + 0.3 * 0.2 * p1_games_win
p2_win_factor = 0.7 * 0.2 * p2_score_win + 0.3 * 0.2 * p2_games_win

print(p1_base_mark.shape)
print(p1_advanced_factor.shape)
print(p1_win_factor.shape)
    
p1_mark = p1_base_mark * (1 + p1_advanced_factor)
p2_mark = p2_base_mark * (1 + p2_advanced_factor)

plt.plot(p1_score_win[:300], label='p1_score_win')
plt.plot(p1_games_win[:300], label='p2_score_win')

plt.xlabel('Index')
plt.ylabel('Mark')
plt.title('Marks of p1 and p2')
plt.legend()

plt.show()

