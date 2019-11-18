DROP TABLE Notice_board;
DROP TABLE Stuff_schedule;
DROP TABLE Medical_history;
DROP TABLE Guest;
DROP TABLE Canteen_menu;
DROP TABLE Donate;
DROP TABLE Visit;
DROP TABLE Get;
DROP TABLE Make_an_appointment;
-- DROP TABLE Contribute; 
-- DROP TABLE Notify;
-- DROP TABLE Alert; --
-- DROP TABLE Control; --
-- DROP TABLE Fill_in; --
-- DROP TABLE Create_Report; --
-- DROP TABLE Assign; --
-- DROP TABLE Receive; --
-- DROP TABLE Conclude agreement; --
DROP TABLE Negotiate_a_purchase;
DROP TABLE Hospital_equipment;
DROP TABLE Optional_treatment;
DROP TABLE Patient;
DROP TABLE Employee;


CREATE TABLE Employee (
  Name          VARCHAR(30)   NOT NULL,
  Surname       VARCHAR(30)   NOT NULL,   
  Address       VARCHAR(30)   NOT NULL,
  Dob           VARCHAR(15)   NOT NULL,
  Phone         VARCHAR(12)   NOT NULL,
  Email         VARCHAR(30)   NOT NULL,
  Qualification VARCHAR(20)   NOT NULL,
  Type          VARCHAR(15)   NOT NULL,
  E_ID          VARCHAR(15)   NOT NULL  PRIMARY KEY
);

CREATE TABLE Notice_board(
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
  T_id   VARCHAR(15)     NOT NULL    PRIMARY KEY
);

CREATE TABLE Guest(
  Name VARCHAR(30)   NOT NULL,
  G_ID VARCHAR(15)   NOT NULL    PRIMARY KEY
);

CREATE TABLE Canteen_menu(
  Type      VARCHAR(15)   NOT NULL,
  E_ID      VARCHAR(15)  REFERENCES Employee(E_ID),
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
  Time timestamp      NOT NULL, 
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
  Date DATE           NOT NULL,
  PRIMARY KEY(P_ID,E_ID)
);

CREATE TABLE Negotiate_a_purchase(
  Supply_manager    VARCHAR(30)    REFERENCES Employee(E_ID),
  Economic_manager  VARCHAR(30)    REFERENCES Employee(E_ID),
  HE_ID          VARCHAR(15)    REFERENCES Hospital_equipment(HE_ID),
  NP_ID        VARCHAR(30)    PRIMARY KEY
);

-- CREATE TABLE Contribute(
-- 	Amount_of_money	 INT  NOT NULL,
-- 	G_ID     VARCHAR(15)  NOT NULL    REFERENCES Guest(G_ID),
-- 	E_ID     VARCHAR(15)  NOT NULL    REFERENCES Employee(E_ID),
-- 	PRIMARY KEY(G_ID,E_ID)
-- );
-- CREATE TABLE Notify(
-- 	E_ID     VARCHAR(15)    NOT NULL   REFERENCES Employee(E_ID),
-- 	P_ID 	 VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
-- 	PRIMARY KEY(P_ID,E_ID)
-- )
-- CREATE TABLE Manages(
-- 	E_ID     VARCHAR(15)    NOT NULL   REFERENCES Employee(E_ID),
-- 	P_ID 	 VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
-- 	PRIMARY KEY(P_ID,E_ID)
-- )

INSERT INTO Patient VALUES
('Alice', 'Nemartyanova', 'Russia', '12/08/00', 'terapevt', '200', 'female', 'not', 'Apat'),
('Zhandos', 'Kip', 'Kazakhstan', '23/11/00', 'terapevt', '200', 'male', 'not', 'Zpat');

INSERT INTO Employee VALUES
('Alice', 'Martyanova', 'Ne znau', '12/05/00', '43254523324', 'alicem@gmail.com', 'WELL', 'Nurse', '2AM'),
('Shamil', 'Khastiev', 'Kazan', '23/11/00', '89064675162', 'shamilk@gmail.com', 'LOL', 'Cleaning', '3SK'),
('M sekzhan', 'Talgat', 'Ayagoz', '03/02/01', '89047611375', 'bekzhant@gmail.com', 'GOOD', 'Doctor', '1BT');

INSERT INTO Make_an_appointment VALUES
('Apat','2AM','2008-03-20'),
('Apat','3SK','2018-11-18'),
('Zpat','1BT','2018-11-25'),
('Zpat','2AM','2019-09-20'),
('Apat','1BT','2018-12-20');


SELECT * FROM Employee as d INNER JOIN  Make_an_appointment as m
ON m.E_ID = d.E_ID and m.P_ID = 'Apat'
WHERE
m.Date = (SELECT MAX(Date) FROM Make_an_appointment
WHERE Make_an_appointment.P_ID = 'Apat') 
and d.type = 'Doctor' 
and ((d.surname LIKE 'L%' or d.surname LIKE 'M%' ) 
and (d.name NOT LIKE 'L%' and d.name NOT LIKE 'M%'))
or ((d.name LIKE 'L%' or d.name LIKE 'M%')
and (d.surname NOT LIKE 'L%' and d.surname NOT LIKE 'M%'));



--script