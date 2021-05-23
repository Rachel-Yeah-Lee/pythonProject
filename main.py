from operator import itemgetter

class Student:
    def __init__(self, name, ID, gender, sortByID):
        self.name = name
        self.ID = ID
        self.gender = gender
        self.sortByID = sortByID
    def __lt__(self, object): # less than 的縮寫
        if self.sortByID: # 如果藥用學號(ID)做排序的話
            return self.ID < object.ID
        return self.name < object.name
    def __repr__(self): # 實作該物件要如何呈現
        return"{}:{}".format(self.name, self.ID)


if __name__ == '__main__':
    stud1 = Student("Jack", "003", "male", False)
    stud2 = Student("Mary", "002", "female", False)
    stud3 = Student("Henry", "001", "male", False)
    students = [stud1, stud2, stud3]
    print("unsort: ", students)
    students.sort()
    print("sorted: ", students)

    l = ["hello", "HELP", "Helo"]
    l.sort(key=str.lower)

    l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
    l.sort(key=itemgetter(1))
