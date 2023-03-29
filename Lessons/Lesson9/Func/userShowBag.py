def userShowBag(user):
    print('\n Hi', user['name'])

    if len(user['bag']) > 0:
        print('in yure bag:')
        for i in user['bag']:
            print(i)

    else:
        print('your bag is empty\n')

    