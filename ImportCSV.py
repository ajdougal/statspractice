import csv
import pprint

row_dictionary = []
team_enum = set()
game_date_enum = set()
team_dict = dict()
point_dict = dict()
line_count = 0
with file("AustinSol2018-stats.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if line_count is not 0:
            row_dictionary.append(row)
            team_enum.add(row[2])
            game_date_enum.add(row[0])
            if row[2] not in team_dict:
                team_dict[row[2]] = dict()
                point_dict[row[2]] = dict()
            if row[0] not in team_dict[row[2]]:
                team_dict[row[2]][row[0]] = []
                point_dict[row[2]][row[0]] = dict()
            team_dict[row[2]][row[0]].append(row)

        line_count += 1

print len(team_dict['Atlanta Hustle']['2018-05-19 19:06'])
previous_home = 0
previous_away = 0
point_counter = 0
point_dict['Atlanta Hustle'] = dict()
point_dict['Atlanta Hustle']['2018-05-19 19:06'] = dict()
for event in team_dict['Atlanta Hustle']['2018-05-19 19:06']:
    if previous_home is not int(event[5]) or previous_away is not int(event[6]):
        point_counter += 1
        point_dict['Atlanta Hustle']['2018-05-19 19:06'][point_counter] = []
    point_dict['Atlanta Hustle']['2018-05-19 19:06'][point_counter].append(event)
    previous_home = int(event[5])
    previous_away = int(event[6])
pprint.pprint(point_dict, depth=4)

