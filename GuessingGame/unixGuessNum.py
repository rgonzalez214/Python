# Rolando Gonzalez
# Course:       Unix 3377


# Import the save_to_out_file module so that I can make the function call to print ot file
import save_to_output_file

# import the return_random_number from the generate_random_number module so that
# I can make the function call that generates and stores the random number
from generate_random_number import return_random_number

setValue = 7  # set the max value of turns
randnum = 0  # initialized randnum for function call
save_value = ''  # initiate the value for save_value


# create the main user-defined function
def main():

    # output the first print statement to the user
    print('Guess the random number in 7 turns')

    # set the value of current_ran_val from the random function call
    global current_rand_val
    current_rand_val = return_random_number(randnum)

    # Begin the for loop that iterates within the range of the max value of turns
    for x in range(setValue):

        # generate turns based on the range of x with an offset of +1
        turns = x + 1

        # set the count_down counter to contain the difference between
        # setValue and the current number of iterations of x in the loop.
        count_down = (setValue - 1) - x

        # prompt user for input
        print('Enter a value')

        # retrieve the explicit integer input value from user
        user_input = int(input())

        # if statement to decide on plural form of turns
        if count_down >= 1:
            if count_down == 1:
                plural_turn = ' turn'
            else:
                plural_turn = ' turns'
        else:
            plural_turn = ' turns'

        # if the user's input value does not match the current_rand_val
        # let the user know along with current number of turns left to guess
        # if user inputs a higher value
        if user_input > current_rand_val:
            print('High Guess')
            print('you have ' + str(count_down) + plural_turn + ' left to guess')

            # if user inputs a lower value
        elif user_input < current_rand_val:
            print('Low Guess')
            print('you have ' + str(count_down) + plural_turn + ' left to guess')

        # if the user's input value matches the current_rand_val
        # let the user know along with the number of turns it took then exit with break.
        if user_input == current_rand_val:

            # if statement to decide on plural form of turns
            if turns <= 1:
                save_value = 'you guess right in ' + str(turns) + ' turn'
            else:
                save_value = 'you guess right in ' + str(turns) + ' turns'

            # congratulate the user
            print('Congratulations!')
            print(save_value)

            # pass the turns value to the save_to_output_file module's turns value to print to file
            save_to_output_file.turns = x + 1

            # ask user for their name and save it user_name in save_to_output_file
            save_to_output_file.user_name = input('Enter your name: ')

            # run the file_save function in save_to_output_file
            save_to_output_file.file_save()
            # exit with break
            break

    # once iteration of x reaches setValue, exit and run the you_lose function
    else:
        you_lose()


# you lose function prints out letting the user know they are out of turns.
def you_lose():
    print('The correct value is ' + str(current_rand_val))


# Checks if the python interpreter is accessing this code as the main program, then it runs main()
# allows for future expansion if used from another program.
if __name__ == '__main__':
    main()
