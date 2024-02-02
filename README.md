# Problems

## Problem1

- Develop a model that captures the **flow of play as points occur and apply it to one or more of the matches**比赛中随着得分发生的比赛流程，并将其应用到一个或多个比赛中. Your model should identify which player\ is performing better at a given time in the match, as well as how much better they are performing. Provide a visualization based on your model to depict the match flow. Note: in tennis, the player serving has a much higher probability of winning the point/game. You may wish to factor this into your model in some way.
- A tennis coach is skeptical that “momentum” plays any role in the match. Instead, he postulates that swings in play and runs of success by one player are random. Use your model/metric to assess this claim.  **result analysis**

## Problem2

- Coaches would love to know if there are indicators that can help determine when the flow of play is about to change from favoring one player to the other.
  o Using the data provided for at least one match, develop a model that predicts these swings in the match. What factors seem most related (if any)? **Correlation Studies**
  o Given the differential in past match “momentum” swings how do you advise a player going into a new match against a different player **Advice Derived from the Findings**

## Problem3

- Test the model you developed on one or more of the other matches. How well do you predict the swings in the match? If the model performs poorly at times, can you identify any factors that might need to be included in future models? How generalizable is your model to other matches (such as Women’s matches), tournaments, court surfaces, and other sports such as table tennis.**Generalization analysis**
  ·在一个或多个其他比赛上测试你开发的模型。你预测比赛中的转变有多准确？如果模型有时表现不佳，你能识别出可能需要在未来模型中包括的任何因素吗？你的模型对其他比赛（如女子比赛）、锦标赛、球场表面和其他运动（如乒乓球）有多通用？
  Produce a report of no more than 25 pages with your findings and include a one- to two-page memo summarizing your results with advice for coaches on the role of “momentum”, and how to prepare players to respond to events that impact the flow of play during a tennis match.

# Definations

计分：
·比赛：五盘三胜（温布尔登男子比赛）
·盘：一组游戏；6局赢一盘，但玩家必须以两局以上获胜 直到比分达到6 – 6时进行抢七（见下文）
·局：一系列得分；玩家获得4分时获胜，但必须以两分以上获胜。见下文“计分一个游戏”。

计分一个游戏：
·0分 = Love
·1分 = 15
·2分 = 30
·3分 = 40
·平分 = All（例如，“30平”）
·40 – 40 = Deuce（双方获得相同分数，至少各3分）
·发球方赢得Deuce分 = Ad-in（或“优势内”）
·接发球方赢得Deuce分 = Ad-out

发球：球员轮流作为“发球方”（发球的球员）和“接发球方”。在职业网球中，发球方往往有很大优势。每个分球员有两次发球机会，将球发入“发球区”。两次尝试都未能将发球发入比赛区的情况是“双误”，并且返回球的球员获得该分。

·破发 – 当接发球方赢得一局。
·破发点 – 如果接发球方赢得该分，他们将赢得该局的分数。
·保发 – 当发球方赢得游戏。

抢七：每盘比赛在一方赢得6局，并且至少领先两局时结束（即，6 – 4）。如果不是，比赛继续进行，直到达到6 – 6平局。此时进行抢七。在温布尔登，抢七是先赢得7分（必须以2分以上获胜），除了比赛的第五盘是先赢得10分（必须以2分以上获胜）。

休息时间/场地的一侧：在第1局后以及之后每两局，球员更换场地的一侧。从第三局开始，在每次换边时允许90秒休息时间。在抢七中，球员每赢得六分换一次边。球员还在每盘比赛结束后至少休息2分钟。允许医疗暂停和一次洗手间休息。
