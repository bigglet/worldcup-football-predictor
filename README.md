# Worldcup Football Predictor

Welcome to the worldcup predictor, containing all the data needed for predicting the 2018 world cup scores. The tournament will work as follows:
1. Use the dataset provided to either:
  - Train a model for prediction
  - Test heuristic algorithms on predicting the winner of games (e.g. highest-elo.py)
  - Or just look at it and make your own csv of who you think will win
2. Use your method from above to output a .csv file for the worldcup group games predicted by your model.
3. Repeat stage (2) after the group stages with the second provided list of games

Scores will be allocated as following:
- 1 point for correct prediction of group stage game
- 2 points for a last 16 correct prediction 
- 3 points for a quater or semi final 
- 5 points for correct prediction of the worldcup final

---

# The Data
The data is output as two csv files, x and y. X is the input data and looks as follows:

Home Team | Away Team | Home Team Elo | Away Team Elo | Year | Friendly (Y/N) | Worldcup (Y/N)
---|---|---|---|---|---|---
England | Brazil | 1974 | 2012 | 2017 | 0 | 1

And the output Y will be as follows:

| Winner |
| ------ |
| -1 |

The possible values are, 1 for a home win, 0 for a draw and -1 for a home loss.

---

Running the scripts. To run all the scipts, make sure you have `scikitlearn`, `numpy` and `pickle installed`. Once these have been installed check that the scripts work by running:
```bash
  python dataset-maker.py
```
and decide whether you want to test on a 80/20 split OR the 2018 worldcup. Then run:
```bash
  python models-simple.py
```
and see what accuracy these simple models obtain.
