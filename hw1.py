import csv

# print("asdf")

with open('nips-word-stream.csv', 'rb') as f:
	reader = csv.reader(f)
	my_data = []
	for row in reader:
		my_data.append(row[0])

m = 12419


#1 part a
table = [False]*m

for word in my_data:
	x = int(word)
	table[x-1] = True

F0 = sum(table)

print(F0)

#1 part b

a = 33212
b = 74895
M = 100003

my_min = M;

for word in my_data:
	x = int(word)
	h = (a*x + b) % M
	if h < my_min:
		# print("h is")
		# print(h)
		# print("when x is")
		# print(x)
		my_min = h

#F0_hat = M/my_min

#print(F0_hat)

#1 part c
table = [0]*m

for word in my_data:
	x = int(word)
	table[x-1] = table[x-1]+1

# F1 = sum(table)
# print(F1)
# print(len(my_data))

i = 0
for entry in table:
	table[i] = entry*entry
	i = i+1

F2 = sum(table)
print(F2)

