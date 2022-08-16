from Player import Player;

class Choice(object):
    def __init__(self, player1, player2):
        self.player1 = player1;
        self.player2 = player2;
    
    def decide(self):
        c = [self.player1.play, self.player2.play];
        rock_paper = [0, 1];
        rock_scissors = [0, 2];
        paper_scissors = [1, 2];
        if c == rock_paper or c == rock_paper[::-1]: #[::-1] significa que eu estou pegando a lista ao contrário
            return self.player1.name if self.player1.play == 1 else self.player2.name;
        if c == rock_scissors or c == rock_scissors[::-1]:
            return self.player1.name if self.player1.play == 0 else self.player2.name;
        if c == paper_scissors or c == rock_scissors[::-1]:
            return self.player1.name if self.player1.play == 2 else self.player2.name;
        return 'draw';