import constants


def index_to_team(index):
    return constants.TEAMS[index-1]


def create_dict_team_and_players():
    num_players_per_team = int(len(constants.PLAYERS) /
                               len(constants.TEAMS))
    dict_team_and_players = {}
    for team in constants.TEAMS:
        list_players = []
        for i in range(num_players_per_team):
            list_players.append(constants.PLAYERS[i])
            dict_team_and_players[team] = list_players
    return dict_team_and_players


def count_num_players(dict_team_and_players, team):
    return len(dict_team_and_players[team])


def extract_player_names(dict_team_and_players, team):
    list_player_names = []
    for player in dict_team_and_players[team]:
        list_player_names.append(player['name'])
    return list_player_names


if __name__ == "__main__":
    while True:
        print('\nBASKETBALL TEAM STATS TOOL\n')
        print('---- MENU----')
        print('')
        print('Here are your choices:')
        print(' 1) Display Team Stats')
        print(' 2) Quit')
        print('')
        option = int(input('Enter an option > '))
        print('')
        if option == 1:
            print('Select a team')
            print('1) Panthers')
            print('2) Bandits')
            print('3) Warriors')
            print('')
            index = int(input('Enter an option > '))
            print('')
            team = index_to_team(index)
            dict_team_and_players = create_dict_team_and_players()
            num_players = count_num_players(dict_team_and_players, team)
            list_player_names = extract_player_names(dict_team_and_players, team)
            print('Team: {} Stats'.format(team))
            print('--------------------')
            print('Total players: {}'.format(num_players))
            print('')
            print('Players on Team: ')
            print(' {}'.format(', '.join(map(str, list_player_names))))
            print('')
            input('Press ENTER to continue... ')
            print('')
        if option == 2:
            print('Thank you!')
            print('')
            break
