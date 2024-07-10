import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Number of customers to generate
num_bookings = 150

car_brands = [
    "Perodua", "Proton", "Honda", "Toyota", "Nissan",
    "Mazda", "BMW", "Mercedes-Benz", "Volkswagen", "Ford"
]

def generate_license_plate():
    letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    numbers = ''.join(random.choices('0123456789', k=3))
    return f"{letters} {numbers}"

# Generate start_date and end_date
# def generate_date():
#     start_date = fake.date_between(start_date='30d', end_date='today')
#     end_date = fake.date_between(start_date='-30d', end_date='today')

#     if start_date > end_date:
#         start_date, end_date = end_date, start_date
#     return (start_date, end_date)

# print(type(generate_date()[1]))


# Function to generate customer data
def generate_customers(num_bookings):
    bookings = []
    for _ in range(num_bookings):
        custname = fake.name()
        custphone = fake.random_int(min=60100000000, max=60199999999)
        brand = random.choice(car_brands)
        plate_number = generate_license_plate()
        seats = random.choice([4, 5, 7, 9])
        rental_rate = round(random.uniform(50, 200), 2)
        drivername = fake.name()
        driverphone = fake.random_int(min=60100000000, max=60199999999)

        start_date =  start_date = fake.date_between(start_date='-30d', end_date='today')
        end_date = start_date + timedelta(days=random.randint(1, 14))

        rental_fee = rental_rate * (end_date - start_date).days

        booking = {
            "Customer": custname,
            "Customer Phone Number": custphone,
            "Brand": brand,
            "Plate Number": plate_number,
            "Seats": seats,
            "Rental Rate": rental_rate,
            "Driver": drivername,
            "Driver Phone Number": driverphone,
            "Start Date": start_date,
            "End Date": end_date,
            "Rental Fee (RM)": rental_fee
        }

        bookings.append(booking)

    return bookings

# Generate customer data
bookings = generate_customers(num_bookings)



# Save customer data to a text file with header
# header = f"\n{'ID':40}{'Hotel Name':>20}{'Rate/Night':>20}{'Net Commission':>20}"
header = f"\n{'Customer':25} | {'Phone Number':>21} | {'Brand':>15} | {'Plate Number':>12} | {'Seats':>5} | {'Rental Rate':>12} | {'Driver':>25} | {'Driver Phone Number':>20} | {'Start Date'} | {'End Date'} | {'Rental Fee (RM)':>15}\n"
divider = f"{'=' * 190}\n"

filename = 'booking.txt'
with open(filename, 'w') as file:
    file.write(header)
    file.write(divider)
    
    for booking in bookings:
        file.write(f"{booking['Customer']:25} | {booking['Customer Phone Number']:>21} | {booking['Brand']:>15} | {booking['Plate Number']:>12} | {booking['Seats']:>5} | {booking['Rental Rate']:>12.2f} | {booking['Driver']:>25} | {booking['Driver Phone Number']:>20} | {booking['Start Date']} | {booking['End Date']} | {booking['Rental Fee (RM)']:>15.2f}\n")

print(f"Customer data has been saved to {filename} with the header.")