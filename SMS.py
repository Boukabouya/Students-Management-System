Students_list = []
Teachers_list = []

class Person:
    def __init__(self, ID, first_name, last_name, date_of_birth, phone_number, email_address):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.email_address = email_address

class Student(Person):
    def __init__(self, ID, first_name, last_name, date_of_birth, address, phone_number, email_address):
        super().__init__(ID, first_name, last_name, date_of_birth, phone_number, email_address)
        self.address = address

class Teacher(Person):
    def __init__(self, ID, first_name, last_name, date_of_birth, phone_number, email_address):
        super().__init__(ID, first_name, last_name, date_of_birth, phone_number, email_address)

def add_person():
    print("What type of person do you want to add? (Student/Teacher)")
    person_type = input().lower() 
    
    if person_type == "student":
        print("Enter student information:")
        ID = input("ID: ")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        date_of_birth = input("Date of birth (YYYY-MM-DD): ")
        address = input("Address: ")
        phone_number = input("Phone number: ")
        email_address = input("Email address: ")
        
        new_student = Student(ID, first_name, last_name, date_of_birth, address, phone_number, email_address)
        Students_list.append(new_student)
        print("New student added successfully!")
        
    elif person_type == "teacher":
        print("Enter teacher information:")
        ID = input("ID: ")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        date_of_birth = input("Date of birth (YYYY-MM-DD): ")
        phone_number = input("Phone number: ")
        email_address = input("Email address: ")
        
        new_teacher = Teacher(ID, first_name, last_name, date_of_birth, phone_number, email_address)
        Teachers_list.append(new_teacher)
        print("New teacher added successfully!")
        
    else:
        print("Invalid person type. Please enter 'Student' or 'Teacher'.")

# prompt the user to add new people until they indicate they're done

while True:
    add_person()  # calling add_person() function here #1 
    print("Do you want to add another person? (Y/N)") # y N 
    response = input().lower()
    if response == "y":
         add_person()
    elif response == "n": 
        print("Exiting...")
        break
    else :
        print("Invalid response. Please enter 'Y' or 'N'.")

#In summary, the return statement is not needed in this code because it does not accomplish anything 
# - the add_person() function is called directly from within the if statement, and we don't need to return a value from the function
        
# iterate over the Students_list and print out the attributes of each student
for student in Students_list:
    print("ID:", student.ID)
    print("Name:", student.first_name, student.last_name)
    print("Date of birth:", student.date_of_birth)
    print("Address:", student.address)
    print("Phone number:", student.phone_number)
    print("Email address:", student.email_address)
    print()


# iterate over the Teachers_list and print out the attributes of each teacher
for teacher in Teachers_list:
    print("ID:", teacher.ID)
    print("Name:", teacher.first_name, teacher.last_name)
    print("Date of birth:", teacher.date_of_birth)
    print("Phone number:", teacher.phone_number)
    print("Email address:", teacher.email_address)
    print()

def edit_teacher():
    teacher_id = input("Enter the ID of the teacher you want to edit: ")# id = 01 
    
    # Find the teacher object with the matching ID
    matching_teachers = [teacher for teacher in Teachers_list if teacher.ID == teacher_id] # mt=[1,2,3 ]
    # each teacher in the list comprehension is an instance of the Teacher class,
    # with its own set of attributes that were assigned when the object was created using the Teacher constructor.
    
    # Check if any teacher objects were found
    if len(matching_teachers) == 0:
        print("No teacher found with ID", teacher_id)
        return
    elif len(matching_teachers) > 1:
        print("Multiple teachers found with ID", teacher_id)
        return
    
    teacher = matching_teachers[0]
    
    # Prompt the user for new values for each attribute of the teacher
    print("Enter new information for the teacher (leave blank for no change):")
    
    new_first_name = input("First name ({}): ".format(teacher.first_name))
    if new_first_name != "":
        teacher.first_name = new_first_name
    
    new_last_name = input("Last name ({}): ".format(teacher.last_name))
    if new_last_name != "":
        teacher.last_name = new_last_name
    
    new_date_of_birth = input("Date of birth ({}): ".format(teacher.date_of_birth))
    if new_date_of_birth != "":
        teacher.date_of_birth = new_date_of_birth
    
    new_phone_number = input("Phone number ({}): ".format(teacher.phone_number))
    if new_phone_number != "":
        teacher.phone_number = new_phone_number
    
    new_email_address = input("Email address ({}): ".format(teacher.email_address))
    if new_email_address != "":
        teacher.email_address = new_email_address
    
    print("Teacher information updated successfully.")


def edit_student():
    print("Enter the ID of the student you want to edit:")
    id = input()
    
    # find the student with the given ID in the list of students
    for student in Students_list:
        if student.ID == id:
            print("Enter the new information for the student:")
            student.first_name = input("First name: ")
            student.last_name = input("Last name: ")
            student.date_of_birth = input("Date of birth (YYYY-MM-DD): ")
            student.address = input("Address: ")
            student.phone_number = input("Phone number: ")
            student.email_address = input("Email address: ")
            print("Student information updated successfully!")
            return
     
    # if no student with the given ID is found, print an error message
    print("No student with ID", id, "was found.")

def delete_person():
    print("What type of person do you want to delete? (Student/Teacher)")
    person_type_delete = input().lower() 
    
    if person_type_delete == "student":

      print("Enter the ID of the person you want to delete:")
      id_to_delete = input()
    
      # search for the person with the given ID in the Students_list
      for student in Students_list:
         if student.ID == id_to_delete:
             Students_list.remove(student)
             print("Student with ID", id_to_delete, "deleted successfully!")
             return
      # if the person wasn't found in either list, print an error message
      print("Student with ID", id_to_delete, "not found.")
    elif person_type_delete == "teacher":

      print("Enter the ID of the person you want to delete:")
      id_to_delete = input()
    # search for the person with the given ID in the Teachers_list
      for teacher in Teachers_list:
         if teacher.ID == id_to_delete: 
             Teachers_list.remove(teacher)
             print("Teacher with ID", id_to_delete, "deleted successfully!")
             return
      # if the person wasn't found in either list, print an error message
      print("teacher with ID", id_to_delete, "not found.")
    else:
        print("Invalid person type. Please enter 'Student' or 'Teacher'.")
while True:
    print("Do you want to add, edit, or delete a person? (A/E_teacher/E_student/D/N)")
    response = input().lower()
    
    if response == "a":
        add_person()
    elif response == "e_teacher":
        edit_teacher()
    elif response == "e_student":
        edit_student()
    elif response == "d":
        delete_person()
    elif response == "n":
        print("Exiting...")
        break
    else:
        print("Invalid response. Please enter 'A', 'E_teacher' , 'E_student', 'D', or 'N'.")
