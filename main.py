from operator import itemgetter
import re
import sys

class Student:

    def __init__(self, name, ID, gender, sortByID):
        self.name = name
        self.ID = ID
        self.gender = gender
        self.sortByID = sortByID
    def __lt__(self, kkk): # less than 的縮寫。
        if self.sortByID: # 如果要用學號(ID)做排序的話
            return self.ID < kkk.ID
        return self.name < kkk.name
    def __repr__(self): # 實作該物件要如何呈現
        return"{}:{}".format(self.name, self.ID)


if __name__ == '__main__':
    # pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
    # search_string = "some.user@example.com"
    # match = re.match(pattern, search_string)
    # if match:
    #     domain = match.groups()
    #     print(domain)
    # pattern = "A .$"
    # search_string ="A ."
    # match = re.match(pattern, search_string)
    # if match:
    #     template = "'{}' matches pattern '{}'"
    # else:
    #     template = "'{}' does not match pattern '{}'"
    # print(template.format(search_string, pattern))

    # stud1 = Student("Jack", "003", "male", False)
    # stud2 = Student("Mary", "002", "female", False)
    # stud3 = Student("Henry", "001", "male", False)
    # students = [stud1, stud2, stud3]
    # print("unsort: ", students)
    # students.sort()
    # print("sorted: ", students)

    # l = [('h', 4), ('a', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
    # song_library = [("Phantom Of The Opera", "Sarah Brightman"), ("Knocking On Heaven's Door", "Guns N' Roses"),
    #                 ("Captain Nemo", "Sarah Brightman"),
    #                 ("Patterns In The Ivy", "Opeth"),
    #                 ("November Rain", "Guns N' Roses"),
    #                 ("Beautiful", "Sarah Brightman"),
    #                 ("Mal's Song", "Vixy and Tony")]
    # artists = set()
    #
    # for song, artist in song_library:
    #     artists.add(artist)
    # print(artists)
    # pattern = re.compile("\s")
    # txt = "The rain in Spain"
    # x = pattern.search(txt)
    #
    # print("The first white-space character is located in position:", x.group())
    dic = {"key1" : "value1", "key2" : "value2"}
    for key, value in dic.items():
        print()

