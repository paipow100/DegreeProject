import os
# pandas module https://pandas.pydata.org/
import pandas as pd
import random

# https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
# allows to view all columns of the csv when printed out
pd.set_option('display.expand_frame_repr', False)
# usage when calling int_selection and no method needed
null = "null"
# changes based on the current method you are on, to re-print values for 'help'
current_method = []
# gets the path of the running script to find data.csv and stores in a variable
# https://note.nkmk.me/en/python-script-file-path/
data_csv_location = os.path.join(os.path.dirname(__file__), 'data.csv')


# region core
def print_line_break():
    # prints a simple line to screen
    print("---------------------------")


# prints the options key values in the method
# This is called in int_selection
def print_options(options):
    for key in options.keys():
        print(options[key])


def current_method_set(method):
    # Clears the array current_method
    current_method.clear()
    # adds to the array from the pass through 'method'
    current_method.append(method)
    # https://www.w3schools.com/python/python_arrays.asp


# core loop which allows re-usability on all the menu items
# takes in Options (dictionary) and method (method name without () )
def int_selection(options, method1, method2, method3, method4):
    # passes through the called 'options' to run the method
    print_options(options)
    # lets the user input a selection or a pre-defined option
    selection_input = input("Please select an option: ")
    # bool to check if it has printed, to prevent spam the method to the console
    has_printed = False
    # start of the while loop to check if the input isn't 0
    while selection_input != 0:
        # checks if input == 1 and if the method passed through is not null.
        # null is used as the variable above for ease of access instead of using the "" each time
        if selection_input == "1" and method1 != "null":
            # prints the line break method to show a line before moving to the selected method
            print_line_break()
            # goes to the method passed through when method is called
            method1()
            # breaks out of the loop
            break
        elif selection_input == "2" and method2 != "null":
            print_line_break()
            method2()
            break
        elif selection_input == "3" and method3 != "null":
            print_line_break()
            method3()
            break
        elif selection_input == "4" and method4 != "null":
            print_line_break()
            method4()
            break
        elif selection_input == "exit":
            exit_application()
        elif selection_input == "main menu":
            print_line_break()
            main_menu()
            break
        elif selection_input == "help":
            # checks if the bool has_printed is false
            if not has_printed:
                print_options(options)
                selection_input = input("Please select an option: ")
        # else is the default call if none of the other sections of the loop are met
        else:
            print("Invalid option, please try again")
            # re-asks user to input an option - Doesn't break out of loop to allow selection above
            selection_input = input("Please select an option: ")


def exit_application():
    exit_confirmation = {
        0: 'Are you sure?',
        1: '[1] Yes',
        2: '[2] No'
    }
    # returns to the current method (section) the user was on
    return_back = current_method[0]
    # calls in_selection and passing in the above dictionary
    # on press 1 'yes' it has passed through 'exit' which will close the application
    # on press 2 'no' it will return the user back to the place they were previously on
    # Any other press will return the default 'else' in the loop. The 'null' prevent it calling a method
    int_selection(exit_confirmation, exit, return_back, null, null)


# endregion

# region menu options
def start():
    start_text = {
        0: 'Welcome to the helpdesk',
        1: '---------------------------',
        2: 'Helpful commands that can be used anytime',
        3: 'type "help" to display options',
        4: 'type "main menu" to go back to the main menu',
        5: 'type "exit" to exit the application',
        6: '---------------------------',
        7: 'Select options displayed on the screen with numbers',
        8: 'ticket ID must start with a IRN',
        9: '---------------------------'
    }
    print_options(start_text)
    input("Press enter to continue")
    print_line_break()
    main_menu()


def main_menu():
    current_method_set(main_menu)
    main_menu_options = {
        0: 'What would you like to do?',
        1: '[1] Create a new ticket',
        2: '[2] View open tickets',
        3: '[3] Exit'
    }
    int_selection(main_menu_options, create_ticket_menu, ticket_menu, exit_application, null)


# region CSV options
def read_csv():
    # reads a specified CSV file
    read_csv.a = pd.read_csv(data_csv_location)
    # adds a title to the index name
    read_csv.a.index.name = 'Ticket'
    # updates the CSV file when called
    read_csv.a.update


def create_ticket_menu():
    current_method_set(create_ticket_menu)
    ticket_id = 'IRN' + str(random.randint(0, 99999))
    print("Please provide information for the ticket")
    title = input("Title: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email_address = input("Email Address: ")
    company = input("Company: ")
    service = 'Service Request'
    summary = input("Brief Summary of the problem: ")
    description = input("Description in detail of the problem: ")
    assignee = 'IT Team'
    ticket_status = 'New'
    data = {  # https://datascienceparichay.com/article/pandas-append-dataframe-to-existing-csv/
        'ID': ticket_id,
        'Title': [title],
        'First Name': [first_name],
        'Last Name': [last_name],
        'Email Address': [email_address],
        'Company': [company],
        'Service': [service],
        'Summary': [summary],
        'Description': [description],
        'Assignee': [assignee],
        'Ticket Status': [ticket_status]
    }

    # dataframe from dictionary
    df = pd.DataFrame(data)
    # saves the 'data' to the CSV on a new line
    df.to_csv('data.csv', mode='a', index=False, header=False)
    print_line_break()
    print("Ticket has been created, you will be notified of any changes")
    print("Your Ticket ID is: " + ticket_id)
    input("Press enter to go to the main menu")
    print_line_break()
    main_menu()


def ticket_menu():
    current_method_set(ticket_menu)
    view_ticket_options = {
        1: '[1] View all tickets',
        2: '[2] View ticket by ID',
        3: '[3] Search tickets by column and input value',
        4: '[4] Back'
    }
    int_selection(view_ticket_options, read_all_tickets, view_ticket_by_id, search_for_tickets, main_menu)


def read_all_tickets():
    current_method_set(read_all_tickets)
    read_ticket_options = {
        0: 'What would you like to do?',
        1: '[1] Edit a ticket',
        2: '[2] Back',
        3: '[3] Main Menu'
    }
    read_csv()
    print(read_csv.a)
    print_line_break()
    int_selection(read_ticket_options, edit_ticket, ticket_menu, main_menu, null)


def view_ticket_by_id():
    current_method_set(view_ticket_by_id)
    view_ticket_options = {
        0: 'What would you like to do?',
        1: '[1] Edit a ticket',
        2: '[2] Back',
        3: '[3] Main Menu'
    }
    read_csv()
    csv = read_csv.a
    tn_input = input('Please enter the Ticket Number: ')
    output_filtered_csv = csv[(csv['ID'] == tn_input)]
    print(output_filtered_csv)
    # https://www.youtube.com/watch?v=ClNP-lTzKgI&t=376s
    print_line_break()
    int_selection(view_ticket_options, edit_ticket, ticket_menu, main_menu, null)


def search_for_tickets():
    current_method_set(search_for_tickets)
    column_id = {
        'ID': 'ID',
        'Title': 'Title',
        'First Name': 'First Name',
        'Last Name': 'Last Name',
        'Email Address': 'Email Address',
        'Company': 'Company',
        'Service': 'Service',
        'Summary': 'Summary',
        'Description': 'Description',
        'Assignee': 'Assignee',
        'Ticket Status': 'Ticket Status'
    }
    view_ticket_options = {
        0: 'What would you like to do?',
        1: '[1] Edit a ticket',
        2: '[2] Back',
        3: '[3] Main Menu'
    }
    read_csv()
    csv = read_csv.a
    print_options(column_id)
    column_input = input('Enter the search column: ')
    while column_input != 0:
        if column_input in column_id.keys():
            value = input('Please enter the value you want to search:  ')
            output_filtered_csv = csv[(csv[column_input] == value)]
            print(output_filtered_csv)
            break
        elif column_input == "exit":
            exit_application()
        elif column_input == "main menu":
            print_line_break()
            main_menu()
            break
        else:
            print("Invalid option, please try again")
            column_input = input('Enter the search column: ')
    input("Press enter to go to the Ticket Menu")
    print_line_break()
    int_selection(view_ticket_options, edit_ticket, ticket_menu, main_menu, null)
    # https://www.askpython.com/python/dictionary/check-if-key-exists-in-a-python-dictionary


def edit_ticket():
    current_method_set(edit_ticket)
    edit_ticket_options = {
        1: '[1] Delete ticket',
        2: '[2] Amend ticket',
        3: '[3] Main Menu'
    }
    int_selection(edit_ticket_options, delete_ticket, amend_ticket, main_menu, null)


def delete_ticket():
    # TO DO! CHANGE IF'S TO WHILE LOOPS LIKE ABOVE
    current_method_set(delete_ticket)
    read_csv()
    csv = read_csv.a
    print("You have selected to delete a ticket")
    print("Type Cancel to return to the Ticket menu")
    print_line_break()
    delete = input("Enter a ticket number to delete: ")
    print_line_break()
    print("Are you sure you want to delete this Ticket?")
    print("You are unable to recover if you delete the Ticket")
    print("Typing No returns back to the Ticket menu")
    print_line_break()
    if delete.isdigit():
        confirmation = input("Are you sure? type Yes or No: ")
        int_delete = int(delete)
        if confirmation == "Yes":
            if int_delete in csv.index:
                csv.drop([int_delete], inplace=True)
                csv.to_csv("data.csv", index=False, encoding="utf-8")
                print("you have successfully deleted Ticket " + str(int_delete))
                input("Press Enter to return to the main menu")
                print_line_break()
                main_menu()
            else:
                print("This Ticket doesn't exist")
                input("Press enter to try again")
                print_line_break()
                delete_ticket()
        elif confirmation == "No":
            edit_ticket()
        else:
            print("Invalid Selection")
            input("Press Enter to go back to the Ticket menu")
            edit_ticket()
    elif delete == "Cancel":
        edit_ticket()
    else:
        print("Invalid selection, please try again")
        input("Press Enter to go back to the Ticket menu")


def amend_ticket():
    # TO DO! CHANGE IF'S TO WHILE LOOPS LIKE ABOVE
    current_method_set(amend_ticket)
    read_csv()
    csv = read_csv.a
    column_id = {
        'ID': 'ID',
        'Title': 'Title',
        'First Name': 'First Name',
        'Last Name': 'Last Name',
        'Email Address': 'Email Address',
        'Company': 'Company',
        'Service': 'Service',
        'Summary': 'Summary',
        'Description': 'Description',
        'Assignee': 'Assignee',
        'Ticket Status': 'Ticket Status'
    }
    print("You have selected to edit a ticket")
    print("Type Cancel to return to the Ticket menu")
    print_line_break()
    input_ticket = input("Enter Ticket number to edit: ")
    print_line_break()
    print("Are you sure you want to edit this Ticket?")
    print("You are unable to recover the data you edit in the Ticket")
    print("Typing No returns back to the Ticket menu")
    print_line_break()
    if input_ticket.isdigit():
        int_input_ticket = int(input_ticket)
        print_options(column_id)
        input_column_id = input("Enter a Column Name: ")
        if input_column_id in column_id.keys():
            print_line_break()
            input_new_value = input("Enter a new value: ")
            print_line_break()
            print("Are you sure you want to change the value: " + str(
                csv.loc[int_input_ticket, input_column_id]) + " to " + input_new_value + "?")
            confirmation = input("Are you sure? type Yes or No: ")
            print_line_break()
            if confirmation == "Yes":
                csv.loc[int_input_ticket, input_column_id] = input_new_value
                csv.to_csv("data.csv", index=False, encoding="utf-8")
                print("You have successfully updated the ticket")
                input("Press enter to return back to the Main menu")
                print_line_break()
                main_menu()
            elif confirmation == "No":
                edit_ticket()
            else:
                print("Invalid Selection")
                input("Press Enter to go back to the Ticket menu")
                edit_ticket()
        else:
            print("Invalid selection, please try again")
            input("Press Enter to go back to the Ticket menu")
            edit_ticket()
    elif input_ticket == "Cancel":
        edit_ticket()
    else:
        print("Invalid selection, please try again")
        input("Press Enter to go back to the Ticket menu")
        edit_ticket()


# endregion
# endregion

start()
