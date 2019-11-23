import random
from random import randrange
import psycopg2
import string
from faker import Faker
faker = Faker('en_US')

print("-------------------------------------------")
print("Welcome to the hospital database interface!")
print("-------------------------------------------")
print("")
print("Please, input some needed amounts for our system:")
print("     Amount of employees:")
print("     (it should be >=5, as we should have at least 1 employee for each type: -doctor, -nurse, -supply manager, -economic manager, -receptionist)")
employee_amount = int(input())
while(employee_amount <5):
    print("Sorry, give number of employees that is greater or equal 5! Input again:")
    employee_amount = int(input())   
doctor_amount = random.randint(1,employee_amount- 4)
nurse_amount = random.randint(1,employee_amount - 3 - doctor_amount)
supply_manager_amount = random.randint(1,employee_amount - 2 - doctor_amount - nurse_amount)
economic_manager_amount = random.randint(1, employee_amount - supply_manager_amount  - doctor_amount - nurse_amount - 1)
receptionist_amount = employee_amount - supply_manager_amount  - doctor_amount - nurse_amount - economic_manager_amount
print("So, we have in total " + str(employee_amount) + " employees and randomly were decided that we have:" )
print(str(doctor_amount) +" doctor(s), "  + str(nurse_amount) + " nurse(s), " + str(supply_manager_amount) + " supply_manager(s), " + str(economic_manager_amount) + " economic_manager(s), " + str(receptionist_amount) + " receptionist(s)")
print("     Amount of patients:")
print("     it should be >=1, as we want to fill in all tables to simulate working of the our hospital database")
patient_amount = int(input())
while(patient_amount < 1):
    print("Sorry, give number of patients that is greater or equal 1! Input again:")
    patient_amount = int(input())
print("     Amount of guests:")
print("     it should be >=1, as we want to fill in all tables to simulate working of the our hospital database")
guest_amount = int(input())
while(guest_amount < 1):
    print("Sorry, give number of guests that is greater or equal 1! Input again:")
    guest_amount = int(input())
print("     Amount of treatments:")
print("     it should be >=1, as we want to fill in all tables to simulate working of the our hospital database")
treatment_amount = int(input())
while(treatment_amount < 1):
    print("Sorry, give number of treatments that is greater or equal 1! Input again:")
    treatment_amount = int(input())
print("     Amount of hospital equipments:")
print("     it should be >=1, as we want to fill in all tables to simulate working of the our hospital database")
hospital_equipment_amount = int(input())
while(hospital_equipment_amount < 1):
    print("Sorry, give number of hospital equipments that is greater or equal 1! Input again:")
    hospital_equipment_amount = int(input())
print("     Amount of appoinments between the particular doctor and the particular patient:")
print("     it should be >=1, as we want to fill in all tables to simulate working of the our hospital database")
appointment_amount = int(input())
while(appointment_amount < 1):
    print("Sorry, give number of appointment_amount that is greater or equal 1! Input again:")
    appointment_amount = int(input())
print("Thanks!")
print("-------------------------------------------------------------------------------")


agreement_types = ["Confidentiallity", "Assurance", "Donor"]
diagnosis = ["infection", "curing", "illness", "preparation to surgery", "virus", "injury"] #in real life should be extended, now only for insert table
hospital_equipment_names = ["bandage", "brace", "cast", "catheter", "crutches", "defibrillator", "diagnostic equipment", "forceps", "incubator", "scalpel", "sling", "splint", "thermometer", "tongue depressor", "wheelchair", "X-ray"]
treatments = ["Acne", "Allergy testing", "Arrhythmia", "Asthma", "Bariatric surgery","Barium enema", "Back pain", "Bladder cancer",  "Blood pressure test", "Bowel incontinence", "Breast lift", "Blurred vision", "Broken nose", "Breathlessness", "Cancer tests", "Cardiac electrophysiology", "Cataracts", "Cerebral palsy", "Cheek implants", "Colposcopy", "Coronary angioplasty", "Chest pain", "Coughing", "Depression", "Diabetes", "Diarrhoea", "Dysphagia", "Eczema", "Endometriosis", "Eyelid problems", "Facelift",  "Fibroids", "Foot pain", "Frozen shoulder", "Gastroscopy", "Glaucoma", "General medicine", "Hair loss", "Heartburn", "Herpes", "Hip pain", "Hydrocele", "Itchy skin", "Knee pain", "Liver disease", "Medical admission", "Night sweats", "Obesity", "Scoliosis", "Tongue tie", "Urology", "Radiotherapy"]
qualifications = ["high", "medium", "intern"]
types_of_employee = ["Nurse", "Doctor", "Economic Manager", "Supply Manager", "Receprionist"]
ward_types_of_hospital = ["Emergency department", "Cardiology", "General Surgery", "Gynecology", "Critical Care", "Neurology", "Pain Management", "Physiotherapy", "Oncology"]
schedule_examples = ["Do work related to patients","Do work related to your responsability zone"] # just examples to fill in table, can(and should) be much more detail
notice_board_example = "Some important announcement! It will be done somehow at sometime with some activity in the our hospital!"
used_id = []
doctors = []
nurses  = []
supply_managers = []
economic_managers = []
receptionists = []
stationary_patients = []
stat = []
stationary_patient_amount = 0

def generating_IDS(flag):
    ids =  []
    if flag == "E": 
        for i in range(employee_amount): ids.append('E-' + str(i+1) ) 
    elif flag == "P":
        for i in range(patient_amount): ids.append('P-' + str(i+1)) 
    elif flag == "G":    
        for i in range(guest_amount): ids.append('G-' + str(i+1)) 
    elif flag == "HE":
        for i in range(hospital_equipment_amount): ids.append('HE-' + str(i+1)) 
    elif flag == "T":
        for i in range(treatment_amount): ids.append('T-' + str(i+1)) 
    return ids
E_IDs = generating_IDS("E")  #employees ids
P_IDs = generating_IDS("P")  #patients ids
HE_IDs = generating_IDS("HE") #hospital equipment ids
T_IDs = generating_IDS("T")  #treatment ids
G_IDs = generating_IDS("G") #guests ids

def random_id(ids):
    id = random.choice(ids)
    while (id in used_id):
        id = random.choice(ids)
    used_id.append(id)
    return id

def insert_employee():
    s = "INSERT INTO Employee VALUES\n"
    for i in range(employee_amount):
        s += "("
        s = s + "'" + faker.first_name() + "'," #name
        s = s + "'" + faker.last_name() + "'," #surname
        s = s + "'" + faker.address().replace("\n"," ") + "',"
        s = s + "'" + str(faker.date_of_birth()) + "'," #date of birth
        s = s + "'" + faker.phone_number() + "'," #phone number
        s = s + "'" + faker.email() + "'," #email
        s = s + "'" + random.choice(qualifications) + "'," #qualification
        eid = random_id(E_IDs)
        flag = 0
        global doctor_amount
        global nurse_amount
        global economic_manager_amount
        global supply_manager_amount
        global  receptionist_amount
        while(flag == 0):
            type_of_employee = random.choice(types_of_employee)
            if type_of_employee == "Doctor" and doctor_amount>0:
                doctors.append(eid)
                doctor_amount-=1
                flag = 1
            elif type_of_employee == "Nurse" and nurse_amount>0:
                nurses.append(eid)
                nurse_amount-=1
                flag = 1
            elif type_of_employee == "Economic Manager" and economic_manager_amount>0:
                economic_managers.append(eid)
                economic_manager_amount-=1
                flag = 1
            elif type_of_employee =="Supply Manager" and supply_manager_amount>0:
                supply_managers.append(eid)
                supply_manager_amount-=1
                flag = 1
            elif type_of_employee == "Receprionist" and receptionist_amount>0:
                receptionists.append(eid)
                receptionist_amount-=1
                flag = 1
        s = s + "'" + type_of_employee + "'," #type
        s = s + "'" + eid + "'" #id
        s += ")"
        if (i < employee_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s
def insert_patient():
    s = "INSERT INTO Patient VALUES\n"
    for i in range(patient_amount):
        s += "("
        s = s + "'" + faker.first_name() + "'," #name
        s = s + "'" + faker.last_name() + "'," #surname
        s = s + "'" + faker.address().replace("\n"," ") + "'," #city
        s = s + "'" + str(faker.date_of_birth()) + "'," #date of birth
        s = s + "'" + random.choice(["male", "female"]) + "',"  #sex
        patient_type = random.choice(["stationary", "ambulatory"])
        pid = random_id(P_IDs)
        global stationary_patient_amount
        if patient_type  == "stationary":
            stationary_patients.append(pid)
            stat.append(pid)
            stationary_patient_amount+=1
        s = s + "'" + patient_type + "',"  #type
        s = s + "'" + pid + "'" #id
        s += ")"
        if (i < patient_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s
def insert_stationary_patient():
    s = "INSERT INTO Stationary_patient VALUES\n"
    for i in range(stationary_patient_amount):
        s += "("
        s = s + "'" + random.choice(ward_types_of_hospital) + "',"  #ward type
        s = s + "'" + str(random.randrange(100, 500)) + "'," #room
        pid = random.choice(stat)
        stat.remove(pid)
        s = s + "'" + pid + "'" #id
        s += ")"
        if (i < stationary_patient_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s    
def insert_guest():
    s = "INSERT INTO Guest VALUES\n"
    for i in range(guest_amount):
        s += "("
        s = s + "'" + faker.name() + "'," #name
        s = s + "'" + random_id(G_IDs) + "'" #id
        s += ")"
        if (i < guest_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s    
def insert_make_appointment():
    s = "INSERT INTO Make_an_appointment VALUES\n"
    for i in range(appointment_amount):
        s += "("
        s = s + "'" + random.choice(P_IDs) + "'," #Patient
        s = s + "'" + random.choice(doctors) + "'," #Employee
        s = s + "'" + str(faker.date_time_this_decade()) + "'" #Date
        s += ")"
        if (i < appointment_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s
def insert_optional_treatment():
    s = "INSERT INTO Optional_treatment VALUES\n"
    global treatment_amount
    if treatment_amount>len(treatments):
        treatment_amount = treatments
    for i in range(treatment_amount):
        s += "("
        s = s + "'" + random_id(treatments) + "'," #Patient
        s = s + "'" + str(random.randrange(500, 100000)) + "'," #Employee
        s = s + "'" + random_id(T_IDs) + "'" #T_ID
        s += ")"
        if (i < treatment_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s
def insert_get_optional_treatment():
    s = "INSERT INTO Get_optional_treatment VALUES\n"
    number_of_records = 5 # by default?
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(P_IDs) + "'," #Patient
        s = s + "'" + random.choice(T_IDs) + "'," #Employee
        s = s + "'" + str(faker.date_time_this_decade()) + "'" #T_ID
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s
def insert_visit():
    s = "INSERT INTO Visit VALUES\n"
    number_of_records = 3 # by default?
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(stationary_patients) + "'," #Patient
        s = s + "'" + random.choice(G_IDs) + "'," #Employee
        s = s + "'" + str(faker.date_time_this_decade()) + "'" #T_ID
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s    
def insert_notice_board():
    s = "INSERT INTO Notice_board VALUES\n"
    number_of_records = 1 # by default?
    for i in range(number_of_records):
        s += "("
        s = s + "'" + notice_board_example + "'," #Patient
        s = s + "'" + str(faker.date_time_this_decade()) + "'," #T_ID
        s = s + "'" + random.choice(receptionists) + "'" #Employee
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s
def insert_stuff_schedule():
    s = "INSERT INTO Stuff_schedule VALUES\n"
    number_of_records = len(nurses) + len(economic_managers) + len(supply_managers) + len(receptionists) # by default?
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(schedule_examples) + "'," #Patient
        s = s + "'" + str(faker.date_time_this_decade()) + "'," #T_ID
        s = s + "'" + random.choice(nurses+supply_managers+economic_managers+receptionists) + "'" #Employee
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s
def insert_hospital_equipment():
    s = "INSERT INTO Hospital_equipment VALUES\n"
    global hospital_equipment_amount
    if hospital_equipment_amount>len(hospital_equipment_names):
        hospital_equipment_amount = len(hospital_equipment_names)
    for i in range(hospital_equipment_amount):
        s += "("
        s = s + "'" + random_id(hospital_equipment_names) + "'," #Patient
        s = s + "'" + str(random.randrange(5, 250)) + "'," #T_ID
        s = s + "'" + random_id(HE_IDs) + "'" #Employee
        s += ")"
        if (i < hospital_equipment_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s
def insert_medical_history():
    s = "INSERT INTO Medical_history VALUES\n"
    for i in range(patient_amount):
        used_id.remove('P-' + str(i+1))
    for i in range(patient_amount):
        s += "("
        s = s + "'" + random.choice(diagnosis) + "',"
        start_date = faker.past_date(start_date="-30d", tzinfo=None)
        end_date = faker.future_date(end_date="+30d", tzinfo=None)
        s = s + "'" + str(start_date) +  "',"
        s = s + "'" + str(end_date) +  "',"
        s = s + "'" + random.choice(doctors) + "',"
        s = s + "'" + random_id(P_IDs) + "'" #Employee
        s += ")"
        if (i < patient_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s    
def insert_donate():
    number_of_records = 5 #default
    s = "INSERT INTO Donate VALUES\n"
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(P_IDs) + "'," #pid
        s = s + "'" + random.choice(receptionists) + "'," #eid
        s = s + "'" + str(random.randrange(50, 10000)) + "'," #amount of money
        s = s + "'" + str(faker.date_time_this_decade()) + "'" #amount of money
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s         
def insert_conclude_agreement():
    number_of_records = 3 #default
    s = "INSERT INTO Conclude_agreement VALUES\n"
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(agreement_types) + "'," #pid
        s = s + "'" + random.choice(P_IDs) + "'," #eid
        s = s + "'" + random.choice(economic_managers) + "'," #eid
        s = s + "'" + str(faker.date_time_this_decade()) + "'" #amount of money
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    # print(s)
    return s         
def insert_control():
    s = "INSERT INTO Control VALUES\n"
    for i in range(hospital_equipment_amount):
        used_id.remove('HE-' + str(i+1))
    for i in range(hospital_equipment_amount):
        s += "("
        s = s + "'" + random_id(HE_IDs) + "',"
        s = s + "'" + random.choice(supply_managers) + "'" #amount of money
        s += ")"
        if (i < hospital_equipment_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'

    # print(s)
    return s       


main_insert = insert_employee()  + insert_patient()  + insert_guest()
if stationary_patient_amount>0:
    main_insert += insert_stationary_patient() + insert_visit()
main_insert += insert_make_appointment() + insert_optional_treatment() + insert_get_optional_treatment() + insert_notice_board() + insert_stuff_schedule() + insert_hospital_equipment() + insert_medical_history()  + insert_donate() + insert_conclude_agreement() + insert_control()

print("So, our database has the following insert:\n")
print("\n")
print(main_insert)
print("--------------------------------------------------------------------")

truncate = """
            TRUNCATE Patient CASCADE;
            TRUNCATE Employee CASCADE;
            TRUNCATE Stationary_patient CASCADE;
            TRUNCATE Guest CASCADE;
            TRUNCATE Make_an_appointment CASCADE;
            TRUNCATE Optional_treatment CASCADE;
            TRUNCATE Get_optional_treatment CASCADE;
            TRUNCATE Visit CASCADE;
            TRUNCATE Notice_board CASCADE;
            TRUNCATE Stuff_schedule CASCADE;
            TRUNCATE Hospital_equipment CASCADE;
            TRUNCATE Medical_history CASCADE;
            TRUNCATE Donate CASCADE;
            TRUNCATE Conclude_agreement CASCADE;
            TRUNCATE Control CASCADE;
           """
con = psycopg2.connect(database="dmd_project", user="postgres", password="12345", host="127.0.0.1", port="5432")
print("Database opened successfully")
print("--------------------------------------------------------------------")
cur = con.cursor()


cur.execute(truncate);

query = "SELECT * FROM Patient"
query1 =""" SELECT * FROM Employee as d INNER JOIN  Make_an_appointment as m
             ON m.E_ID = d.E_ID and m.P_ID = 'Apat'
             WHERE m.Date = (SELECT MAX(Date) FROM Make_an_appointment
             WHERE Make_an_appointment.P_ID = 'Apat') 
             and d.type = 'Doctor' 
             and ((d.surname LIKE 'L%' or d.surname LIKE 'M%' ) and (d.name NOT LIKE 'L%' and d.name NOT LIKE 'M%'))
             or ((d.name LIKE 'L%' or d.name LIKE 'M%') and (d.surname NOT LIKE 'L%' and d.surname NOT LIKE 'M%'));
        """
query2 = """
            SELECT e.E_ID, Count(e.E_ID) AS TOTAL, COUNT(e.E_ID)/56.0 as AVERAGE
            FROM Employee as e INNER JOIN  Make_an_appointment as m
            ON m.E_ID = e.E_ID 
            WHERE
            m.date > current_date - interval '1 year'
            GROUP BY e.E_ID
         """ 
query3 ="""
            SELECT M.P_ID
            FROM patient as p INNER JOIN  Make_an_appointment as m
            ON m.P_ID = P.P_ID 
            WHERE
            Date > current_date - interval '1 week'
            GROUP By M.P_ID
            HAVING Count(M.P_ID)>1
            INTERSECT
            SELECT M.P_ID
            FROM patient as p INNER JOIN  Make_an_appointment as m
            ON m.P_ID = P.P_ID 
            WHERE
            Date > current_date - interval '2 week' and date < CURRENT_DATE - INTERVAL '1 week'
            GROUP By M.P_ID
            HAVING Count(M.P_ID)>1
            INTERSECT
            SELECT M.P_ID
            FROM patient as p INNER JOIN  Make_an_appointment as m
            ON m.P_ID = P.P_ID 
            WHERE
            Date > current_date - interval '1 week'
            GROUP By M.P_ID
            HAVING Count(M.P_ID)>1
            INTERSECT
            SELECT M.P_ID
            FROM patient as p INNER JOIN  Make_an_appointment as m
            ON m.P_ID = P.P_ID 
            WHERE
            Date > current_date - interval '2 week' and date < CURRENT_DATE - INTERVAL '1 week'
            GROUP By M.P_ID
            HAVING Count(M.P_ID)>1
        """
query4 ="""
            SELECT SUM(T.cnt) as Amount
            FROM
            (SELECT COUNT(p.P_id)*200 AS cnt FROM patient as p INNER JOIN  Make_an_appointment as m
              ON m.P_ID = P.P_ID 
              WHERE 
              Date > current_date - interval '1 month'
              GROUP By M.P_ID, P.dob
              HAVING Count(M.P_ID)<3 and EXTRACT(YEAR from AGE(P.dob))<50
             UNION ALL
             SELECT COUNT(p.P_id)*400 AS cnt FROM patient as p INNER JOIN  Make_an_appointment as m
              ON m.P_ID = P.P_ID 
              WHERE 
              Date > current_date - interval '1 month'
              GROUP By M.P_ID, P.dob
              HAVING Count(M.P_ID)<3 and EXTRACT(YEAR from AGE(P.dob))>49
             UNION ALL
             SELECT COUNT(p.P_id)*500 AS cnt FROM patient as p INNER JOIN  Make_an_appointment as m
              ON m.P_ID = P.P_ID 
              WHERE 
              Date > current_date - interval '1 month'
              GROUP By M.P_ID, P.dob
              HAVING Count(M.P_ID)>2 and EXTRACT(YEAR from AGE(P.dob))>49
             UNION ALL
             SELECT COUNT(p.P_id)*250 AS cnt FROM patient as p INNER JOIN  Make_an_appointment as m
              ON m.P_ID = P.P_ID 
              WHERE 
              Date > current_date - interval '1 month'
              GROUP By M.P_ID, P.dob
              HAVING Count(M.P_ID)>2 and EXTRACT(YEAR from AGE(P.dob))<50
             ) as T

        """                        


cur.execute(main_insert)

cur.execute(query);    
rows = cur.fetchall()

print("output:")
for row in rows:
    print(row) 
con.commit()
print("--------------------------------------------------------------------")
print("Records inserted successfully")
con.close()
