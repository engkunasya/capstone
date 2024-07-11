import os


def add_customer(filename_booking):
    if os.path.exists(filename_booking):
        try:
            with open(filename_booking, "r") as file:
                lines = file.readlines()
                
                # header = f"\n{'ID':40}{'Hotel Name':>20}{'Rate/Night':>20}{'Net Commission':>20}"
                # print(header)
                # print("=" * 100)

                for line in lines:
                    line = line.strip()
                    if "|" in line:
                        cust_id, cust, phone, car_brand, plate, seats, rental_rate, driver, driver_no, start_date, ticket_date, today, duration, status, rental_fee = line.split("|")
                    # print("second debug",duration)
                     

                search_cust = input("\nEnter the ID of customer: ").strip().upper()
                selected_cust = None

                for line in lines:
                    if "|" in line:
                        parts = line.strip().split("|")
                        cust_id = parts[0].strip()
                        status = parts[13].strip
                        
                        cust_duration = parts[12].strip()
                        cust_status = parts[13].strip()
                        if cust_id.upper() == search_cust:
                            selected_cust = line
                            break

                if selected_cust:
                   print(f"Customer is valid with name {selected_cust.strip().split("|")[1]}")
                   cust_index = selected_cust.strip().split("|")[0]
                   duration = int(selected_cust.strip().split("|")[12])
                   

                   return cust_index, duration
                else:
                    print(f"Customer with ID '{search_cust}' not found or expired.")

        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename_booking}' does not exist.")









def read_file_hotel(filename_hotel):
    if os.path.exists(filename_hotel):
        try:
            with open(filename_hotel, "r") as file:
                header = f"\n{'ID':40}{'Hotel Name':>20}{'Rate/Night':>20}{'Net Commission':>20}"
                print(header)
                print("=" * 100)
                for line in file.readlines():
                    line = line.strip()
                    if line and "|" in line:
                        hotel_id, hotel, hotel_price, Net_commission = line.split("|")
                        print(f"{hotel_id.strip():40}{hotel.strip():>20}{hotel_price.strip():>20}{Net_commission.strip():>20}")
        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename_hotel}' does not exist.")

def add_booking_hotel(filename_hotel, filename_chooseaddon, chosed_cust, duration):
    if os.path.exists(filename_hotel):
        try:
            with open(filename_hotel, "r") as file:
                lines = file.readlines()
                
                header = f"\n{'ID':40}{'Hotel Name':>20}{'Rate/Night':>20}{'Net Commission':>20}"
                print(header)
                print("=" * 100)

                for line in lines:
                    line = line.strip()
                    if "|" in line:
                        hotel_id, hotel, hotel_price, net_commission = line.split("|")
                        print(f"{hotel_id.strip():40}{hotel.strip():>20}{hotel_price.strip():>20}{net_commission.strip():>20}")

                
                search_hotel = input("\nEnter the ID to select: ").strip().upper()
                selected_hotel = None
                # for line in lines:
                #     if "|" in line:
                #         parts = line.strip().split("|")
                #         cust_id = parts[0].strip()
                #         status = parts[13].strip
                        
                #         cust_duration = parts[12].strip()
                #         cust_status = parts[13].strip()

                for line in lines:
                    if "|" in line:
                        parts = line.strip().split("|")
                        hotel_id = parts[0].strip()
                        

                        if hotel_id.upper() == search_hotel:
                            selected_hotel = line.strip().split("|")
                           
                            print("selectedhotel:",selected_hotel)

                            com_per_night = selected_hotel[3]
                            print("com final debug", com_per_night)
                            break

                if selected_hotel:
                    with open(filename_chooseaddon, "a") as choose_file:
                        print("com_per_night",com_per_night)
                        print("duration", duration)
                        
                        tol_commission = int(duration) * float(com_per_night)
                        print("total comm", tol_commission)
                        tol_commission_str = str(tol_commission) 
                        duration_str = str(duration)
                        print("total commission",tol_commission)
                        book_hoter_str = f"{chosed_cust}  | {selected_hotel} | {com_per_night} | {duration_str} | {tol_commission}\n"
                        choose_file.write( book_hoter_str)
                    print(f"Hotel with ID '{search_hotel}' added to {chosed_cust}.")
                else:
                    print(f"Hotel with ID '{search_hotel}' not found.")

        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename_hotel}' does not exist.")


def read_file_tour(filename_tour):
    if os.path.exists(filename_tour):
        try:
            with open(filename_tour, "r") as file:
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


def add_booking_tour(filename_tour, filename_chooseaddon, chosed_cust):
    if os.path.exists(filename_tour):
        try:
            with open(filename_tour, "r") as file:
                lines = file.readlines()
                
                header = f"\n{'ID':40}{'Tour Name':>20}{'Rate/Day':>20}{'Commission':>20}"
                print(header)
                print("=" * 100)

                for line in lines:
                    line = line.strip()
                    if "|" in line:
                        tour_id, tour, tour_price, net_commission = line.split("|")
                        print(f"{tour_id.strip():40}{tour.strip():>20}{tour_price.strip():>20}{net_commission.strip():>20}")

                search_tour = input("\nEnter the ID to select: ").strip().upper()
                selected_tour = None

                for line in lines:
                    if "|" in line:
                        parts = line.strip().split("|")
                        tour_id = parts[0].strip()
                        if tour_id.upper() == search_tour:
                            selected_tour = line
                            break

                if selected_tour:
                    with open(filename_chooseaddon, "a") as choose_file:
                        choose_file.write(chosed_cust + selected_tour + "\n")
                    print(f"Tour with ID '{search_tour}' added to Customer: {chosed_cust}.")
                else:
                    print(f"Tour with ID '{search_tour}' not found.")

        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File '{filename_tour}' does not exist.")
# Example usage
# add_booking_hotel("hotel.txt", "choosehotel.txt")


def main():
    filename_booking = "booking.txt"
    chosed_cust, duration = add_customer(filename_booking)
    
    while chosed_cust:
            print("\nMain Menu:")
            print("🏨   1. Addon Hotel")
            print("🤠   2. Addon Tour-Guide")
            print("🚪   3. Exit")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                filename_hotel = "hotels.txt"
                filename_chooseaddon = "bookservices.txt"
                # read_file_hotel(filename_hotel)

                add_booking_hotel(filename_hotel,filename_chooseaddon, chosed_cust, duration)
            
            elif choice == "2":
                filename_tour = "tours.txt"
                filename_chooseaddon = "bookservices.txt"

                add_booking_tour(filename_tour,filename_chooseaddon, chosed_cust, duration)

            elif choice == "3":
                print("\nExiting...")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
