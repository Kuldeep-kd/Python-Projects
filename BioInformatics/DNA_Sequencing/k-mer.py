def Count(dna, pattern):
    k = len(pattern)
    matches = 0
    positions = []
    for x in range(0, len(dna)):
        if dna[x] == pattern[0]:
            if(str(dna[x:x+k]) == pattern):
                matches += 1
                positions.append("{}".format(x))
    return matches, positions
x,y = Count(DNA,"CTTGATCAT")
print(" ".join(y))