import csv
from subject import SubjectTable, showSubjectChoice, modifySubject
from teacher import Teacher
from thuattoan import show, ShowFullSchedule, ShowWithTeacherName, ShowWithDayOfWeek, ShowWithCourseID, advancedSort

sb = SubjectTable()
sb.readData()
gv = Teacher()
gv.readData()
advancedSort()

while True:
    show()
    choice = int(input("Chọn lựa chọn: "))
    if choice == 1:
        print('toi da den')
        ShowFullSchedule(gv, sb)
    elif choice == 2:
        ShowWithTeacherName(gv, sb)
    elif choice == 3:
        ShowWithDayOfWeek(gv, sb)
    elif choice == 4:
        ShowWithCourseID(sb)
    elif choice == 5:
        while True:
            showSubjectChoice()
            choice1 = int(input())
            if not modifySubject(choice1, sb):
                break
    elif choice == 6:
        while True:
            Teacher.showTeacherChoice()
            choice1 = int(input())
            if not Teacher.modifyTeacher(choice1, gv):
                break
    elif choice == 7:
        sb.writeData()
    elif choice == 8:
        break
    else:
        print("ERROR!!")
        print("You gay!!!")
        