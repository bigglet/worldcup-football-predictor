import urllib2
import requests
import pickle

def get_web_data(url):
	req = urllib2.Request(url,headers = {'User-Agent': 'Mozilla'})
	page = urllib2.urlopen(req)
	return page.read()

def scrape(start_year,end_year,teams):
	years = {}
	for year in range(start_year,end_year+1):
		print year
		url = 'http://www.eloratings.net/'+str(year)+'.tsv'
		data = get_web_data(url)
		
		years[year] = {}
		
		data_list =  data.split("	")

		for i in range(len(data_list)):
			name_ab = data_list[i]
			if(name_ab.isalpha()):
				elo = data_list[i+1]
				years[year][teams[name_ab]] = elo
	return years

def save(elo):
	with open('elo.pckl', 'wb') as f:
		pickle.dump(elo,f)
	with open('elo.pckl', 'rb') as f:
		dic = pickle.load(f)
	print("Finished saving data")

def get_teams():
	url = 'http://www.eloratings.net/en.teams.tsv'
	req = urllib2.Request(url,headers = {'User-Agent': 'Mozilla'})
	page = urllib2.urlopen(req)
	d = page.read()
	teams_list = d.split("\n")
	team_dict = {}
	for i in range(len(teams_list)):	
		abrev = teams_list[i].split("\t")[0]
		if '_' not in abrev and abrev is not '':
			team_dict[abrev] = teams_list[i].split("\t")[1]	
	return team_dict

def main():
	teams = get_teams()
	elo = scrape(1901,2018, teams)
	#save(elo)


if __name__ == '__main__':
	main()

