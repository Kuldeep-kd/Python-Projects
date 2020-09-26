def Count(dna, pattern):
    k = len(pattern)
    matches = 0

    for x in range(0, len(dna)):
        if dna[x] == pattern[0]:
            if(str(dna[x:x+k]) == pattern):
                matches += 1
    return matches

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
	return int(ans)


def ComputingFrequencies(Text,k):
	arr = [0]*(4**(k)-1)
	for x in range(0,len(Text)-1):
		Number = PatternToNumber(Text[x:x+k])
		if not Number == None:
			arr[Number] += 1

	return " ".join(str(x) for x in arr)


print(ComputingFrequencies('AACCTTGCATAAAAGGGGGGTCGAAACCATTAAAGAATGTATTATCCTGATACGCAGTGACTCTAGCGCGGGAACAGGAGAGTAGTATCCTGACAGCGCCTCGTAGTAAGAAAACCCGGCACGTGGCGCCGCGTCTCCGATCTAATATCTGTGTTTGGGATCGAGAATGCGTCTTTGAAATCATCTGGTCATCGCCTGCCAATAGAGATCGATAAGGTGTAGGGGTTCTCATTATCCGAGCCAATGCATATTCCGCCCTACACTCTGGGTATACTAAGATGCTCCAAACGCCCAACCACGCTAGTACGCGCACTAACCCCTTGTACACGCGTTCCGGTGCCCGTAGACATTGGCATGTCTCCCTAGCGTGGGCAGCTCCCCTCATCTATACCAGTTGAGGTATAAGAATCTTAAGGGCGAACAATTTTAAGGAGTCTGACTGATCCACATCGCGGCAGAGCCCCCGTCCTGTTCCTACCCTTACGTGGAGAAGTATGTGGGTCTAGTTGACTACTTCACGACAGCTATGGAGTAAGAGTGTTCCCACCCTTAGCTTCCCCAAGGAGCCAAATTTCGCGAGAAACCAGCCATGCGAGACACTAGCAAAGCTGGCGACCACCTCTTACCACAGTGAGGATACTCAGATTTTGTGGGAGCTCCTTACCTTGGTATTCTCCTTGCTTACCCCCCGT',6))
# NumberToPattern(5437,8)
# PatternToNumber('ATGCAA')