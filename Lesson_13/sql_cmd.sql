-- CREATE TABLE Students (ST_Id INT Primary Key, Name VARCHAR(50), DoB DateTime, Address VARCHAR (100), Phone_Number VARCHAR (15), Email VARCHAR (50));
-- CREATE TABLE Subjects (Sub_Id INT Primary Key, Name VARCHAR(50));
-- CREATE TABLE Scores (ST_Id INT, Sub_Id INT, Prog_Score Float, End_Score FLoat, Final_Score Float);
-- CREATE TABLE Subject (Id INT, Name VARCHAR(50), DoB DateTime, Address VARCHAR (100), Phone_Number VARCHAR (15), Email VARCHAR (50));
-- ALTER TABLE Employee ADD Salary INT;
-- INSERT INTO Students (ST_Id, Name, DoB, Address, Phone_Number, Email) VALUES (1, 'Arvind Singh', '1999-09-12', 'Ha Noi', '0987687556', 'hta@gmail.com');
-- INSERT INTO Employee (Id, Name, Address, Salary) VALUES (2, 'Pham Thi Nga',	 'Bac Ninh', 1000);
-- UPDATE Employee SET Address = 'Hà Nội', Salary = 100 WHERE Id =1;
SELECT * FROM Students;