import random

def generate_tour_id(index):
    return f"T{index:03d}"

def generate_tour_name(n):
    tour_names = [
        "WALK WALK", "EXPEDIA", "HAPPY TOUR", "JOM HIKE", 
        "GO GO GO", "ANDALUSIA", "PIGEON GUIDE", "JALAN SAT", 
        "EXPRESS KING", "HIDDEN GERM", "SECRET WORLD", "LALALAND"
    ]
    return tour_names[n]

def generate_rate_per_day():
    return round(random.uniform(100, 700), 2)

def generate_commission(rate):
    return round(rate * 0.10, 2)

tours = []

# Starting index after H005
start_index = 0

for i in range(start_index, start_index + 12):
    tour_id = generate_tour_id(i)
    tour_name = generate_tour_name(i)
    rate_per_day = generate_rate_per_day()
    commission = generate_commission(rate_per_day)
    
    tours.append(f"{tour_id:5} | {tour_name:>25} | {rate_per_day:>10} | {commission:>10}\n")

with open('tours.txt', 'w') as file:
    header = f"{"ID":5} | {"tour Name":>25} | {"Rate/Day":>10} | {"Commission":>10}\n"
    border = f"{"=" * len(header)}\n"
    file.write(header)
    file.write(border)
    for tour in tours:
        file.write(tour)

print("tour list saved to tours.txt")