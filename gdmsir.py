import time
x = ("Good Morning Sir")
y = ("Good Afternoon Sir")
z = ("Good Evening Sir")

pt = time.strftime("%H:%M:%S")
if pt >= "00:00:00" and pt < "12:00:00":
    print(x)
elif pt >= "12:00:00" and pt < "16:00:00":
    print(y)
else:
    print(z)




