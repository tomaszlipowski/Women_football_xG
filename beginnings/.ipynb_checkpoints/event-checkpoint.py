from mplsoccer import Sbopen
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D


parser = Sbopen()
df_wc = parser.match(competition_id = 43, season_id = 106)
#df_lineup = parser.lineup(69301)
#df_lineup.info()
#df_event, df_related, df_freeze, df_tactics = parser.event(69301)
#df_related.info()
#df_freeze.info()
#df_tactics.info()
list_match_id = []
for _, match in df_wc.iterrows():
    list_match_id.append(match.match_id)
shots_dict = {}
counter = 0
#1494 shots
#542 long distance
for match in list_match_id:
    df_event = parser.event(match)[0]
    shot_rows = df_event[df_event['type_name'] == "Shot"]
    for _, shot in shot_rows.iterrows():
        counter += 1
        shots_dict[f'shot_{counter}'] = {'x': shot.x, 'y': shot.y, 'result': shot.outcome_name}

x_values = [shot['x'] for shot in shots_dict.values()]
y_values = [shot['y'] for shot in shots_dict.values()]
colors = []
shapes = []
edge_colors = []
for shot in shots_dict.values():
    x = shot['x']
    y = shot['y']
    result = shot['result']
    if x < 102 or y < 18 or y > 62:        
        colors.append('green')
    else:
        colors.append('blue')
    if result == 'Goal':
        shapes.append('^')
        edge_colors.append('black')
    elif result == 'Saved':
        shapes.append('^')
        edge_colors.append('none')
    else:
        shapes.append('o')
        edge_colors.append('none')
fig, ax = plt.subplots(figsize = (6, 7))
for x, y, color, shape, edge_color in zip(x_values, y_values, colors, shapes, edge_colors):
    plt.scatter(x, y, c = color, marker = shape, edgecolors = edge_color)
legend_elements = [
    Line2D([0], [0], marker = 'o', color = 'w', label = 'Shot from Penalty Area', markerfacecolor = 'blue', markersize = 10),
    Line2D([0], [0], marker = '^', color = 'w', label = 'Accurate Shot', markerfacecolor = 'green', markersize = 10),
    Line2D([0], [0], marker = '^', color = 'w', label = 'Goal', markerfacecolor = 'green', markeredgecolor = 'black', markersize = 10)
]
plt.legend(handles=legend_elements, loc='upper left')
plt.xlim(59, 120)
plt.ylim(0, 80)
rect1 = patches.Rectangle((102, 18), 18, 44, linewidth = 4, edgecolor = 'black', facecolor = 'none')
rect2 = patches.Rectangle((114, 30), 6, 20, linewidth = 4, edgecolor = 'black', facecolor = 'none')
circle = patches.Circle((60, 40), radius=10, linewidth = 4, edgecolor = 'black', facecolor = 'none')
ax.add_patch(circle)
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.axvline(x = 60, color = 'black', linestyle = '-', linewidth = 4)
ax.set_facecolor('#e0e0e0')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Strzały na mundialu w Katarze', fontsize = 14)
plt.show()