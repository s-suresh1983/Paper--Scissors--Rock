with open('player1.txt', 'r') as file1:
    player_1 = file1.readlines()
with open('player2.txt', 'r') as file2:
    player_2 = file2.readlines()
draws = 0
player_1_wins = 0
player_2_wins = 0
for i in range(len(player_1)):
    if player_1[i].strip() == player_2[i].strip():
        draws += 1
    elif player_1[i].strip() == 'R':
        if player_2[i].strip() == 'S':
            player_1_wins += 1
        elif player_2[i].strip() == 'P':
            player_2_wins += 1
    elif player_1[i].strip() == 'P':
        if player_2[i].strip() == 'R':
            player_1_wins += 1
        elif player_2[i].strip() == 'S':
            player_2_wins += 1
    elif player_1[i].strip() == 'S':
        if player_2[i].strip() == 'P':
            player_1_wins += 1
        elif player_2[i].strip() == 'R':
            player_2_wins += 1
with open('result.txt', 'w') as file3:
    file3.write('Player1 wins: ' + str(player_1_wins) + '\n')
    file3.write('Player2 wins: ' + str(player_2_wins) + '\n')
    file3.write('Draws: ' + str(draws) + '\n')
    