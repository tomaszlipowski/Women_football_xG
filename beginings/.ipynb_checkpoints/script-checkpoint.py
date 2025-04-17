import csv
from parameters import parameters_data
import matplotlib.pyplot as plt


def filtred_data_function(yards):
    filtered_data = []
    #takes all players from 2 csv files
    #5423
    with open("filtred_players.csv", "r", encoding="latin-1") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            #filters through distance
            #119
            if float(row['ShoDist']) >= yards:
                new_row = {
                    'Player': row['Player'],
                    'Avg_Dist': round(float(row['ShoDist']), 2)
                }
                if new_row not in filtered_data:
                    filtered_data.append(new_row)

    final_data = []
    for row in filtered_data:
        for row2 in parameters_data:
            #filtred players found in fifa.csv
            #70
            if row['Player'] == row2['Player'] or row['Player'] == row2['Player_full_name']:
                new_row = {
                    'Player': row['Player'], 
                    'Height': row2['Height'],
                    'Weight': row2['Weight'],
                    'Avg_Dist': row['Avg_Dist']
                }
                
                final_data.append(new_row)

    return final_data

def results(final_data, avg_height, avg_weight):
    total_height = 0
    total_weight = 0
    num_players = len(final_data)

    for player in final_data:
        total_height += player['Height']
        total_weight += player['Weight']

    avg_height.append(round(total_height / num_players, 2))
    avg_weight.append(round(total_weight / num_players, 2))
    print(f'Number of players: {num_players}')
    print(f'Average height: {round(total_height / num_players, 2)}')
    print(f'Average weight: {round(total_weight / num_players, 2)}')

    return avg_height, avg_weight

def plots(ax, yards, parameter, label, color, lim1, lim2):
    ax.bar(yards, parameter, width=0.4, label=label, color=color, edgecolor='black')
    ax.set_xlabel('Yards', fontsize=12)
    ax.set_ylabel(label, fontsize=12)
    ax.set_title(label + ' depending on yards', fontsize=14)
    ax.set_ylim(lim1, lim2)
    ax.set_xticks(yards)
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_facecolor('#e0e0e0')
    ax.grid(True)
    for i, v in enumerate(parameter):
        ax.text(yards[i], v + 0.1, str(v), ha='center', va='bottom', fontsize=10)


avg_height = []
avg_weight = []
yards = [31.5, 30, 28.5, 27]
for yard in yards:
    final_data = filtred_data_function(yard)
    print(f'Yards: {yard}')
    avg_height, avg_weight = results(final_data, avg_height, avg_weight)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
plots(ax1, yards, avg_height, 'Average height', 'steelblue', 171, 179)
plots(ax2, yards, avg_weight, 'Average weight', 'indianred', 73, 76)
plt.tight_layout()
plt.show()

#https://www.kaggle.com/datasets/vivovinco/20212022-football-player-stats
#https://www.kaggle.com/datasets/vivovinco/20222023-football-player-stats?resource=download
#https://www.kaggle.com/datasets/maso0dahmed/football-players-data