from os.path import exists
from tabulate import tabulate
from datetime import datetime
from prettytable import PrettyTable

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if(value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    
    return value
#---------------------------------------------------------------------------------------- read from booking.txt
def get_booking_by_id(booking_id, input_file_path):
    with open(input_file_path, 'r') as file:
        # Skip the header line
        headers = file.readline().strip()
        booking_headers = "BookingID|Customer|StartDay|EndDay"
        
        # Read the lines and find the matching booking
        for line in file:
            columns = line.strip().split('|')
            if columns[0] == booking_id:
                booking_info = [columns[0], columns[2], columns[4], columns[5]]
                return booking_headers, booking_info
        else:
            print(f"BookingID {booking_id} not found.")
            return booking_headers, None    
#---------------------------------------------------------------------------------------- read from service.txt
def get_service_by_id(service_id, input_file_path):
    with open(input_file_path, 'r') as file:
        # Skip the header line
        headers = file.readline().strip()
        service_headers = "ServiceID|ServiceName|Price|CommissionPerDay(%)"
        
        # Read the lines and find the matching service
        for line in file:
            columns = line.strip().split('|')
            if columns[0] == service_id:
                service_info = [columns[0], columns[1], columns[2], columns[3]]
                return service_headers, service_info
        else:
            print(f"ServiceID {service_id} not found.")
            return service_headers, None
#---------------------------------------------------------------------------------------- calculate duration
def calculate_duration(start_day, end_day):
    start_date = datetime.strptime(start_day, '%d/%m/%Y')
    end_date = datetime.strptime(end_day, '%d/%m/%Y')
    duration = (end_date - start_date).days
    return duration
#---------------------------------------------------------------------------------------- write information into bookservice.txt
def combine_booking_service(booking_id, service_id):
    # Check if BookingID already exists in bookservices.txt 
    with open('bookservices.txt', 'r') as check_file:
        for line in check_file:
            if line.startswith(booking_id):
                print(f"BookingID {booking_id} already exists in bookservices.txt. Process cancelled.")
                return
    
    # Get booking and service data
    booking_headers, booking_info = get_booking_by_id(booking_id, 'booking.txt')
    service_headers, service_info = get_service_by_id(service_id, 'services.txt')
    
    if not booking_info or not service_info:
        print("Unable to find the specified BookingID or ServiceID.")
        return
    
    # Call calculate duration
    duration = calculate_duration(booking_info[2], booking_info[3])
    
    # Calculate total commission
    price_per_day = float(service_info[2])
    commission_percent = float(service_info[3])
    total_price = price_per_day * duration
    total_commission = total_price * commission_percent
    
    # Combine headers
    combined_headers = f"BookingID|Customer|ServiceID|ServiceName|PricePerDay(RM)|Duration|TotalPrice(RM)|CommissionPercent(%)|TotalCommission(RM)"
    
    # Combine data
    combined_info = f"{booking_info[0]}|{booking_info[1]}|{service_info[0]}|{service_info[1]}|{price_per_day:.2f}|{duration}|{total_price:.2f}|{service_info[3]}|{total_commission:.2f}"
    
    with open('bookservices.txt', 'a') as output_file:
        # If the file is empty, write the headers
        if output_file.tell() == 0:
            output_file.write(combined_headers + '\n')
        
        # Write the combined information
        output_file.write(combined_info + '\n')
    
    print("Data have been successfully added into bookservices.txt!")
#---------------------------------------------------------------------------------------- print information in bookservices.txt to terminal


########################################## Choice 1 - BOOK SERVICES FOR CUSTOMERS #######################################
def print_combined_output(file_path):
    with open(file_path, 'r') as file:
        # Read the header and strip newline character
        headers = file.readline().strip().split('|')
        
        # Initialize a list to hold rows of data
        rows = []
        
        # Read each line and add it as a row of data
        for line in file:
            data = line.strip().split('|')
            rows.append(data)
        
        # Print the table using tabulate
        print(tabulate(rows, headers=headers, tablefmt='pretty'))
#---------------------------------------------------------------------------------------- print booking
def print_booking_details(file_path):
    # Initialize a PrettyTable object
    table = PrettyTable()

    # Define the columns
    table.field_names = ["BookingID", "Customer", "StartDay", "EndDay"]

    # Read the file and add rows to the table
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip the header
        fields = line.strip().split('|')
        booking_id = fields[0]
        customer = fields[2]
        start_day = fields[4]
        end_day = fields[5]
        table.add_row([booking_id, customer, start_day, end_day])

    # Print the formatted table
    print(table)
#---------------------------------------------------------------------------------------- print services
def print_service_details(file_path):
    # Initialize a PrettyTable object
    table = PrettyTable()

    # Define the columns
    table.field_names = ["ServiceID", "ServiceName", "PricePerDay"]

    # Read the file and add rows to the table
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip the header
        fields = line.strip().split('|')
        service_id = fields[0]
        service_name = fields[1]
        price_per_day = fields[2]
        table.add_row([service_id, service_name, price_per_day])

    # Print the formatted table
    print(table)
#---------------------------------------------------------------------------------------- to book a service 
def book_service(booking_id, booking_file_path='booking.txt'):
    if not booking_id:
        return "Invalid booking_id or service_id."
    
    # Read the booking file and find the corresponding booking
    with open(booking_file_path, 'r') as file:
        lines = file.readlines()

    # Find the booking with the given booking_id
    booking_found = False
    for line in lines[1:]:  # Skip the header
        fields = line.strip().split('|')
        if fields[0] == booking_id:
            booking_found = True
            end_day = fields[5]
            end_day_date = datetime.strptime(end_day, '%d/%m/%Y')
            current_date = datetime.now()

            # Check if the end date is in the past
            if end_day_date < current_date:
                return f"Booking ID: {booking_id} cannot proceed as the end date {end_day} has already passed."
            break

    if not booking_found:
        return f"Booking ID: {booking_id} not found."
    
    # Allow user to enter the service_id
    print_service_details('services.txt')
    service_id = input("Enter Service ID: ")
    if not service_id:
        return "Invalid service_id."

    print(f"Booking ID: {booking_id} has been successfully booked for Service ID: {service_id}.")
    
    return "Booking successful."


############################################### Choice 2 - MANAGE SERVICES ##############################################
#---------------------------------------------------------------------------------------- print service 
def print_services(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Print headers
    headers = lines[0].strip().split('|')
    print(f"{headers[0]:<10} | {headers[1]:<20} | {headers[2]:<10} | {headers[3]:<20} | {headers[4]:<15}")
    print('-' * 85)
    
    # Print each service
    for line in lines[1:]:
        service = line.strip().split('|')
        print(f"{service[0]:<10} | {service[1]:<20} | {service[2]:<10} | {service[3]:<20} | {service[4]:<15}")
#---------------------------------------------------------------------------------------- add service 
def add_service():
    service_id = input("Enter new Service ID (H - Hotel & T - Tour Guide Agency): ")
    service_name = input("Enter new Service Name: ")
    price_per_day = input("Enter Price per Day for the Service: ")
    commission_percent = input("Enter Commision Percentage(%) for the Service: ")
    agent_name = input("Enter Agent Name for the Service: ")
    
    with open('services.txt', 'a') as file:
        file.write(f"{service_id}|{service_name}|{price_per_day}|{commission_percent}|{agent_name}\n")
    
    print(f"Service {service_name} added successfully.")
#---------------------------------------------------------------------------------------- edit service 
def edit_service():
    service_id = input("Enter the Service ID to edit: ")
    found = False
    services = []

    try:
        with open('services.txt', 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if parts[0] == service_id:
                    found = True
                    current_service_name = parts[1]
                    current_price_per_day = parts[2]
                    current_commission_percent = parts[3]
                    current_agent_name = parts[4]
                    
                    print(f"Current Service Name: {current_service_name}")
                    print(f"Current Price per Day: {current_price_per_day}")
                    print(f"Current Commission Percentage: {current_commission_percent}")
                    print(f"Current Agent Name: {current_agent_name}")
                    
                    new_service_name = input("Enter new Service Name (or press Enter to keep current): ")
                    new_price_per_day = input("Enter new Price per Day (or press Enter to keep current): ")
                    new_commission_percent = input("Enter new Commission Percentage (or press Enter to keep current): ")
                    new_agent_name = input("Enter new Agent Name (or press Enter to keep current): ")
                    
                    new_service_name = new_service_name if new_service_name else current_service_name
                    new_price_per_day = new_price_per_day if new_price_per_day else current_price_per_day
                    new_commission_percent = new_commission_percent if new_commission_percent else current_commission_percent
                    new_agent_name = new_agent_name if new_agent_name else current_agent_name
                    
                    services.append(f"{service_id}|{new_service_name}|{new_price_per_day}|{new_commission_percent}|{new_agent_name}\n")
                else:
                    services.append(line)
        
        if not found:
            print(f"Service ID {service_id} not found.")
        else:
            with open('services.txt', 'w') as file:
                file.writelines(services)
            print(f"Service ID {service_id} updated successfully.")
    
    except FileNotFoundError:
        print("The file 'services.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
#---------------------------------------------------------------------------------------- delete service 
def delete_service():
    service_id = input("Enter the Service ID to delete: ")
    found = False
    services = []

    try:
        with open('services.txt', 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                
                if parts[0] == service_id:
                    found = True
                    print(f"Service ID: {parts[0]}")
                    print(f"Service Name: {parts[1]}")
                    print(f"Price per Day: {parts[2]}")
                    print(f"Commission Percentage: {parts[3]}")
                    print(f"Agent Name: {parts[4]}")
                    confirm = input("Are you sure you want to delete this service? (yes/no): ").lower()
                    if confirm == 'yes':
                        print(f"Deleting Service: {parts[1]}")
                        print(f"Service ID {service_id} deleted successfully.")
                    else:
                        print("Service deletion cancelled.")
                        services.append(line)
                else:
                    services.append(line)

        if not found:
            print(f"Service ID {service_id} not found.")
        else:
            with open('services.txt', 'w') as file:
                file.writelines(services)
    
    except FileNotFoundError:
        print("The file 'services.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
#================================================  SERVICES MENU ================================================
def ManageServices():
    print_services('services.txt')
    choice = -1
    while choice != 0:
        print()
        print("*************************************")
        print(":     0 - Return to Main Menu        :")
        print(":     1 - Add Service                :")
        print(":     2 - Edit Service               :")
        print(":     3 - Delete Service             :")
        print(":     4 - Available Service          :")
        print("*************************************")
        print()
        
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be an integer")
        
        if choice == 0:
            print("\nReturning to Main Menu ...\n")
        elif choice == 1:
            add_service()
        elif choice == 2:
            edit_service()
        elif choice == 3:
            delete_service()
        elif choice == 4:
            print_services('services.txt')
        else:
            print("Invalid choice. Please try again.")


############################################ Choice 3 - REPORT ON THE COMMISSION ######################################
def read_bookings():
    bookings = []
    file_path = 'bookservices.txt'
    with open(file_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            data = line.strip().split('|')
            booking = dict(zip(headers, data))
            bookings.append(booking)
    return bookings
# ---------------------------------------------------------------------------------- Total Commission Received
def calculate_total_commission(bookings):
    total_commission = sum(float(booking['TotalCommission(RM)']) for booking in bookings)
    return total_commission
#----------------------------------------------------------------------------------- Top 3 highest commission
def find_top_commissions(bookings, top_n=3):
    sorted_bookings = sorted(bookings, key=lambda booking: float(booking['TotalCommission(RM)']), reverse=True)
    return sorted_bookings[:top_n]
def print_top_commissions(top_commissions):
    table = PrettyTable()
    table.field_names = ["Customer Name", "Service Name", "Total Commission (RM)"]
    table.align["Customer Name"] = "l"
    table.align["Service Name"] = "l"
    table.align["Total Commission (RM)"] = "r"

    for booking in top_commissions:
        table.add_row([booking['Customer'], booking['ServiceName'], f"{booking['TotalCommission(RM)']}"])

    print("\nTop 3 Highest Commission Bookings:")
    print(table)
#----------------------------------------------------------------------------------- ServiceName and it's total commission
def calculate_service_commissions(bookings):
    service_commissions = {}
    for booking in bookings:
        service_name = booking['ServiceName']
        commission = float(booking['TotalCommission(RM)'])
        if service_name in service_commissions:
            service_commissions[service_name] += commission
        else:
            service_commissions[service_name] = commission
    return service_commissions
#----------------------------------------------------------------------------------- Print and sort commission from services
def print_service_commissions(service_commissions):
    
    # Sort service_commissions dictionary by Total Commission (RM) in descending order
    sorted_commissions = sorted(service_commissions.items(), key=lambda x: x[1], reverse=True)

    table = PrettyTable()
    table.field_names = ["Service Name", "Total Commission (RM)"]
    table.align["Service Name"] = "l"
    table.align["Total Commission (RM)"] = "r"

    for service_name, total_commission in service_commissions.items():
        table.add_row([service_name, f"{total_commission:.2f}"])

    print("\nTotal Commission Received by Each Service:")
    print(table)
#================================================= REPORT MENU ==================================================
def ReportMenu(bookings):
    choice = -1
    
    while choice != 0:
        print()
        print("******************************************")
        print(":     0 - Return to Main Menu             :")
        print(":     1 - Total Commission Received       :")
        print(":     2 - Top 3 Highest Commission        :")
        print(":     3 - List of Service and Commission  :")
        print("******************************************")
        print()
        
        choice = keyboardInput(int, "Choice [0, 1, 2, 3]: ", "Choice must be an integer")
        
        if choice == 0:
            print("\nReturning to Main Menu ...\n")
        elif choice == 1:
            total_commission = calculate_total_commission(bookings)
            print("+-------------------------------+---------------+")
            print(f"|   Total Commission Received   |   RM {total_commission:.2f}   |")
            print("+-------------------------------+---------------+")
        elif choice == 2:
            top_commissions = find_top_commissions(bookings)
            print_top_commissions(top_commissions)
        elif choice == 3:
            service_commissions = calculate_service_commissions(bookings)
            print_service_commissions(service_commissions)
        else:
            print("Invalid choice. Please try again.")
#--------------------------------------------------------------------------------------------------------------------------------
def BookedServices(file_path):
    table = PrettyTable()

    # Define the columns
    table.field_names = ["BookingID","CustomerName","ServiceID", "ServiceName", "PricePerDay"]

    # Read the file and add rows to the table
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip the header
        fields = line.strip().split('|')
        booking_id = fields[0]
        customer = fields[1]
        service_id = fields[2]
        service_name = fields[3]
        total_price = fields[6]
        table.add_row([booking_id, customer, service_id, service_name, total_price])

    # Print the formatted table
    print(table)


################################################### MAIN MENU ####################################################
def MainMenu():
    #bold = "\033[1m"  # ANSI escape sequence for bold text
    #reset = "\033[0m"  # ANSI escape sequence to reset text attributes
    
    print("\n\033[31m-------------<< Welcome To Hotel and Tour Booking System >>------------\033[0m\n")

    choice = -1
    while choice != 0:
        print("******************************")
        print("          \033[1m\033[46m MAIN MENU \033[0m           ")
        print(":     0 - Exit                :")
        print(":     1 - Book a service      :")
        print(":     2 - Manage Services     :")
        print(":     3 - Current Booked Services     :")
        print(":     4 - Print Report        :")
        print("******************************")
        
        choice = keyboardInput(int, "Choice [0, 1, 2, 3]: ", "Choice must be integer")
        if (choice == 0):
            print("Thank You for using our system")
        elif (choice == 1):
            print_booking_details('booking.txt')
            booking_id = input("Choose a booking ID to add Hotel or Tour booking: ")
            result = book_service(booking_id)
            print(result)
            #combine_booking_service(booking_id, service_id)
        elif (choice == 2):
            ManageServices()
        elif (choice == 3):
            BookedServices('bookservices.txt')
        elif (choice == 4):
            bookings = read_bookings()
            ReportMenu(bookings)
            
MainMenu()