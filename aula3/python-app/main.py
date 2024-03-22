import sys

def soma(a,b):
    return a + b

args = sys.argv[1:]
print(args)

operacao = args[0]

if operacao == "soma":
    a = int(args[1])
    b = int(args[2])
    print(soma(a,b))

