import mysql.connector as sql
from texttable import Texttable
from datetime import datetime
from mysql.connector import Error
        
# Prepare the header and data for the table
roomFields=["ROOM_NO", "CATEGORY", "ALLOTED_TO","RENT", "DATE_IN", "DATE_OUT"]
roomDtype=['t', 't', 't', 'i', 't', 't'] # Set column data types
user_Fields=["NAME", "EMAIL", 'PHONE_NO', 'AGE', 'ROOM_NO', 'RENT', 'DATE_IN', 'DATE_OUT']
user_Dtypes=['t', 't', 't', 'i', 'i', 'i', 't', 't']
def view(subj, fields, dtype):
    con = sql.connect(host="localhost",  
                              user="root",       
                              passwd="root",     
                              database="hotel_management")
    try:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {subj}")
        result = cur.fetchall()
        
        if result:
            result.insert(0, fields)
            t = Texttable(0)
            t.set_cols_dtype(dtype)
            t.add_rows(result) # Add the result row
            print(t.draw()) # Print the formatted table
            return True
        else:
            print("NOTHING TO SEE HERE....")
            return False
    finally:
        con.close()  # Ensures the connection is closed no matter what

view('rooms', roomFields, roomDtype)
view('occupied', roomFields, roomDtype)
view('vacant', roomFields, roomDtype)
view('empview', user_Fields, user_Dtypes)

# Function to insert job application into the database
def job_application(con):
    cur = con.cursor()

    # Collecting job application details from user
    print("Please fill out your job application details:")

    name = input("Name: ")
    email = input("Email: ")
    passwd = input("Password: ")  
    phone_no = input("Phone Number: ")
    age = int(input("Age: "))
    designation = input("Designation Applied For: ")
    DOJ = datetime.now().date()  # Gives the date as YYYY-MM-DD

    # Insert data into the job_applications table
    query = 'insert into applications(name, email, passwd, phone_no, age, designation, DOJ) values(%s, %s, %s, %s, %s, %s, %s)'
    
    values = (name, email, passwd, phone_no, age, designation, DOJ)

    try:
        cur.execute(query, values)
        con.commit()
        print("Job application submitted successfully!")
    except Error as e:
        print("Error inserting data into MySQL table:", e)
        con.rollback()

# Main function to drive the application
def main():
    con = sql.connect(host="localhost",  
                      user="root",       
                      passwd="root",
                      database="hotel_management")
    try:    
        if con:
            # Menu to select actions
            while True:
                print("\nWelcome to Hotel Management Job Portal")
                print("1. Apply for a job")
                print("2. Exit")

                choice = input("Enter your choice: ")
                
                if choice == '1':
                    job_application(con)
                elif choice == '2':
                    print("Exiting the application.")
                    break
                else:
                    print("Invalid choice!!")
    finally:
            con.close()
main()