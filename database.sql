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
	Name      	  VARCHAR(30)   NOT NULL,
	Surname       VARCHAR(30)   NOT NULL,   
	Address       VARCHAR(30)   NOT NULL,
	Dob           VARCHAR(15)   NOT NULL,
	Phone         VARCHAR(12)   NOT NULL,
	Email         VARCHAR(30)   NOT NULL,
	Qualification VARCHAR(20)   NOT NULL,
	Contract      VARCHAR(15)   NOT NULL,
	Type          VARCHAR(15)   NOT NULL,
	E_ID          VARCHAR(15)   NOT NULL	PRIMARY KEY
);

CREATE TABLE Noticeboard(
	News	          VARCHAR(1000),
	Upcoming_events   VARCHAR(1000),
	Date              DATE          NOT NULL,
	E_ID 	          VARCHAR(15)   REFERENCES Employee(E_ID),
	PRIMARY KEY(Date,E_ID)
);

CREATE TABLE Stuff_schedule(
	Shedule   VARCHAR(1000)  NOT NULL,
	Date      DATE           NOT NULL,
	E_ID 	  VARCHAR(15)    REFERENCES Employee(E_ID),
	PRIMARY KEY(Date,E_ID)
);

CREATE TABLE Hospital_equipment(
	HE_ID	VARCHAR(15)   NOT NULL	PRIMARY KEY
);

CREATE TABLE Medical_history(
	M_ID			 VARCHAR(30)   NOT NULL		PRIMARY KEY(M_ID),
	Ilness 			 VARCHAR(30)   NOT NULL,
	Duration		 VARCHAR(50)   NOT NULL,
	Attending_doctor VARCHAR(30)   NOT NULL,
	P_ID 			 VARCHAR(15)   NOT NULL		REFERENCES Patient(P_ID),
);

CREATE TABLE Optional_treatment(
	Duration VARCHAR(30)   NOT NULL,
	Price 	 INT           NOT NULL,
	T_id	 VARCHAR(15)   NOT NULL		PRIMARY KEY(T_id)
);

CREATE TABLE Guest(
	Name VARCHAR(30)   NOT NULL,
	G_ID VARCHAR(15)   NOT NULL		PRIMARY KEY(G_ID)
);

CREATE TABLE Canteen_menu(
	Type      VARCHAR(15)   NOT NULL,
	E_ID 	  VARCHAR(15)	REFERENCES Employee(E_ID),
	PRIMARY KEY(Type,E_ID)
);

CREATE TABLE Patient(
	Fullname      VARCHAR(30)   NOT NULL,
	Address       VARCHAR(30)   NOT NULL,
	Dob           VARCHAR(15)   NOT NULL,
	Ward_type     VARCHAR(12)   NOT NULL,
	Room_num 	  VARCHAR(20)   NOT NULL,
	Sex      	  VARCHAR(15)   NOT NULL,
	Type          VARCHAR(15)   NOT NULL,
	P_ID          VARCHAR(15)   NOT NULL	PRIMARY KEY
);

CREATE TABLE Donate(
	P_ID VARCHAR(15)    NOT NULL 	REFERENCES Patient(P_ID),
	E_ID VARCHAR(15)    NOT NULL	REFERENCES Employee(E_ID),
	Amount_of_money INT NOT NULL,
	PRIMARY KEY(P_ID,E_ID)
);

CREATE TABLE Visit(
	P_ID VARCHAR(15)    NOT NULL 	REFERENCES Patient(P_ID),
	E_ID VARCHAR(15)    NOT NULL	REFERENCES Employee(E_ID),
	Time timestamp 		NOT NULL, 
	PRIMARY KEY(P_ID,E_ID,Time)
);

CREATE TABLE Get(
	P_ID VARCHAR(15)    NOT NULL 	REFERENCES Patient(P_ID),
	T_ID VARCHAR(15)    NOT NULL	REFERENCES Optional_treatment(T_ID),
	PRIMARY KEY(P_ID,T_ID)
);

CREATE TABLE Make_an_appointment(
	P_ID VARCHAR(15)    NOT NULL 	REFERENCES Patient(P_ID),
	E_ID VARCHAR(15)    NOT NULL	REFERENCES Employee(E_ID),
	Date DATE 		    NOT NULL,
	PRIMARY KEY(P_ID,E_ID)
);
<<<<<<< HEAD
	INSERT INTO Hospital_equipment VALUES
	('qwe'),
	('rewt'),
	('feww');


--shoma loh 
=======

CREATE TABLE Negotiate_a_purchase(
	Supply_manager		VARCHAR(30)		REFERENCES Employee(E_ID),
	Economic_manager	VARCHAR(30)		REFERENCES Employee(E_ID),
	HE_ID		  		VARCHAR(15)		REFERENCES Hospital_equipment(HE_ID),
	NP_ID				VARCHAR(30)		PRIMARY KEY
);




































>>>>>>> 4a8b123239eba95fd1e932c9e4e26814647c1e92
