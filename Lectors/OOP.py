# Реализация класса

class People:
    # Инициализируем человека
    def __init__(self, name="", surname="", age=0, gender="male"):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def print_info(self):
        # Прописываем информацию о человеке
        print("Class: People\nName={}\nSurname={}"
              "\nAge={}\nGender={}".format(self.name,
                                           self.surname,
                                           self.age,
                                           self.gender))

class Student(People):
    # Инициализация студента
    def __init__(self, name="", surname="", age=0, gender="male", group="no-group"):
        super().__init__(name=name, surname=surname, age=age, gender=gender)
        self.group = group
        print("Init!")

    def print_info(self):
        print("Class: Student\nName={}\nSurname={}"
              "\nAge={}\nGender={}\nGroup={}".format(self.name,
                                                     self.surname,
                                                     self.age,
                                                     self.gender,
                                                     self.group))

# Обращаемся к методам и свойствам этого объекта

new_student = Student(name="Petr", surname="Petrenko",
                      age=19, gender="male", group="ITN-41")

old_student = Student(name="Karina", surname="Borisova",
                      age=20, gender="female", group="ITN-42")

new_student.print_info()
old_student.print_info()
print(new_student.name)
print(new_student.group)

class Employee(People):
    def __init__(self, name="", surname="", age=0, gender="male", post="specialist"):
        super().__init__(name=name, surname=surname, age=age, gender=gender)
        self.post = post

    def print_info(self):
        print("Class: People\nName={}\nSurname={}"
              "\nAge={}\nGender={}\nPost={}".format(self.name,
                                                    self.surname,
                                                    self.age,
                                                    self.gender,
                                                    self.post))

# Интерфейсы
class InformalParserInterface:
    def load_data_source(self, path, file_name):
        # Загрузка данных
        raise NotImplementedError

    def extract_text(self, full_file_name):
        # Вывод данных
        raise NotImplementedError


class Test:
  public_attribute = 42
  __private_attribute = [1, 2 ,3]

print(Test.public_attribute)

print(Test.__private_attribute)
