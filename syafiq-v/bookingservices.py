

        # elif (choice == 1):
        #     printProduct(filename)
        # elif (choice == 2):
        #     addProduct(filename)
        # elif (choice == 3):
        #     editProduct(filename)
        # elif (choice == 4):
        #     deleteProduct(filename)

class BOOKSERVICE:
    def __init__(self, filename):
        self.filename = filename
        self.createfile(filename)  # Ensure file creation when initializing

    def keyboardInput(self, datatype, caption, errorMessage, defaultValue=None):
        value = None
        isInvalid = True
        while isInvalid:
            try:
                user_input = input(caption)
                if user_input.strip() == "" and defaultValue is not None:
                    value = defaultValue
                else:
                    value = datatype(user_input)
            except ValueError:
                print(errorMessage)
            else:
                isInvalid = False
        return value

    def createfile(self, filename):
        try:
            with open(filename, "xt") as file:
                file.write("BookingID | Hotel | Tour Agency | Commission\n")
        except FileExistsError:
            print("File already exists")

    def Titlename(self, filename):
        with open(filename, "wt") as file:
            file.write("BookingID | Hotel | Tour Agency | Commission")
        self.doMenu()

    def doMenu(self):
        choice = -1
        while choice != 0:
            print("-----------------------")
            print("|0  -  Exit           |")
            print("|1  -  List           |")
            print("|2  -  Add ID         |")
            print("|3  -  Add Hotel      |")
            print("|4  -  Add TourAgency |")
            print("|5  -  Delete         |")
            print("-----------------------")
            choice = self.keyboardInput(int, "Choice(0-5): ", "Choice must be Integer", defaultValue=0)
            if choice == 0:
                print("Exiting program.")
            elif choice == 1:
                self.printProduct(self.filename)
            else:
                print("Invalid choice. Please choose again.")

    def printProduct(self, filename):
        try:
            with open(filename, "rt") as filehandler:
                lines = filehandler.readlines()
            for index, line in enumerate(lines):
                if index == 0:
                    print(f"{'No':<5} {line.strip()}")
                    print("=" * 80)
                else:
                    ID, Hotel, TourAgency, TotalCommission = line.strip().split("|")
                    print(f"{index:<5} {ID.strip():<20} {Hotel.strip():>20} {TourAgency.strip():>20} {float(TotalCommission.strip()):>20.2f}")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Something went wrong when printing the products:", e)


# Usage example:
filename = "bookingservices.txt"
service = BOOKSERVICE(filename)
service.doMenu()


# book_service = BOOKSERVICE().createfile(filename)
# def Addaisyah(filename):
#     with open(filename, "r") as filehandler:
#         line = filehandler.readline()
#         with open()



