# This program gets employee data from the user and saves it as records in the employee.txt file.

def write_emp_infor():
    # get the number of employee data from user input
    num_emps = int(input('How many employees records to create? '))
    # open file employee.txt for writing
    with open('employee.txt', 'w') as emp_file:
        emp_file.write('Name\t')
        emp_file.write('ID Number\t')
        emp_file.write('Department\t')
        emp_file.write('\n')
        for emp in range(1, num_emps+1):
            # get data of number emp
            print(f'Enter information for employee {emp}:')
            name = input('Name: ')
            id_num = input('ID number: ')
            dept = input('Department: ')

            # write the employee's information as a record to the file
            emp_file.write(name + '\t')
            emp_file.write(id_num + '\t')
            emp_file.write(dept + '\t')
            emp_file.write('\n')

            # print separate line between users
            print('------------------------------------')
        print(f'All employee information are saved!')

def read_emp_info():
    # open file
    with open('employee.txt', 'r') as emp_file:
        # read line by line and print information
        for ind, line in enumerate(emp_file.readlines()):
            if ind == 0:
                continue
            print(f'*********** Information of employee {ind + 1}: *************')
            name = line.split("\t")[0]
            print(f'Name: {name}')
            id_num = line.split("\t")[1]
            print(f'ID Number: {id_num}')
            dept = line.split("\t")[2]
            print(f'Department: {dept}')
            # print separate line between users
            print('------------------------------------')


# call the main function
# main()
if __name__ == '__main__':
    read_emp_info()