from ursina import *

class Piece(Button):
    def __init__(self, board, color, type, position):
        super().__init__(
            parent=board,
            origin=(-.5,.5),
            color=color,
            position=(position[0],-position[1]),
            texture=load_texture(f'../textures/{type}.jpg'),
            highlight_color = self.color.tint(.3)
        )

class Board(Entity):
    Types = [
        'none',
        'pawn'
    ]
    
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            origin=(-.5,.5),
            position=(-.5,.5),
            texture='white_cube',
            texture_scale=(8,8),
            color=color.dark_gray,
        )
        self.pieces = [
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0]
        ]
        self.flipedTable = random.random() * 2 >= 1;
        self.board_parent = Entity(parent=self, scale=(1/8,1/8))
        self.mountBoard()
    
    def firstColor(self):
        return color.white if self.flipedTable else color.black
    def secondColor(self):
        return color.white if not self.flipedTable else color.black
    
    def mountBoard(self):
        for y in range(len(self.pieces)):
            for x in range(len(self.pieces[y])):
                if self.pieces[y][x] != 0:
                    piece = Piece(
                        board = self.board_parent,
                        color= self.firstColor() if y > 3 else self.secondColor(), 
                        type= Board.Types[self.pieces[y][x]], 
                        position = (x,y)
                    )
                    self.pieces[y][x] = piece
        print(self.pieces)