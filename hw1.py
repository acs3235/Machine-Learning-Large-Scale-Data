# coding=utf-8
from __future__ import division
import csv
import math

import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

import random

tls.set_credentials_file(username = 'acs3235', api_key = 'ry5w4i1zp0')


# with open('nips-word-stream.csv', 'rb') as f:
# 	reader = csv.reader(f)
# 	my_data = []
# 	for row in reader:
# 		my_data.append(row[0])

# m = 12419


# #1 part a
# table = [False]*m

# for word in my_data:
# 	x = int(word)
# 	table[x-1] = True

# F0 = sum(table)

# print(F0)

# #1 part b

# a = 33212
# b = 74895
# M = 100003

# my_min = M;

# for word in my_data:
# 	x = int(word)
# 	h = (a*x + b) % M
# 	if h < my_min:
# 		my_min = h

# if my_min == 0:
# 	F0_hat = 'infinity'
# else:
# 	F0_hat = M/my_min


# print(F0_hat)

# #1 part c
# table = [0]*m

# for word in my_data:
# 	x = int(word)
# 	table[x-1] = table[x-1]+1

# # F1 = sum(table)
# # print(F1)
# # print(len(my_data))

# i = 0
# for entry in table:
# 	table[i] = entry*entry
# 	i = i+1

# F2 = sum(table)
# print(F2)

# #1 part d
# with open('f2-hash.csv', 'rb') as f:
# 	reader = csv.reader(f)
# 	z_hash = []
# 	for row in reader:
# 		z_hash.append(int(row[0]))

# Z = 0

# for word in my_data:
# 	x = int(word)
# 	Z = Z + z_hash[x-1]

# F2_hat = Z*Z
# print(F2_hat)

# #1 part e
# from collections import Counter
# data = Counter(my_data)
# mode_cell = data.most_common(1)  # Returns the highest occurring item
# mode = int(mode_cell[0][0])
# print(mode)

# #1 part f
# counter = 0
# for word in my_data:
# 	x = int(word)
# 	if counter == 0:
# 		mode_hat = x
# 		counter = counter + 1
# 	else:
# 		if x == mode_hat:
# 			counter = counter + 1
# 		else:
# 			counter = counter - 1

# print(mode_hat)

#2 part a
a = 134598
b = 542234
M = 600011

my_min = M;

with open('pubmed−word−stream.csv','r') as input_file:
	for line in input_file:
		reader = csv.reader(line)
		my_data = []
		for row in reader:
			print(int(row[0]))
			my_data.append(int(row[0]))

		for x in my_data:
			h = (a*x + b) % M
			if h < my_min:
				my_min = h

if my_min == 0:
	F0_hat_2 = 'infinity'
else:
	F0_hat_2 = M/my_min

print(F0_hat_2)


#2 part b
k = 10

with open(’pubmed−word−stream.csv’,’r’) as input_file:
for line in input_file:
	reader = csv.reader(line)
	my_data = []
	for row in reader:
		my_data.append(int(row[0]))

	counts = [0] * k
	modes = [0] * k

for x in my_data:
	if x in modes:
		counts[modes.index(x)] = counts[modes.index(x)] + 1
	else:
		if 0 in counts:
			i = counts.index(0)
			counts[i] = 1
			modes[i] = x
		else:
			i = 0
			for count in counts:
				counts[i] = count - 1
				i = i + 1


# #Problem 3
# with open('nips-word-stream.csv', 'rb') as f:
# 	reader = csv.reader(f)
# 	my_data = []
# 	for row in reader:
# 		my_data.append(int(row[0]))

# M = 100003

# def guessF0(a,b,M,this_data):
# 	my_min = M;

# 	for x in this_data:
# 		h = (a*x + b) % M
# 		if h < my_min:
# 			my_min = h

# 	if my_min == 0:
# 		F0_hat = 'infinity'
# 	else:
# 		F0_hat = M/my_min

# 	return F0_hat

# F0_hats = []

# a_array = np.random.randint(M, size=5)
# b_array = np.random.randint(M, size=5)


# for a in a_array:
# 	for b in b_array:
# 		ans = guessF0(a,b,M,my_data)
# 		if ans != 'infinity':
# 			print(ans)
# 			F0_hats.append(math.log(ans/F0,10))


# data = [
#     go.Histogram(
#         x=F0_hats
#     )
# ]
# plot_url = py.plot(data, filename='basic-histogram')

# #Problem 4
# #We will try using the K Minimum Values method (KMV)

# def KMV(a,b,M,k,this_data):
# 	my_mins = [M] * k;
# 	maxmin = M

# 	for x in this_data:
# 		h = (a*x + b) % M
# 		if h < maxmin:
# 			if h not in my_mins:
# 				my_mins.remove(maxmin)
# 				my_mins.append(h)
# 				maxmin = max(my_mins)

# 	if maxmin == 0:
# 		F0_hat = 'infinity'
# 	else:
# 		F0_hat = M*(k-1)/maxmin

# 	return F0_hat

# F0_hats = []

# a_array = np.random.randint(M, size=5)
# b_array = np.random.randint(M, size=5)
# k = 5

# for a in a_array:
# 	for b in b_array:
# 		ans = KMV(a,b,M,k,my_data)
# 		if ans != 'infinity':
# 			F0_hats.append(math.log(ans/F0,10))


# data = [
#     go.Histogram(
#         x=F0_hats
#     )
# ]
# plot_url = py.plot(data, filename='basic-histogram')

# #Math 2
# def cnt(x, y, M):
	
