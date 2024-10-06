import csv

customers = open("customers-100.csv", "r")
customer = customers.readline()
while customer != "":
    customer_attr = customer.split(',')
    if customer_attr[0].isnumeric():
        print(int(customer_attr[0]) + 100)
    customer = customers.readline()
customers.close()

customers_2 = open("customers-100.csv", "r")
all_customer_data = customers_2.readlines()
for customer in all_customer_data:
    if customer.split(',')[0].isnumeric():
        print(int(customer.split(',')[0]) + 100)

search_id = int(input('enter id: '))
customers_csv = csv.reader(open("customers-100.csv"))
for line in customers_csv:
    if line[0].isnumeric():
        if int(line[0]) == search_id:
            print("found it!")
