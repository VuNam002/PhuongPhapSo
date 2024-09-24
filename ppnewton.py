#newton
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
    while True:
        x1 = x0 - f.subs(x, x0) / D_fx.subs(x, x0)
        error = abs(x1 - x0)
        if error < epsilon:
            break
        x0 = x1
    return x1

# Chọn giá trị ban đầu và epsilon
x0 = float(input("Nhập giá trị ban đầu: "))
epsilon = float(input("Nhập epsilon: "))

# Tìm nghiệm dương nhỏ nhất
Nghiem_duong_nho_nhat = newton(x0, epsilon)
print(f"Nghiệm dương nhỏ nhất: {Nghiem_duong_nho_nhat:.6f}")
