# input <- 사용자의 입력을 받아온다. input("질문") input은 String값으로 반환된다.
age = int(input("How old are you?"))  # int() <- int형으로 형변환

print("user answer", age)

# type <- 변수의 type을 알려준다.
print(type(age))

if age < 18:
    print("You can't drink")
elif age <= 35 and age >= 18:
    print("can!")
elif age == 60 or age == 70:
    print("Hi")
else:
    print("Go ahead")
