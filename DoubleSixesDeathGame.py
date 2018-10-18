import random
import math
import numpy
import pandas
import matplotlib.pyplot as plt


def roll_dice():
    is_double_sixes = False
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    if dice_1 == 6 and dice_2 == 6:
        is_double_sixes = True
    return is_double_sixes


def play_game():
    still_alive = True
    the_round = 1
    player_count = 0

    while still_alive is True:
        the_round_power = the_round - 1
        number_of_players = int(math.pow(10, the_round_power))
        print("The round is: " + str(the_round) + " The number of players is: " + str(number_of_players))
        player_list = list(range(number_of_players))
        for player in player_list:
            player_count += 1
            roll = roll_dice()
            if roll is True:
                print("\nThe player that rolled double sixes was: " + str(player_count)
                      + " The final round is: " + str(the_round) + "\n")
                still_alive = False
                break
            else:
                continue

        the_round += 1
    return the_round - 1, player_count


if __name__ == '__main__':

    times_to_play = 10
    play_count_list = list(range(times_to_play))
    round_lost_list = list()
    player_lost_list = list()
    for play in play_count_list:
        round_lost, player_lost = play_game()
        player_lost_list.append(player_lost)
        round_lost_list.append(round_lost)
    print("Mean, Median, StDv of the round the game was lost: " + str(numpy.mean(round_lost_list)) + " | "
          + str(numpy.median(round_lost_list)) + " | " + str(round(float(numpy.std(round_lost_list)), 4)))
    print("Mean, Median, StDv of the player who lost the game was: " + str(numpy.mean(player_lost_list)) + " | "
          + str(numpy.median(player_lost_list)) + " | " + str(round(float(numpy.std(player_lost_list)), 4)))

    # Save the data
    df = pandas.DataFrame()
    df["Round Lost"] = round_lost_list
    df["Player Lost"] = player_lost_list
    df.to_excel("Data.xlsx")

    # # Make a plot
    # f, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.hist(round_lost_list)
    # ax1.set_ylabel("Number")
    # ax1.set_xlabel("The round game was lost")
    # ax2.hist(player_lost_list)
    # ax2.set_ylabel("Number")
    # ax2.set_xlabel("The player who lost")
    # plt.show()
