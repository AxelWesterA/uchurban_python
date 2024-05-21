grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list(students)
students_list.sort()

a1 = sum(grades[0])
a2 = sum(grades[1])
a3 = sum(grades[2])
a4 = sum(grades[3])
a5 = sum(grades[4])

b1 = len(grades[0])
b2 = len(grades[1])
b3 = len(grades[2])
b4 = len(grades[3])
b5 = len(grades[4])

c1 = a1/b1
c2 = a2/b2
c3 = a3/b3
c4 = a4/b4
c5 = a5/b5

# a = [a1, a2, a3, a4, a5]
# b = [b1, b2, b3, b4, b5]
c = [c1, c2, c3, c4, c5]


arenge_students_grades = dict(zip(students_list, c))

print(arenge_students_grades)


