"#1. First Python code :D"

def boolean_to_string(b):
    return "True" if b else "False"


"#2. Still learning Syntaxis"
"Create a function which translates a given DNA string into RNA."

def dna_to_rna(dna):
    rna = []
    for x in dna:
        if x == "T":
            rna.append("U")
        else:
            rna.append(x)
    rna_string = "".join(rna)
    return rna_string


dna_to_rna("TTGACCGCCGCC")            
