
class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.'* self.SIZE * self.SIZE) #['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self):
        # ㅡ 3줄
        # ㅣ 3줄
        # /  3줄
        #비기는 조건: 다 채워졌는데 위에것에 해당되지 않을때
        #즉 self.board에 . 이 없어야함
            return self.turn

        for x in range(1, self.board):
            return 'd' #draw

    def change_turn(self):
        pass



if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()
    game_engine.set(3, 2)
    game_engine.show_board()
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    print(game_engine.set_winner())
    game_engine.change_turn()
    print(game_engine.turn)



