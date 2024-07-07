import os


#===== FOR HOTEL =====
def create_file(filename):
    if not os.path.exists(filename):
        try:
            with open(filename, "x") as file:
                file.write("hotel | hotel_id | Price | Total\n")
        except IOError as e:
            print(f"Error creating file: {e}")
    else:
        print(f"File '{filename}' already exists.")

def add_hotel(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "a") as file:
                hotel = input("Enter the hotel name: ")
                hotel_id = input("Enter the hotel id: ")
                price = input("Enter the price/night (RM): ")
                total_commission = 0.1 * float(price)
                file.write(f"\n{hotel} | {hotel_id} | {price} | {total_commission}")
        except IOError as e:
            print(f"Error adding hotel: {e}")
    else:
        print(f"File '{filename}' does not exist.")

def read_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                for line in file.readlines():
                    line = line.strip()
                    if line and "|" in line:
                        hotel, hotel_id, price, total_commission = line.split("|")
                        print(f"{hotel.strip():40}{hotel_id.strip():>20}{price.strip():>20}{total_commission.strip():>20}")
        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename}' does not exist.")

import os

def edit_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r+") as file:
                lines = file.readlines()
                file.seek(0)

                found = False
                for line_index, line in enumerate(lines):
                    line = line.strip()
                    if "|" in line:
                        hotel, hotel_id, price, total = line.split("|")
                        print(f"{hotel.strip():40}{hotel_id.strip():>20}{price.strip():>20}{total.strip():>20}")

                search_hotel = input("Enter the hotel to edit or delete: ").strip().lower()
                edited = False
                for line_index, line in enumerate(lines):
                    if "|" in line:
                        parts = line.strip().split("|")
                        hotel = parts[0].strip()
                        if hotel.lower() == search_hotel:
                            print("\n1. Edit hotel")
                            print("2. Edit hotel_id")
                            print("3. Edit price")
                            print("4. Delete hotel")
                            print("5. Exit")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                new_hotel = input("Enter the new hotel: ").strip()
                                parts[0] = new_hotel
                                edited = True
                                print(f"hotel '{hotel}' has been updated to '{new_hotel}'.")
                            elif choice == "2":
                                new_hotel_id = input("Enter the new hotel_id: ").strip()
                                if new_hotel_id.isdigit():
                                    parts[1] = new_hotel_id
                                    edited = True
                                    print(f"hotel_id '{hotel_id}' has been updated to '{new_hotel_id}'.")
                                else:
                                    print("Invalid input. hotel_id must be a number.")
                            elif choice == "3":
                                new_price = input("Enter the new price: ").strip()
                                try:
                                    float(new_price)
                                    parts[2] = new_price
                                    edited = True
                                    print(f"Price '{price}' has been updated to '{new_price}'.")
                                except ValueError:
                                    print("Invalid input. Price must be a number.")
                            elif choice == "4":
                                confirmation = input(f"Are you sure you want to delete '{hotel}'? (y/n): ").strip().lower()
                                if confirmation == "y":
                                    del lines[line_index]
                                    edited = True
                                    print(f"hotel '{hotel}' has been deleted.")
                                    break  # Exit after deletion
                                else:
                                    print(f"Deletion of '{hotel}' canceled.")
                            elif choice == "5":
                                print("Exiting...")
                                break
                            else:
                                print("Invalid choice. Try again.")
                                print("")
                            if edited:
                                lines[line_index] = " | ".join(parts) + "\n"
                            break

                if not edited:
                    print(f"hotel '{search_hotel}' not found.")

                file.seek(0)
                file.writelines(lines)
                file.truncate()
        except IOError as e:
            print(f"Error editing file: {e}")
    else:
        print(f"File '{filename}' does not exist.")

def main():
    while True:
        print("1. Create new file")
        print("2. Choose existing file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename to create: ")
            create_file(filename)
            while True:
                print("\nOperations:")
                print("1. Add hotel")
                print("2. Read file")
                print("3. Edit file")
                print("4. Back to main menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    add_hotel(filename)
                elif sub_choice == "2":
                    read_file(filename)
                elif sub_choice == "3":
                    edit_file(filename)
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Try again.")
        
        elif choice == "2":
            filename = input("Enter the existing filename: ")
            while True:
                if os.path.exists(filename):
                    print("\nOperations:")
                    print("1. Add hotel")
                    print("2. Read file")
                    print("3. Edit file")
                    print("4. Back to main menu")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        add_hotel(filename)
                    elif sub_choice == "2":
                        read_file(filename)
                    elif sub_choice == "3":
                        edit_file(filename)
                    elif sub_choice == "4":
                        break
                    else:
                        print("Invalid choice. Try again.")
                else:
                    print(f"File '{filename}' does not exist.")
                    break
        
        elif choice == "3":
            print("\nExiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()