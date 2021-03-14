def bulka(func):
    def wrapper():
        print('verhniaya bulochka')
        func()
        print('nizhniuaya bulochka')
    return wrapper


def pomidor(func):
    def wrapper():
        print('pomidor')
        func()
    return wrapper


# @bulka
# @pomidor
def kotleta():
    print('kotleta')


kotleta = bulka(pomidor(kotleta))
kotleta()
