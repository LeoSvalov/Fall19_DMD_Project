import random
from random import randrange
from datetime import timedelta
from datetime import datetime
import string
from faker import Faker


faker = Faker()
filename = "database.sql"
E_IDs = []
P_IDs = []

def delete_old(filename: str):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    f = open(filename, "w")
    for line in lines:
        f.write(line)
        if line.startswith("--script"):
            break
    f.close()
def fill_employee(filename: str):
    qualifications = ["high", "mid", "low"]
    types = ["Nurse", "Doctor", "Economic Manager", "Supply Manager", "Receprionist"]
    number_of_records = 5
    f = open(filename, "a")
    query = "INSERT INTO Employee VALUES\n"
    for i in range(number_of_records):
        query += "("
        query = query + "'" + random.choice(names) + "'," #name
        query = query + "'" + random.choice(surnames) + "'," #surname
        query = query + "'" + random.choice(cities) + "'," #city
        query = query + "'" + random_date() + "'," #date of birth
        query = query + "'" + "8" + str(random.randrange(1000000000, 9999999999)) + "'," #phone number
        query = query + "'" + random_string(10)+"@gmail.com" + "'," #email
        query = query + "'" + random.choice(qualifications) + "'," #qualification
        query = query + "'" + random.choice(types) + "'," #type
        query = query + "'" + random_id(E_IDs) + "'" #id
        query += ")"
        if (i < number_of_records-1):
            query += ',\n'
        else:
            query += ';\n'
    print(query)
    f.write(query)
    f.write("\n")
def fill_patient(filename: str):
    ward_types = ["terapevt", "lor", "hor", "mor", "dor"]
    number_of_records = 5
    f = open(filename, "a")
    query = "INSERT INTO Patient VALUES\n"
    for i in range(number_of_records):
        query += "("
        query = query + "'" + random.choice(names) + "'," #name
        query = query + "'" + random.choice(surnames) + "'," #surname
        query = query + "'" + random.choice(cities) + "'," #city
        query = query + "'" + random_date() + "'," #date of birth
        query = query + "'" + random.choice(ward_types) + "',"  #ward type
        query = query + "'" + str(random.randrange(100, 300)) + "'," #room
        query = query + "'" + random.choice(["male", "female"]) + "',"  #sex
        query = query + "'" + random.choice(["stat", "ambul"]) + "',"  #type
        query = query + "'" + random_id(P_IDs) + "'" #id
        query += ")"
        if (i < number_of_records-1):
            query += ',\n'
        else:
            query += ';\n'
    print(query)
    f.write(query)
    f.write("\n")
def fill_Make_an_appointment(filename: str):
    number_of_records = 5
    f = open(filename, "a")
    query = "INSERT INTO Patient VALUES\n"
    for i in range(number_of_records):
        query += "("
        query = query + "'" + random.choice(P_IDs) + "'," #Patient
        query = query + "'" + random.choice(E_IDs) + "'," #Employee
        query = query + "'" + random_date() + "'" #Date
        query += ")"
        if (i < number_of_records-1):
            query += ',\n'
        else:
            query += ';\n'
    print(query)
    f.write(query)
    f.write("\n")
def random_date():
    start = datetime.strptime('1/1/2009', '%d/%m/%Y')
    end = datetime.strptime('1/1/2019', '%d/%m/%Y')
    delta = end - start
    random_days = randrange(delta.days)
    return (start + timedelta(days=random_days)).strftime('%d/%m/%y')
def random_id(ids: list):
    id = random_string(15)
    while (id in ids):
        id = random_string(15)
    ids.append(id)
    return id
def random_string(l: int):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(l))
# delete_old(filename)
# fill_patient(filename)
# fill_employee(filename)
# fill_Make_an_appointment(filename)
import psycopg2
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
            ('Apat','2AM','2008-03-20'),
            ('Apat','3SK','2019-11-18'),
            ('Zpat','1BT','2018-11-25'),
            ('Zpat','3SK','2018-09-20'),
            ('Zhpat','3SK','2018-09-20'),
            ('Apat','1BT','2018-12-20'),
            ('Lpat','3SK','2019-11-19'),
            ('Lpat','1BT','2019-11-18'),
            ('Lpat','2AM','2019-11-13'),
            ('Lpat','2BT','2019-11-10'),
            ('Lpat','3BT','2019-11-07'),
            ('Lpat','4BT','2019-11-05'),
            ('Lpat','5BT','2019-11-01'),
            ('Lpat','6BT','2019-10-30'),
            ('Lpat','7BT','2019-10-28'),
            ('Lpat','8BT','2019-10-23'),
            ('Lpat','9BT','2019-10-21');
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
