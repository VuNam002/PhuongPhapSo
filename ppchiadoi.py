## Bài 3.2.
def Chia_doi(a, b, n):
    for i in range(n):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def Day_cung(a, b, n):
    for i in range(n):
        fa = f(a)
        fb = f(b)
        c = a - fa * (b - a) / (fb - fa)
        a, b = b, c # gán a = b, b = c
    return c

# Nhập hàm f(x) từ bàn phím
fx = input("Nhập hàm f(x):  ")
f = lambda x: eval(fx)

# Nhập a,b,n 
a=float(input("Nhập khoảng phân li a: "))
b =float(input("Nhâp khoảng phân li b: "))
n=int(input("Nhập số bước lăp: "))

Nghiem_gan_dung_chia_doi = Chia_doi(a, b, n)


# Tính nghiệm gần đúng bằng phương pháp dây cung
Nghiem_gan_dung_day_cung = Day_cung(a, b, n)


print(f"Phương pháp chia đôi: Nghiệm gần đúng = {Nghiem_gan_dung_chia_doi}")
print(f"Phương pháp dây cung: Nghiệm gần đúng = {Nghiem_gan_dung_day_cung}" )