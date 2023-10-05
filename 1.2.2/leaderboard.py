try:
    f = open("file.txt","r")
except:
    f = open("file.txt","x")
players = {}

# def get_player_data():
#     name = ""
#     score = ""
#     for line in f:
#         index = 0
#         while line[index] != ",":
#             name = name + line[index]
#             index += 1
#             if len(line) <= index:
#                 break
#         print(name)
#         players[name] = score
#         name = ""
#         score = ""
#     f.seek(0)
#     # for line in f:
#     #     index = 0
    
#     #     while line[index] :
#     #         score = score + line[index]
#     #         print(line[index])
#     #         index += 1
#     #         if len(line) <= index:
#     #             break
#     # print(score)
    
        




# get_player_data()
def get_player_data():
    for line in f:
        player = line.replace('\n',"").split(",")
        players[player[0]] = int(player[1])
    return(players)
