def NumberToPattern(number,k):
	Template = { 0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}
	ans = ''
	while not len(ans) == k:
		mod = int(number % 4)
		number /= 4
		ans += Template[mod]
	print(ans[::-1])

def PatternToNumber(pattern):
	Template = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
	ans = 0
	pattern = pattern[::-1]
	for i in range(0, len(pattern)):
		ans += Template[pattern[i]] * (4**i)

	print(ans)


#NumberToPattern(5437,7)
PatternToNumber('ATGCAA')
