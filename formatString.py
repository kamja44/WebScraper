my_name = "kamja"
my_age = 20
my_hair_color = "brown"

# format String <- 변수를 포함한 String
# f"Hello I'm{my_name}, I have {my_age} years in the earth, "
print(
    f"Hello I'm {my_name}, I have {my_age} years in the earth {my_hair_color} is my hair color")


def make_juice(fruit):
    return f"{fruit} + 🍹"


def add_ice(juice):
    return f"{juice} + 🧊"


def add_sugar(iced_juice):
    return f"{iced_juice} + 🍬"
# return 키워드는 함수를 종료한다. 즉, return을 만나면 함수는 끝 <- return 다음줄부터 실행 x


juice = make_juice("🍎")
print(juice)
cold_juice = add_ice(juice)
print(cold_juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)
