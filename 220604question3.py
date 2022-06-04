# 질문 print_board 이쁘게 출력이 안되서 물어봄
from typing import List, Tuple, Optional
# 현욱


class Board:
    def __init__(self, size: int = 15):
        self.size: int = size
        self.board: List[List[int]] = [[0] * size for i in range(size)]
        self.whites: List[Tuple[int, int]] = []
        self.blacks: List[Tuple[int, int]] = []

    def add_stone(self, coor: Tuple[int, int], color: str) -> None:
        if coor in self.whites + self.blacks:
            print('이미돌이 놓여 있습니다 다시 입력하세요')
            return
        elif (len(self.whites) + len(self.blacks) % 2 == 1):
            if color == 'white':
                self.whites.append(coor)
                self.board[coor[0]][coor[1]] = 2
            else:
                print('다시 입력하세요 : White 차례입니다')

        elif (len(self.whites) + len(self.blacks) % 2 == 0):
            if color == 'black':
                self.blacks.append(coor)
                self.board[coor[0]][coor[1]] = 1
            else:
                print('다시 입력하세요 : black 차례입니다')

    def stones_in_a_row(self, cont: int) -> Optional[str]:
        for i in range(self.size):
            for j in range(self.size):

                temp = []  # 가로
                for k in range(cont):
                    temp.append((i, j + k))
                flag_blacks = True
                flag_whites = True
                for x in temp:
                    if not x in self.blacks:
                        flag_blacks = False
                    if not x in self.whites:
                        flag_whites = False
                if flag_blacks:
                    return 'black win'
                elif flag_whites:
                    return 'white win'

                temp = []  # 세로
                for k in range(cont):
                    temp.append((i+k, j))
                flag_blacks = True
                flag_whites = True
                for x in temp:
                    if not x in self.blacks:
                        flag_blacks = False
                    if not x in self.whites:
                        flag_whites = False
                if flag_blacks:
                    return 'black win'
                elif flag_whites:
                    return 'white win'

                temp = []  # 대각위로
                for k in range(cont):
                    temp.append((i-k, j+k))
                flag_blacks = True
                flag_whites = True
                for x in temp:
                    if not x in self.blacks:
                        flag_blacks = False
                    if not x in self.whites:
                        flag_whites = False
                if flag_blacks:
                    return 'black win'
                elif flag_whites:
                    return 'white win'

                temp = []  # 대각아래로
                for k in range(cont):
                    temp.append((i+k, j+k))
                flag_blacks = True
                flag_whites = True
                for x in temp:
                    if not x in self.blacks:
                        flag_blacks = False
                    if not x in self.whites:
                        flag_whites = False
                if flag_blacks:
                    return 'black win'
                elif flag_whites:
                    return 'white win'

    def __str__(self):
        result = ''
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in self.whites:
                    result += 'o '
                elif (i, j) in self.blacks:
                    result += 'x '
                else:
                    result += '. '
            result += '\n'
        return result

    def print_board(self):
        print(self)


s = Board()
s.add_stone((1, 3), 'black')
s.print_board()  # print된 보드출력 / () <- 이거안주면 함수주소나옴
s.board  # s.board = self.board 출력됨 리스트 원본나옴
# s.blacks 나 s.whites 하면 self.blacks 랑 self.whites 원본나옴
