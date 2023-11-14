from prettytable import PrettyTable

table = PrettyTable()
table.header = False


n = int(input())
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        row.append(i * j)
    table.add_row(row)
print(table)