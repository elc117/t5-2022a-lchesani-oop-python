import random
from secrets import choice;
from Player import Player;
from Choice import Choice;







if __name__ == '__main__':
    computer = Player('pc');
    player = Player(input('Digite seu nome '));
    player.play = 0;
    choice = Choice(player, computer);
    while player.play in range(0, 3):
        computer.play = random.choice([0, 1, 2]);
        player.play = int(input('Rock[0], paper[1], scissors[2]! (anything diff to exit)'));
        r = choice.decide();
        if r == 'draw':
            print('draw');
        else:
            print(r + ' wins');