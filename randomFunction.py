from dis import dis
import random
"""from random import randint <- random라이브러리(모듈)에서 randint함수를 import한다.
import random <- random 라이브러리 통채로 import
외부 라이브러리 사용
Python Standard Library <- default function(built-in function)


user_choice = int(input("Choose number."))

pc_choice = random.randint(1, 50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
    print("Higer! Computer chose", pc_choice)
"""
distance = 0
# while True:
#   print() <- while의 조건이 True일 경우 계속 만복
while distance < 20:
    print("I'm running: ", distance, "km")
    distance = distance + 1
