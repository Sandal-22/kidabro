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