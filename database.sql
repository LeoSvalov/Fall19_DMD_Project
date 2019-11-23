DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- 1
CREATE TABLE Employee (
  Name          VARCHAR(30)   NOT NULL,
  Surname       VARCHAR(30)   NOT NULL,   
  Address       VARCHAR(150)   NOT NULL,
  DoB           Date   NOT NULL,
  Phone         VARCHAR(25)   NOT NULL,
  Email         VARCHAR(50)   NOT NULL,
  Qualification VARCHAR(20)   NOT NULL,
  Type          VARCHAR(25)   NOT NULL,
  E_ID          VARCHAR(15)   NOT NULL  PRIMARY KEY
);

-- 2
CREATE TABLE Patient(
  Name      VARCHAR(30)   NOT NULL,
  Surname      VARCHAR(30)   NOT NULL,
  Address       VARCHAR(150)   NOT NULL,
  DoB           Date  NOT NULL,
  Sex          VARCHAR(15)   NOT NULL,
  Type          VARCHAR(15)   NOT NULL,
  P_ID          VARCHAR(15)   NOT NULL  PRIMARY KEY
);

-- 3
CREATE TABLE Stationary_patient (
    Ward_type       VARCHAR(12) NOT NULL,
    Room_num        VARCHAR(15) NOT NULL,
    P_ID            VARCHAR(15) NOT NULL        REFERENCES Patient(P_ID)    PRIMARY KEY
);

--4
CREATE TABLE Guest(
  Name VARCHAR(30)   NOT NULL,
  G_ID VARCHAR(15)   NOT NULL    PRIMARY KEY
);

--5
CREATE TABLE Make_an_appointment(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  E_ID VARCHAR(15)    NOT NULL  REFERENCES Employee(E_ID),
  Date timestamp           NOT NULL,
  PRIMARY KEY(P_ID,E_ID,Date)
);

--6
CREATE TABLE Optional_treatment(
  Name VARCHAR(30)   NOT NULL,
  Price    INT           NOT NULL,
  T_id   VARCHAR(15)     NOT NULL    PRIMARY KEY
);

-- 7
CREATE TABLE Get_optional_treatment (
    P_ID            varchar(15) NOT NULL        REFERENCES Patient(P_ID),
    T_ID            varchar(15) NOT NULL        REFERENCES Optional_treatment(T_ID),
    Date 			date 		NOT NULL,
    PRIMARY KEY(P_ID, T_ID, Date)
);

-- 8
CREATE TABLE Visit(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  G_ID VARCHAR(15)    NOT NULL  REFERENCES Guest(G_ID),
  Date timestamp      NOT NULL, 
  PRIMARY KEY(P_ID,G_ID,Date)
);

-- 9
CREATE TABLE Notice_board(
  News_and_Events            VARCHAR(1000),
  Date              DATE          NOT NULL,
  E_ID             VARCHAR(15)   REFERENCES Employee(E_ID),
  PRIMARY KEY(Date,E_ID)
);

--10 
CREATE TABLE Stuff_schedule(
    Schedule        VARCHAR(1000)   NOT NULL,
    Date            DATE            NOT NULL,
    E_ID            varchar(15)     NOT NULL    REFERENCES Employee(E_ID),
    PRIMARY KEY(Date,E_ID)
);

-- 11
CREATE TABLE Hospital_equipment(
    Name        VARCHAR(50)     NOT NULL,
    Amount          INT             NOT NULL,
    HE_ID           VARCHAR(15)     NOT NULL    PRIMARY KEY
);

-- 12
CREATE TABLE Medical_history(
  Diagnosis        VARCHAR(500)   NOT NULL,
  Treatment_start Date            NOT NULL,
  Treatment_end   Date            NOT NULL,
  E_ID        VARCHAR(15)   REFERENCES Employee(E_ID),
  P_ID        VARCHAR(15)   NOT NULL    REFERENCES Patient(P_ID)
);

-- 13
CREATE TABLE Donate(
  P_ID VARCHAR(15)    NOT NULL   REFERENCES Patient(P_ID),
  E_ID VARCHAR(15)    NOT NULL  REFERENCES Employee(E_ID),
  Amount_of_money INT NOT NULL,
  Date            timestamp       NOT NULL,
  PRIMARY KEY(P_ID,Date)
);

-- 14
CREATE TABLE Conclude_agreement (
    Type            VARCHAR(30)     NOT NULL,
    P_ID            VARCHAR(15)     NOT NULL    REFERENCES Patient(P_ID),
    Economic_manager            VARCHAR(15)     NOT NULL    REFERENCES Employee(E_ID),
    Date            timestamp       NOT NULL,
    PRIMARY KEY(Type, P_ID, Date)
);

-- 15
CREATE TABLE Control (
    HE_ID           VARCHAR(15)     NOT NULL,
    Supply_manager  VARCHAR(15)     NOT NULL    REFERENCES Employee(E_ID),
    PRIMARY KEY(HE_ID, Supply_manager)
);
