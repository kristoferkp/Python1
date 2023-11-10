vanus = int(input("Mis on teie vanus?"))
if vanus < 16 and vanus >= 0:
    print("Ei ole veel lubatud hääletada")
elif vanus < 18 and vanus > 0:
    print("On lubatud hääletada kohalikel valimistel")
elif vanus >= 18 and vanus <= 110:
    print("On lubatud hääletada nii kohalikel kui ka riigikogu valimistel")
elif vanus < 0 or vanus > 110:
    print("Vigane vanus")