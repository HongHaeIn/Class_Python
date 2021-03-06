import tkinter

from tictactoe_game_engine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine
        self.init_GUI()


    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.TK()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}')
        self.root.resizable(width=False, height=False)

    def click_handler(self, event):
        pass

    def draw_board(self):
        pass

if __name__ == '__main':
    ttt_GUI = TictactoeGUI
