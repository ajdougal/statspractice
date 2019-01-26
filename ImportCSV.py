import csv

row_dictionary = []
team_enum = set()
game_date_enum = set()
game_dict = dict()
line_count = 0
with file("AustinSol2018-stats.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if line_count is not 0:
            row_dictionary.append(row)
            team_enum.add(row[2])
            game_date_enum.add(row[0])
            if row[2] not in game_dict:
                game_dict[row[2]] = dict()
            if row[0] not in game_dict[row[2]]:
                game_dict[row[2]][row[0]] = []
            game_dict[row[2]][row[0]].append(row)

        line_count += 1

print team_enum
print game_date_enum
print game_dict['Atlanta Hustle']['2018-05-05 18:36']

