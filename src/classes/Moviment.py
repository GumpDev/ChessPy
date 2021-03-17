from ursina import *

class SquareView(Entity):
    def __init__(self, position, board):
        super().__init__(
            parent=board.board_parent,
            origin=(-.5,.5),
            color=color.yellow.tint(.5),
            position=(position[0]+.5,position[1]-.5),
            model='quad',
            texture='white_cube',
            scale=(1, 1),
            z = -.05
        )

class SquaresView():
    views = []
    
    def __init__(self, type, position, board, direction_piece):
        if type == 'pawn':
            if position[1] == -6 or position[1] == -1:
                self.views.append(SquareView(
                    board=board,
                    position=(position[0],position[1]+direction_piece*2)
                ))
            self.views.append(SquareView(
                board=board,
                position=(position[0],position[1]+direction_piece)
            ))
    
    def destroy(self):
        for view in self.views:
            view.disable()