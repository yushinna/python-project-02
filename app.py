import constants
import copy
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def clean_data(players):
    updated_players = copy.deepcopy(players)
    # split guardians to list
    for player in updated_players:
        player['guardians'] = player['guardians'].split(' and ')
    # convert height format from str to int
    for player in updated_players:
        player['height'] = int(player['height'].replace(' inches', ''))
    # convert experience format from str to boolen
    for player in updated_players:
        if player['experience'] == 'NO':
            player['experience'] = False
        if player['experience'] == 'YES':
            player['experience'] = True
    return updated_players


def split_players_by_experience(players):
    players_inexperienced = []
    players_experienced = []
    for player in players:
        if player['experience'] == False:
            players_inexperienced.append(player)
        if player['experience'] == True:
            players_experienced.append(player)
    return players_inexperienced, players_experienced


def create_dict_team_and_players(players, teams):
    num_players_per_team = int(len(players) /
                               len(teams))
    dict_team_and_players = {}
    start = 0
    for team in teams:
        dict_team_and_players[team] = players[start:start+num_players_per_team]
        start += num_players_per_team
    return dict_team_and_players


def index_to_team(index, teams):
    return teams[index-1]


def count_num_players(list_selected_team_and_players):
    return len(list_selected_team_and_players)


def extract_player_names(list_selected_team_and_players):
    list_player_names = []
    for player in list_selected_team_and_players:
        list_player_names.append(player['name'])
    return list_player_names


def count_num_inexperienced(list_selected_team_and_players):
    count = 0
    for player in list_selected_team_and_players:
        if player['experience'] == False:
            count += 1
    return count


def calculate_total_height(list_selected_team_and_players):
    list_player_height = []
    for player in list_selected_team_and_players:
        list_player_height.append(player['height'])
    return sum(list_player_height)


def extract_guardian_names(list_selected_team_and_players):
    list_guardian_names = []
    for player in list_selected_team_and_players:
        list_guardian_names.append(', '.join(map(str, player['guardians'])))
    return list_guardian_names


def show_team_stat():
    while True:
        clear_screen()
        print('\nBASKETBALL TEAM STATS TOOL\n')
        print('---- MENU----\n')
        print('Select a team')
        print('1: Panthers')
        print('2: Bandits')
        print('3: Warriors')
        try:
            index = input('\nEnter a team number > ')
            if index != '1' and index != '2' and index != '3':
                raise ValueError
            else:
                selected_team = index_to_team(int(index), constants.TEAMS)
                # merge inexperienced players and experienced players
                list_selected_team_and_players = dict_team_and_players_inexperienced[selected_team]\
                                                 + dict_team_and_players_experienced[selected_team]
                # create stat
                num_players = count_num_players(list_selected_team_and_players)
                list_player_names = extract_player_names(list_selected_team_and_players)
                num_inexperienced = count_num_inexperienced(list_selected_team_and_players)
                num_experienced = num_players - num_inexperienced
                average_height = calculate_total_height(list_selected_team_and_players) / num_players
                list_gurdian_names = extract_guardian_names(list_selected_team_and_players)
                # print stat
                clear_screen()
                print('Team: {} Stats'.format(selected_team))
                print('--------------------')
                print('Total players: {}\n'.format(num_players))
                print('Players on Team: ')
                print(' {}\n'.format(', '.join(map(str, list_player_names))))
                print('Number of inexperienced players: {}\n'.format(num_inexperienced))
                print('Number of experienced players: {}\n'.format(num_experienced))
                print('Average height: {0:.2f} inches\n'.format(average_height))
                print('Guardians of all the players on that team: ')
                print(' {}\n'.format(', '.join(map(str, list_gurdian_names))))
                input('Press ENTER to continue... ')
                break
        except ValueError:
            print('\nInvalid input! Please enter 1, 2 or 3.')
            input('\nPress ENTER to continue... ')


if __name__ == "__main__":
    # load and clean the data
    updated_players = clean_data(constants.PLAYERS)
    players_inexperienced, players_experienced = split_players_by_experience(updated_players)
    dict_team_and_players_inexperienced = create_dict_team_and_players(players_inexperienced, constants.TEAMS)
    dict_team_and_players_experienced = create_dict_team_and_players(players_experienced, constants.TEAMS)
    while True:
        clear_screen()
        print('\nBASKETBALL TEAM STATS TOOL\n')
        print('---- MENU----\n')
        print('Here are your choices:')
        print(' 1: Display Team Stats')
        print(' 2: Quit')
        try:
            option = input('\nEnter an option > ')
            if option != '1' and option != '2':
                raise ValueError
            if option == '1':
                show_team_stat()
            if option == '2':
                print('\nThank you!\n')
                break
        except ValueError:
            print('\nInvalid input! Please enter 1 or 2.')
            input('\nPress ENTER to continue... ')
