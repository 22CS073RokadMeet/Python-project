class Guesser:
    def guessing_number(self):
        print("Guesser kindly guess the Number")
        guess_num = int(input())
        return guess_num

class Player:
    def guessing_number(self):
        print("Player kindly guess the Number")
        guess_num = int(input())
        return guess_num

class Umpire:
    def __init__(self):
        self.num_from_guesser = 0
        self.num_from_player1 = 0
        self.num_from_player2 = 0
        self.num_from_player3 = 0

    def collect_num_from_guesser(self):
        g = Guesser()
        self.num_from_guesser = g.guessing_number()

    def collect_num_from_players(self):
        p1 = Player()
        p2 = Player()
        p3 = Player()
        self.num_from_player1 = p1.guessing_number()
        self.num_from_player2 = p2.guessing_number()
        self.num_from_player3 = p3.guessing_number()

    def compare(self):
        player1 = 0
        player2 = 0
        player3 = 0

        if self.num_from_guesser == self.num_from_player1:
            if self.num_from_guesser == self.num_from_player2 and self.num_from_guesser == self.num_from_player3:
                print("Sab ne sahi ans diya!Sab winner hain!")
                player1 += 1
                player2 += 1
                player3 += 1
            elif self.num_from_guesser == self.num_from_player2:
                print("Player1 aur Player2 jeet gaye!")
                player1 += 1
                player2 += 1
            elif self.num_from_guesser == self.num_from_player3:
                print("Player1 aur Player3 jeet gaye!")
                player1 += 1
                player3 += 1
            else:
                print("Player1 won the game")
                player1 += 1
        elif self.num_from_guesser == self.num_from_player2:
            if self.num_from_guesser == self.num_from_player3:
                print("Player2 aur Player3 won the game")
                player2 += 1
                player3 += 1
            else:
                print("Player2 won the game")
                player2 += 1
        elif self.num_from_guesser == self.num_from_player3:
            print("Player3 won the game")
            player3 += 1
        else:
            print("Sab ka sab galat hain.App game har gaye!!")

        print("Score of player1 :", player1)
        print("Score of player2 :", player2)
        print("Score of player3 :", player3)

def guesser_game():
    print("Game Started")
    u = Umpire()
    u.collect_num_from_guesser()
    u.collect_num_from_players()
    u.compare()

if __name__ == "__main__":
    guesser_game()


print("This project is made by 22CS073")