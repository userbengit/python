for index in range(0,5):
	print(index)
for index in range(5,10):
	if index == 8:
		continue
	print(index)

s_denominator = 0

for i in range(100):
	if i==1:
			continue

	if i % 2 == 0:
			continue
	print(i)

	s_denominator += 1/i

s = 1/s_denominator
s = round(s,2)
print(s)