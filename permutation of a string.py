from itertools import permutations 

ini_str = "abc"

print("Initial string", ini_str) 

permutation = [''.join(p) for p in permutations(ini_str)] 

print("Resultant List", str(permutation)) 
