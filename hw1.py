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

#1 part d
with open('f2-hash.csv', 'rb') as f:
	reader = csv.reader(f)
	z_hash = []
	for row in reader:
		z_hash.append(int(row[0]))

Z = 0

for word in my_data:
	x = int(word)
	Z = Z + z_hash[x-1]

F2_hat = Z*Z
print(F2_hat)

#1 part e
from collections import Counter
data = Counter(my_data)
mode_cell = data.most_common(1)  # Returns the highest occurring item
mode = int(mode_cell[0][0])
print(mode)

#1 part f
counter = 0
for word in my_data:
	x = int(word)
	if counter == 0:
		mode_hat = x
		counter = counter + 1
	else:
		if x == mode_hat:
			counter = counter + 1
		else:
			counter = counter - 1

print(mode_hat)