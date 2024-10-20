_P_ = int(input("Enter Your Percentage: "))

if _P_ >= 90 and _P_ <= 100:
    print("YOu have Excellent Result")
elif _P_ >= 80 and _P_ < 90:
    print("YOu have A Result")
elif _P_ >= 70 and _P_ < 80:
    print("YOu have B Result")
elif _P_ >= 60 and _P_ < 70:
    print("YOu have C Result")
elif _P_ >= 50 and _P_ < 60:
    print("YOu have D Result")
elif _P_ < 50 and _P_ >= 0:
    print("Or Gema Khed Nalayak")
else: 
    print("Chawlian marne ko nhi ka, jo kaha hai wo kar")