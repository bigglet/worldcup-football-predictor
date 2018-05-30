#model elo as a normal distribution with mean of current elo rating and standard deviation from historical data

import numpy as np
import csv
import pickle

def load_elo():
	with open('elo.pckl', 'rb') as f:
		elo = pickle.load(f)	#open elo ratings derived from the scraping website
	return elo

def load_teams():
	with open('teams.tsv', 'rb') as f:
		teams = []
		r = csv.reader(f)
		for row in r:
			teams.append(row[0])
	return teams	

def get_all_elo(t, elo):
	team_elo = []
	for year in range(1901,2018):
		if(t == 'Korea Republic'):
			t = 'South Korea'
		try:
			team_elo.append(elo[year][t])
		except:
			pass
	return team_elo

def main():
    teams = load_teams()
    elo = load_elo()
    print teams
    for t in teams:
        team_elo = np.array(get_all_elo(t, elo)).astype(np.float)
        std_elo = np.std(team_elo)
        try:
            mean_elo = elo[2018][t]
        except:
            mean_elo = np.mean(team_elo)
        print t, mean_elo, std_elo
        #create a dictionary for teams to norm params
    

if __name__ == '__main__':
	main()

