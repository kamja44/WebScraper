# list

days_of_week = ["Mon", "Tue", "Wed", "Thr", "Fri"]

# list's methods

# print(days_of_week.count("Wed"))
# days_of_week.clear()
print(days_of_week)
# days_of_week.reverse()
# print(days_of_week)
days_of_week.append("Sat")
print(days_of_week)
days_of_week.append("Sun")
print(days_of_week)
days_of_week.remove("Sun")
print(days_of_week)

# list의 요소에 접근
# list[index] index는 0부터시작
print(days_of_week[2])  # Wed출력

# list 안의 list(2중 list)도 가능
days_of_week.append(["kamja"])
print(days_of_week)

# list의 뒤에서부터 접근가능
# 즉, list[-1] = [kamja]출력
# 뒤에서부터 접근할 때는 -1부터 시작
print(days_of_week[-1])
