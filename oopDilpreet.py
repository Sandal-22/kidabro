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