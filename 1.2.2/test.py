# dictionary = {"name":12,"second":123}

# for i in range(len(dictionary)):
#     print(range(i+1))
list_num = [10,12,11]
player_score = 10
index = 0
for name in range(len(list_num)):
    if int(list_num[index]) <= player_score:
        break
    else:
        index += 1