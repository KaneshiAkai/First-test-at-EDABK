import csv
import sys
from subject import SubjectTable
from teacher import Teacher

listSubject = SubjectTable.listSubject
def ShowFullSchedule(tea, sub):
    listSubject = sub.listSubject
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    print("| IDClass  | CourseID      | Name                                           |   Thu    | Time                 | Study Place          | Teacher's name         |")
    
    for subject in listSubject:
        print(f"| {subject.getID():<8} | {subject.getCourseID():<13} | {subject.getName():<46} | {subject.getDayOfWeek():<8} | {subject.getTime():<20} | {subject.getPlace():<20} | {subject.getTeacherName():<22} |")
    
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    while True:
            print("press \"ok\" to continue")
            press=input()
            if press == 'ok':
                return
    
def ShowWithTeacherName(tea, sub):
    listSubject = sub.listSubject
    print("List of tea:")
    for num, teacher in enumerate(Teacher.listTeacher):
        print(f"{num}. {teacher.getName()}")
    choice = int(input("Enter the number of the teacher: ")) 
    if choice > len(Teacher.listTeacher) - 1:
        print("Invalid number!")
        while True:
            print("press \"ok\" to continue")
            press=input()
            if press == 'ok':
                return True  
    selected_teacher = Teacher.listTeacher[choice]
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    print("| IDClass  | CourseID      | Name                                           |   Thu    | Time                 | Study Place          | Teacher's name         |")
    
    for subject in listSubject:
        i=0
        if subject.getTeacherName() == selected_teacher.getName():
            print(f"| {subject.getID():<8} | {subject.getCourseID():<13} | {subject.getName():<46} | {subject.getDayOfWeek():<8} | {subject.getTime():<20} | {subject.getPlace():<20} | {subject.getTeacherName():<22} |")
        i+=1
        
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    while True:
            print("press \"ok\" to continue")
            press=input()
            if press == 'ok':
                return
    
def advancedSort():
    i = j = 0
    for subject in listSubject:
        subject.setStatus(False)
    for subject in listSubject:
        for teacher in Teacher.listTeacher:
            if (checkFree(teacher, subject)):
                subject.setStatus(True)
                subject.setTeacherName(teacher.getName())
                break
            j+=1
        i+=1
            
def checkFree(tea, sub):
    if ((tea.getSubject1() == sub.getName()) or (tea.getSubject2() == sub.getName())):
        cut1 = ""
        cut2 = ""
        c = sub.getTime()
        for i in range(4):
            cut1 += c[i]
        for i in range(5, 9):
            cut2 += c[i]
        _start = compare(cut1)
        _end = compare(cut2) - 1;
        _day = int(sub.getDayOfWeek())    #ở đây Python khá hay, có build in đổi sang integẻ
        if (tea.checkBusy(_start, _end, _day) == True):
            tea.setBusy(_start,_end,_day)
            return True
    return False
    
def compare(s):
    if s == "0645":
        return 1
    if s == "0730":
        return 2
    if s == "0815" or s == "0825":
        return 3
    if s == "0910" or s == "0920":
        return 4
    if s == "1005" or s == "1015":
        return 5
    if s == "1100":
        return 6
    if s == "1145" or s == "1230":
        return 7
    if s == "1315":
        return 8
    if s == "1400" or s == "1410":
        return 9
    if s == "1455" or s == "1505":
        return 10
    if s == "1550" or s == "1600":
        return 11
    if s == "1645":
        return 12
    if s == "1730":
        return 13
    return 0

def ShowWithDayOfWeek(gv, DayOfWeek):
    choice = input("Chọn ngày trong tuần: ")
    
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    print("| IDClass  | CourseID      | Name                                           |   Thu    | Time                 | Study Place          | Teacher's name         |")
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    
    for subject in listSubject:
        if subject.getDayOfWeek() == choice:
            print(f"| {subject.getID():<8} | {subject.getCourseID():<13} | {subject.getName():<46} | {subject.getDayOfWeek():<8} | {subject.getTime():<20} | {subject.getPlace():<20} | {subject.getTeacherName():<22} |")
    
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    while True:
            print("press \"ok\" to continue")
            press=input()
            if press == 'ok':
                return
    
def ShowWithCourseID(sub):
    print("List sub")
    for num, subject in enumerate(SubjectTable.listSubject):
        print(f"{num}. {subject.CourseID}")
    courseID = input("Nhập vào mã học phần: ")
    
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    print("| IDClass  | CourseID      | Name                                           |   Thu    | Time                 | Study Place          | Teacher's name         |")
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    
    for subject in listSubject:
        if subject.getCourseID() == courseID:
            print(f"| {subject.getID():<8} | {subject.getCourseID():<13} | {subject.getName():<46} | {subject.getDayOfWeek():<8} | {subject.getTime():<20} | {subject.getPlace():<20} | {subject.getTeacherName():<22} |")
    
    print("+----------+---------------+------------------------------------------------+----------+----------------------+----------------------+------------------------+")
    while True:
            print("press \"ok\" to continue")
            press=input()
            if press == 'ok':
                return

def show():
    print("HIP HOP")
    print("1. Xem toàn bộ thời khóa biểu")
    print("2. Xem theo tên giáo viên")
    print("3. Xem theo ngày trong tuần")
    print("4. Xem theo mã học phần")
    print("5. Sửa đổi thông tin theo môn học")
    print("6. Sửa đổi thông tin theo giáo viên")
    print("7. Tiến hành lưu sang file mới")
    print("8. Thoát khỏi chương trình")
    


    
    
    