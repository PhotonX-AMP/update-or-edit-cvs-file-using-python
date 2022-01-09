# Importing CSV and creation of a list
import csv

# Creaton of an empty list
data_list = []


# Opening the CSV file to read the values and populate an empty list
with open('employeedata.csv', 'r') as file:
    database = csv.reader(file)
    for row in database:
        data_list.append(row) 


# Describing the program
print("\nThis program emables you to view and edit the domain name of the email addresses in the CSV file: ''employeedata.csv'' \n")


# Displaying the database
selector = input("Would you like to see the database? (Y/N): ").lower()

if(selector == "y"):
    for i in range(len(data_list)):
        print(data_list[i])

# Entering the new domain
domain = input("\nEnter the new domain: ").lower()

# Modifying the list
for i in range(len(data_list)-1):
    data_list[i+1][4] = domain
    data_list[i+1][5] = data_list[i+1][3] + data_list[i+1][4]

# Displaying the modified database 
selector = input("Would you like to see the  new database file? (Y/N): ").lower()

if(selector == "y"):
    for i in range(len(data_list)):
        print(data_list[i])

# Saving the CSV file
Change_file = input("Would you like to save changes to the file? (Y/N): ").lower()
 
if (Change_file == "y"):
    with open('new_employeedata.csv', 'w', newline='') as file:
        New_data_list = csv.writer(file)
        for i in range(len(data_list)):
            New_data_list.writerow(data_list[i])
            print("Operation sucessfull!")