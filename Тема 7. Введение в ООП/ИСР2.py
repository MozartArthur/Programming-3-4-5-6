# Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.

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

  @property
  def nik(self):
    return self.__nik
    
  @nik.setter
  def title(self, value):
    self.__nik = str(value)

  @nik.deleter
  def title(self):
    self.__nik = None

  @property
  def text(self):
    return self.__text
    
  @text.setter
  def text(self, value):
    self.__text = str(value)

  @text.deleter
  def text(self):
    self.__text = None
  
  def show(self):      
    print("author: " + str(self.author))
    print("nik: " + str(self._title))


record_test = Record('Владимир Путин', 'Статья')
comment_test = Comment('Аноним', 'Молодец')
record_test.show_comment(comment=comment_test)