import random
from random import randrange
import psycopg2
import string
from faker import Faker
faker = Faker('en_US') # the pseudo-random is generated by using this remarkable library
from queries import * 
import psycopg2.extras
import sys


# We ask from you some amounts for generationg insertions
# But needs to say that we generate some data in some tables with the default amount (it seems not neccecary to ask for our case.)
# We always generate:
#  - 5 insertions into GET_OPTIONAL_TREATMENT table
#  - 3 insertions into VISIT table
#  - 1 insertion into NOTICE_BOARD table
#  - 5 insertions into DONATE table
#  - 3 insertions into CONCLUDE_AGREEMENT table

#needed variables
employee_amount = 0 
patient_amount = 0
guest_amount = 0
treatment_amount = 0
hospital_equipment_amount = 0 
appointment_amount = 0
doctor_amount = 0
nurse_amount = 0
economic_manager_amount = 0
supply_manager_amount = 0
receptionist_amount = 0
stationary_patient_amount = 0
flazok = 0 # temporary variable

# lists of ids of different types for keeping track during generating psedo-random insertions
used_id = []
doctors = []
nurses  = []
supply_managers = []
economic_managers = []
receptionists = []
stationary_patients = []
stat = [] 
P_IDs = []

# some dictionaries for choosing from it. It can be extended a lot. But for insertions of database, it is enough to have mostly abstract ones. (our team thinks that, at least :) )
agreement_types = ["Confidentiallity", "Assurance", "Donor"]
diagnosis = ["infection", "curing", "illness", "preparation to surgery", "virus", "injury"] 
hospital_equipment_names = ["bandage", "brace", "cast", "catheter", "crutches", "defibrillator", "diagnostic equipment", "forceps", "incubator", "scalpel", "sling", "splint", "thermometer", "tongue depressor", "X-ray"]
treatments = ["Acne", "Allergy testing", "Arrhythmia", "Asthma", "Bariatric surgery","Barium enema", "Back pain", "Bladder cancer",  "Blood pressure test", "Bowel incontinence", "Breast lift", "Blurred vision", "Broken nose", "Breathlessness", "Cancer tests", "Cardiac electrophysiology", "Cataracts", "Cerebral palsy", "Cheek implants", "Colposcopy", "Coronary angioplasty", "Chest pain", "Coughing", "Depression", "Diabetes", "Diarrhoea", "Dysphagia", "Eczema", "Eyelid problems", "Facelift",  "Fibroids", "Foot pain", "Frozen shoulder", "Gastroscopy", "Glaucoma", "General medicine", "Hair loss", "Heartburn", "Herpes", "Hip pain", "Hydrocele", "Itchy skin", "Knee pain", "Liver disease", "Night sweats", "Obesity", "Scoliosis", "Tongue tie", "Urology", "Radiotherapy"]
qualifications = ["high", "medium", "intern"]
types_of_employee = ["Nurse", "Doctor", "Economic Manager", "Supply Manager", "Receprionist"]
ward_types_of_hospital = ["Emergency department", "Cardiology", "General Surgery", "Gynecology", "Critical Care", "Neurology", "Pain Management", "Physiotherapy", "Oncology"]
schedule_examples = ["Do work related to patients","Do work related to your responsability zone"] 
notice_board_example = "Some important announcement! It will be done somehow at sometime with some activity in the our hospital!"



# functions that are needed for generating data and implementing required queries


# the starting one if we've decided to generate new insertions
def start():
    global employee_amount
    global patient_amount 
    global guest_amount 
    global treatment_amount 
    global hospital_equipment_amount  
    global appointment_amount
    global doctor_amount
    global nurse_amount
    global economic_manager_amount
    global supply_manager_amount
    global receptionist_amount
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
    if treatment_amount > len(treatments): treatment_amount = len(treatments)
    print("     Amount of hospital equipments:")
    print("     it should be >=1, as we want to fill in all tables to simulate working of the our hospital database")
    hospital_equipment_amount = int(input())
    while(hospital_equipment_amount < 1):
        print("Sorry, give number of hospital equipments that is greater or equal 1! Input again:")
        hospital_equipment_amount = int(input())
    if hospital_equipment_amount > len(hospital_equipment_names): hospital_equipment_amount = len(hospital_equipment_names)
    print("     Amount of appoinments between the particular doctor and the particular patient:")
    print("     it should be >=1, as we want to fill in all tables to simulate working of the our hospital database")
    appointment_amount = int(input())
    while(appointment_amount < 1):
        print("Sorry, give number of appointment_amount that is greater or equal 1! Input again:")
        appointment_amount = int(input())
    print("Thanks!\n")

# generating ids of all types (depends of flag that we pass)
def generating_IDS(flag):
    ids = []
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

# choosing id that was not in use before
def random_id(ids):
    id = random.choice(ids)
    while (id in used_id):
        id = random.choice(ids)
    used_id.append(id)
    return id

#inserting in all tables that we currently have in our database
def insert_employee():
    s = "INSERT INTO Employee VALUES\n"
    for i in range(employee_amount):
        s += "("
        s = s + "'" + faker.first_name() + "'," 
        s = s + "'" + faker.last_name() + "'," 
        s = s + "'" + faker.address().replace("\n"," ") + "',"
        s = s + "'" + str(faker.date_of_birth()) + "'," 
        s = s + "'" + faker.phone_number() + "'," 
        s = s + "'" + faker.email() + "'," 
        s = s + "'" + random.choice(qualifications) + "'," 
        eid = random_id(E_IDs)
        flag = 0
        global doctor_amount
        global nurse_amount
        global economic_manager_amount
        global supply_manager_amount
        global receptionist_amount
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
        s = s + "'" + type_of_employee + "'," 
        s = s + "'" + eid + "'" 
        s += ")"
        if (i < employee_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s
def insert_patient():
    s = "INSERT INTO Patient VALUES\n"
    for i in range(patient_amount):
        s += "("
        s = s + "'" + faker.first_name() + "'," 
        s = s + "'" + faker.last_name() + "'," 
        s = s + "'" + faker.address().replace("\n"," ") + "'," 
        s = s + "'" + str(faker.date_of_birth()) + "'," 
        s = s + "'" + random.choice(["male", "female"]) + "'," 
        patient_type = random.choice(["stationary", "ambulatory"])
        pid = random_id(P_IDs)
        global stationary_patient_amount
        if patient_type  == "stationary":
            stationary_patients.append(pid)
            stat.append(pid)
            stationary_patient_amount+=1
        s = s + "'" + patient_type + "',"  
        s = s + "'" + pid + "'" 
        s += ")"
        if (i < patient_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s
def insert_stationary_patient():
    s = "INSERT INTO Stationary_patient VALUES\n"
    for i in range(stationary_patient_amount):
        s += "("
        s = s + "'" + random.choice(ward_types_of_hospital) + "',"  
        s = s + "'" + str(random.randrange(100, 500)) + "'," 
        pid = random.choice(stat)
        stat.remove(pid)
        s = s + "'" + pid + "'" 
        s += ")"
        if (i < stationary_patient_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s    
def insert_guest():
    s = "INSERT INTO Guest VALUES\n"
    for i in range(guest_amount):
        s += "("
        s = s + "'" + faker.name() + "'," 
        s = s + "'" + random_id(G_IDs) + "'" 
        s += ")"
        if (i < guest_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s    
def insert_make_appointment():
    s = "INSERT INTO Make_an_appointment VALUES\n"
    for i in range(appointment_amount):
        s += "("
        s = s + "'" + random.choice(P_IDs) + "'," 
        s = s + "'" + random.choice(doctors) + "',"
        s = s + "'" + str(faker.date_time_this_decade()) + "'" 
        s += ")"
        if (i < appointment_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s
def insert_optional_treatment():
    s = "INSERT INTO Optional_treatment VALUES\n"
    for i in range(treatment_amount):
        s += "("
        s = s + "'" + random_id(treatments) + "'," 
        s = s + "'" + str(random.randrange(500, 100000)) + "'," 
        s = s + "'" + random_id(T_IDs) + "'" 
        s += ")"
        if (i < treatment_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s
def insert_get_optional_treatment():
    s = "INSERT INTO Get_optional_treatment VALUES\n"
    number_of_records = 5 # by default
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(P_IDs) + "'," 
        s = s + "'" + random.choice(T_IDs) + "'," 
        s = s + "'" + str(faker.date_time_this_decade()) + "'" 
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s
def insert_visit():
    s = "INSERT INTO Visit VALUES\n"
    number_of_records = 3 # by default
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(stationary_patients) + "'," 
        s = s + "'" + random.choice(G_IDs) + "'," 
        s = s + "'" + str(faker.date_time_this_decade()) + "'" 
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s    
def insert_notice_board():
    s = "INSERT INTO Notice_board VALUES\n"
    number_of_records = 1 # by default
    for i in range(number_of_records):
        s += "("
        s = s + "'" + notice_board_example + "'," 
        s = s + "'" + str(faker.date_time_this_decade()) + "'," 
        s = s + "'" + random.choice(receptionists) + "'" 
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s
def insert_stuff_schedule():
    s = "INSERT INTO Stuff_schedule VALUES\n"
    number_of_records = len(nurses) + len(economic_managers) + len(supply_managers) + len(receptionists)
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(schedule_examples) + "',"
        s = s + "'" + str(faker.date_time_this_decade()) + "'," 
        s = s + "'" + random.choice(nurses+supply_managers+economic_managers+receptionists) + "'" 
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s
def insert_hospital_equipment():
    s = "INSERT INTO Hospital_equipment VALUES\n"
    for i in range(hospital_equipment_amount):
        s += "("
        s = s + "'" + random_id(hospital_equipment_names) + "'," 
        s = s + "'" + str(random.randrange(5, 250)) + "'," 
        s = s + "'" + random_id(HE_IDs) + "'" 
        s += ")"
        if (i < hospital_equipment_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'
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
    return s    
def insert_donate():
    number_of_records = 5 #default
    s = "INSERT INTO Donate VALUES\n"
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(P_IDs) + "'," 
        s = s + "'" + random.choice(receptionists) + "'," 
        s = s + "'" + str(random.randrange(50, 10000)) + "'," 
        s = s + "'" + str(faker.date_time_this_decade()) + "'" 
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s         
def insert_conclude_agreement():
    number_of_records = 3 #default
    s = "INSERT INTO Conclude_agreement VALUES\n"
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(agreement_types) + "'," 
        s = s + "'" + random.choice(P_IDs) + "'," 
        s = s + "'" + random.choice(economic_managers) + "'," 
        s = s + "'" + str(faker.date_time_this_decade()) + "'" 
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n\n'
    return s         
def insert_control():
    s = "INSERT INTO Control VALUES\n"
    for i in range(hospital_equipment_amount):
        used_id.remove('HE-' + str(i+1))
    for i in range(hospital_equipment_amount):
        s += "("
        s = s + "'" + random_id(HE_IDs) + "',"
        s = s + "'" + random.choice(supply_managers) + "'" 
        s += ")"
        if (i < hospital_equipment_amount-1):
            s += ',\n'
        else:
            s += ';\n\n'

    return s       

# the parsing an output of quiries
def first_query(flag,rows):
    patient_id = ""
    if flag == 0:
        print("Please, choose the patient(by P_ID) that have lost the bag:")
        if flazog == 1:
            print("input pid, it must be in form P-i, where i - number is in between 1 and " + str(patient_amount))
        else:
            print("input pid, it must be in form P-i, where i - number is in between 1 and 20")
            global P_IDs
            for i in range(20):
                P_IDs.append("P-" + str(i+1))
        patient_id = input()
        while(not(patient_id in P_IDs)):
            print("There is no patient with such P_ID, please, try again:")
            patient_id = input()
        global query1       
        query = query1.replace('INPUT',patient_id)
        return query
    elif flag == 1:
        file = open("result_query1.txt", "w")
        file.seek(0)
        titles = ["E_ID", "Name", "Surname"]
        sep = 55*'-'
        print("| {: ^15} | {: ^15} | {: ^15} |".format(*titles), file = file)
        print(sep, file = file)
        for row in rows:
            print("| {: ^15} | {: ^15} | {: ^15} |".format(*row), file = file)
        if len(rows)!=0:
            print(sep, file = file)
        print("You can see the output of the query in the result_query1.txt")
        file.close()
        return 0
def second_query(rows):
    file = open("result_query2.txt","w")
    sep = 128*'-'
    titles = ["E_ID", "Name" , "Surname", "Count", "Average", "Day of week", "Time slot"]
    print("| {: ^15} | {: ^15} | {: ^15} | {: ^15} | {: ^15}  | {: ^15} | {: ^15} |".format(*titles),file = file)
    print(sep, file = file)
    c = rows[0]['e_id']
    j = 0
    for row in rows:
        u = row["e_id"]
        if u != c:
            print(sep, file = file)
            c = row['e_id']
        row['app_count_avg'] = round(row['app_count_avg'],3)
        row['time_slot'] = str(row['time_slot'])    
        row['time_slot'] = row['time_slot'] + ":00"
        print("| {: ^15} | {: ^15} | {: ^15} | {: ^15} | {: ^15}  | {: ^15} | {: ^15} |".format(*row), file =  file)
    if len(rows)!=0:
        print(sep, file = file)
    file.close()
    print("You can see the output of the query in the result_query2.txt")
def third_query(rows):
    file = open("result_query3.txt","w")
    titles = ["P_ID"]
    sep = 19*'-'
    print("| {: ^15} |".format(*titles), file = file)
    print(sep, file = file)
    for row in rows:
        print("| {: ^15} |".format(*row), file = file)
    if len(rows)!=0:
        print(sep, file = file)
    file.close()
    print("You can see the output of the query in the result_query3.txt")
def fourth_query(rows):
    file = open("result_query4.txt","w")
    for row in rows:
        print("The expected monthly income: " + str(rows[0][0]) + " rub.", file = file)
    print("You can see the output of the query in the result_query4.txt")
    file.close()
def fifth_query(rows):
    file = open("result_query5.txt", "w")
    titles = ["E_ID", "Name", "Surname"]
    sep = 55*'-'
    print("| {: ^15} | {: ^15} | {: ^15} |".format(*titles), file = file)
    print(sep, file = file)
    for row in rows:
        print("| {: ^15} | {: ^15} | {: ^15} |".format(*row), file = file)
    if len(rows)!=0:
        print(sep, file = file)
    print("You can see the output of the query in the result_query5.txt")
    file.close()

# implementation of queries
def implement_queries(main_insert):
    con = psycopg2.connect(database="dmd_project", user="postgres", password="12345", host="127.0.0.1", port="5432")
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(truncate)
    # if we didn't put '1' in the very beginning --> means that we use an insert that have already been generated and  stored in 'query_insert.txt'
    if flazog != "1": 
        file = open("query_insert.txt", "r")
        main_insert = file.read()
        file.close()
    cursor.execute(main_insert)
    
    loop = "1"
    while(loop == "1"):
        print("Input number of the query to implement: ")
        print("""
                1. A patient claims that she forgot her bag in the room where she had a medical appointment on the last time she came to the hospital. 
                   The problem is that she had several appointments on that same day. She believes that the doctor’s name (first or last name, but not both) starts with “M” or “L”.
                   Find all the possible doctors that match the description.
                
                2. The hospital management team wants to get statistics on the appointments per doctors. 
                   For each doctor, the report should present the total and average number of appointments in each time slot of the week during the last year.
                
                3. The hospital wants to retrieve information on the patients who had an appointment during the previous month.
                   However, an information which is relevant for some managers is to find which patients visited the hospital every week, at least twice a week. 
                   Such patients probably should receive home visits from doctors.
                
                4. Managers want to project the expected monthly income if the hospital start to charge a small value from each patient.
                   The value per appointment would depend on the age and the number of appointments per month. The rules were summarise in the description of phase 3.
                
                5. The managers want to reward experienced and long serving doctors. 
                   For that, they want to find out the doctors who have attended at least five patients per year for the last 10 years.
                   Also, such doctors should have had attended a total of at least 100 patients in this period.
              """)
        flag = int(input())
        while(flag<1 and flag>5):
            print("Wrong number! We had 5 queries to implement --> it must be >0 and <6")
            flag = int(input())
        if flag == 1: 
            cursor.execute(first_query(0,""));
            rows = cursor.fetchall()
            first_query(1,rows)
        elif flag == 2:
            cursor.execute(query2) 
            rows = cursor.fetchall()
            second_query(rows)
        elif flag == 3:
            cursor.execute(query3) 
            rows = cursor.fetchall()
            third_query(rows)
        elif flag == 4:
            cursor.execute(query4)
            rows = cursor.fetchall()
            fourth_query(rows)
        elif flag == 5:
            cursor.execute(query5)
            rows = cursor.fetchall()
            fifth_query(rows)
        print("\nDo you want to request another query? (if yes, input '1', anything otherwise)")
        loop = input()
    
    
    
    con.commit()
    con.close()

if __name__ == "__main__":
    # --------------------------------------
    print("""
    Do you want to generate new insert data or we can use already created large one?
    (To generate new, type '1', otherwise it will use the existed insert that saved in query_insert.txt)
        """)
    global flazog
    flazog = input() # decide to use stored insert or generate new
    main_insert = ""
    if flazog == "1": # --> generate new
        start() #input data
        E_IDs = generating_IDS("E")  #employees ids
        P_IDs = generating_IDS("P")  #patients ids
        HE_IDs = generating_IDS("HE") #hospital equipment ids
        T_IDs = generating_IDS("T")  #treatment ids
        G_IDs = generating_IDS("G") #guests ids

        main_insert = insert_employee()  + insert_patient()  + insert_guest()
        if stationary_patient_amount>0:
            main_insert += insert_stationary_patient() + insert_visit()
        main_insert += insert_make_appointment() + insert_optional_treatment() + insert_get_optional_treatment() + insert_notice_board() + insert_stuff_schedule() + insert_hospital_equipment() + insert_medical_history()  + insert_donate() + insert_conclude_agreement() + insert_control()
        f = open("insert.txt","w+")
        f.write(main_insert)
        f.close()
        print("The insert that our database has you can see in the insert.txt")
    implement_queries(main_insert)