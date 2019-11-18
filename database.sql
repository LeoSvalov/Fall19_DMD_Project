CREATE TABLE Employee (

	Fullname      VARCHAR(30)   NOT NULL,   
	Address       VARCHAR(30)   NOT NULL,
	Dob           VARCHAR(15)   NOT NULL,
	Phone         VARCHAR(12)   NOT NULL,
	Email         VARCHAR(30)   NOT NULL,
	Qualification VARCHAR(20)   NOT NULL,
	Contract      VARCHAR(15)   NOT NULL,
	Type          VARCHAR(15)   NOT NULL,
	E_id           VARCHAR(15)   NOT NULL,
	HE_id		   VARCHAR(15),
	PRIMARY KEY (E_id)
);

CREATE TABLE Noticeboard(
	News	          VARCHAR(1000),
	Upcoming_events   VARCHAR(1000),
	Date              DATE          NOT NULL,
	E_id 	          VARCHAR(15)   REFERENCES Employee(E_id),
	PRIMARY KEY(Date,E_id)
);

CREATE TABLE Stuff_schedule(
	Shedule  VARCHAR(1000)  NOT NULL,
	Date      DATE          NOT NULL,
	E_id 	  VARCHAR(15)   REFERENCES Employee(E_id),
	PRIMARY KEY(Date,E_id)
);

CREATE TABLE Hospital_equipment(
	HE_id VARCHAR(15)   NOT NULL,
	PRIMARY KEY (HE_id)
);

CREATE TABLE Medical_history(
	Ilness 			 VARCHAR(30)   NOT NULL,
	Duration		 VARCHAR(50)   NOT NULL,
	Attending_doctor VARCHAR(30)   NOT NULL,
	P_id 			 VARCHAR(15)   NOT NULL,
	PRIMARY KEY (P_id)
);

CREATE TABLE Optional_treatment(
	Duration VARCHAR(30)   NOT NULL,
	Price 	 INT           NOT NULL,
	I_id	 VARCHAR(15)   NOT NULL,
	PRIMARY KEY(I_id)
);

CREATE TABLE Guest(
	Name VARCHAR(30)   NOT NULL,
	G_id VARCHAR(15)   NOT NULL,
	PRIMARY KEY(G_id)
);

CREATE TABLE Canteen_menu(
	Type      VARCHAR(15)   NOT NULL,
	E_id 	  VARCHAR(15)REFERENCES Employee(E_id),
	PRIMARY KEY(Type,E_id)
);

CREATE TABLE Patient(
	Fullname      VARCHAR(30)   NOT NULL,
	Address       VARCHAR(30)   NOT NULL,
	Dob           VARCHAR(15)   NOT NULL,
	Ward_type     VARCHAR(12)   NOT NULL,
	Room_num 	   VARCHAR(20)   NOT NULL,
	Sex      	   VARCHAR(15)   NOT NULL,
	Type          VARCHAR(15)   NOT NULL,
	P_id           VARCHAR(15)   NOT NULL,
	PRIMARY KEY (P_id)
);

CREATE TABLE Donate(
	P_ID VARCHAR(15)    NOT NULL,
	E_ID VARCHAR(15)    NOT NULL,
	Amount_of_money INT NOT NULL,
	PRIMARY KEY(P_ID,E_ID)
);

CREATE TABLE Visit(
	P_ID VARCHAR(15)    NOT NULL,
	E_ID VARCHAR(15)    NOT NULL,
	Time timestamp 		NOT NULL, 
	PRIMARY KEY(P_ID,E_ID,Time)
);

CREATE TABLE Get(
	P_ID VARCHAR(15)    NOT NULL,
	T_ID VARCHAR(15)    NOT NULL,
	PRIMARY KEY(P_ID,T_ID)
);
CREATE TABLE Make_an_appointment(
	P_ID VARCHAR(15)    NOT NULL,
	E_ID VARCHAR(15)    NOT NULL,
	PRIMARY KEY(P_ID,E_ID)
);
	INSERT INTO Hospital_equipment VALUES
	('qwe'),
	('rewt'),
	('feww');