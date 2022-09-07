def say_hello(name, age):
    print(f"Hello {name} you are {age} years old")


# position arguments < - argument의 위치를 알고있다. 즉, 자리에 기반하여 argument를 보낸다.
say_hello("kamja", 20)
# keyword arguments < - argumet의 이름에 값을 정해준다. arguemnt의 자리가 바뀌어도 상관없다.
say_hello(age=20, name="kamja")
