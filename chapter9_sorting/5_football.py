'''
Manchester United,30,3,5,88,20

team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68
'''
class TeamStat:
    def __init__(self, _name, _points, _goal_difference) -> None:
        self.name: str = _name
        self.points: int = _points
        self.goal_difference: int = _goal_difference


def teamstats_insertion_sort(teamstat_list):
    for sort_range in range(1, len(teamstat_list)):
        for current_index in range(sort_range, 0, -1):
            previous_index = current_index - 1
            if teamstat_list[previous_index].points < teamstat_list[current_index].points:
                break
            if teamstat_list[previous_index].points == teamstat_list[current_index].points and\
                teamstat_list[previous_index].goal_difference < teamstat_list[current_index].goal_difference:
                break

            teamstat_list[previous_index], teamstat_list[current_index] = teamstat_list[current_index], teamstat_list[previous_index]

    return teamstat_list


input_strings = input('Enter Input : ').split('/')
teamstats = []

for team_data in input_strings:
    name, wins, loss, draws, scored, conceded = team_data.split(',')
    points = 3*int(wins) + 1*int(draws)
    goal_difference = int(scored) - int(conceded)
    teamstat = TeamStat(name, points, goal_difference)
    teamstats.append(teamstat)

sorted_teamstats = teamstats_insertion_sort(teamstats)[::-1]
print('== results ==')
for teamstat in sorted_teamstats:
    print(f"['{teamstat.name}', {{'points': {teamstat.points}}}, {{'gd': {teamstat.goal_difference}}}]")
