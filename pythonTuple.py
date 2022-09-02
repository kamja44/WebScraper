# Tuple <- 불변성(튜플을 생성한 이후 변경할 수 없다.)
# LIST는 변수, TUPLE는 상수로 생각
# 튜플명 = ()
days = ("Mon", "Tue", "Wed")  # 튜플 생성
# List
# 리스트명 = []

# 튜플의 원소에 접근 <- 리스트와 동일
# 튜플명[index] index는 0부터 시작
print(days[1])  # Tue 출력

# Tuple의 뒤에서부터 접근가능
# 즉, tuple[-1] = "Wed"출력
# 뒤에서부터 접근할 때는 -1부터 시작
print(days[-1])
