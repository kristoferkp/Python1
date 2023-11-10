n1 = float(input("Esita esimene arv: "))
tehe = str(input("Esita matemaatiline tehe ('+', '-', '*', '/'): "))
n2 = float(input("Esita teine arv: "))
if n2 == 0:
    print("Nulliga ei saa jagada.")
elif tehe == '+' or tehe == '-' or tehe == '*' or tehe == '/':
    print(eval(str(n1) + tehe + str(n2)))