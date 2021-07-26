import sys

crossings = {}
for x in sys.stdin:
	x = x.strip()
	beg = x[0]
	end = x[-1]

	if beg in crossings:
		crossings[beg] += 1
	else:
		crossings[beg] = 1

	if end != beg:x
		if end in crossings:
			crossings[end] += 1
		else:
			crossings[end] = 1

sorted_list = sorted(crossings, key=lambda x: (crossings[x], x))

for x in sorted_list:
	print(x, crossings[x])