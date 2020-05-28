def print_dice_results(dice_results, index, dice_dictionary):

    if dice_results.count(index) < 2:
        print('Vous avez ', dice_results.count(index) , dice_dictionary(index, 1))
    else:
        print('Vous avez ', dice_results.count(index) , dice_dictionary(index, 2))
