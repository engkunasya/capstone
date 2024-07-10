import random

def generate_hotel_id(index):
    return f"H{index:03d}"

def generate_hotel_name():
    hotel_names = [
        "Sunset Inn", "Oceanview Hotel", "Mountain Retreat", "Urban Stay", 
        "Coastal Resort", "Riverside Hotel", "Grand Palace", "Royal Plaza", 
        "The Elegant Lodge", "City Center Hotel", "Luxury Suites", "Paradise Resort",
        "Seaside Escape", "Highland Hotel", "Forest Lodge", "Harbor Hotel",
        "Skyline Inn", "Desert Oasis", "Historic Hotel", "Comfort Stay",
        "Green Valley Resort", "Beachfront Hotel", "Lakeside Inn", "The Heritage",
        "Premier Hotel", "Winter Wonderland", "Springtime Hotel", "Autumn Lodge",
        "Summer Breeze Hotel", "The Cosmopolitan", "Urban Oasis", "Majestic Resort",
        "Downtown Hotel", "Countryside Inn", "Metropolitan Hotel", "Royal Garden",
        "Peaceful Retreat", "Serene Hotel", "Charming Inn", "Boutique Hotel",
        "Modern Hotel", "Classic Inn", "Seaview Hotel", "Island Resort",
        "Hilltop Hotel", "Grove Hotel", "Parkside Inn", "Vineyard Resort",
        "Mystic Hotel", "The Grand Hotel"
    ]
    return random.choice(hotel_names)

def generate_rate_per_night():
    return round(random.uniform(100, 700), 2)

def generate_commission(rate):
    return round(rate * 0.10, 2)

hotels = []

# Starting index after H005
start_index = 6

for i in range(start_index, start_index + 50):
    hotel_id = generate_hotel_id(i)
    hotel_name = generate_hotel_name()
    rate_per_night = generate_rate_per_night()
    commission = generate_commission(rate_per_night)
    
    hotels.append(f"{hotel_id} | {hotel_name} | {rate_per_night} | {commission}")

with open('hotels.txt', 'w') as file:
    for hotel in hotels:
        file.write(hotel + '\n')

print("Hotel list saved to hotels.txt")
