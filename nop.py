#Bài 3.2
def Chia_doi(a, b, n):
    print(f"{'Iteration':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<15}")
    for i in range(n):
        c = (a + b) / 2
        print(f"{i+1:<10}{a:<15.6f}{b:<15.6f}{c:<15.6f}{f(c):<15.6f}")
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def Day_cung(a, b, n):
    print(f"{'Iteration':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<15}")
    for i in range(n):
        fa = f(a) #tính giá trị f tại a
        fb = f(b)
        c = a - fa * (b - a) / (fb - fa) #công thức lặp
        print(f"{i+1:<10}{a:<15.6f}{b:<15.6f}{c:<15.6f}{f(c):<15.6f}")
        a, b = b, c  # gán a = b, b = c
    return c

# Nhập hàm f(x) từ bàn phím
fx = input("Nhập hàm f(x): ")
f = lambda x: eval(fx)

# Nhập a, b, n
a = float(input("Nhập khoảng phân li a: "))
b = float(input("Nhâp khoảng phân li b: "))
n = int(input("Nhập số bước lặp: "))

print("\nPhương pháp chia đôi:")
Nghiem_gan_dung_chia_doi = Chia_doi(a, b, n)

print("\nPhương pháp dây cung:")
Nghiem_gan_dung_day_cung = Day_cung(a, b, n)

# Hiển thị nghiệm gần đúng với 5 chữ số sau dấu phẩy
print(f"\nPhương pháp chia đôi: Nghiệm gần đúng = {Nghiem_gan_dung_chia_doi:.5f}")
print(f"Phương pháp dây cung: Nghiệm gần đúng = {Nghiem_gan_dung_day_cung:.5f}")




#Bài 3.5
def Chia_doi(a, b, epsilon):
    print(f"{'Iteration':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<15}")
    i = 0
    while abs(b - a) > epsilon:
        i += 1
        c = (a + b) / 2
        print(f"{i:<10}{a:<15.6f}{b:<15.6f}{c:<15.6f}{f(c):<15.6f}")
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Nhập hàm f(x) từ bàn phím
fx = input("Nhập hàm f(x): ")
f = lambda x: eval(fx)

# Nhập a, b, epsilon
a = float(input("Nhập khoảng phân li a: "))
b = float(input("Nhập khoảng phân li b: "))
epsilon = float(input("Nhập sai số epsilon: "))

print("\nPhương pháp chia đôi:")
Nghiem_gan_dung_chia_doi = Chia_doi(a, b, epsilon)

# Hiển thị nghiệm gần đúng với 5 chữ số sau dấu phẩy
print(f"\nPhương pháp chia đôi: Nghiệm gần đúng = {Nghiem_gan_dung_chia_doi:.5f}")

#Bài loga bài 3.5
import math

def Chia_doi(a, b, epsilon):
    print(f"{'Lần lặp':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<15}")
    i = 0
    while abs(b - a) > epsilon:
        i += 1
        c = (a + b) / 2
        print(f"{i:<10}{a:<15.6f}{b:<15.6f}{c:<15.6f}{f(c):<15.6f}")
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Nhập hàm f(x) từ bàn phím
fx = input("Nhập hàm f(x), sử dụng 'math.log' cho log tự nhiên: ")
f = lambda x: eval(fx)

# Nhập a, b, epsilon
a = float(input("Nhập khoảng phân li a: "))
b = float(input("Nhập khoảng phân li b: "))
epsilon = float(input("Nhập sai số epsilon: "))

print("\nPhương pháp chia đôi:")
Nghiem_gan_dung_chia_doi = Chia_doi(a, b, epsilon)

# Hiển thị nghiệm gần đúng với 5 chữ số sau dấu phẩy
print(f"\nPhương pháp chia đôi: Nghiệm gần đúng = {Nghiem_gan_dung_chia_doi:.5f}")


#Bài 3.6 (ý b)
def Day_cung(a, b, n):
    print(f"{'Iteration':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<15}")
    for i in range(n):
        fa = f(a)
        fb = f(b)
        c = a - fa * (b - a) / (fb - fa)
        print(f"{i+1:<10}{a:<15.6f}{b:<15.6f}{c:<15.6f}{f(c):<15.6f}")
        a, b = b, c  # gán a = b, b = c
    return c

# Nhập hàm f(x) từ bàn phím
fx = input("Nhập hàm f(x): ")
f = lambda x: eval(fx)

# Nhập a, b, n
a = float(input("Nhập khoảng phân li a: "))
b = float(input("Nhâp khoảng phân li b: "))
n = int(input("Nhập số bước lặp: "))

print("\nPhương pháp dây cung:")
Nghiem_gan_dung_day_cung = Day_cung(a, b, n)

print(f"Phương pháp dây cung: Nghiệm gần đúng = {Nghiem_gan_dung_day_cung:.5f}")



#Bài 3.6(a,c)
def Day_cung(a, b, epsilon):
    print(f"{'Lần lặp':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<15}")
    i = 0
    while abs(b - a) > epsilon: #vòng lạp thực hiện khi khoảng cách a và b>epsilon
        i += 1
        fa = f(a)
        fb = f(b)
        c = a - fa * (b - a) / (fb - fa) #công thức lặp
        print(f"{i:<10}{a:<15.6f}{b:<15.6f}{c:<15.6f}{f(c):<15.6f}")
        a, b = b, c  # gán a = b, b = c
    return c

# Nhập hàm f(x) từ bàn phím
fx = input("Nhập hàm f(x): ")
f = lambda x: eval(fx)

# Nhập a, b, epsilon
a = float(input("Nhập khoảng phân li a: "))
b = float(input("Nhập khoảng phân li b: "))
epsilon = float(input("Nhập sai số epsilon: "))

print("\nPhương pháp dây cung:")
Nghiem_gan_dung_day_cung = Day_cung(a, b, epsilon)

# Hiển thị nghiệm gần đúng với 5 chữ số sau dấu phẩy
print(f"Phương pháp dây cung: Nghiệm gần đúng = {Nghiem_gan_dung_day_cung:.5f}")




# Newton,3.7
import sympy as sp

# Nhập biến x
x = sp.Symbol('x')

# Nhập hàm f(x) từ bàn phím (ví dụ: sin(x) hoặc cos(x))
expression = input("Nhập hàm f(x): ")
f = sp.sympify(expression)  # Chuyển biểu thức thành đối tượng sympy

# Tính đạo hàm của hàm f(x)
D_fx = sp.diff(f, x)

# Áp dụng phương pháp Newton-Raphson
def newton(x0, epsilon):
    iteration = 0 #khởi tạo số lần lặp
    print(f"{'Iteration':<10}{'x0':<20}{'f(x0)':<20}{'D_fx(x0)':<20}{'x1':<20}{'Error':<20}")
    while True:
        f_x0 = float(f.subs(x, x0)) # Tính giá trị hàm f(x) tại x0 bằng cách thay x=x0 
        D_fx_x0 = float(D_fx.subs(x, x0))
        x1 = x0 - f_x0 / D_fx_x0
        error = abs(x1 - x0) # tính sai số
        print(f"{iteration:<10}{x0:<20.10f}{f_x0:<20.10f}{D_fx_x0:<20.10f}{x1:<20.10f}{error:<20.10f}")
        if error < epsilon:
            break
        x0 = x1 # cập nhật giá trị x0 cho bước lặp tiếp theo
        iteration += 1
    return x1

# Chọn giá trị ban đầu và epsilon
x0 = float(input("Nhập giá trị ban đầu: "))
epsilon = float(input("Nhập epsilon: "))

# Tìm nghiệm dương nhỏ nhất
Nghiem_duong_nho_nhat = newton(x0, epsilon)
print(f"Nghiệm dương nhỏ nhất: {Nghiem_duong_nho_nhat:.6f}")



#Bài 3.9 lặp đơn
import math

def lap_don(phi, x0, e, q):
    """
    Hàm thực hiện phương pháp lặp đơn.

    Args:
        phi: Hàm phi(x).
        x0: Giá trị x ban đầu.
        e: Sai số.
        q: Hệ số q trong công thức kiểm tra sai số.

    Returns:
        Nghiệm x1 của phương trình.
    """
    print(f"{'Iteration':<10}{'x0':<15}{'x1':<15}{'Error':<15}")
    print("-" * 50)
    
    iteration = 0
    x1 = phi(x0)
    err = abs(x1 - x0)
    print(f"{iteration:<10}{x0:<15.10f}{x1:<15.10f}{err:<15.10f}")
    
    while err >= e * (1 - q) / q:
        x0 = x1
        x1 = phi(x0)
        err = abs(x1 - x0)
        iteration += 1
        print(f"{iteration:<10}{x0:<15.10f}{x1:<15.10f}{err:<15.10f}")
    
    return x1

def phi(x):
    # Định nghĩa hàm phi(x)
    return math.sin(x) + 0.25

x0 = 1  # Giá trị x ban đầu
e = 0.005  # Sai số
q = 0.5    # Hệ số q

x1 = lap_don(phi, x0, e, q)
print(f"\nNghiệm của phương trình là: {x1:.2f}")  # In ra kết quả với 2 chữ số thập phân


# Bài 3.13
import math
import sympy as sp

def newton_raphson(f, Df, x0, e):
    """
    Hàm thực hiện phương pháp Newton-Raphson.

    Args:
        f: Hàm f(x).
        Df: Hàm đạo hàm của f(x), Df(x).
        x0: Giá trị x ban đầu.
        e: Sai số.

    Returns:
        Nghiệm x1 của phương trình.
    """
    print(f"{'Iteration':<10}{'x0':<15}{'x1':<15}{'Error':<15}")
    print("-" * 50)
    
    iteration = 0
    x1 = x0 - f(x0) / Df(x0)
    err = abs(x1 - x0)
    print(f"{iteration:<10}{x0:<15.10f}{x1:<15.10f}{err:<15.10f}")
    
    while err >= e:
        x0 = x1
        x1 = x0 - f(x0) / Df(x0)
        err = abs(x1 - x0)
        iteration += 1
        print(f"{iteration:<10}{x0:<15.10f}{x1:<15.10f}{err:<15.10f}")
    
    return x1

# Nhập hàm f(x) từ bàn phím
f_input = input("Nhập hàm f(x) (ví dụ: sin(x) + 3*cos(x) - 2): ")

# Chuyển đổi chuỗi nhập vào thành hàm sử dụng sympy
x = sp.symbols('x')
f_sympy = sp.sympify(f_input)
Df_sympy = sp.diff(f_sympy, x)

# Chuyển đổi hàm sympy thành hàm python
f = sp.lambdify(x, f_sympy, 'math')
Df = sp.lambdify(x, Df_sympy, 'math')

# Nhập các giá trị ban đầu từ bàn phím
x0_1 = float(input("Nhập giá trị x0 thứ nhất: "))
x0_2 = float(input("Nhập giá trị x0 thứ hai: "))
e = float(input("Nhập sai số e: "))

print("Nghiệm thứ nhất:")
x1_1 = newton_raphson(f, Df, x0_1, e)
print(f"\nNghiệm của phương trình là: {x1_1:.10f}\n")

print("Nghiệm thứ hai:")
x1_2 = newton_raphson(f, Df, x0_2, e)
print(f"\nNghiệm của phương trình là: {x1_2:.10f}")



#Bài 3.15,3.16,3.17
import math
import sympy as sp

def newton_raphson(f, Df, x0, tolerance):
    """
    Hàm thực hiện phương pháp Newton-Raphson.

    Args:
        f: Hàm f(x).
        Df: Hàm đạo hàm của f(x), Df(x).
        x0: Giá trị x ban đầu.
        tolerance: Độ thay đổi tối thiểu giữa hai lần lặp liên tiếp.

    Returns:
        Nghiệm x1 của phương trình.
    """
    print(f"{'Iteration':<10}{'x0':<15}{'x1':<15}{'Error':<15}")
    print("-" * 50)

    iteration = 0
    x1 = x0 - f(x0) / Df(x0)
    err = abs(x1 - x0)
    print(f"{iteration:<10}{x0:<15.10f}{x1:<15.10f}{err:<15.10f}")

    while err >= tolerance:
        x0 = x1
        x1 = x0 - f(x0) / Df(x0)
        err = abs(x1 - x0)
        iteration += 1
        print(f"{iteration:<10}{x0:<15.10f}{x1:<15.10f}{err:<15.10f}")

    return x1

#Bài 3.20
 

# Nhập hàm f(x) từ bàn phím
f_input = input("Nhập hàm f(x) ( x**4 + 0.9*x**3 - 2.3*x**2 + 3.6*x - 25.2): ")

# Chuyển đổi chuỗi nhập vào thành hàm sử dụng sympy
x = sp.symbols('x')
f_sympy = sp.sympify(f_input)
Df_sympy = sp.diff(f_sympy, x)

# Chuyển đổi hàm sympy thành hàm python
f = sp.lambdify(x, f_sympy, 'math')
Df = sp.lambdify(x, Df_sympy, 'math')

# Nhập các giá trị ban đầu từ bàn phím
x0 = float(input("Nhập giá trị x0 ban đầu: "))
tolerance = float(input("Nhập giá trị tolerance: "))

print("Nghiệm của phương trình:")
x1 = newton_raphson(f, Df, x0, tolerance)
print(f"\nNghiệm của phương trình là: {x1:.10f}")


import math

def Chia_doi(f, a, b, epsilon):
    """
    Tìm nghiệm gần đúng của phương trình f(x) = 0 trên khoảng [a, b] bằng phương pháp chia đôi.

    Args:
      f: Hàm số f(x).
      a: Cận dưới của khoảng phân li.
      b: Cận trên của khoảng phân li.
      epsilon: Sai số cho phép.

    Returns:
      Nghiệm gần đúng của phương trình.
    """
    print(f"{'Lần lặp':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<15}")
    i = 0
    while abs(b - a) > epsilon:
        i += 1
        c = (a + b) / 2
        print(f"{i:<10}{a:<15.6f}{b:<15.6f}{c:<15.6f}{f(c):<15.6f}")
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def Newton(f, df, x0, epsilon, max_iter=10):
    """
    Tìm nghiệm gần đúng của phương trình f(x) = 0 bằng phương pháp Newton.

    Args:
      f: Hàm số f(x).
      df: Đạo hàm của hàm số f(x).
      x0: Điểm bắt đầu.
      epsilon: Sai số cho phép.
      max_iter: Số lần lặp tối đa.

    Returns:
      Nghiệm gần đúng của phương trình.
    """
    print(f"{'Lần lặp':<10}{'x':<15}{'f(x)':<15}")
    x = x0
    for i in range(1, max_iter + 1):
        print(f"{i:<10}{x:<15.6f}{f(x):<15.6f}")
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    return x

# Định nghĩa các hàm số và đạo hàm của chúng
def f1(x):
    return math.exp(x) - math.sin(x)

def df1(x):
    return math.exp(x) - math.cos(x)

def f2(x):
    return math.log(x) - 3*x + 5

def df2(x):
    return 1/x - 3

def f3(x):
    return x - math.cos(x)

def df3(x):
    return 1 + math.sin(x)

def f4(x):
    return x * math.sin(x) + 3 * math.cos(x) - x

def df4(x):
    return x * math.cos(x) + math.sin(x) - 3 * math.sin(x) - 1

# a) f(x) = e^x - sin x = 0 trên [-4; -3]
print("\na) f(x) = e^x - sin x = 0 trên [-4; -3]")
print("\nPhương pháp chia đôi:")
nghiem_chia_doi_a = Chia_doi(f1, -4, -3, 1e-5)
print(f"\nPhương pháp chia đôi: Nghiệm gần đúng = {nghiem_chia_doi_a:.5f}")
print("\nPhương pháp Newton:")
nghiem_newton_a = Newton(f1, df1, -3.5, 1e-5)
print(f"\nPhương pháp Newton: Nghiệm gần đúng = {nghiem_newton_a:.5f}")


# c) f(x) = x - cos x = 0 trên [0; 1]
print("\nc) f(x) = x - cos x = 0 trên [0; 1]")
print("\nPhương pháp chia đôi:")
nghiem_chia_doi_c = Chia_doi(f3, 0, 1, 1e-5)
print(f"\nPhương pháp chia đôi: Nghiệm gần đúng = {nghiem_chia_doi_c:.5f}")
print("\nPhương pháp Newton:")
nghiem_newton_c = Newton(f3, df3, 0.5, 1e-5)
print(f"\nPhương pháp Newton: Nghiệm gần đúng = {nghiem_newton_c:.5f}")

# d) f(x) = x sin x + 3 cos x - x = 0 trên [-6; 6]
print("\nd) f(x) = x sin x + 3 cos x - x = 0 trên [-6; 6]")
print("\nPhương pháp chia đôi:")
nghiem_chia_doi_d = Chia_doi(f4, -6, 6, 1e-5)
print(f"\nPhương pháp chia đôi: Nghiệm gần đúng = {nghiem_chia_doi_d:.5f}")
print("\nPhương pháp Newton:")
nghiem_newton_d = Newton(f4, df4, 0, 1e-5)
print(f"\nPhương pháp Newton: Nghiệm gần đúng = {nghiem_newton_d:.5f}")
