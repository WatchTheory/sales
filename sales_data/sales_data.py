import csv
from faker import Faker                 # Import libraries 
from datetime import date, datetime     
import random

zip_code = ['19020-PA' , '070807-NJ', '02301-MA', '76039-TX', '55330-MN', '44256-OH', '08096-NJ', '60053-IL', '94806-CA', '27909-NC', '30083-GA', '77566-TX']      # Create a list of zip code 
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Seattle', 'Mimia']        # Create a list of cities

# Initialize the Faker object
fake = Faker()

start_date = date(2000, 1, 1)       # start date calender 
end_date = date(2026, 12, 31)       # end date 

# Function to generate fake data
def generate_fake_data(num_entries=10):
    data = []                               # create an list
    for _ in range(num_entries):                # create a for loop 
        entry = [                                 # Create a list and assign entry to it   
            fake.random_int(min=0, max=100),         # create random fake int
            fake.random_int(min=50, max=999),+
            fake.random_int(min=1, max=10),
            product := random.choice(zip_code),     # Create random choice of the zip codes
            city := random.choice(cities),          # Create the random choice for cities

            # fake.random_company_product(),
            # fake.city(),
            fake.date_between(start_date='-5y', end_date='today'),
            fake.random_int(min=0, max=10),
            fake.pyfloat(
                min_value=10.5,
                max_value=75.5,
                right_digits=2,
                positive=True)

        ]                                       # Closing the entry
        data.append(entry)                  # Adding entry to data
    return data                         # returning the data

# Number of fake entries you want to generate
num_entries = 1000

# Generate the fake data
sales_data = generate_fake_data(num_entries)

# Write the data to a CSV file
with open('fake_zip_codes_csvdata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order_id', 'product_id', 'store_id', 'product_name', 'city', 'date_of_sale', 'quantity', 'sales_amount'])
    writer.writerows(sales_data)

print(f"{num_entries} fake entries have been generated and written to fake_zipcode_csvdata.csv")






# import csv
# from faker import Faker
# from faker_commerce import Provider
# from datetime import date, datetime

# # Initialize the Faker object
# fake = Faker()
# fake.add_provider(Provider)

# # print(fake.ecommerce_name().split(' ')[-1])

# start_date = date(2000, 1, 1)
# end_date = date(2026, 12, 31)

# # Function to generate fake data
# def generate_fake_data(num_entries=10):
#     data = []
#     for _ in range(num_entries):
#         entry = [
#             fake.random_int(min=0, max=100),
#             fake.random_int(min=50, max=999),
#             fake.random_int(min=1, max=10),
#             fake.ecommerce_name().split(' ')[-1],
#             fake.city(),
#             fake.date_between(start_date=start_date, end_date=end_date),
#             fake.random_int(min=0, max=10),
#             fake.pyfloat(
#                 min_value=10.5,
#                 max_value=75.5,
#                 right_digits=2,
#                 positive=True)
            
#         ]
#         data.append(entry)
#     return data

# # Number of fake entries you want to generate
# num_entries = 5000

# # Generate the fake data
# sales_data = generate_fake_data(num_entries)

# # Write the data to a CSV file
# with open('salesfakecsvdata.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['order_id', 'product_id', 'store_id', 'product_name', 'city', 'date_of_sale', 'quantity', 'sales_amount'])
#     writer.writerows(sales_data)

# print(f"{num_entries} fake entries have been generated and written to salesfakecsvdata.csv")