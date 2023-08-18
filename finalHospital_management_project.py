''' the name of the group members are
    1. Dilpreet Brar
    2. Jashanpreet
    3. Bhawna
    4. Harpreet Singh'''

# class created for doctors having id, name, speciality, thiming ,qualification and room-number
class Doctor:
    def __init__(self, id, name, speciality, timing, qualification, room_number):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number


# the funtion to display the doctors info
def display_doctors(doctors):
    print("Id   Name                 Speciality        Timing        Qualification   Room Number\n")
    for doctor in doctors:
        print(f"{doctor.id:<5}{doctor.name:<23}{doctor.speciality:<15}{doctor.timing:<15}{doctor.qualification:<16}{doctor.room_number}\n")

# the funtion to serach a doctor by his or her ID
def search_doctor_by_id(doctors, doctor_id):
    for doctor in doctors:
        if doctor.id == doctor_id:
            return doctor
    return None
# the funtion to search doctor by name
def search_doctor_by_name(doctors, doctor_name):
    for doctor in doctors:
        if doctor.name.lower() == doctor_name.lower():
            return doctor
    return None
# the fucntion to add a doctor
def add_doctor(doctors):
    id = int(input("Enter the doctor's ID: "))
    name = input("Enter the doctor's name: ")
    speciality = input("Enter the doctor's speciality: ")
    timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
    qualification = input("Enter the doctor's qualification: ")
    room_number = input("Enter the doctor's room number: ")
    new_doctor = Doctor(id, name, speciality, timing, qualification, room_number)
    doctors.append(new_doctor)
    print(f"Doctor whose ID is {id} has been added")
# the function to edit a doctor list
def edit_doctor_info(doctors, doctor_id):
    doctor = search_doctor_by_id(doctors, doctor_id)
    if doctor:
        print(f"Editing information for Doctor with ID {doctor_id}")
        doctor.name = input("Enter new Name: ")
        doctor.speciality = input("Enter new Speciality: ")
        doctor.timing = input("Enter new Timing: ")
        doctor.qualification = input("Enter new Qualification: ")
        doctor.room_number = input("Enter new Room number: ")
        print(f"Doctor whose ID is {doctor_id} has been edited")
    else:
        print("Can't find the doctor with the same ID on the system")

#the class and the fucntion for the patient

class Patient:
    def __init__(self, id, name, disease, gender, age):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

#function to display patients
   
def display_patients(patients):
    print("ID   Name                   Disease       Gender           Age\n")
    for patient in patients:
        print(f"{patient.id:<5}{patient.name:<23}{patient.disease:<15}{patient.gender:<15}{patient.age}\n")

#funtion to search patient by id

def search_patient_by_id(patients, patient_id):
    for patient in patients:
        if patient.id == patient_id:
            return patient
    return None

#function to add patient

def add_patient(patients):
    id = int(input("Enter Patient id: "))
    name = input("Enter Patient name: ")
    disease = input("Enter Patient disease: ")
    gender = input("Enter Patient gender: ")
    age = int(input("Enter Patient age: "))
    new_patient = Patient(id, name, disease, gender, age)
    patients.append(new_patient)
    print(f"Patient whose ID is {id} has been added")

#function to edit patients information

def edit_patient_info(patients, patient_id):
    patient = search_patient_by_id(patients, patient_id)
    if patient:
        print(f"Editing information for Patient with ID {patient_id}")
        patient.name = input("Enter new Name: ")
        patient.disease = input("Enter new disease: ")
        patient.gender = input("Enter new gender: ")
        patient.age = int(input("Enter new age: "))
        print(f"Patient whose ID is {patient_id} has been edited")
    else:
        print("Can't find the Patient with the same ID on the system")

#the list of doctors

doctors = [
    Doctor(21, "Dr.Gody", "ENT", "5am-11am", "MBBS,MD", 17),
    Doctor(32, "Dr.Vikram", "Physician", "10pm-3am", "MBBS,MD", 45),
    Doctor(17, "Dr.Amy", "Surgeon", "8pm-2am", "BDM", 8),
    Doctor(33, "Dr.David", "Artho", "10am-4pm", "MBBS,MS", 40),
    Doctor(123, "Dr. Ross", "Headackes", "8pm-10am", "MST", 102),
    Doctor(66, "Dr. Mike", "Heart", "9am-5pm", "MS", 2)
]
#the list of patients
patients = [
    Patient(12, "Pankaj", "Cancer", "Male", 30),
    Patient(13, "Janina", "Cold", "Female", 23),
    Patient(14, "Alonna", "Malaria", "Female", 45),
    Patient(15, "Ravi", "Diabetes", "Male", 65)
]
#the match case for the main menu..............this main menu also contains the match case for both doctors and patients elements
while True:
    print("Welcome to Alberta Hospital (AH) Management system")
    print("Select from the following options, or select 0 to stop:")
    print("1 - Doctors")
    print("2 - Patients")
    print("3 - Exit Program")
    choice = int(input(">>> "))

    if choice == 1:
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            sub_choice = int(input("Type your choice here = "))

            if sub_choice == 1:
                display_doctors(doctors)
            elif sub_choice == 2:
                doctor_id = int(input("Enter the doctor Id: "))
                doctor = search_doctor_by_id(doctors, doctor_id)
                if doctor:
                    display_doctors([doctor])
                else:
                    print("Can't find the doctor with the same ID on the system")
            elif sub_choice == 3:
                doctor_name = input("Enter the doctor name: ")
                doctor = search_doctor_by_name(doctors, doctor_name)
                if doctor:
                    display_doctors([doctor])
                else:
                    print("Can't find the doctor with the same name on the system")
            elif sub_choice == 4:
                add_doctor(doctors)
            elif sub_choice == 5:
                doctor_id = int(input("Please enter the id of the doctor that you want to edit their information: "))
                edit_doctor_info(doctors, doctor_id)
            elif sub_choice == 6:
                break
            else:
                print("Invalid choice! Please select a valid option.")
    elif choice == 2:
        while True:
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient Info")
            print("5 - Back to the main menu")
            sub_choice = int(input("Type your choice here >>>>"))

            if sub_choice == 1:
                display_patients(patients)
            elif sub_choice == 2:
                patient_id = int(input("Enter the patient Id: "))
                patient = search_patient_by_id(patients, patient_id)
                if patient:
                    display_patients([patient])
                else:
                    print("Can't find the patient with the same ID on the system")
            
            elif sub_choice == 3:
                add_patient(patients)
            elif sub_choice == 4:
                patient_id = int(input("Please enter the id of the Patient that you want to edit their information: "))
                edit_patient_info(patients, patient_id)    
            elif sub_choice == 5:
                break
            else:
                print("Invalid choice! Please select a valid option.")
    elif choice == 3:
        print("Thanks for using the program. Bye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
