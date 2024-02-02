
# datasets
1. Wimbledon_featured_matches.csv 原始数据
2. player_12.csv 选手每局表现数据（for training）
   引入新量：
   player1_strength: 选手总得分/全部比赛场数
   p1_distance_run_normal: normalization之后的p1_distance_run_normal
   player1_dist: 选手当局跑动距离/两人加起来的跑动距离
   （这里可以再考虑加个pressure，由前面的set game point差值和当前值加权构成）
   这里只有一个player1 因为这两个player的在赛场上表现的属性是一样的 把他们接在一起了
   目的：用赛场表现数据 预测比赛胜负（见LR.ipynb）
   
4. performance.csv 选手每局表现数据 (result)


# Codes
1. LR: 逻辑回归+performance分析 原来random split有0.78~8.0的acc，后来把测试集单独第一场比赛拿出来变成了0.75 :(
   表现得分计算方式：x=log(单场逻辑回归probability*10*(2381/(2381+4903))+1) if 自己发球，else x=log(单场逻辑回归probability*10*(4903/(2381+4903))+1) if 对手发球
   2381数据集中自己发球输球的次数，4903是自己发球赢球的次数
   current performance: 最近三局x的平均/maximum_point
   overall performance: 累计x的平均 /maximum_point
   maximum_point=log(10*(2381/(2381+4903))+1) 即一个选手在一局中可能获得的最高得分
3. decision_tree：决策树+随机森林（缺点不能弄成概率，也就是后来预测选手表现的基准参照）
4. data_overview：草搞+神经网络（乱七八糟的 output全是nan）
