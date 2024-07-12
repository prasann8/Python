"""

                      DOCTOR SERVICE APP


        User is Doctor
        Doctor should be able to add patients
        Doctor should be able to add consultations of a patient

        doctor: user of application
        patient: pid, name, phone, email, dob, gender, created_on
        consultation: cid, pid, remarks, medicines, next_followup, created_on    


"""

"""
        create table Consultation(
            cid int primary key auto_increment,
            pid int,
            remarks varchar(256),
            medicine varchar(20),
            next_followup datetime,
            created_on datetime,
            FOREIGN KEY (pid) REFERENCES Patient(pid)
        )
"""
import datetime

class Consultation:
    
    def __init__(self, cid=0, pid=0, remarks="", medicine="", next_followup="",):
        self.cid = cid
        self.pid = pid
        self.remarks = remarks
        self.medicine = medicine
        self.next_followup = next_followup
        self.created_on = datetime.datetime.now()

    def add_consultation_details(self):
        self.pid = input("Enter Patient ID: ")
        self.remarks = input("Enter Patient remarks: ")
        self.medicine = input("Enter Patient medicines: ")
        self.next_followup = input("Enter next_followup (yyyy-mm-dd hh:mm:ss): ")

    def show(self):
        print("========CONSULTATION=========")

        consultation = """
        {cid} | {pid} 
        {remarks} | {medicine}
        {next_followup} | {created_on}
        """.format_map(vars(self))

        print(Consultation)

        print("=============================")