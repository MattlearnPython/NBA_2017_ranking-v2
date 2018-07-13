import numpy as np
import csv

def if_win(score_1, score_2):
    if score_1 > score_2:
        return 1
    else:
        return 0
     
if __name__ == '__main__':
	# Load data
    matchup = []
    with open('NBA_2017.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            matchup.append(row[0]) # row is a list 
    
    # Setup
    n_games = len(matchup) // 4
    record = []
    teams = []
    for i in range(n_games):
        score = []
    
        visitor = matchup[4*i + 0]
        home = matchup[4*i + 2]
    
        if visitor not in teams:
            teams.append(visitor)
       
        score.append(visitor)
        score.append(float(matchup[4*i + 1]))
        score.append(home)
        score.append(float(matchup[4*i + 3]))
    
        record.append(score)

    n_teams = len(teams)

    # Create Markov chains (transition matrix)
    M = np.zeros((n_teams, n_teams))
    for i in range(n_games):

        visitor_idx = teams.index(record[i][0])
        visitor_score = record[i][1]
        home_idx = teams.index(record[i][2])
        home_score = record[i][3]

        total_score = home_score + visitor_score

        M[home_idx, home_idx] += (home_score / total_score + if_win(home_score, visitor_score))
        M[visitor_idx, visitor_idx] += (visitor_score / total_score + if_win(visitor_score, home_score))
        M[home_idx, visitor_idx] += (visitor_score / total_score + if_win(visitor_score, home_score))
        M[visitor_idx, home_idx] += (home_score / total_score + if_win(home_score, visitor_score))
    
    # Normalization
    M = M / np.sum(M, axis=1).reshape((n_teams, 1))
    
    # Calculate state distribution and output the ranking 
    tmp = np.ones((1, n_teams))
    w_0 = tmp / np.sum(tmp)
    T = [10, 100, 1000, 10000]
    rankDict = dict()
    for t in T:
        rank = []
        M_t = np.eye(n_teams)
        for i in range(t):
            M_t = np.dot(M_t, M)
            w_t = np.dot(w_0, M_t)

        sorted_indices = np.argsort(w_t) 
        for j in sorted_indices.tolist()[0]:
            rank.append(teams[j])
        rankDict[str(t)] = rank[::-1]






