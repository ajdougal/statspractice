import csv


csv_path = "AustinSol2018-stats.csv"


# This method takes in a csv path and returns a dictionary with event rows ordered by:
# Team
#    -> Game Date
#         -> Ordered List of Events
def transform_csv_into_dict_ordered_by_team_and_game(csv_path):
    action_enum = set()
    team_enum = set()
    game_date_enum = set()
    output_dict = dict()
    line_count = 0
    with file("AustinSol2018-stats.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            action_enum.add(row[8])
            if line_count is not 0:
                team_enum.add(row[2])
                game_date_enum.add(row[0])
                if row[2] not in output_dict:
                    output_dict[row[2]] = dict()
                if row[0] not in output_dict[row[2]]:
                    output_dict[row[2]][row[0]] = []
                output_dict[row[2]][row[0]].append(row)

            line_count += 1
    return output_dict


def count_number_of_turnovers(point):
    turnovers = 0
    for inner_event in point:
        if inner_event[8] in ("Drop" or "Stall" or "Throwaway"):
            turnovers += 1
    return turnovers


def fill_in_point_dict(inner_td):
    inner_pd = dict()
    for inner_team in inner_td:
        for inner_game in inner_td[inner_team]:
            previous_home = 0
            previous_away = 0
            point_counter = 0
            for event in inner_td[inner_team][inner_game]:
                if previous_home is not int(event[5]) or previous_away is not int(event[6]):
                    point_counter += 1
                    inner_pd[inner_team][inner_game][point_counter]['raw'] = []
                inner_pd[inner_team][inner_game][point_counter]['raw'].append(event)
                previous_home = int(event[5])
                previous_away = int(event[6])
    return inner_pd


def main():
    team_game_dict = transform_csv_into_dict_ordered_by_team_and_game(csv_path=csv_path)
    point_dict = fill_in_point_dict(team_game_dict)
    meta_point_dict = transform_point_dict_into_point_dict_with_metadata(point_dict)
    print meta_point_dict


# This method takes in a game_dict produced by "transform_csv_into_dict_ordered_by_game(csv_path)" and
# transforms it into a dictionary of points with additional structure and metadata used for statistical analyses
# Structure:
#
# point_dict:
#   -> Team
#     -> Game
#       -> Point
#         -> "raw" - Raw array of events
#         -> "meta" - Metadata which includes:
#           -> Game Victory Boolean
#           -> Offense or Defense
#           -> Players list (array)
#           -> Score at end of point boolean
#           -> Turnover count for point
def transform_point_dict_into_point_dict_with_metadata(inner_point_dict):
    return inner_point_dict


main()