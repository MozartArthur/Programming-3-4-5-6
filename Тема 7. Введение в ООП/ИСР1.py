# Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

class Record: # класс запись

    def __init__(self, author, text):
        self.__author = author
        self.__text = text

class Comment (Record): # класс комментарий (наследует класс запись)

    def __init__(self, nickname, textcom):
        self.__nickname = nickname
        self.__textcom = textcom
