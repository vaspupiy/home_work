
class Person:
    """Person class"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Name and surname: {self.name} {self.surname}'


class Teacher(Person):

    def to_teach(self, subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)


class Pupil(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledges = []

    def to_take(self, subj):
        self.knowledges.append(subj)


class Subject:
    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def my_list(self):
        return self.subjects


s = Subject("maths", "physics", "chemistry")
t = Teacher("Ivan", "Petrov")
print(t)

p_1 = Pupil("Po", "Per")
p_2 = Pupil("Terry", "Bob")
print(f"{p_1}; {p_2}")

t.to_teach(s, p_2, p_1)
print(p_1.knowledges[0].my_list())
