import random;


def choices(player, computer):
    c = [player, computer];
    rock_paper = [0, 1];
    rock_scissors = [0, 2];
    paper_scissors = [1, 2];
    if c == rock_paper or c == rock_paper[::-1]: #[::-1] significa que eu estou pegando a lista ao contrário
        return 'player' if player == 1 else 'computer';
    if c == rock_scissors or c == rock_scissors[::-1]:
        return 'player' if player == 0 else 'computer';
    if c == paper_scissors or c == rock_scissors[::-1]:
        return 'player' if player == 2 else 'computer';
    return 'draw';
    
if __name__ == '__main__':
    playersChoice = 0;
    while playersChoice in range(0, 3):
        playersChoice = int(input('Rock[0], paper[1], scissors[2]! (anything diff to exit)'));
        computersChoice = random.choice([0, 1, 2]);
        r = choices(playersChoice, computersChoice);
        if r == 'draw':
            print('draw');
        else:
            print(r + ' wins');