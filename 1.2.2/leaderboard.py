try:
    f = open("file.txt","x")
except:
    f = open("file.txt","r")
players = {}


    
        




# get_player_data()
def check_file():
    lines_file = 0
    with open("file.txt","r") as f:
        for line in f:

            if len(line) > 1:
                lines_file += 1
    if lines_file == 0:
        raise Exception("NO PLAYER INFO")


def get_player_data():

    better_list = {}
    
    with open("file.txt","r") as f:

        for line in f:
            data = line.replace('\n',"").split(",")
            if data[0] in players:
                if int(data[1]) > players[data[0]]:
                    players[data[0]] = data[1]
            else:
                players[data[0]] = int(data[1])
        f.seek(0)
    biggest_num = 0
    biggest_name = ""

    for _ in range(len(players)):

        for player in players:
            if players[player] > biggest_num:
                biggest_num = players[player]
                biggest_name = player

        
        better_list.update({biggest_name:biggest_num})
        players.pop(biggest_name)
        biggest_num = 0

                
            


    return(better_list)

def set_new_player(name,points):
    amount_lines = 0
    length_line = 0
    with open("file.txt","r") as f:
        for line in f:
            amount_lines += 1
            length_line = len(line)
    if amount_lines <= 1 and length_line == 0:
        with open("file.txt","a") as f:
            info = f"{name},{points}"
            f.write(info)

    else:
        with open("file.txt","a") as f:
            info = f"\n{name},{points}"
            f.write(info)

# set_new_player("daviiiid",11)
get_player_data()