import random

def generate_hotel_id(index):
    return f"H{index:03d}"

def generate_hotel_name(n):
    hotel_names = [
        "Sunset Inn", "Oceanview Hotel", "Mountain Retreat", "Urban Stay", 
        "Coastal Resort", "Riverside Hotel", "Grand Palace", "Royal Plaza", 
        "The Elegant Lodge", "City Center Hotel", "Luxury Suites", "The Grand Hotel"
    ]
    return hotel_names[n]

def generate_rate_per_night():
    return round(random.uniform(100, 700), 2)

def generate_commission(rate):
    return round(rate * 0.10, 2)

hotels = []

# Starting index after H005
start_index = 0

for i in range(start_index, start_index + 12):
    hotel_id = generate_hotel_id(i)
    hotel_name = generate_hotel_name(i)
    rate_per_night = generate_rate_per_night()
    commission = generate_commission(rate_per_night)
    
    hotels.append(f"{hotel_id:5} | {hotel_name:>25} | {rate_per_night:>10} | {commission:>10}\n")

with open('hotels.txt', 'w') as file:
    header = f"{"ID":5} | {"Hotel Name":>25} | {"Rate/Night":>10} | {"Commission":>10}\n"
    border = f"{"=" * len(header)}\n"
    file.write(header)
    file.write(border)
    for hotel in hotels:
        file.write(hotel)

print("Hotel list saved to hotels.txt")
