# SmartRegistrationSystem-usingPython
The Smart Registration System is a Python-based application designed to securely register students by validating their details.
The system ensures correct input formats and improves data reliability during the registration process.

**Features**
Accepts Student ID, Email ID, Password, and Referral Code
Validates user inputs
Prevents invalid registrations
Beginner-friendly Python logic

**Technologies Used**
Python 3
Built-in Python string validation methods

**inputs:**
Student Id , Email Id . Password, Referral code

***Validation Rules Implemented***
**1.Student Id:**
*Condition are:*
Must start with "CSE"
4th character must be - 
Last 3 characters must be digits 
*How i checked:* 
Using slicing for 1st 4 characters and using isdigit() method for last 3 characters 
**2.email id:**
*Conditions are:*
Must contain @ and . 
@ must not be first or last character 
Email must end with .edu 
*How i checked:* 
Using count() method for “@” and “.” and indexing for “@” and slicing for last 4 characters  
**3.password:**
*Conditions are:*
Length ≥ 8 
First character must be uppercase letter 
Must contain at least one digit 
*How i checked:* 
Using len() function and using title() method to check first is capital or not by equating title() method to 
original string . 
**4.referral code:**
*Conditions are:*
Must start with "REF"
Next 2 characters must be digits 
Last character must be @ 
*How i checked:* 
Using slicing for the first 3 characters and for 2 next characters isdigit() and indexing for last character.

