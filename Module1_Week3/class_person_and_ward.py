from itertools import count
from abc import ABC, abstractmethod

class Person(ABC):
  @abstractmethod
  def __init__(self, name, yob):
    self._name = name
    self._yob = yob

  @abstractmethod
  def describe(self):
    pass

class Student(Person):
  def __init__(self, name, yob, grade):
    super().__init__(name, yob)
    self._grade = grade

  def describe(self):
    return print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Teacher(Person):
  def __init__(self, name, yob, subject):
    super().__init__(name, yob)
    self._subject = subject

  def describe(self):
    return print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Doctor(Person):
  def __init__(self, name, yob, specialist):
    super().__init__(name, yob)
    self._specialist = specialist

  def describe(self):
    return print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:
  def __init__(self, name):
    self._name = name
    self._list_people = []

  def add_person(self, person):
    self._list_people.append(person)

  def describe(self):
    print(f"Ward Name : {self._name}")
    for p in self._list_people:
      print(p.describe())

  def count_doctor(self):
    count = 0
    for d in self._list_people:
      if isinstance(d, Doctor):
        count += 1
    return count

  def sort_age(self):
    self._list_people.sort(key=lambda x: x._yob, reverse = True)

  def compute_average(self):
    count = 0
    sum_teacher = 0
    for t in self._list_people:
      if isinstance(t, Teacher):
        count += 1
        sum_teacher += t._yob
    return sum_teacher / count




student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
student1 . describe ()

teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
teacher1 . describe ()

doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
doctor1 . describe ()


teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward (name =" Ward1 ")
ward1.add_person ( student1 )
ward1.add_person ( teacher1 )
ward1.add_person ( teacher2 )
ward1.add_person ( doctor1 )
ward1.add_person ( doctor2 )
ward1.describe ()

print ( f"Number of doctors : { ward1 . count_doctor ()}")

ward1 . sort_age ()
ward1 . describe ()


print ( f"Average year of birth ( teachers ): { ward1 . compute_average ()}")