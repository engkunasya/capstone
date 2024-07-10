import os
from datetime import datetime


#===== FOR HOTEL =====



def read_file_hotel(filename_booking_hotel):
    if os.path.exists(filename_booking_hotel):
        try:
            with open(filename_booking_hotel, "r") as file:
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
        print(f"File '{filename_booking_hotel}' does not exist.")


    
def add_booking_hotel(filename_booking_hotel):
    if os.path.exists(filename_booking_hotel):
        try:
            with open("hotels.txt", "r+") as file:
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
                        print(f"{hotel_id.strip():40}")

                search_hotel = input("\nEnter the ID to edit or delete: ").strip().upper()
                edited = False
                for line_index, line in enumerate(lines):
                    if "|" in line:
                        parts = line.strip().split("|")
                        hotel_id = parts[0].strip()
                        if hotel_id.upper() == search_hotel:
                            try:
                                with open(filename_booking_hotel, "a") as file:

                                    file.write(f"\ncust{hotel_id} | {hotel} | {hotel_price} | {Net_commission}")


                            except IOError as e:
                                print(f"Error adding hotel: {e}")
                            # print("\n1. Edit hotel")
                            # print("2. Edit hotel_id")
                            # print("3. Edit hotel_price")
                            # print("4. Delete hotel")
                            # print("5. Exit\n")
                            # choice = input("Enter your choice: ")
                            # if choice == "1":
                            #     new_hotel = input("Enter the new hotel: ").strip()
                            #     parts[0] = new_hotel
                            #     edited = True
                            #     print(f"hotel '{hotel}' has been updated to '{new_hotel}'.")
                            # elif choice == "2":
                            #     new_hotel_id = input("Enter the new hotel_id: ").strip()
                            #     if new_hotel_id.isdigit():
                            #         parts[1] = new_hotel_id
                            #         edited = True
                            #         print(f"hotel_id '{hotel_id}' has been updated to '{new_hotel_id}'.")
                            #     else:
                            #         print("Invalid input. hotel_id must be a number.")
                            # elif choice == "3":
                            #     new_hotel_price = input("Enter the new hotel_price: ").strip()
                            #     try:
                            #         float(new_hotel_price)
                            #         parts[2] = new_hotel_price
                            #         edited = True
                            #         print(f"hotel_Price '{hotel_price}' has been updated to '{new_hotel_price}'.")
                            #     except ValueError:
                            #         print("Invalid input. hotel_Price must be a number.")
                            # elif choice == "4":
                            #     confirmation = input(f"\nAre you sure you want to delete '{hotel}'? (y/n): ").strip().lower()
                            #     if confirmation == "y":
                            #         del lines[line_index]
                            #         edited = True
                            #         print(f"hotel '{hotel}' has been deleted.")
                            #         break  # Exit after deletion
                            #     else:
                            #         print(f"Deletion of '{hotel}' canceled.")
                            # elif choice == "5":
                            #     print("Exiting...")
                            #     break
                            # else:
                            #     print("Invalid choice. Try again.")
                            #     print("")
                            # if edited:
                            #     lines[line_index] = " | ".join(parts) + "\n"
                            # break

                if not edited:
                    print(f"hotel '{search_hotel}' not found.")

                file.seek(0)
                file.writelines(lines)
                file.truncate()
        except IOError as e:
            print(f"Error editing file: {e}")
    else:
        print(f"File '{filename_booking_hotel}' does not exist.")

        

    
    
        



#--------FOR TOUR -----------------




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



def main():
    while True:
        print("\nMain Menu:")
        print("🏨   1. Manage Hotel            3. *Exit")
        print("🤠   2. Manage Tour-Guide")
        choice = input("\nEnter your choice:\n\U0001F449  ")

        if choice == "1":
            filename_booking_hotel = "hotels.txt"
            while True:
                if os.path.exists(filename_booking_hotel):
                    read_file_hotel(filename_booking_hotel)

                    sub_choice = input("\nInsert hotel's id:\n\U0001F449  ")

                    

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