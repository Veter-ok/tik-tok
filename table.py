from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Страна", "Площадь", "Население"]
table.add_row(["Россия", 17125191, 146171015])
table.add_row(["Канада", 9984670, 38478150])
table.add_row(["Китай", 9598962, 1449670556])
table.add_row(["США", 9525067, 333449281])
table.add_row(["Бразилия", 8515767, 209429060])
print(table)
