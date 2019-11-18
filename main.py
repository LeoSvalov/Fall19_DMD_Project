import random
from random import randrange
from datetime import timedelta
from datetime import datetime
import string

filename = "database.sql"
names = ["Curt", "Curtis", "Cushla", "Cuthbert", "Cy", "Cynddelw", "Cynthia", "Cyprian", "Cyril", "Cyrille", "Cyrille", "Cyrus", "Cystenian", "Da", "Daffodil", "Dafydd", "Dag", "Dagmar", "Dagmar"]
surnames = ["Curt", "Curtis", "Cushla", "Cuthbert", "Cy", "Cynddelw", "Cynthia", "Cyprian", "Cyril", "Cyrille", "Cyrille", "Cyrus", "Cystenian", "Da", "Daffodil", "Dafydd", "Dag", "Dagmar", "Dagmar"]
cities = ["Astana", "Almaty", "Moscow", "Piter", "Kostanay"]
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
delete_old(filename)
fill_patient(filename)
fill_employee(filename)
fill_Make_an_appointment(filename)
