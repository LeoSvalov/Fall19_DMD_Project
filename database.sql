DROP TABLE Notice_board;
DROP TABLE Stuff_schedule;
DROP TABLE Hospital_equipment;
DROP TABLE Medical_history;
DROP TABLE Optional_treatment;
DROP TABLE Guest;
DROP TABLE Canteen_menu;
DROP TABLE Patient;
DROP TABLE Donate;
DROP TABLE Visit;
DROP TABLE Get;
DROP TABLE Make_an_appointment;
DROP TABLE Employee;


CREATE TABLE Employee (
  Name          VARCHAR(30)   NOT NULL,
  Surname       VARCHAR(30)   NOT NULL,   
  Address       VARCHAR(30)   NOT NULL,
  Dob           VARCHAR(15)   NOT NULL,
  Phone         VARCHAR(12)   NOT NULL,
  Email         VARCHAR(30)   NOT NULL,
  Qualification VARCHAR(20)   NOT NULL,
  Contract      VARCHAR(15)   NOT NULL,
  Type          VARCHAR(15)   NOT NULL,
  E_ID          VARCHAR(15)   NOT NULL  PRIMARY KEY
);

CREATE TABLE Noticeboard(
  News            VARCHAR(1000),
  Upcoming_events   VARCHAR(1000),
  Date              DATE          NOT NULL,
  E_ID             VARCHAR(15)   REFERENCES Employee(E_ID),
  PRIMARY KEY(Date,E_ID)
);

CREATE TABLE Stuff_schedule(
  Shedule   VARCHAR(1000)  NOT NULL,
  Date      DATE           NOT NULL,
  E_ID     VARCHAR(15)    REFERENCES Employee(E_ID),
  PRIMARY KEY(Date,E_ID)
);

CREATE TABLE Hospital_equipment(
  HE_ID  VARCHAR(15)   NOT NULL  PRIMARY KEY
);

CREATE TABLE Patient(
  Name      VARCHAR(30)   NOT NULL,
  Surname      VARCHAR(30)   NOT NULL,
  Address       VARCHAR(30)   NOT NULL,
  Dob           VARCHAR(15)   NOT NULL,
  Ward_type     VARCHAR(12),
  Room_num     VARCHAR(20),
  Sex          VARCHAR(15)   NOT NULL,
  Type          VARCHAR(15)   NOT NULL,
  P_ID          VARCHAR(15)   NOT NULL  PRIMARY KEY
);

CREATE TABLE Medical_history(
  M_ID       VARCHAR(30)   NOT NULL    PRIMARY KEY,
  Ilness        VARCHAR(30)   NOT NULL,
  Duration     VARCHAR(50)   NOT NULL,
  Attending_doctor VARCHAR(30)   NOT NULL,
  P_ID        VARCHAR(15)   NOT NULL    REFERENCES Patient(P_ID)
);

CREATE TABLE Optional_treatment(
  Duration VARCHAR(30)   NOT NULL,
  Price    INT           NOT NULL,
  T_id   VARCHAR(15)   NOT NULL    PRIMARY KEY
);

CREATE TABLE Guest(
  Name VARCHAR(30)   NOT NULL,
  G_ID VARCHAR(15)   NOT NULL    PRIMARY KEY
);

CREATE TABLE Canteen_menu(
  Type      VARCHAR(15)   NOT NULL,
  E_ID     VARCHAR(15)  REFERENCES Employee(E_ID),
  PRIMARY KEY(Type,E_ID)
);


CREATE TABLE Donate(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  E_ID VARCHAR(15)    NOT NULL  REFERENCES Employee(E_ID),
  Amount_of_money INT NOT NULL,
  PRIMARY KEY(P_ID,E_ID)
);

CREATE TABLE Visit(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  E_ID VARCHAR(15)    NOT NULL  REFERENCES Employee(E_ID),
  Time timestamp     NOT NULL, 
  PRIMARY KEY(P_ID,E_ID,Time)
);

CREATE TABLE Get(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  T_ID VARCHAR(15)    NOT NULL  REFERENCES Optional_treatment(T_ID),
  PRIMARY KEY(P_ID,T_ID)
);

CREATE TABLE Make_an_appointment(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  E_ID VARCHAR(15)    NOT NULL  REFERENCES Employee(E_ID),
  Date DATE         NOT NULL,
  PRIMARY KEY(P_ID,E_ID)
);

CREATE TABLE Negotiate_a_purchase(
  Supply_manager    VARCHAR(30)    REFERENCES Employee(E_ID),
  Economic_manager  VARCHAR(30)    REFERENCES Employee(E_ID),
  HE_ID          VARCHAR(15)    REFERENCES Hospital_equipment(HE_ID),
  NP_ID        VARCHAR(30)    PRIMARY KEY
);


INSERT INTO Employee VALUES
('Alice', 'Martyanova', 'Ne znau', '12/05/00', '43254523324', 'alicem@gmail.com', 'WELL', 'ktk', 'Nurse', '2AM'),
('Shamil', 'Khastiev', 'Kazan', '23/11/00', '89064675162', 'shamilk@gmail.com', 'LOX', 'kek', 'Cleaning', '3SK'),
('Bekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhantalgat01@gmail.com', 'GOOD', 'ftna', 'Doctor', '1BT');

INSERT INTO Patient  VALUES
('Alice', 'Nemartyanova', 'Russia', '12/08/2000', 'terapevt', '200', 'female', 'not', 'Apat');

INSERT INTO Patient VALUES
('Alice', 'Nemartyanova', 'Russia', '12/08/00', 'terapevt', '200', 'female', 'not', 'Apat'),
('Zhandos', 'Kip', 'Kazakhstan', '23/11/00', 'terapevt', '200', 'male', 'not', 'Zpat');

INSERT INTO Make_an_appointment VALUES
('Apat','2AM','2008-03-20'),
('Apat','3SK','2018-11-18'),
('Zpat','1BT','2018-11-25'),
('Zpat','2AM','2019-09-20'),
('Apat','1BT','2018-12-20');

INSERT INTO Employee VALUES
('Llice', 'Martyanova', 'Ne znau', '12/05/00', '43254523324', 'alicem@gmail.com', 'WELL', 'ktk', 'Doctor', '2AM'),
('Mhamil', 'Khastiev', 'Kazan', '23/11/00', '89064675162', 'shamilk@gmail.com', 'LOX', 'kek', 'Doctor', '3SK'),
('Mekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhantalgat01@gmail.com', 'GOOD', 'Doctor', 'Doctor', '1BT');

INSERT INTO Make_an_appointment VALUES
('Apat','2AM','2008-03-20'),
('Apat','3SK','2008-03-20');


--script