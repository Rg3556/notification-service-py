delivery = {
"sender": "Charlie",
"recipient": " Anika ",
"price": 16.99,
"status": "In Transit",
"stops": ["New York", "Denver", "San Francisco"]
}



#full_name = delivery["sender"]+ delivery["recipient"]
#print(full_name)

print(delivery['sender']+delivery['recipient'])


#sender = delivery["sender"]
#recipient = delivery["recipient"]
# print(f"A delievery from {sender} to {recipient}")


print("A delievery from " + delivery["sender"] + " to" + delivery["recipient"])

print(len(delivery["stops"]))

print(delivery["stops"][0])

print(delivery["stops"][-1])

for s in delivery["stops"]:
    print(s)


# 11
def calculate_area(length, width):
    return length * width
area = calculate_area (length=4, width=2)
print(area)

stops = delivery["stops"]
print(type(stops))

