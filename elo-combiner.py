import pickle
import csv 

def load_elo():
	with open('elo.pckl', 'rb') as f:
		elo = pickle.load(f)	#open elo ratings derived from the scraping website
		print elo
		print type(elo)

	return elo

def load_teams():
	with open('teams.tsv', 'rb') as f:
		teams = []
		r = csv.reader(f)
		for row in r:
			teams.append(row[0])
		print teams
	return teams

def load_matches(teams_2018, elo):
	with open('results.csv', 'rb') as f:
		team_count = [0] * len(teams_2018)
		home_team_list = []
		away_team_list = []
		home_score_list = []
		away_score_list = []
		year_list = []
		reader = csv.reader(f)
		for row in reader:
			home_team = row[1]
			away_team = row[2]
			
			home_score = row[3]
			away_score = row[4]

			if(home_team == 'Korea Republic'):
				home_team = 'South Korea'
				team_count[8] += 1
			if(away_team == 'Korea Republic'):
				away_team = 'South Korea'
				team_count[8] += 1
			year = row[0][6:10]

			if( any( home_team in t for t in teams_2018 ) and any( away_team in t for t in teams_2018 ) ):
				try:
					print(elo[int(year)][home_team]) #HERE
					print(elo[int(year)][away_team]) #HERE
					home_team_list.append(home_team)
					away_team_list.append(away_team)
					home_score_list.append(home_score)
					away_score_list.append(away_score)
					year_list.append(year)
					for t in range(len(teams_2018)):
						if (home_team == teams_2018[t]) or (away_team == teams_2018[t]):
							team_count[t] += 1
				except:
					print "No ELO for the team in this year"

			#check here if there is one of the teams which has changed names i.e West Germany - Germany, USSR - Russia
	return home_team_list, away_team_list, year_list, home_score_list, away_score_list
	
def get_elo(team_list, elo, year_list):
	team_elo = []
	for i in range(len(team_list)):
		team_elo.append(elo[int(year_list[i])][team_list[i]])
	return team_elo

def load_data():
	elo = load_elo()
	teams_2018 = load_teams()
	home_team_list, away_team_list, year_list, home_score_list, away_score_list = load_matches(teams_2018, elo)
	return elo, teams_2018, home_team_list, away_team_list, year_list, home_score_list, away_score_list

def build_csv(x,name):		#convert list of lists to a csv file
	#split dataset into 80/20 for train/test
	print x
	print len(x), len(x[0])
	raw_input(name)

	with open('data-standard/'+name+'.csv', 'wb') as f:
		#write to csv
		writer = csv.writer(f)
		for i in range(len(x[0])):
			r = []
			for j in range(len(x)):
				r.append(x[j][i])
			writer.writerow(r)

def split_and_save_data(x,y):
	l = len(x[0])


	x_train = []
	y_train = []

	x_test = []
	y_test = []

	for i in range( len(x) ):
		x_train.append( x[i][0:int(0.8*l)] )
		x_test.append( x[i][int(0.8*l):l] )

	for i in range( len(y) ):
		y_train.append( y[i][0:int(0.8*l)] )
		y_test.append( y[i][int(0.8*l):l] )

	build_csv(x,'x')
	build_csv(y,'y')

	build_csv(x_train, 'x_train')
	build_csv(y_train, 'y_train')
	
	build_csv(x_test, 'x_test')
	build_csv(y_test, 'y_test')

def main():
	elo, teams_2018, home_team_list, away_team_list, year_list, home_score_list, away_score_list = load_data()

	home_elo = get_elo(home_team_list, elo, year_list)
	away_elo = get_elo(away_team_list, elo, year_list)

	#Create list of lists to build into csv for dataset builder
	x = []
	x.append(home_team_list)
	x.append(away_team_list)
	x.append(home_elo)
	x.append(away_elo)
	x.append(year_list)

	y = []
	y.append(home_score_list)
	y.append(away_score_list)

	print x, y
	print 'Press Enter to Save to CSV!'
	raw_input()
	
	split_and_save_data(x,y)


	print len(home_elo)
	print len(away_elo)

	print len(year_list)

	print len(home_team_list)
	print len(away_team_list)

	print len(home_score_list)
	print len(home_score_list)

if __name__ == '__main__':
	main()
