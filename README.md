# Data Modeling and Databases project during the Fall 2019 semester, Innopolis University
**Team** - [Lev Svalov](https://github.com/LeoSvalov), [Shamil Khastiev](https://github.com/sham1lk), [Alisa Martyanova](https://github.com/AlisaMartyanova), [Bekzhan Talgat](https://github.com/Beka-13), [Zhandos Kipshakbaev](https://github.com/InnoZhan)

## Description of the project
 The project was about producing a database design for a **Hospital Management System** used to manage any hospital.
### The first phase
During the first phase, we were required to come up with domain description in the form of **requirements** (functional and non-functional) and **use-case diagrams**.
### The second phase
During the second phase, we were required to create **an entity-relationship diagram** based on our domain description. Any choices we made *(about weak and strong entities, total and partial participation, single and multi-valued attributes, etc)* are well-explained in the report of the 2nd phase.
### The third phase
In the last phase, we were creating an implementation of the database. 
There we needed to make the following points of the implementation:
- **Create database structure**: convert the ER diagram into a real database using Data Definition Language (DDL). The dumb file *(file with bunch of creates tables)* should be for the PostgreSQL as well as for the MySQL. The database *(all tables)* must be in the [3NF](https://en.wikipedia.org/wiki/Third_normal_form).
- **Populate your database with sample data**: All tables of our database should be inserting with some sample data. So, we have created a script that generates it. The code of the generator you can see in the  ```main.py```. We're using the library [**faker**](https://github.com/joke2k/faker) that generates an enourmous amount of data of different types.
- **Implement 5 proposed queries**: We should write a script that interacts with our database and perform select queries that are described in the ```[F19] DMD Project Phase III.pdf```. The script was created in the python (see code in the ```main.py```) using library **psycopg2** that helps us interacting with the database. Our SQL implementation of proposed queries you can see in the ```queries.py```. 
- **The final report of the project**: We've provided changed the ER and Use-case diagrams with well-explained design decision and feedback changes. 

We had fun and enjoyed doing the project. Cheers!
