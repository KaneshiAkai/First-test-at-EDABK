import csv
import os

class SubjectTable:
    listSubject = []
    
    

    def __init__(self, IDClass="", CourseID="", Name="", DayOfWeek="", Time="", Place="", TeacherName=""):
        self.IDClass = IDClass
        self.CourseID = CourseID
        self.Name = Name
        self.DayOfWeek = DayOfWeek
        self.Time = Time
        self.Place = Place
        self.TeacherName = TeacherName
        
    def readData(self):
        file_path = 'Python version\TKB.csv'
        print(f"Đường dẫn tệp: {os.path.abspath(file_path)}")
        try:
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 7:
                        IDClass, CourseID, Name, DayOfWeek, Time, Place, TeacherName = row
                        newsubject = SubjectTable(IDClass, CourseID, Name, DayOfWeek, Time, Place, TeacherName)
                        SubjectTable.listSubject.append(newsubject)
                    else:
                        print(f"Lỗi định dạng ở dòng: {reader.line_num}")
        except FileNotFoundError:
            print("File không tồn tại hoặc đường dẫn không chính xác.")
        except TypeError:
            print("Sai TypeError.")

    def showSubject(self):
        print("+----------+--------------+----------------------------------------------------+----------+----------------------+--------------------+------------------------+")
        print("| {:<8} | {:<12} | {:<50} | {:<8} | {:<20} | {:<18} |".format("Class ID", "Course ID", "Subject Name", "Day", "Time", "Place", "Teacher Name"))
        print("+----------+--------------+----------------------------------------------------+----------+----------------------+--------------------+------------------------+")
        for subject in SubjectTable.listSubject:
            print("| {:<8} | {:<12} | {:<50} | {:<8} | {:<20} | {:<18} | {:<18} |".format(subject.IDClass, subject.CourseID, subject.Name, subject.DayOfWeek, subject.Time, subject.Place, subject.TeacherName))
        print("+----------+--------------+----------------------------------------------------+----------+----------------------+--------------------+------------------------+")

    def addSubject(self):
        IDClass = input("Enter the ID of class: ")
        CourseID = input("Enter course ID: ")
        Name = input("Enter subject name: ")
        DayOfWeek = input("Enter day of the week: ")
        Time = input("Enter time: ")
        Place = input("Enter place: ")
        TeacherName = input("Enter teacher name: ")
        newsubject = SubjectTable(IDClass, CourseID, Name, DayOfWeek, Time, Place, TeacherName)
        SubjectTable.listSubject.append(newsubject)
        
    def writeData(self):
        with open("Python version\TKB_new.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Class ID", "Course ID", "Subject Name", "Day", "Time", "Place", "Teacher Name"])
            for subject in SubjectTable.listSubject:
                writer.writerow([subject.IDClass, subject.CourseID, subject.Name, subject.DayOfWeek, subject.Time, subject.Place, subject.TeacherName])
                
    def delSubject(self):
        for num, subject in enumerate(SubjectTable.listSubject):
            print(f"{num}. {subject.getName()}")
        delSubjectPos = int(input("Enter the position of the subject to delete: "))
        if 0 <= delSubjectPos < len(SubjectTable.listSubject):
            del SubjectTable.listSubject[delSubjectPos]
            print("Subject deleted successfully!")
        else:
            print("Invalid position!")
     
    def searchSubject(self):
        searchName = input("Enter the name of the subject to search: ")
        print("Search results:")
        print("+----------+--------------+----------------------------------------------------+----------+----------------------+--------------------+------------------------+")
        print("| {:<8} | {:<12} | {:<50} | {:<8} | {:<20} | {:<18} | {:<22} |".format("Class ID", "Course ID", "Subject Name", "Day", "Time", "Place", "Teacher Name"))
        print("+----------+--------------+----------------------------------------------------+----------+----------------------+--------------------+------------------------+")
        for subject in SubjectTable.listSubject:
            if searchName in subject.Name.lower():
                print("| {:<8} | {:<12} | {:<50} | {:<8} | {:<20} | {:<18} | {:<22} |".format(subject.IDClass, subject.CourseID, subject.Name, subject.DayOfWeek, subject.Time, subject.Place, subject.TeacherName))
        print("+----------+--------------+----------------------------------------------------+----------+----------------------+--------------------+------------------------+")
        while True:
            print("press \"ok\" to continue")
            press=input()
            if press == 'ok':
                return
               
    def ByID(self):
        SubjectTable.listSubject.sort(key=lambda subject: subject.IDClass)
        print("Subjects sorted by ID successfully!")
        while True:
            print("press \"ok\" to continue")
            press=input()
            if press == 'ok':
                return

    def sortByName(self):
        SubjectTable.listSubject.sort(key=lambda subject: subject.Name)
        print("Subjects sorted by name successfully!")
        while True:
            print("press \"ok\" to continue")
            press=input()
            if press == 'ok':
                return

    def writeData(self):
        try:
            with open("Python version\TKB_NEW.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Class ID", "Course ID", "Subject Name", "Day", "Time", "Place", "Teacher Name"])
                for subject in SubjectTable.listSubject:
                    writer.writerow([subject.IDClass, subject.CourseID, subject.Name, subject.DayOfWeek, subject.Time, subject.Place, subject.TeacherName])
            print("lưu dữ liệu sang file mới thành công !")
        except FileNotFoundError:    
            print("File bi ngu roi !!!")
        except TypeError:
            print("Sai TypeError.")
    


    def setTeacherName(self, _TeacherName):
        self.TeacherName = _TeacherName

    def setNewTeacher(self, subjectPos, newTeacher):
        # Implement logic to set new teacher
        pass

    def getID(self):
        return self.IDClass

    def getName(self):
        return self.Name

    def getTime(self):
        return self.Time

    def getDayOfWeek(self):
        return self.DayOfWeek

    def getPlace(self):
        return self.Place

    def getTeacherName(self):
        return self.TeacherName

    def getCourseID(self):
        return self.CourseID

    def setStatus(self, _status):
        self.status = _status

    def getStatus(self):
        return self.status
    
def showSubjectChoice():
    print("1. Add subject")
    print("2. Delete subject")
    print("3. Search subject")
    print("4. Sort subjects by ID")
    print("5. Sort subjects by name")
    print("6. Exit")
    
def modifySubject(choice, sb):
    if choice == 1:
        print("Adding subject: ")
        sb.addSubject()
        return True
    elif choice == 2:
        print("Deleting subject:")
        sb.delSubject()
        return True
    elif choice == 3:
        print("Searching subject:")
        sb.searchSubject()
        return True
    elif choice == 4:
        print("Sorting subjects by ID:")
        sb.sortByID()
        return True
    elif choice == 5:
        print("Sorting subjects by name:")
        sb.sortByName()
        return True
    elif choice == 6:
        print("Exiting subject modification process")
        return False
    else:
        print("Error! \nPlease enter a valid choice.")
        return False