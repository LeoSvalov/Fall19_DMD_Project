import random
from random import randrange
import psycopg2
import string
from faker import Faker
faker = Faker('en_US')

# print("-------------------------------------------")
# print("Welcome to the hospital database interface!")
# print("-------------------------------------------")
# print("")
print("Please, input some needed amounts for our system:")
print("     Amount of employees:")
employee_amount = int(input())
print("     Amount of patients:")
patient_amount = int(input())
print("     Amount of guests:")
guest_amount = int(input())
print("     Amount of treatments:")
treatment_amount = int(input())
print("     Amount of hospital equipments:")
hospital_equipment_amount = int(input())
print("     Amount of appoinments between the particular doctor and the particular patient:")
appointment_amount = int(input())
# print("Thanks!")
qualifications = ["high", "mid", "low"]
types_of_employee = ["Nurse", "Doctor", "Economic Manager", "Supply Manager", "Receprionist"]
ward_types_of_hospital = ["terapevt", "lor", "hor", "mor", "dor"]
canteen_menu_types = ["vegan", "non vegan"]
used_id = []

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
        s = s + "'" + random.choice(types_of_employee) + "'," #type
        s = s + "'" + random_id(E_IDs) + "'" #id
        s += ")"
        if (i < employee_amount-1):
            s += ',\n'
        else:
            s += ';\n'
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
        s = s + "'" + random.choice(ward_types_of_hospital) + "',"  #ward type
        s = s + "'" + str(random.randrange(100, 500)) + "'," #room
        s = s + "'" + random.choice(["male", "female"]) + "',"  #sex
        s = s + "'" + random.choice(["stat", "ambul"]) + "',"  #type
        s = s + "'" + random_id(P_IDs) + "'" #id
        s += ")"
        if (i < patient_amount-1):
            s += ',\n'
        else:
            s += ';\n'
    # print(s)
    return s
def insert_guest():
    s = "INSERT INTO Guest VALUES\n"
    for i in range(guest_amount):
        s += "("
        s = s + "'" + faker.name() + "'," #name
        s = s + "'" + random_id(P_IDs) + "'" #id
        s += ")"
        if (i < guest_amount-1):
            s += ',\n'
        else:
            s += ';\n'
    # print(s)
    return s    
def insert_make_appointment():
    s = "INSERT INTO Make_an_appointment VALUES\n"
    for i in range(appointment_amount):
        s += "("
        s = s + "'" + random.choice(P_IDs) + "'," #Patient
        s = s + "'" + random.choice(E_IDs) + "'," #Employee
        s = s + "'" + str(faker.date_time_this_decade()) + "'" #Date
        s += ")"
        if (i < appointment_amount-1):
            s += ',\n'
        else:
            s += ';\n'
    # print(s)
    return s
def insert_canteen():
    s = "INSERT INTO Canteen_menu VALUES\n"

    for i in range(guest_amount):
        s += "("
        s = s + "'" + random.choice(canteen_menu_types) + "'," #name
        s = s + "'" + random.choice(E_IDs) + "'" #id
        s += ")"
        if (i < guest_amount-1):
            s += ',\n'
        else:
            s += ';\n'
    # print(s)
    return s
def insert_donate():
    number_of_records = 3
    s = "INSERT INTO Donate VALUES\n"
    for i in range(number_of_records):
        s += "("
        s = s + "'" + random.choice(P_IDs) + "'," #pid
        s = s + "'" + random.choice(E_IDs) + "'," #eid
        s = s + "'" + str(random.randrange(10, 1000000)) + "'" #amount of money
        s += ")"
        if (i < number_of_records-1):
            s += ',\n'
        else:
            s += ';\n'
    # print(s)
    return s         



patient_insert = insert_patient()
employee_insert =  insert_employee()
make_appointment  = insert_make_appointment()


con = psycopg2.connect(database="dmd_project", user="postgres", password="12345", host="127.0.0.1", port="5432")
print("Database opened successfully")
cur = con.cursor()
 # надо для всех заполненных нами таблиц
cur.execute("TRUNCATE Patient CASCADE;");
cur.execute("TRUNCATE Employee CASCADE;");
cur.execute("TRUNCATE Make_an_appointment CASCADE;");

insert =""" 
            INSERT INTO Patient VALUES
            ('Alice', 'Nemartyanova', 'Russia', '2008-03-20', 'terapevt', '200', 'female', 'not', 'Apat'),
            ('Zhandos', 'Kip', 'Kazakhstan', '2008-03-20', 'terapevt', '200', 'male', 'not', 'Zpat'),
            ('Zhandos', 'Kip', 'Kazakhstan', '2008-03-20', 'terapevt', '200', 'male', 'not', 'Zhpat'),
            ('Leva', 'Svalov', 'Ekat', '2008-03-20', 'terapevt', '200', 'male', 'not', 'Lpat');

            INSERT INTO Employee VALUES
            ('Alice', 'Martyanova', 'Ne znau', '12/05/00', '43254523324', 'alicem@gmail.com', 'WELL', 'Nurse', '2AM'),
            ('Shamil', 'Khastiev', 'Kazan', '23/11/00', '89064675162', 'shamilk@gmail.com', 'LOL', 'Cleaning', '3SK'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '1BT'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '2BT'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '3BT'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '4BT'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '5BT'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '6BT'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '7BT'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '8BT'),
            ('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '9BT');


            INSERT INTO Make_an_appointment VALUES
            ('Apat','2AM','2008-03-20 06:00:00'),
            ('Apat','3SK','2019-11-18 06:00:00'),
            ('Zpat','1BT','2018-11-25 06:00:00'),
            ('Zpat','3SK','2018-09-20 06:00:00'),
            ('Zhpat','3SK','2018-09-20 06:00:00'),
            ('Apat','1BT','2018-12-20 06:00:00'),
            ('Lpat','3SK','2019-11-19 06:00:00'),
            ('Lpat','1BT','2019-11-18 06:00:00'),
            ('Lpat','2AM','2019-11-13 06:00:00'),
            ('Lpat','2BT','2019-11-10 06:00:00'),
            ('Lpat','3BT','2019-11-07 06:00:00'),
            ('Lpat','4BT','2019-11-05 06:00:00'),
            ('Lpat','5BT','2019-11-01 06:00:00'),
            ('Lpat','6BT','2019-10-30 06:00:00'),
            ('Lpat','7BT','2019-10-28 06:00:00'),
            ('Lpat','8BT','2019-10-23 06:00:00'),
            ('Lpat','9BT','2019-10-21 06:00:00');
        """
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
cur.execute(insert);

cur.execute(query4);    
rows = cur.fetchall()
print("output:")
for row in rows:
    print(row) 
con.commit()
print("Records inserted successfully")
con.close()
