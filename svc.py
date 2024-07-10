import os
from datetime import datetime


#===== FOR HOTEL =====


def add_hotel(filename_hotel):
    if os.path.exists(filename_hotel):
        try:
            with open(filename_hotel, "a") as file:
                hotel_id = "H" + datetime.now().strftime("%Y%m%d%H%M%S%f") #generate time-based-id
                hotel = input("Enter the hotel name: ")
                hotel_price = input("Enter the hotel_price/night (RM): ")
                Net_commission = 0.1 * float(hotel_price)
                file.write(f"\n{hotel_id} | {hotel} | {hotel_price} | {Net_commission}")
        except IOError as e:
            print(f"Error adding hotel: {e}")
    else:
        print(f"File '{filename_hotel}' does not exist.")

def read_file_hotel(filename_hotel):
    if os.path.exists(filename_hotel):
        try:
            with open(filename_hotel, "r") as file:
                header = f"\n{'ID':40}{'Hotel Name':>20}"
                print(header)
                print("=" * 100)
                for line in file.readlines():
                    line = line.strip()
                    if line and "|" in line:
                        hotel_id, hotel, hotel_price, Net_commission = line.split("|")
                        print(f"{hotel_id.strip():40}{hotel.strip():>20}")
        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename_hotel}' does not exist.")


def edit_file_hotel(filename_hotel):
    if os.path.exists(filename_hotel):
        try:
            with open(filename_hotel, "r+") as file:
                lines = file.readlines()
                file.seek(0)
                header = f"\n{'ID':40}{'Hotel Name':>20}{'Rate/Night':>20}{'Net Commission':>20}"
                print(header)
                print("=" * 100)

                found = False
                for line_index, line in enumerate(lines):
                    line = line.strip()
                    if "|" in line:
                        #header print once
                        hotel_id, hotel , hotel_price, Net = line.split("|")
                        print(f"{hotel_id.strip():40}{hotel.strip():>20}{hotel_price.strip():>20}{Net.strip():>20}")

                search_hotel = input("\nEnter the ID to edit or delete: ").strip().lower()
                edited = False
                for line_index, line in enumerate(lines):
                    if "|" in line:
                        parts = line.strip().split("|")
                        hotel = parts[0].strip()
                        if hotel.lower() == search_hotel:
                            print("\n1. Edit hotel")
                            print("2. Edit hotel_id")
                            print("3. Edit hotel_price")
                            print("4. Delete hotel")
                            print("5. Exit\n")
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
                                new_hotel_price = input("Enter the new hotel_price: ").strip()
                                try:
                                    float(new_hotel_price)
                                    parts[2] = new_hotel_price
                                    edited = True
                                    print(f"hotel_Price '{hotel_price}' has been updated to '{new_hotel_price}'.")
                                except ValueError:
                                    print("Invalid input. hotel_Price must be a number.")
                            elif choice == "4":
                                confirmation = input(f"\nAre you sure you want to delete '{hotel}'? (y/n): ").strip().lower()
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
        print(f"File '{filename_hotel}' does not exist.")

#--------FOR TOUR -----------------


def add_tour(filename_tour):
    if os.path.exists(filename_tour):
        try:
            with open(filename_tour, "a") as file:
                tour_id = "T" + datetime.now().strftime("%Y%m%d%H%M%S%f")
                tour = input("Enter the tour agency: ")
                tour_price = input("Enter the tour rate/day (RM): ")
                Net_commission = 0.1 * float(tour_price)
                file.write(f"\n{tour_id} | {tour} | {tour_price} | {Net_commission}")
        except IOError as e:
            print(f"Error adding tour: {e}")
    else:
        print(f"File '{filename_tour}' does not exist.")

def read_file_tour(filename_tour):
    if os.path.exists(filename_tour):
        try:
            with open(filename_tour, "r") as file:
                # Print the header once
                header = f"\n{'ID':40}{'Tour Agency':>20}{'Rate/Day':>20}{'Net Commission':>20}" 
                print(header)
                print("=" * 100)
                for line in file.readlines():
                    line = line.strip()
                    if line and "|" in line:
                        tour_id, tour, tour_price, Net_commission = line.split("|")
                        print(f"{tour_id.strip():40}{tour.strip():>20}{tour_price.strip():>20}{Net_commission.strip():>20}")
                        
        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename_tour}' does not exist.")


def edit_file_tour(filename_tour):
    if os.path.exists(filename_tour):
        try:
            with open(filename_tour, "r+") as file:
                lines = file.readlines()
                file.seek(0)

                found = False
                  # Print the header once
                header = f"\n{'ID':40}{'Tour Guide':>20}{'Rate/Day':>20}{'Net Commission':>20}" 
                print(header)
                print("=" * 100)
                for line_index, line in enumerate(lines):
                    line = line.strip()
                    if "|" in line:
                       
                        tour_id, tour, tour_price, Net = line.split("|")
                        print(f"{tour_id.strip():40}{tour.strip():>20}{tour_price.strip():>20}{Net.strip():>20}")

                search_tour = input("Enter the ID to edit or delete: ").strip().lower()
                edited = False
                for line_index, line in enumerate(lines):
                    if "|" in line:
                        parts = line.strip().split("|")
                        tour = parts[0].strip()
                        if tour.lower() == search_tour:
                            print("\n1. Edit tour")
                            print("2. Edit tour_id")
                            print("3. Edit tour_price")
                            print("4. Delete tour")
                            print("5. Exit")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                new_tour = input("Enter the new tour: ").strip()
                                parts[0] = new_tour
                                edited = True
                                print(f"tour '{tour}' has been updated to '{new_tour}'.")
                            elif choice == "2":
                                new_tour_id = input("Enter the new tour_id: ").strip()
                                if new_tour_id.isdigit():
                                    parts[1] = new_tour_id
                                    edited = True
                                    print(f"tour_id '{tour_id}' has been updated to '{new_tour_id}'.")
                                else:
                                    print("Invalid input. tour_id must be a number.")
                            elif choice == "3":
                                new_tour_price = input("Enter the new tour_price: ").strip()
                                try:
                                    float(new_tour_price)
                                    parts[2] = new_tour_price
                                    edited = True
                                    print(f"tour_Price '{tour_price}' has been updated to '{new_tour_price}'.")
                                except ValueError:
                                    print("Invalid input. tour_Price must be a number.")
                            elif choice == "4":
                                confirmation = input(f"Are you sure you want to delete '{tour}'? (y/n): ").strip().lower()
                                if confirmation == "y":
                                    del lines[line_index]
                                    edited = True
                                    print(f"tour '{tour}' has been deleted.")
                                    break  # Exit after deletion
                                else:
                                    print(f"Deletion of '{tour}' canceled.")
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
                    print(f"tour '{search_tour}' not found.")

                file.seek(0)
                file.writelines(lines)
                file.truncate()
        except IOError as e:
            print(f"Error editing file: {e}")
    else:
        print(f"File '{filename_tour}' does not exist.")

def main():
    while True:
        print("\nMain Menu:")
        print("🏨   1. Manage Hotel            3. *Exit")
        print("🤠   2. Manage Tour-Guide")
        choice = input("\nEnter your choice:\n\U0001F449  ")

        if choice == "1":
            filename_hotel = "hotel.txt"
            while True:
                if os.path.exists(filename_hotel):
                    print("\nOperations:")
                    print("1. Add hotel             3. Edit file ")
                    print("2. Read all hotels       4. Back to main menu")
    
                    sub_choice = input("\nEnter your choice:\n\U0001F449  ")

                    if sub_choice == "1":
                        add_hotel(filename_hotel)
                    elif sub_choice == "2":
                        read_file_hotel(filename_hotel)
                    elif sub_choice == "3":
                        edit_file_hotel(filename_hotel)
                    elif sub_choice == "4":
                        break
                    else:
                        print("Invalid choice. Try again.")
                else:
                    print(f"File '{filename_hotel}' does not exist.")
                    break

        elif choice == "2":
            filename_tour = "tour.txt"
            while True:

                if os.path.exists(filename_tour):
                    print("\nOperations:")
                    print("1. Add tour agency            3. Edit file")
                    print("2. Read all tour agencies     4. Back to main menu")
                    sub_choice = input("\nEnter your choice:\n\U0001F449  ")
                    

                    if sub_choice == "1":
                        add_tour(filename_tour)
                    elif sub_choice == "2":
                        read_file_tour(filename_tour)
                    elif sub_choice == "3":
                        edit_file_tour(filename_tour)
                    elif sub_choice == "4":
                        break
                    else:
                        print("Invalid choice. Try again.")
                else:
                    print(f"File '{filename_tour}' does not exist.")
                    break
 
        
        
            
        
        elif choice == "3":
            print("\nExiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()