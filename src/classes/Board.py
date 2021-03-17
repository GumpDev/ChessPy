from ursina import *
from src.classes.Moviment import SquaresView
class Piece(Draggable):
    def __init__(self, board, _color, type, position):
        super().__init__(
            parent=board.board_parent,
            origin=(-.7,.625),
            color=color.white,
            position=(position[0],-position[1]),
            texture=load_texture(f'../textures/{type}_{_color}.png'),
            scale=(.7, .8),
            highlight_color = self.color.tint(.3),
            z = -.1
        )
        self.type = type
        self.piece_color = _color
        self.startPosition = (self.x,self.y)
        self.direction_piece = 1 if self.y <= -6 else -1
        self.view = SquaresView(
            type="",
            position=(position[0],-position[1]),
            direction_piece=self.direction_piece,
            board=board
        )
        
        def hide():
            if(self.view):
                self.view.destroy()
        
        def show():
            if(board.turn == self.piece_color): 
                hide()
                
                self.view = SquaresView(
                    type=type,
                    position=(position[0],-position[1]),
                    board=board,
                    direction_piece=self.direction_piece
                )
            
        self.on_click = show
        
        def drop():
            if(board.turn == self.piece_color):   
                self.x = round(self.x)
                self.y = round(self.y)
                if not self.startPosition == (round(self.x), round(self.y)):
                    self.startPosition = (self.x,self.y)
                    board.turn = 'white' if self.piece_color == 'black' else 'black'
                    hide()
            else:
                self.x = self.startPosition[0]
                self.y = self.startPosition[1] 
            
        self.drop = drop

class Board(Entity):
    Types = [
        'none',
        'pawn',
        'bishop',
        'knight',
        'rook',
        'queen',
        'king'
    ]
    turn = 'white'
    
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            origin=(-.5,.5),
            position=(-.5,.5),
            texture=load_texture(f'../textures/board.png'),
            texture_scale=(4,4),
            color=color.white
        )
        self.pieces = [
            [4,3,2,5,6,2,3,4],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [4,3,2,5,6,2,3,4]
        ]
        self.flipedTable = random.random() * 2 >= 1;
        self.board_parent = Entity(parent=self, scale=(1/8,1/8))
        self.mountBoard()
    
    def firstColor(self):
        return 'white' if self.flipedTable else 'black'
    def secondColor(self):
        return 'white' if not self.flipedTable else 'black'
    
    def mountBoard(self):
        for y in range(len(self.pieces)):
            for x in range(len(self.pieces[y])):
                if self.pieces[y][x] != 0:
                    self.pieces[y][x] = Piece(
                        board = self,
                        _color= self.firstColor() if y > 3 else self.secondColor(), 
                        type= Board.Types[self.pieces[y][x]], 
                        position = (x,y)
                    )
                else:
                    self.pieces[y][x] = False