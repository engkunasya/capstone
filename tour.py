# #===== FOR TOUR =====
# import os

# # class Service:
# #     def __init__(self, name, id, price, total_commission):
# #         self.name = name
# #         self.id = id
# #         self.price = price
# #         self.total_commission = total_commission

# # class Hotel(Service):
# #     def __init__(self, name, id, price, total_commission):
# #         super().__init__(name, id, price, total_commission)
# #         pass
# #     def __str__(self):
# #         return 
    





# def create_file_tour(filename_tour):
#     if not os.path.exists(filename_tour):
#         try:
#             with open(filename_tour, "x") as file:
#                 file.write("tour | tour_id | tour_Price | Total Commission\n")
#         except IOError as e:
#             print(f"Error creating file: {e}")
#     else:
#         print(f"File '{filename_tour}' already exists.")

# def add_tour(filename_tour):
#     if os.path.exists(filename_tour):
#         try:
#             with open(filename_tour, "a") as file:
#                 tour = input("Enter the tour name: ")
#                 tour_id = input("Enter the tour id: ")
#                 tour_price = input("Enter the tour price/night (RM): ")
#                 total_commission = 0.1 * float(tour_price)
#                 file.write(f"\n{tour} | {tour_id} | {tour_price} | {total_commission}")
#         except IOError as e:
#             print(f"Error adding tour: {e}")
#     else:
#         print(f"File '{filename_tour}' does not exist.")

# def read_file_tour(filename_tour):
#     if os.path.exists(filename_tour):
#         try:
#             with open(filename_tour, "r") as file:
#                 for line in file.readlines():
#                     line = line.strip()
#                     if line and "|" in line:
#                         tour, tour_id, tour_price, total_commission = line.split("|")
#                         print(f"{tour.strip():40}{tour_id.strip():>20}{tour_price.strip():>20}{total_commission.strip():>20}")
#         except IOError as e:
#             print(f"Error reading file: {e}")
#     else:
#         print(f"File '{filename_tour}' does not exist.")


# def edit_file_tour(filename_tour):
#     if os.path.exists(filename_tour):
#         try:
#             with open(filename_tour, "r+") as file:
#                 lines = file.readlines()
#                 file.seek(0)

#                 found = False
#                 for line_index, line in enumerate(lines):
#                     line = line.strip()
#                     if "|" in line:
#                         tour, tour_id, tour_price, total = line.split("|")
#                         print(f"{tour.strip():40}{tour_id.strip():>20}{tour_price.strip():>20}{total.strip():>20}")

#                 search_tour = input("Enter the tour to edit or delete: ").strip().lower()
#                 edited = False
#                 for line_index, line in enumerate(lines):
#                     if "|" in line:
#                         parts = line.strip().split("|")
#                         tour = parts[0].strip()
#                         if tour.lower() == search_tour:
#                             print("\n1. Edit tour")
#                             print("2. Edit tour_id")
#                             print("3. Edit tour_price")
#                             print("4. Delete tour")
#                             print("5. Exit")
#                             choice = input("Enter your choice: ")
#                             if choice == "1":
#                                 new_tour = input("Enter the new tour: ").strip()
#                                 parts[0] = new_tour
#                                 edited = True
#                                 print(f"tour '{tour}' has been updated to '{new_tour}'.")
#                             elif choice == "2":
#                                 new_tour_id = input("Enter the new tour_id: ").strip()
#                                 if new_tour_id.isdigit():
#                                     parts[1] = new_tour_id
#                                     edited = True
#                                     print(f"tour_id '{tour_id}' has been updated to '{new_tour_id}'.")
#                                 else:
#                                     print("Invalid input. tour_id must be a number.")
#                             elif choice == "3":
#                                 new_tour_price = input("Enter the new tour_price: ").strip()
#                                 try:
#                                     float(new_tour_price)
#                                     parts[2] = new_tour_price
#                                     edited = True
#                                     print(f"tour_Price '{tour_price}' has been updated to '{new_tour_price}'.")
#                                 except ValueError:
#                                     print("Invalid input. tour_Price must be a number.")
#                             elif choice == "4":
#                                 confirmation = input(f"Are you sure you want to delete '{tour}'? (y/n): ").strip().lower()
#                                 if confirmation == "y":
#                                     del lines[line_index]
#                                     edited = True
#                                     print(f"tour '{tour}' has been deleted.")
#                                     break  # Exit after deletion
#                                 else:
#                                     print(f"Deletion of '{tour}' canceled.")
#                             elif choice == "5":
#                                 print("Exiting...")
#                                 break
#                             else:
#                                 print("Invalid choice. Try again.")
#                                 print("")
#                             if edited:
#                                 lines[line_index] = " | ".join(parts) + "\n"
#                             break

#                 if not edited:
#                     print(f"tour '{search_tour}' not found.")

#                 file.seek(0)
#                 file.writelines(lines)
#                 file.truncate()
#         except IOError as e:
#             print(f"Error editing file: {e}")
#     else:
#         print(f"File '{filename_tour}' does not exist.")


# def main():
#     while True:
       
#         print("1. Choose existing hotel file")
#         print("2. Choose existing tour-service file")
#         print("3. Exit")
#         choice = input("Enter your choice: ")


#         e
            
#         elif choice == "3":
#             print("\nExiting...")
#             break
        
#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()   