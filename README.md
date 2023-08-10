# Phone Number Management System

This project is a simple Python program that allows you to manage phone number records using a MySQL database. You can perform actions such as adding, modifying, deleting, and displaying records.

## Prerequisites

Before you run the program, make sure you have the following:

- Python 3 installed on your system.
- MySQL server running on your localhost.
- Required MySQL connector library installed (`mysql-connector-python`).

You can install the connector library using the following command:
```bash
pip install mysql-connector-python


# Usage
1.Open the phone_number_management.py file in a code editor or IDE.

2.Modify the MySQL connection parameters:
    Update the host, user, password, and database values in the con=mycon.connect(...) line according to your MySQL configuration.

3.Run the script
    python phone_number_management.py

4.Follow the on-screen instructions to perform various actions on the phone number records.

# Features
1.Add Records: Add a new phone number record with details such as serial number, phone number, firstname, lastname, address, and email ID.

2.Modify Records: Modify phone number records. You can choose to modify phone numbers, first names, last names, addresses, or email IDs.

3.Delete Records: Delete a phone number record based on the firstname.

4.Display Records: Display all phone number records.

5.Display a Particular Record: Display the record of a specific person based on their firstname.

