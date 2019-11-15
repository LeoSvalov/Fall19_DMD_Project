CREATE TABLE Employee (

	Fullname:      VARCHAR(30),
	Address:       VARCHAR(30),
	Dob:           VARCHAR(15),
	Phone:         VARCHAR(12),
	Email:         VARCHAR(30),
	Qualification: VARCHAR(20),
	Contract:      VARCHAR(15),
	Type:          VARCHAR(15),
	E_id           VARCHAR(15),
	PRIMARY KEY (E_id)
);

CREATE TABLE Noticeboard(
	News:	          VARCHAR(1000),
	Upcoming_events:  VARCHAR(1000),
	Date              DATE,
	PRIMARY KEY(Date),
	FOREIGN KEY (E_id) REFERENCES Employee(E_id)
);

CREATE TABLE Stuff_schedule(
	Shedule:  VARCHAR(1000),
	Date      DATE,
	PRIMARY KEY(Date),
	FOREIGN KEY (E_id) REFERENCES Employee(E_id)
);

CREATE TABLE Hospital_equipment(
	HE_id	VARCHAR(15),
	PRIMARY KEY (HE_id)
);

CREATE TABLE Medical_history(
	Ilness 			 VARCHAR(30),
	Duration		 VARCHAR(50),
	Attending_doctor VARCHAR(30),
	P_id 			 VARCHAR(15),
	PRIMARY KEY (HE_id)
);



-- here we go
-- CREATE TABLE Patient{
-- 	P_ID : INT
-- }