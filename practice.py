table_names = ["Deacon", "Izail", "Samuel"]
print(table_names)

table_names.pop(0)
print(table_names)

table_names.append("Ben")
print(table_names)

# Use a loop to print through "{name} is at my table"

for name in table_names:
    print(f"{name} is at my table")