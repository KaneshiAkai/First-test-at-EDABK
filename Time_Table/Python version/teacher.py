import csv

class Day:
    def __init__(self):
        self.lessions = [True] * 13
    def setDefaultLessions(self):
        for i in range(13):
            self.lessions[i]=True
    def setBusyLessions(self, startBusy, endBusy):
        for i in range(startBusy, endBusy + 1):
            self.lessions[i]=False
    def checkBusy(self, start, end):
        for i in range(start, end + 1):
            if not self.lessions[i]:
                return False
        return True
    
class Schedule:
    def __init__(self):
        self.dayOfWeek = [True] * 7
        self.day = [Day() for _ in range(7)]
    def setDefaultDay(self):
        for i in range(7):
            self.dayOfWeek[i] = True
        for i in range(7):
            self.day[i].setDefaultLessions()
    def checkBusy(self, start, end, numOfDay):
        return self.day[numOfDay].checkBusy(start,end)
    def setBusy(self,start,end,numOfDay):
        self.day[numOfDay].setBusyLessions(start,end)  

class Teacher:
    
    def __init__(self,name="",telNum="",subject1="",subject2=""):
        self.name = name
        self.telNum = telNum
        self.subject1 = subject1
        self.subject2 = subject2
        self.schedule = Schedule()
        
    listTeacher = []
    
    def setDefaultSchedule(self):
        self.schedule.setDefaultDay()
    
    def readData(self):
        try:
            print('Tri dep trai tuyet voi !!!')
            with open('Time_Table\Python version\giaovienData.csv', mode='r') as file:
                for line in file:
                    name, telNum, subject1, subject2 = line.strip().split(',')
                    new_teacher = Teacher(name, telNum, subject1, subject2)
                    new_teacher.setDefaultSchedule()
                    Teacher.listTeacher.append(new_teacher)
        except FileNotFoundError:
            print('Error!') 
        
    def Teacher(self):
        print("List of teachers: ")
        for teacher in Teacher.listTeacher:
            print(f"Name: {teacher.name}")
            print(f"Number: {teacher.telNum}")
            print(f"Subject 1: {teacher.subject1}")
            print(f"Subject 2: {teacher.subject2}")
            
    def showTeacherChoice():
        print("1. Add teacher")
        print("2. Remove teacher")
        print("3. Sort by teacher name")
        print("4. Exit")
        
    def modifyTeacher(choice, tc):
        if choice==1:
            name = input("Enter the name of teacher: ")
            phone = input("Enter the number of teacher: ")
            subject1 = input("Enter the first subject: ")
            subject2 = input("Enter the second subject: ")
            newTeacher = Teacher(name,phone,subject1,subject2)
            Teacher.listTeacher.append(newTeacher)
            print("Completely adding new Teacher !")
            return True
        elif choice==2:
            print("List of teachers")
            for nm, teacher in enumerate(Teacher.listTeacher):
                print(f"{nm}. {teacher.name}")
            print ("Removing teacher by index \n Enter the index of teacher that want to remove: ")
            deepchoice = int(input())
            if deepchoice > len(Teacher.listTeacher) - 1:
                print("Invalid number!")
                while True:
                    print("press \"ok\" to continue")
                    press=input()
                    if press == 'ok':
                        return True  
            for teacher in Teacher.listTeacher:
                if teacher.name == Teacher.listTeacher[deepchoice].name:
                    del Teacher.listTeacher[deepchoice]
                    print("Completely removing teacher !")
        elif choice==3:
            Teacher.sortByName()
            print("Teachers sorted by name successfully !")
            while True:
                print("press \"ok\" to continue")
                press=input()
                if press == 'ok':
                    return
        elif choice == 4:
            return False
            
    def sortByName():
        Teacher.listTeacher.sort(key = lambda teacher: teacher.name)
    
    def getName(self):
        return self.name

    def getSubject1(self):
        return self.subject1

    def getSubject2(self):
        return self.subject2

    def checkBusy(self, start, end, numOfDay):
        return self.schedule.checkBusy(start, end, numOfDay)

    def setBusy(self, start, end, numOfDay):
        self.schedule.setBusy(start, end, numOfDay)