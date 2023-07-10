import os.path
x="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# count the number of characters in x and store the result in c
c=len(x)
print(c)

# save amino acids 1–24
m=x[89:110]
#print(m)

# write the result in the isinsuline file
with open("ainsulin-seq-clean.txt", 'w') as f:
    f.write(m)
#confirming the characteres writen the isinsuline file

print(len(m))



