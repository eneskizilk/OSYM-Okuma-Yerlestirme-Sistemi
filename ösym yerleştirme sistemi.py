class Student:       # This class was created for the first question.

    def __init__(self, sName, sLastname, sNumber):
        self.name = sName
        self.lastname = sLastname
        self.__number = sNumber

    def __str__(self):
        return self.name + " " + self.lastname + " " + str(self.__number)


def readFile1():  # It reads the text file and converts it into a list
    file4 = open("answers.txt", "r", encoding="utf-8")
    answerList = []
    for line in file4:
        line = line.strip()
        line = line.split(" ")
        answerList.append(line)
    file4.close()
    return answerList

answerList = readFile1()


def readFile2():  # It reads the text file and converts it into a list
    file6 = open("key.txt", "r", encoding="utf-8")
    keyList = []
    for line in file6:
        line = line.strip()
        keyList.append(line)
    file6.close()
    return keyList

keyList = readFile2()


def readFile3():  # It reads the text file and converts it into a list
    uni = open("university.txt", "r", encoding="utf-8")
    UniversityList = []
    for line in uni:
        line = line.strip()
        UniversityList.append(line.split(","))
    uni.close()
    return UniversityList

UniversityList = readFile3()

newUniversityList = []        # The difference between this list and the UniversityList is the university score and the number of places in this list, in the form of int. It was created because there were problems while reducing the number of quotas.
for i in range(len(UniversityList)):
    tempList4 = []
    tempList4.clear()
    tempList4.append(UniversityList[i][0])
    tempList4.append(UniversityList[i][1])
    tempList4.append(int(UniversityList[i][2]))
    tempList4.append(int(UniversityList[i][3]))
    newUniversityList.append(tempList4)


def readFile4():  # It reads the text file and converts it into a list
    stud = open("student.txt", "r", encoding="utf-8")
    studentList = []
    for line in stud:
        line = line.strip()
        studentList.append(line.split(" "))
    stud.close()
    return studentList

studentList = readFile4()


# question1     # By reading the file, a dictionary is created with the key part student number value part name surname and student number.
students = {}
file = open("student.txt", "r", encoding="utf-8")
for line in file:
    linearr = line.split()
    name = linearr[1]
    lastname = linearr[2]
    number = linearr[0]
    students[number] = Student(name, lastname, number)
file.close()

# question2
sortedUniversityList = []  # The list with only universities and their base scores is created.
for j in range(len(UniversityList)):
    for i in range(1):
        tempList = []
        tempList.clear()
        tempList.append(UniversityList[j][2])
        tempList.append(UniversityList[j][1])
    sortedUniversityList.append(tempList)

rightSortedUniversityList = sorted(sortedUniversityList,reverse=True)  # universities are ranked from top to bottom according to their base scores.

# question3
resultlist = []
for i in answerList:
    infolist = []
    infolist.append(i[0])  # adding student number
    student = students.get(i[0])  # From the student dictionary you go to the key with the student number.
    infolist.append(student.name)  # adding student name
    infolist.append(student.lastname)  # adding student lastname
    infolist.append(i[1])  # The student's book type is being added.
    d = 0
    y = 0
    b = 0
    if (i[1] == "A"):  # Here students with A book type are selected.

        for s in range(40):
            if (i[2][s] == keyList[0][s]):  # In this line, it is checked whether the answer of the student and the answer of the question are the same.
                d += 1
            elif (i[2][s] != keyList[0][s]):  # If the answers do not match, this question is checked to see if it is empty.
                if (i[2][s] == "*"):
                    b += 1
                else:  # If the answers are unequal and not empty, the question is considered incorrect.
                    y += 1
    if (i[1] == "B"):  # Here students with B book type are selected.

        for s in range(40):
            if (i[2][s] == keyList[1][s]):
                d += 1
            elif (i[2][s] != keyList[1][s]):
                if (i[2][s] == "*"):
                    b += 1
                else:
                    y += 1
    infolist.append(d)  # adding number of correct answer
    infolist.append(y)  # adding number of wrong answer
    infolist.append(b)  # adding number of blank answer
    infolist.append(d - y / 4)  # adding number of net answer
    infolist.append((d - y / 4) * 15)  # adding student score
    infolist.append(UniversityList[int(i[3]) - 1][1])  # adding student's first choice. The reason for -1 here starts counting from index 0 while passing to the university list, but 0 index represents the 1st university.
    infolist.append(UniversityList[int(i[4]) - 1][1])  # adding student's second choice
    resultlist.append(infolist)

text2 = ""            # The list is printed in text to print the information to the file.
for eachLine in resultlist:
    text = ""

    for studentDetail in eachLine:
        text += str(studentDetail) + ","

    text2 += text + "\n"  # The reason for "\ n" is to put it down the line and make it look better.

# question4
studentinfoList = []   # This list just contains a student's score, name, surname and number.
a = 0
for i in range(len(resultlist)):

    for i in range(1):
        tempList = []
        tempList.clear()
        tempList.append(resultlist[a][8])
        tempList.append(resultlist[a][1])
        tempList.append(resultlist[a][2])
        tempList.append(resultlist[a][0])
        a += 1
    studentinfoList.append(tempList)

newStudentinfoList = sorted(studentinfoList, reverse=True)  # Students are ranked according to their scores.

resultlist2 = []  # This list was made for the first placement of the student with a high score while students were placed in universities.
for i in answerList:  # The difference between this list and resultList is that students are ranked according to their scores in this list.
    infolist = []
    d = 0
    y = 0
    b = 0
    if (i[1] == "A"):

        for s in range(40):
            if (i[2][s] == keyList[0][s]):
                d += 1
            elif (i[2][s] != keyList[0][s]):
                if (i[2][s] == "*"):
                    b += 1
                else:
                    y += 1
    if (i[1] == "B"):

        for s in range(40):
            if (i[2][s] == keyList[1][s]):
                d += 1
            elif (i[2][s] != keyList[1][s]):
                if (i[2][s] == "*"):
                    b += 1
                else:
                    y += 1
    infolist.append((d - y / 4) * 15)
    infolist.append(i[0])
    student = students.get(i[0])
    infolist.append(student.name)
    infolist.append(student.lastname)
    infolist.append(i[1])
    infolist.append(d)
    infolist.append(y)
    infolist.append(b)
    infolist.append(d - y / 4)
    infolist.append(UniversityList[int(i[3]) - 1][1])
    infolist.append(UniversityList[int(i[4]) - 1][1])
    infolist.append(False)       # False added for student not being able to place it
    infolist.append(int(i[3]))   # The student's first preferred university's rank in the university list is added.
    infolist.append(int(i[4]))   # The student's second preferred university's rank in the university list is added.
    resultlist2.append(infolist)

newresultlist2 = sorted(resultlist2, reverse=True)  # Students are ranked according to their scores, and placement will be done starting with the student with the highest score.


# question5 and question6
newList2 = []  # List for students.
for i in range(len(UniversityList)):
    newList2.append([])  # Inner lists as many as the number of universities are created.

for j in range(len(resultlist)):

    if (newresultlist2[j][12] > newresultlist2[j][13]):  # This if condition prevents the student from entering the second university if the first preference number is higher than the second. Because the "i" value first finds the smallest in the university list. An if condition was written to prevent this.

        for i in range(len(UniversityList)):

            if (newresultlist2[j][9] == newUniversityList[i][1] and float(newresultlist2[j][0]) >= float(newUniversityList[i][2]) and int(newUniversityList[i][3]) > 0 and newresultlist2[j][11] == False):  # The first condition in if was written to find the value of i, and thanks to this value of i, the base score and quota of the university could be reached. In the last if condition, it is checked whether the student is placed somewhere.
                newList2[i].append(newresultlist2[j][2] + " " + newresultlist2[j][3])  # If the student's conditions meet, it is added to the university list.
                newUniversityList[i][3] = newUniversityList[i][3] - 1  # The quota of the university where the student is placed is reduced by one.
                newresultlist2[j][11] = True  # We have printed an extra false on our newresultlist2 list and here we convert it to True if the student is placed in a university.

        for i in range(len(UniversityList)): # You might think why "for" is written twice here. This is because if the first university's ranking in the list is high, the student would be placed in the second university.

            if (newresultlist2[j][10] == newUniversityList[i][1] and float(newresultlist2[j][0]) >= float(newUniversityList[i][2]) and int(newUniversityList[i][3]) > 0 and newresultlist2[j][11] == False):  #If the student cannot be placed in the first choice, the student's second choice is taken into consideration.
                newList2[i].append(newresultlist2[j][2] + " " + newresultlist2[j][3])
                newUniversityList[i][3] = newUniversityList[i][3] - 1
                newresultlist2[j][11] = True


    else:    # If the student's first choice number is small, the "i" value will be considered for the student's first university and will not be a problem.

        for i in range(len(UniversityList)):

            if (newresultlist2[j][9] == newUniversityList[i][1] and float(newresultlist2[j][0]) >= float(newUniversityList[i][2]) and int(newUniversityList[i][3]) > 0 and newresultlist2[j][11] == False):
                newList2[i].append(newresultlist2[j][2] + " " + newresultlist2[j][3])
                newUniversityList[i][3] = newUniversityList[i][3] - 1
                newresultlist2[j][11] = True

            elif (newresultlist2[j][10] == newUniversityList[i][1] and float(newresultlist2[j][0]) >= float(newUniversityList[i][2]) and int(newUniversityList[i][3]) > 0 and newresultlist2[j][11] == False):
                newList2[i].append(newresultlist2[j][2] + " " + newresultlist2[j][3])
                newUniversityList[i][3] = newUniversityList[i][3] - 1
                newresultlist2[j][11] = True


# question7
departmentList = []  # A list with only departments of universities.
for i in range(len(UniversityList)):
    x = UniversityList[i][1].split("Üniversitesi ",2)  # Each university and department takes the element whose name is written and keeps only the department.
    departmentList.append(x[1])

clearDepartmentList = []  # A new list has been created, all typed once, to avoid reprinting an existing department.
for i in range(len(departmentList)):
    if (departmentList[i] in clearDepartmentList):
        i += 1
    else:
        clearDepartmentList.append(departmentList[i])



print("""
1)Search Student with ID
2)Show university/universities and departments lists
3)Output the result text
4)Show student list by success ranking
5)Show placement results
6)Show tudents who were not be able to placed anywhere
7)Show all departments
8)Exit the program
""")

a = True
while (a): # In case the user wants to do more than one action, an endless loop is created.
    number = input("Please enter the number of the transaction you want to do:")  # Action the user wants to do.
    if (number == "1" or number == "2" or number == "3" or number == "4" or number == "5" or number == "6" or number == "7" or number == "8"):  # This code is written to warn the user if the user enters something outside the menu.

        if (number == "1"):

            studentID = input("Please enter the student number:")
            try:  # If there is no student with the number called, it is written to avoid errors.
                student = students.get(studentID)  # In this line, with the input received from the user, the key part of the desired student's number in the dictionary is entered.
                print("-" + student.name + " " + student.lastname) # We take the value side of the key part we came from.
                print(" ")
            except:
                print("no students found")

        if (number == "2"):
            for i in range(len(rightSortedUniversityList)):
                if(rightSortedUniversityList[0][0]==rightSortedUniversityList[i][0]):  # Compares the scores of the universities that were already ranked with the highest scores of other universities.
                    print("-" + rightSortedUniversityList[i][1],rightSortedUniversityList[i][0])
                    print((len(rightSortedUniversityList[i][1])+4) * "-")
        if (number == "3"):
            resultFile = open("result.txt", "w", encoding="utf-8")
            resultFile.write(text2)  # Typed text is exported as result text file.
            resultFile.close()
            print("result.txt file has been saved.")

        if (number == "4"):
            for i in range(len(newStudentinfoList)):
                print("-" + newStudentinfoList[i][3], newStudentinfoList[i][1], newStudentinfoList[i][2],newStudentinfoList[i][0])
                # Each element of the big list we created in the top row is printed.

        if (number == "5"):
            for i in range(len(newList2)):
                print(UniversityList[i][1], " :\n")     # It shows the names of the universities.
                for j in range(len(newList2[i])):
                    print("-", newList2[i][j])          # It shows what students are enrolled in that university.
                print("-------------------------------------------------------------------------")

        if (number == "6"):
            for i in range(len(students)):
                if (newresultlist2[i][11]==False):      # We added True into the settlement condition, if False did not convert to True there, the student could not settle.
                    print("-" + newresultlist2[i][2] + " " + newresultlist2[i][3])   # The names and surnames of the students who could not be placed are shown.

        if (number == "7"):
            for i in range(len(clearDepartmentList)):
                print("-" + clearDepartmentList[i])  # Each department name is printed.

        if (number == "8"):  # To finish the program
            print("The program is over")
            a = False
    else:
        print("The requested action could not be found.")