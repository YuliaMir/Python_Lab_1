'''Составьте в произвольной форме список полей в таблице Pupil,
предполагая, что она будет использоваться в системе учета и
планирования курса «Разработчик на Питоне»'''


CREATE TABLE Pupil (
    Pupil_ID UInt32,
    First_Name String,
    Last_Name String,
    Date_of_Birth Date,
    Gender String,
    Address String,
    Parent_Guardian_Name String,
    Contact_Number String,
    Email_Address String,
    Course_Name String,
    Course_Start_Date Date,
    Course_End_Date Date,
    Course_Duration UInt16,
    Course_Fee Decimal(10, 2),
    Payment_Status String
) ENGINE = MergeTree()
ORDER BY Pupil_ID;
