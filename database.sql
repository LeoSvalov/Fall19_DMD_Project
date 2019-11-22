DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- tables to be done:
-- DROP TABLE Create_Report; --
-- DROP TABLE Assign; --
-- DROP TABLE Receive; --
-- DROP TABLE Conclude agreement; --

-- решить вопрос с fill in и medical history!
-- var
CREATE TABLE Employee (
  Name          VARCHAR(30)   NOT NULL,
  Surname       VARCHAR(30)   NOT NULL,   
  Address       VARCHAR(30)   NOT NULL,
  DoB           VARCHAR(15)   NOT NULL,
  Phone         VARCHAR(12)   NOT NULL,
  Email         VARCHAR(30)   NOT NULL,
  Qualification VARCHAR(20)   NOT NULL,
  Type          VARCHAR(15)   NOT NULL,
  E_ID          VARCHAR(15)   NOT NULL  PRIMARY KEY
);
-- 2
CREATE TABLE Notice_board(
  News            VARCHAR(1000),
  Upcoming_events   VARCHAR(1000),
  Date              DATE          NOT NULL,
  E_ID             VARCHAR(15)   REFERENCES Employee(E_ID),
  PRIMARY KEY(Date,E_ID)
);
-- 2
CREATE TABLE Stuff_schedule(
  Schedule   VARCHAR(1000)  NOT NULL,
  Date      DATE           NOT NULL,
  E_ID     VARCHAR(15)    REFERENCES Employee(E_ID),
  PRIMARY KEY(Date,E_ID)
);
-- 5
CREATE TABLE Hospital_equipment(
  HE_ID  VARCHAR(15)   NOT NULL  PRIMARY KEY
);
-- var
CREATE TABLE Patient(
  Name      VARCHAR(30)   NOT NULL,
  Surname      VARCHAR(30)   NOT NULL,
  Address       VARCHAR(30)   NOT NULL,
  Dob           Date  NOT NULL,
  Ward_type     VARCHAR(12),
  Room_num     VARCHAR(20),
  Sex          VARCHAR(15)   NOT NULL,
  Type          VARCHAR(15)   NOT NULL,
  P_ID          VARCHAR(15)   NOT NULL  PRIMARY KEY
);
-- 10
CREATE TABLE Medical_history(
  Illness        VARCHAR(30)   NOT NULL,
  Duration     VARCHAR(50)   NOT NULL,
  Attending_doctor VARCHAR(30)   NOT NULL,
  E_ID        VARCHAR(15)   REFERENCES Employee(E_ID),
  P_ID        VARCHAR(15)   NOT NULL    REFERENCES Patient(P_ID)
);
-- 5
CREATE TABLE Optional_treatment(
  Duration VARCHAR(30)   NOT NULL,
  Price    INT           NOT NULL,
  T_id   VARCHAR(15)     NOT NULL    PRIMARY KEY
);
-- 5
CREATE TABLE Guest(
  Name VARCHAR(30)   NOT NULL,
  G_ID VARCHAR(15)   NOT NULL    PRIMARY KEY
);
-- 3
CREATE TABLE Canteen_menu(
  Type      VARCHAR(15)   NOT NULL,
  E_ID      VARCHAR(15)  REFERENCES Employee(E_ID),
  PRIMARY KEY(Type,E_ID)
);
-- 3
CREATE TABLE Donate(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  E_ID VARCHAR(15)    NOT NULL  REFERENCES Employee(E_ID),
  Amount_of_money INT NOT NULL,
  PRIMARY KEY(P_ID,E_ID)
);
-- 3
CREATE TABLE Visit(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  E_ID VARCHAR(15)    NOT NULL  REFERENCES Employee(E_ID),
  Time timestamp      NOT NULL, 
  PRIMARY KEY(P_ID,E_ID,Time)
);
-- 1
CREATE TABLE Get(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  T_ID VARCHAR(15)    NOT NULL  REFERENCES Optional_treatment(T_ID),
  PRIMARY KEY(P_ID,T_ID)
);
-- var
CREATE TABLE Make_an_appointment(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  E_ID VARCHAR(15)    NOT NULL  REFERENCES Employee(E_ID),
  Date timestamp           NOT NULL,
  PRIMARY KEY(P_ID,E_ID)
);

CREATE TABLE Negotiate_a_purchase(
  Supply_manager    VARCHAR(30)    REFERENCES Employee(E_ID),
  Economic_manager  VARCHAR(30)    REFERENCES Employee(E_ID),
  HE_ID          VARCHAR(15)    REFERENCES Hospital_equipment(HE_ID),
  NP_ID        VARCHAR(30)    PRIMARY KEY
);

CREATE TABLE Contribute(
	Amount_of_money	 INT  NOT NULL,
	G_ID     VARCHAR(15)  NOT NULL    REFERENCES Guest(G_ID),
	E_ID     VARCHAR(15)  NOT NULL    REFERENCES Employee(E_ID),
	PRIMARY KEY(G_ID,E_ID)
);
CREATE TABLE Notify(
	E_ID     VARCHAR(15)    NOT NULL   REFERENCES Employee(E_ID),
	P_ID 	 VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
	PRIMARY KEY(P_ID,E_ID)
);
CREATE TABLE Control(
	E_ID     VARCHAR(15)    NOT NULL REFERENCES Employee(E_ID),
	HE_ID 	 VARCHAR(15)    NOT NULL   REFERENCES Hospital_equipment(HE_ID),
	PRIMARY KEY(HE_ID,E_ID)
);



--script