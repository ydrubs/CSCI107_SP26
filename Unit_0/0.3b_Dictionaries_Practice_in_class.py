"""
Given the list called 'sales_data' where each element is a tuple representing:
    - Item
    - category
    - quantity sold
    - cost per unit

    1) Create a dictionary called 'revenue' the prints the revenue for each product sold

    2) Use the revenue dictionary to print a tuple of the product with the highest revenue, in the form:

            (product with highest revenue, revenue amount)
"""

sales_data = [
    ("Laptop",        "electronics",  5,   900),
    ("Headphones",    "electronics", 15,    60),
    ("Desk Chair",    "furniture",    7,   120),
    ("Notebook",      "stationery",  40,     3),
    ("Pen Pack",      "stationery",  30,     5),
    ("Monitor",       "electronics",  4,   200),
    ("Couch",         "furniture",    2,  1100),
    ("Lamp",          "furniture",    6,    45)
]


revenue = {}

for i in range(len(sales_data)):
    item = sales_data[i][0]
    sales = sales_data[i][2] * sales_data[i][3]
    revenue[item] = sales
print(revenue)


max_rev = 0
result = 0
for key,value in revenue.items():
    if value > max_rev:
        result = (key, value)
        max_rev = value
print(result)

colors = {
    "Alex": "red",
    "Bella": "blue",
    "Chris": "red",
    "Dana": "green",
    "Eli": "blue",
}

