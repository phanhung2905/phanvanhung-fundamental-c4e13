chieucao = float(input("nhap vao chieu cao cua ban(don vi cm ):"))
m = chieucao / 100
print(m)
input("chieu cao cua ban(don vi m): ")
kg = float(input("nhap vao can nang cua ban?: "))

bmi = kg / m**2
if bmi < 16:
    print("suy dinh duong,", "bmi=", bmi )
elif bmi < 18.5:
    print("thieu can,", "bmi=", bmi)
elif bmi < 25:
    print("nguoi dep,", "bmi=", bmi)
elif bmi < 30:
    print("hoi beo,", "bmi=",bmi)
else:
    print("beo phi,", "bmi=", bmi)


