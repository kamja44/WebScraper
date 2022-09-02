# Dictionary <- key-value 쌍으로 이루어져있음 즉, JS의 Ojbect
# Dictionary는 많은 속성들을 가지고 있는 데이터를 만들 때 사용한다.
# Dictionary 생성
# Dictionary = {
#   "key" : "value",
#   "key" : "value",
#   "key" : "value",
#   ...,
# }
player = {
    "name": "kamja",
    "age": 12,
    "fav_food": ["🥨", "🍙"],  # fav_food = list
}
print(player)

# Dictionary의 요소에 접근
print("Attribute :", player["fav_food"])

# Dictionary에 새로운 요소 추가
player["xp"] = 1500
print("append xp: ", player)

# Dictionary의 fav_food에 새로운 요소 추가하기
player["fav_food"].append("🍖")
print("append fav_food", player)

# Dictionary method
print(player.get("name"))
print("before pop(): ", player.get("fav_food"))
player.pop("fav_food")
print("after pop(): ", player.get("fav_food"))
