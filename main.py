import random, textwrap, os


CONSOLE_WIDTH = 70


def wrapped_print(x):
    print()
    print('\n'.join(textwrap.wrap(x.strip(), width=CONSOLE_WIDTH)))
    print()


def get_shuffled_keys(d):
    """
    Return a randomly ordered list of keys from a dictionary.
    """
    keys = list(d.keys())
    random.shuffle(keys)
    return keys


def get_dict_from_file(folder, file):
    """
    Split file by line and use words before ' ::: ' in each line as front of card
    and words after ' ::: ' as back of card.
    
    Supports multiple commas in 'back' of card.
    """
    d = {}
    with open(folder + '/' + file, 'r') as f:
        for l in f.readlines():
            if not l.startswith('#') and not len(l.strip()) == 0:  # Ignore comments and empty lines
                x = l.split(' ::: ')
                d[x[0]] = x[1]
    return d


def get_cards_from_file(folder, file):
    with open(folder + '/' + file, 'r') as f:
        content = f.readlines()

    cards = {}
    pair_added = False
    for index, line in enumerate(content):
        if not line.startswith('#') and not len(line.strip()) == 0:
            if not pair_added:
                cards[content[index]] = content[index + 1]
                pair_added = True
            else:
                pair_added = False
    
    return cards


def print_file_list(files):
    for i, f in enumerate(files):
        print('{} - {}'.format(i, f))


def ask_user_for_topic(file_list, first_file):
    """
    Asks user to choose a valid number from the dictionary and
    returns the file path for the topic.
    """
    while True:
        if first_file:
            x = input("Choose a topic: ") 
        else:
            x = input("Choose another topic or leave blank to begin: ")

        if x == '' or x == 'q' : return x

        try:
            return file_list[int(x)]
        except ValueError:
            print('Please enter a valid number')
        except IndexError:
            print('\''+ x + '\' is not a valid option.')
            

def get_first_side_from_user():
    while True:
        t = input("Show front [1] or back [2]? ")
        if t == '1' or t == '2':
            return t
        else:
            print('Please enter [1] or [2].')


def display_cards_to_user(card_dict, side):
    """
    Will display cards to user on infinite loop until user
    enters 'q' to quit.
    """
    while True:
        print('*' * CONSOLE_WIDTH)
        print('Shuffling cards... at any time press Enter to continue or q to quit')
        print('*' * CONSOLE_WIDTH)
        services = get_shuffled_keys(card_dict)
        for service in services:
            if side == '2':
                front = card_dict[service]
                back = service
            else:
                front = service
                back = card_dict[service]
            
            wrapped_print(front)
            i = input()
            if i == 'q': return
            wrapped_print(back)
            i = input('-' * CONSOLE_WIDTH)
            if i == 'q': return


def main():
    file_folder = "./csa"

    try:
        file_list = os.listdir(file_folder)
    except FileNotFoundError:
        print('The folder \'{}\' does not exist. Please update the file_folder variable in main() and try again.'.format(file_folder))
        return -1

    # Print file_list
    for i, f in enumerate(file_list):
        print('{} - {}'.format(i, f))

    # Get topics to study from user
    cards = {}
    files_chosen = []
    while True:
        if files_chosen == []:
            file = ask_user_for_topic(file_list, first_file=True)
        else:
            file = ask_user_for_topic(file_list, first_file=False)
        
        if file == 'q':
            print("Quitting...")
            return -1

        if file == '':
            break

        if file not in files_chosen:
            cards = {**cards, **get_cards_from_file(file_folder, file)}
            files_chosen.append(file)
        else:
            print(file + ' has already been added')
        
    if cards == {}:
        print('No topics were selected')
    else:
        side = get_first_side_from_user()
        display_cards_to_user(cards, side)


if __name__=='__main__':
    main()
 