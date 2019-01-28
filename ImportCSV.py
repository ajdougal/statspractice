import csv
import pprint
import turnover_distribution_report

row_dictionary = []
team_enum = set()
game_date_enum = set()
team_dict = dict()
point_dict = dict()
line_count = 0
action_enum = set()


def count_number_of_turnovers(point):
    turnovers = 0
    for inner_event in point:
        if inner_event[8] in ("Drop" or "Stall" or "Throwaway"):
            turnovers += 1
    return turnovers


with file("AustinSol2018-stats.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        action_enum.add(row[8])
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


def fill_in_point_dict(inner_td, inner_pd):
    for inner_team in inner_td:
        for inner_game in inner_td[inner_team]:
            previous_home = 0
            previous_away = 0
            point_counter = 0
            for event in inner_td[inner_team][inner_game]:
                if previous_home is not int(event[5]) or previous_away is not int(event[6]):
                    point_counter += 1
                    inner_pd[inner_team][inner_game][point_counter] = []
                inner_pd[inner_team][inner_game][point_counter].append(event)
                previous_home = int(event[5])
                previous_away = int(event[6])
    return inner_pd


point_dict = fill_in_point_dict(team_dict, point_dict)
function_file_path = "/Users/adougal/Documents/turnover_distribution_report.csv"
turnover_distribution_report.function_in_other_file(file_path=function_file_path, point_dict=point_dict)


def tally_turnovers_for_game(inner_game):
    num_of_turnovers_enum = set()
    turnover_counter = dict()
    for point_iterator in range(1, 1 + len(inner_game)):
        point = inner_game[point_iterator]
        num_of_turnovers = count_number_of_turnovers(point)
        if num_of_turnovers not in num_of_turnovers_enum:
            turnover_counter[num_of_turnovers] = 0
        num_of_turnovers_enum.add(count_number_of_turnovers(point))
        turnover_counter[count_number_of_turnovers(point)] += 1
    final_our_score = inner_game[len(inner_game)][len(inner_game[len(inner_game)]) - 1][5]
    final_their_score = inner_game[len(inner_game)][len(inner_game[len(inner_game)]) - 1][6]
    victory_boolean = final_our_score > final_their_score
    turnover_counter['Victory'] = victory_boolean
    turnover_counter['Opponent'] = inner_game[1][0][2]
    return turnover_counter


def transform_into_percent(inner_tc):
    point_total = 0
    output_tc = dict()
    for key in inner_tc:
        if key not in ("Victory", "Opponent"):
            point_total += int(inner_tc[key])
    for key in inner_tc:
        if key not in ("Victory", "Opponent"):
            output_tc[key] = round(float(inner_tc[key]) / point_total, 3)
        else:
            output_tc[key] = inner_tc[key]
    return output_tc


for team in point_dict:
    for game in point_dict[team]:
        print tally_turnovers_for_game(point_dict[team][game])
        print transform_into_percent(tally_turnovers_for_game(point_dict[team][game]))




