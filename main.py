import random, textwrap, os


def custom_print(x):
    print()
    print('\n'.join(textwrap.wrap(x.strip(), width=70)))
    print()


def get_shuffled_keys(d):
    """ Return a randomly ordered list of keys from a dictionary. """
    keys = list(d.keys())
    random.shuffle(keys)
    return keys


def get_dict_from_file(folder, file):
    d = {}
    with open(folder + '/' + file, 'r') as f:
        for l in f.readlines():
            x = l.split(',')
            d[x[0]] = ','.join(x[1:])
    return d


def print_file_list(files):
    for i, f in enumerate(files):
        print('{} - {}'.format(i, f))


def ask_user_for_topic(file_list):
    """ Asks user to choose a valid number from the dictionary and
    returns the file path for the topic. """
    while True:
        x = input("Select a topic or leave blank to begin: ")
        if x == '' : return x
        try:
            return file_list[int(x)]
        except TypeError:
            print('Please enter a valid number')
        except IndexError:
            print('\''+ x + '\' is not a valid option.')
            

def get_first_side_from_user():
    while True:
        t = input("Show description first [1] or service first [2]? ")
        if t == '1' or t == '2':
            return t
        else:
            print('Please enter [1] or [2].')


def display_cards_to_user(card_dict, side):
    while True:
        print('*' * 18)
        print('Shuffling cards...')
        print('*' * 18)
        services = get_shuffled_keys(card_dict)
        for s in services:
            if side == '1':
                card_1 = card_dict[s]
                message_1 = "PRESS ENTER TO VIEW THE SERVICE: "
                card_2 = s
                message_2 = "PRESS ENTER TO VIEW THE NEXT DESCRIPTION: "
            else:
                card_1 = s
                message_1 = "PRESS ENTER TO VIEW THE DESCRIPTION: "
                card_2 = card_dict[s]
                message_2 = "PRESS ENTER TO VIEW THE NEXT SERVICE: "
            
            custom_print(card_1)
            i = input(message_1)
            if i == 'q': return
            custom_print(card_2)
            i = input(message_2)
            if i == 'q': return


def main():
    file_folder = "./txt"

    file_list = os.listdir(file_folder)

    # Print file_list
    for i, f in enumerate(file_list):
        print('{} - {}'.format(i, f))

    # Get topics to study from user
    cards = {}
    files_chosen = []
    while True:
        file = ask_user_for_topic(file_list)
        if file == '':
            break
        else:
            if file not in files_chosen:
                cards = {**cards, **get_dict_from_file(file_folder, file)}
            files_chosen.append(file)
        
    if cards == {}:
        print('No topics were selected')
    else:
        side = get_first_side_from_user()
        display_cards_to_user(cards, side)


if __name__=='__main__':
    main()
 