from Session17A import Consultation
from Session17 import Patient
from Session15A import Database
from tabulate import tabulate

def main():
    print("=======================")
    print("Welcome to Doctor's App")
    print("=======================")

    db = Database()

    while True:
        print("1: Add New Patient")
        print("2: Update Existing Patient")
        print("3: Delete Existing Patient")
        print("4: View Patient By Phone")
        print("5: View Patient By CID")
        print("6: View All Patient")
        print("7: Add Consultation for patient")
        print("8: View All Consulations")
        print("9: View Consultation of patient")
        print("10. View all followups")
        print("0: To Quit App")

        choice = int(input("Enter your choice:"))



        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "insert into Patient values(null, '{name}', '{phone}', '{email}', '{dob}', '{gender}', '{created_on}' )".format_map(vars(patient))
            db.write(sql)
            print("Patient added Successfully...")


        
        elif choice == 2:
            pass



        elif choice == 3:
            cid = int(input("Enter Customer ID to be deleted:"))
            sql = "delete from Patient where cid={}".format(cid)

            ask = input("Do you want to delete(yes/no)??")
            if ask == "yes":
                db.write(sql)
                print("RECORD DELETED")
            elif ask == "no":
                print("Delete Operation skipped")
            else:
                break


        
        elif choice == 4:
            phone = input("Enter patient's phone number whose data is to be retrieved : ")
            sql = "select * from patient where phone='{}'".format(phone)

            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))


        
        elif choice == 5:
            pid = input("Enter patient's ID whose data is to be retrieved : ")
            sql = "select * from patient where pid='{}'".format(pid)

            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))
    
        

        elif choice == 6:
            sql = "Select * from Patient"
            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))



        elif choice == 7:
            consultation = Consultation()
            consultation.add_consultation_details()
            print(vars(consultation))
            sql = "insert into Consultation values(null, {pid}, '{remarks}', '{medicine}', '{next_followup}', '{created_on}')".format_map(vars(consultation))
            db.write(sql)
            print("Consultation Created...")



        elif choice == 8:
            sql = "Select * from consulation"
            rows = db.read(sql)

            columns = ["cid", "pid", "remarks", "medicine", "next_followup", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))



        elif choice == 9:
            pid = int(input("Enter Patient ID:"))
            sql = "Select * from consultation where pid = {}".format(pid)
            rows = db.read(sql)

            columns = ["cid", "pid", "remarks", "medicine", "next_followup", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))



        elif choice == 10:
            start_date = input("Enter start date in yyyy-mm-dd format:")
            end_date = input("Enter end date in yyyy-mm-dd format:")

            sql = "select * from consultation  where next_followup >= '{}' and next_followup <= '{}'".format(start_date,end_date)
            rows = db.read(sql)

            columns = ["cid", "pid", "remarks", "medicine", "next_followup", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))



        elif choice == 0:

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~HAVE A NICE DAY~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            break


        else:
            print("Invalid Choice")

        


if __name__ == "__main__":
    main()