### Title : Bio Informatics : Reverse Compliment Problem
### Author : Kuldeep Thakre
### 13/06/2020
###

Dict = { "A":"T", "T":"A", "G":"C", "C":"G"}
ReverseComplementerySequence = ""
DNASequence = "TCAGTCTTGAGGCCAGGTCTGCGCAGAGCGATGGGGCCCCCGATTGTCTACCCCACTTCCGTAAGCATTTAAGAACATCATAGTGTGACAGGCCCCTAAGTATAACAGCCGGTTGCCACGAGTGTATTCGGTCGCCACTTGCCTCTGGTTGCTTCGCCGAGGAGCTTAGCCCACAGGAACTCATGCCAAGAGGGCTCCTTCTTTATCCTAAAATAGGTAACTGAGTGGTCATAAACTAAGCTTCATGTAATAGATGATAGATCCGTCTGCCACATGGACCGAAAATGAACAAGGGCGTATAGCGTGCCATGATTCGGTTTCGACTCCTCCGACTGGATGGTTCGGTGGGACTGGGTGAGTCGCAGTGGGTACAACGGCTAAGCGGTCGATCTAACAAATGTCGATGAGGCCATAGAAATCTTAGTCTATCTAGCACTGCGATAGGCTAAATCGTCCTCAACTCCGGCCCGACTGGCAGGCTCACCGAAGATCTCGACTCTCCCTGCAGGGACTACCTAGTCCATGATCGACCGTCCTGATGCCCTAGTGCCCTCGCCCGGCTATCTTGGCCCCTCCAAATATGGCCGTAACATTGATGCCCAAGCTAACTGACTTTAAGCACCCCTCTGAACTTCAGCGAAGAAAGGAGCCGGCCATTGAAAAGTATTCAATACCGCATAGACGACGACGACCATCCAACTATTATCGCTTCCTGAACAAAGGCTGACGTGATCCAAAGCATCATGATTTACCGCTATGGATAACGGCCGTATGTATACGAGAGGCTGCTTCGACATTGCGCGCCCATTGCGGTTTGACACACAATAGGCGATCGTACCACACATGGCTATGACAGTGTTTTTCAACAGGCGGATAAGACCCACTGAGGTCCAAGAGAATGTGAGGACAAGTTTAATGCACCGCAGCTGGTCTTTTGGATATTAAAAACGCTACTGGGATGGTGTAACTAGGTCGTCGAGCAGATATGGCTACTTTGCCGGCGAGCGCACATATCGAAGGCTGTTGCCACTTGCGCTAGAAGCTCCGCGACGCCTACCTTTAATACATGTTAGAGTGCGTGCCCATGATGCTACTCGCTGAACCCCCCCATCGTGTCCATTGTTCTGTCAAAATCGGCCTAAGTTAATCTGAGGCCGCCTCTCTAGCTCCATAAGTTTTCAACCGCAAGGAATTTGAAAAGGATCCGGCTCGTCCGCGGCGATGTCAATAGGCATCCTAGGTACAAACTAACTGGCTCGTAAGAACTGCGAATGCAGGGCTTCGCACGACAACTCACCCCAGAGTCTTATGCTTCGAGTTGGCATCTTGGCGATCGGCTAAGTATTGGTCACTAGCTCTTAGTCGAGTTATTGTTGTGATATGATACCTCAAAAGTCTAGTCTCAGTTAACACTCGTCGGAGAGGCCTTATAATTATTTAGCAGTCTTCAATATCACTTAACCCTGTGCCAGTGAGATTCGAACTCCTTCTTTAGCTCAGACTTTGATACGCTTTGGTGCCGTCTGCCTCAGCCGTCCGTAAGTGCCACCAATGCGTTCGGAGGACTTGGTCTAACCGGACGCCAGCCTCAATTCCAATGGGAGAGCAGTATCAATTCCGATAAAACATCCCTTGTAGGGCGCGGACGGCCGTCAACCGTTCTCCATGCATGGAACATAGGACAATTAGCCCTTGGCCTCGTAACATCTGCACACCCAGATCTTATATGCGGCCAACAATCAGTACCGCGGCTGAGCTAGAACATCTGCCATTATGCCCTGTTTCTACTAAATGTATAACGTGATTGCTGACACATATCTCGCGGACGACCCCAAAACGGACGGTCCGCATCTGGCTACATATCTCCTTCGAGCACGGTAATTGGCTCGAACTTCCCCTATGTAGGATGACATAGCGCGCTATTATGGACACCGCATGCAACCTTCAGACCCAGGAGATAGTCGCCTTTACTCGATGTCGTGGGGGAAGTGCGTTGTCTCTCTCGCTGCAGTCAAAAACGACCAGGTCCAAATTCACATAGTCGAAGAAATGTGGTCGTCCTGTTCTGGCCGCTAATCGGATTTCCGCAAGAAGTGCCTAACCTATCCTCCACTATGTGTGGAAACCTCTTCGAATCGGTTAAACTTGGGCCGTGTGTCGCGACGCGCCGCACTGAGTTGGCGTGGGGTTTGGGATTCGAAGGAGACGGCACCTGTCATAGGCGCAGATAACCTCTAGCTTAGGGTCGCATCCGCTACGGGTGGGGAGCCCAAGCCAGTCACGCTAGGGGTGCTCTCGGTGACGACCCTGTTCTCGTGTCGGGCAGGATCCGGCCTTTGCAAATCAGTGTTTGAACTATGACCGTATAACACCACCTATTGGCGTCGAAGTAACGTGACGTCTACCGCATACGCGGTCAAGTAAGTTCGGTAATGCGCCTCCTTGAAGAAGCGACGCGAAAGTGCCCAGGCAACCACCCCCATTAGAGAGGGCACAAGCCTTCATTTTTCCGACCTTATTGAGGTCTTGAAGGCTTATGGTAGCCCAAACCCTGCTCTCTGCGCCTATCGAATCCTCTCGGGTATAGACAATAGCCCGCGAATCGGACCCCTAAATCGGAGAGGACCGTCCTTAGATGCCTGACAGCACAAACGGGTGGGAGCTCCTGCGACCTTTGGAGGGCTTTTTTCATATCGTTTCATTTTGAAGTCTTGTCCCGTCTTGATTAAGCTTTTGCCCCATCCTCTGTCCAGTTGACACCGGATGACAATTGGCAAGGTCTAATACGTAACCACACCTACTCAGAATTCTCCCGGAATCTGTTCTTGTGAAATACGGGTCCCAAGTCTACTACATCCGCGGAGAGGGCTTTAACGCACTGAAAATGATTTAGATTAAAGTTTGTCTGTTGGAAACGCCCGCGACTCTAGCAATGTGAGACCCGCCTCTGTCGCCCGGCTGGAGCGTGCGAGTTGAGACACGATGATTACCATTTATGACGATTGTTCCAACAGGATGATTGACGTAGATATTCGGCACCTTTATGGCGGGTGCCAATCTAGCAGCGATGATTCGCACATAGCACGGAGACTATCCCTGTCAGGGCCCAGCAGCGTGTTGAAGTGTGCCCAGCCTTTGTCCAAATAGTAAGGGCCAGTCCGCGGGCCACATAGTGGGTATCGGCTACTGGCTATCATAGTGTGACCTAATGGGCGATGAGATATGGCAGGAGACCATCAACAGTTGTCCGGCATAGAAACTACAAATCTGTTACCTTGCATCTCTCGGGGCAGTTGAACATTAGCTCTAAGAGCGTGATAACGTGCTATGTCCTGCAACCCCCGTTCACTTATGGGAGTGGCCATACCCAAGTGTTACACCGTGCCGTGCTGCTTCTTTCACGACGTTAGGGCAGATCGTGGCTCGAAATAGAGGCAGTACGTGACGACCCAGATACTTGCGCGCCCTCAACAAATTTTCACTCGAAAATAGGCATTAAGTGACAAGCCTACGTGTGCGCCCTGGACGGATCGACAGAGGTCTGTCCTGTCCTCCCCGTGGGGACGCAATAGTCAAGGCCGCTTAATCGCGTACGCGAGGACCTGTGCCCTGCGTCTAGCGCGGCTGACTACACACTGGCTTTATTGTACCTAAGCGAAGAATCCGGATTTACCCGTAACGACGACGAATTAGTAGCCTTCTGCGAGCGAGATGTGACTGAGGTCAGTCTATAAACACCTCATATCCAACGTGCTATACATAAGAATTAAACGTGTAGTGCATAGAACAGGATCTAACATTGAGGTCCTTCAGGGTCAGACTTCGGGGCGGGATTAGGTCGTGATATTCAGTACGTTTGGACTGGGGCACTTTGTCTCTACTGAGGGTCCTAACTCAACTTAGTGTTAGAACGCCGACGCCACAATGGCAAGGCGGATACGTCCAAAGCAGTATACCAAGGACCACGACTTCTCTTGAAATGTAGCGCCCTACGTATCGCCCAATGGTAAAAAAGCGTCTGCGAATTACGCCTCAGTATAACTGGTGTCAGGGAGATTAGAGTGGTGAGCTCGTCCAAAAGGATACCCAGGTCTAGCATCATCAGGCTTAGGAGAACCGATGTCAATGGGATGTGCATAGCCCAATACGAGCTCCCAAGCGAATGACGATCAGTAGGATCCATGGAAAGCAAGCATTTTCTAAGGAGATAGCGTCTTGTTATCTCCCATTCTACCACAACGATTATAACAAGTAAGCATATAGGTGGAAACACAGTGGGTGCGGTCCCACGACGCGGACAAGATCACCTGTACATATATCTCGGTGGCATGCCGTCGACTGCCTGGTCCAATAACATTTATAGACAATCAGACTGGCGGGGACCGAAGCGGTGGAATACAAGGAGAACGGTGGCTAGTACAATCAAATGACGAGTAGTCCTTCGCCTGAGGATTAGACCGCAGTATTAGCACTGAGCTACACAGTAGCGGCGGTAAGGCGATGTGGCGGCCTACGCTCTAGGGTGCTCCAAGACTGCCATACAGGGTCGCGCCTGCATGCAAAAAGCGGTCTCTTTAGGACATGGCCTCACTGTACGTCTCCCTGGTCAGCCTGTGGCCGTTTCCCCCTACCTTCAGTATAGATGGTTTACTGTATACATACCATGAAATCCATCTCCCCAGCTGGGCGACAGCCTAAATTAATGTAGCACCTCCAGCGGAACTTATCGCAGTGGGGTCACTTTGTGCTTCGAATAGGGGAGCTAACGGCAAGGGAGTTGGCAGTCGCGTCACGACAATCTGCAAAGCGGAAGCTCGGAGAAGGGAGAGAGGACGATTTACAAGCTTGTAGGGCGCTTAGGTAGCCCTCTACTAATTGTATACTTCTTAATTTCACGATTCCAGACCCATAATACACATGCACCGTATACACGGGAACAGAAATGTCATGAAATCTTAGCTATCGGATCACAAGACAGATACTTTCAATGAAGTCTGATCGTACGCTTAATTCACCATATGCGGCATGTTGGGGAAGTTTACCAGCTTAGAGGACTCAGGGATGAAAACAAGGCGGACTCAGATCAGTGCTGATCCACCTGGCCTCAGGCGGGGCCTGGACCCCCACATACTGGTTTTTTCTACACCGCTTCTTGACTCTCCCCGAATGGTCAGCGCGTTGATTCCTGTTGATGAAAGTTAATGTTAACCAACTCTCTACGGCCGCGTCTATGCCCCCTAAGGTGATGTACTGGGATTGGGTAGGAATTAATGCCTCGAGTGCCAGGGTATTAACGCCTCACTAAGCTGCAAAGGTCGAACTCCAAGGGCCGGCTCGGTCCGAACCTCTGCTGGTTTATCGACAGTCCTTTTGTTCTAGACCGTATTAGGTTTCTCGTCATGGCGAGTCCCCCTCTGTGGGTCACATCAAATATATAAGCTGTAGGTACCGTACGCCCGACTGTTAAGCGTACTAGCGCGAGGCCCCATAGAGAGGCTTGTCGCCGTACCCGTCGACACGCCCACATGCCTTGATGCGAGTTCTAGCCATACGCAGCGTCGAAACTAGGAACGGAGAAGATGTGTGACTTCATGGGAGCTTCGATCATAGCTCTGCTGACGAGAGAGACCGCGTGCCTCTTGATACGTTTCTAATCTATACTCATCGTAATAACAGACAAGCGCTTGACCGCGTGTAATAGCAATAGAACGAGTACCATGCGTCGTATAGTTCGTGACTACTGGATGTGGTCGAATGTTAGCCCATGTAGTTATCGGCGTGGCTCGGAGTAGCCCGTCACTTACGAATGCCCTTACAGTTCAAATGAACAGGTCTAACACGCCCACTCTCCTAGCGAGTTCTTTGAGAAAGTGCGAAGACATAATGGTCTAATATTCTGCGACGACGAGCTTCTGTGAAGTGTGACATAAAGCGCAGTAAGGTGTTCACAGAAAGGGTGCTATACCTCGTCACCCCCGTTTCTGAGCCTCAGGTTCCGGGATGCCGACAAGCCTCTGACGTCCGGCTCGCCCACATCATTGATCGGGACCTATAGGCCGTAGCGACAGTACCCGCTGAAACACGCACGTTATCGGTCGAAGACTAAAGTTTATTTTTGCTGGATCCGTACAGGGGGGACCGATTCTGTACCCGCTGTAGATGTGAGATGCGAGGACACTCCGAGGGGGTGTGTGAAATGCCCTGGCGATCGCTAAGTGGGTAGTTAAGCCGGCACGTATGCAGCCTGAAACCAGTCTGACCCCGTAAATCATCGATAACACTCCCTAATAATTAAATCTTATGAACTTTGTCTGACCTAGTCACGGAGAAACATAACGCAGTGGATCTGTGGCTTCCGGGTTTTACAATCGTCTCTCGGCTGACGTAATAGTGCCTATGTAGCCTTACAGGCCCCATCACTGGAACGTTCGGTCCGCTCCGATCCGTATGGTGTCGAAGTCAACTTTCTACCTCTGAATCTGGATTGATTTTCTCAGTGCTAGTGATCTGCGCACCTGCTTATCGGTGAACCCAGAACCTAGAAATATGGTGTTATAGATAGAAGGCGACTTATGTAATGCGACTAGACTTCCTTCCGTCGCTGTTACAGCCTCAGGCCTTTATGTACCTCGAGCTGATCGTCGTCCGCAACTAAGGGTTTAAGTCGCGTACCTAGAATTAGCACTCTGTCAACTTCGCTCATCACGGAGTAATGGCGAGGAATAATTCGCTATATTGACGAAATGGCTCCGACGAAGATAGGAATGTGCTCGCACGTGCGATGGCAGGTGACGGAGGTCTAAATTCGCATCGAAATCTTTTATGTGAATATAAATAACCTCTCGGCAAGATCCGCGCTATGTTTGAGACACGCGCTCCTCTCACTCACTGTTTACCATCGTGACGGTGTACTCCACAGCTTAGACCAGCTGTAACATAACATGACCCTTAACGCGGTCGCGGGAACCATGCGGGAACAACATAACGGGCCGTTCACGTGGGTAAGAAGAAGCTCAACTTCGGGCGAGGTAGCAGAAAGTTGTATCCTATTTTTACACAGGAAGTTCGCAGGAATAGTGCATCGCTTGGAACCTCTAAAGAGCGTTGTACTAAAGTGAGAAAGTCTTGCTCGGGATCTGTCGCCGTTGTTCCGCCTGGTCTAAACGGTCGGCGGCCTTAACATATCATGGCATGGAACCACTTTGCTCTATTCATTGGATTTGTAGCCTAATGCTCTCCGGGTGCACGGTGCAGTTAATTTGGCTTAGTAAGCGCGCGTCCGAAGCGACTGTTCGAGCTAGAGTGGACACCCTCCTTATGGTGTCTCATGATGGGATTGACGTGTTGTGCAAACCGCATCTCTAATCTACAAGCGTTGACCCGTAGGATTATGGCAAACTGTTGCCGTGATGGGTTACACCTAAGAGGAAAGCCGCAGTCCGTAGCCATGCTTTCTAGGTCACGACCAGTGACGTTTGATTTTTGCATGTCCCTCGAATTAAAATTGCCGATTAGGGAGCCAGTCTGCCTGGGGATACATGAGAGTAACGTCCCAAAAGTATTAGCGTATTCCAGTTTGATCTGCAATGCAGGGCGTTGCTGGTGACCCCGCAGAAATAGGTGCAACGGTCCCTTATGCGACATCCTATTCTGAGAGGTGCTTAAAGCATCCGCGGTTAGCGATGTCCTAGCATGCTAACTGATTACGCCTCGGTTAGAAGCTCGGGTAACAGTGGTGCTTCTCCCGCATGGCCGTTCAGATGCGTCGCAATCCAAAAGGGGACGACCCTCAGGCGCGCCACACCAGGTGTCTTACCATTTGGTGGTTAGCTAGCAAATTAAACAATTGCTATGGTTCAGTGGCAGTAGCTCAGAATCAGCGGGCCTCGACCGACTCTCACGTTCGTGCCCAGGACGGAGCGCACAGGCCCTGCCATAGAAATCACCAGTATGACATATACCGGGCTTATGCCCAGTACACCATCGACTGGGTCGAAACTCCAGGGCCCAATTCTTAACGACTGCCGTGCAGACTGTTCCGCTACCCTTCAGTTTGCTTTAAACGTCCATCCCAGACCGGGCCAGGTCCGTTCGCGTATGTCCCTGGAGTGTCGCGGGTCGTTGATTCTGTTCCCCGAGCTATCGTTGTAAAACGAACATTGCACCGGATAACCCCCGCGCAATTGACTCTGGTACACCTTACCGATCCCGTCAGTATATCAGACCGGAACAACATCGCCGAAGGCTTTCAATAGGAAACGAGTCAGCAAAACTGCTTATATTGGTCAGGCATCAAACGGAATATCGGAATACGGGTGGGCAAGAGACAGCTGCCATCTGTTAAAAATAACACATAATCAATGTCCAGGGTTCTAAGACAATTTCGTAAGTGGACACATTACCCAACAGCCGTGTAAATCGATAAGCACCGCCATCTACAAGGGGTTGCCCATCTGATCATCGGAAGGAGGGTGTAACGACCTTTTAGGGGGATTTTAGTGTACACATACCAAAGGTGCGCTGGGGGGCCGATCCAAAGAAATCGATAGGAGGGATTAGGTAAATCACCGCTTACTTGCGGGCACTACAGATAAGGGTTGCAGCTACCCTCCAAAACT"

for x in DNASequence:
	ReverseComplementerySequence += Dict[x]

print(ReverseComplementerySequence[::-1])