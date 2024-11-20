from prettytable import PrettyTable

table = PrettyTable()

# methods
table.add_column("Pokemon",["Chespin", "Fennekin", "Froakie", "Linoone"])
table.add_column("Type", ["Grass", "Fire", "Water", "Normal"])

# attributes - first we can print the attribute to see the default, if any.
# Then we can change it, as per documentation
print(table.align)
print(table)

table.align = "l"
print(table.align)
print(table)