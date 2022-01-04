--Data Representation - Project
--John Paul Lee - G00387906
--Lecturer - Andrew Beatty
--Code is adapted from code generated through lectures through the semester

-- Command to create the database 'datarepresentation'
CREATE DATABASE datarepresentation;

--Select the database 'datarepresentation' for use
USE datarepresentation;


------------------Electronics-----------------------

--Create table 'electronic' | Electronics Database
CREATE TABLE electronic (
    electronic_id int(11) NOT NULL AUTO_INCREMENT,
    electronic_make VARCHAR (250),
    electronic_model VARCHAR (250),
    electronic_price INT (8),
    PRIMARY KEY (`electronic_id`)
    );

-- Check if the table 'electronic' was created as expected
DESC electronic;


--Populate the table 'electronic'
INSERT INTO electronic VALUES
('1', 'Apple', 'iPhone 11',  '2000'),
('2', 'LG', 'UP77',  '800'),
('3', 'Sony', 'Bravia', '1750'),
('4', 'Samsung', 'Galaxy S21',  '2250'),
('5', 'Dyson', 'V8',  '750');
