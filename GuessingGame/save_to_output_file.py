user_name = ''  # initiate the user name
turns = 0       # initiate turns


def file_save():

    # if statement to decide on plural form of turns
    if turns > 1:
        string_to_save = (str(user_name) + ' ' + str(turns) + ' turns' + '\n')
    else:
        string_to_save = (str(user_name) + ' ' + str(turns) + ' turn' + '\n')

    # target the path to text file in the current directory
    game_results = 'game_results.txt'

    # open the game_results.txt file
    game_results_file = open(game_results, "a+")

    # write the string_to_save value to the game_results.txt
    game_results_file.write(string_to_save)

    # close the file.
    game_results_file.close()
