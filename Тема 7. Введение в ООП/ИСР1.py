# Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

class Record():
  def __init__(self, author, title):
    self.__title = title
    self.__author = author

  def show_comment(self, comment=object):
    print(f"Ник: {comment.nik}, Текст коммента: {comment.text}")

class Comment():
  def __init__(self, nik, text):
    self.__nik = nik
    self.__text = text