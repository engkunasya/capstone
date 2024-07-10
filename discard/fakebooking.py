# import random
# import faker

# # Initialize Faker
# fake = faker.Faker()

# # Number of customers to generate
# num_customers = 10

# # Function to generate customer data
# def generate_customers(num_customers):
#     customers = []
#     for _ in range(num_customers):
#         name = fake.name()
#         email = fake.email()
#         phone = fake.phone_number()
#         hotel_index = random.randint(0, 9)
#         chose_tour_guide = random.choice([True, False])
#         tour_guide_index = random.randint(0, 9) if chose_tour_guide else None
        
#         customer = {
#             "name": name,
#             "email": email,
#             "phone": phone,
#             "hotel_index": hotel_index,
#             "chose_tour_guide": chose_tour_guide,
#             "tour_guide_index": tour_guide_index
#         }
        
#         customers.append(customer)
    
#     return customers

# # Generate customers
# customers = generate_customers(num_customers)

# # Write to customer.txt file
# with open("customer.txt", "w") as file:
#     for customer in customers:
#         file.write(f"Name: {customer['name']}\n")
#         file.write(f"Email: {customer['email']}\n")
#         file.write(f"Phone: {customer['phone']}\n")
#         file.write(f"Hotel Index: {customer['hotel_index']}\n")
#         file.write(f"Chose Tour Guide: {customer['chose_tour_guide']}\n")
#         file.write(f"Tour Guide Index: {customer['tour_guide_index']}\n\n")

# print("Customer data has been written to customer.txt")
