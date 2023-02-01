import random, textwrap


def custom_print(x):
    print()
    print('\n'.join(textwrap.wrap(x.strip(), width=70)))
    print()


def get_random_keys_from_dict(d):
    """ Return a randomly ordered list of keys from a dictionary. """
    keys = list(d.keys())
    random.shuffle(keys)
    return keys


def get_dict_from_txt(path):
    d = {}
    with open(path, 'r') as f:
        for l in f.readlines():
            x = l.split(',')
            d[x[0]] = ','.join(x[1:])
    return d


def print_files(dict):
    for d in dict:
        print('[' + str(d) + ']', end=" ")
        print(dict[d])


def ask_user_one_or_multiple():
    while True:
        i = input("[1] Single topic or [2] multiple topics? ")
        if i == '1' or i == '2':
            return i
        print("Please enter either [1] for a single topic or [2] for multiple topics.")


def ask_user_for_multiple_topics(dict):
    print("Selecting multiple topics...")
    files = []
    while True:
        f = ask_user_for_topic(dict)
        if f in files:
            print('This topic is already chosen.')
        else:
            files.append(f)
            i = input("""Topic selected. Press \'q\' to start study or enter to choose another: """)
            if i == 'q': return files


def ask_user_for_topic(dict):
    """ Asks user to choose a valid number from the dictionary and
    returns the file path for the topic. """
    while True:
        x = input("Select a topic or leave blank to begin: ")
        if x == '' : return x
        try:
            file = 'txt/' + dict[x] + '.txt'
            return file
        except KeyError:
            print('\''+ x + '\' is not a valid option.')


def get_first_side_from_user():
    while True:
        t = input("Show [1] description first or [2] service first? ")
        if t == '1' or t == '2':
            return t
        else:
            print('Please enter [1] or [2].')


def display_cards_to_user(card_dict, side):
    while True:
        print('*' * 18)
        print('Shuffling cards...')
        print('*' * 18)
        services = get_random_keys_from_dict(card_dict)
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
    files_dict = {
        '1': 'Storage and Data Transfer Services',
        '2': 'Compute and CDN Services',
        '3': 'App Integration and Management Services',
        '4': 'Database Services and Utilities',
        '5': 'Compliance, Data, and Identity Services',
        '6': 'AI, ML, and Security Services',
        '7': 'EC2 and VPC Services',
        '8': 'Pre-defined and Developer Services'
    }

    print_files(files_dict)

    cards = {}
    while True:
        path = ask_user_for_topic(files_dict)
        if path == '': break
        cards = {**cards, **get_dict_from_txt(path)}
        
    if cards == {}:
        print('No topics were selected')
    else:
        side = get_first_side_from_user()
        display_cards_to_user(cards, side)


if __name__=='__main__':
    main()
 