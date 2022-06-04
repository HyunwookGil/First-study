# 질문 프로그램 실행시 종료 시키고싶을때 컨+c로 종료가능하나 안되서 질문함
import sys
from typing import List, Tuple, Optional


class Board:
    def __init__(self, size: int = 15):
        self.size: int = size
        self.board: List[List[int]] = [[0] * size for i in range(size)]
        self.whites: List[Tuple[int, int]] = []
        self.blacks: List[Tuple[int, int]] = []

    def start(self):
        self.board[7][7] = 1

    def add_stone(self, coor: Tuple[int, int], color: str) -> None:
        if coor in self.whites + self.blacks:
            print('이미 돌이 놓여 있습니다 다시 입력하세요')
            return
        if (len(self.whites) + len(self.blacks)) % 2 == 1:
            if color == 'white':
                self.whites.append(coor)
                self.board[coor[0]][coor[1]] = 2
            else:
                print('다시 입력 하세요 : WHITE 차례 입니다')

        elif (len(self.whites) + len(self.blacks)) % 2 == 0:
            if color == 'black':
                self.blacks.append(coor)
                self.board[coor[0]][coor[1]] = 1
            else:
                print('다시 입력 하세요 : BLACK 차례 입니다')

    def stones_in_a_row(self, cont: int) -> Optional[str]:
        for i in range(self.size):
            for j in range(self.size):
                temp = []  # 가로
                for k in range(cont):
                    temp.append((i, j + k))  # 가로부터 쭉 확인
                    # i줄에 j번째 위치 쭉 확인
    # temp의 모든원소가 blacks whites 안에 있는지 확인
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
                    temp.append((i + k, j))
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
                    result = result + 'o '
                elif (i, j) in self.blacks:
                    result = result + 'x '
                else:
                    result = result + '. '
            result = result + '\n'

        return result

    # 6목 감지하는 메서드 하나 만들기
    # 흑색돌 하나를 지정해서 하 우 상하 하우 4방향 확인
    def sixmok_check(self, cont: int = 6):
        for i in range(self.size):
            for j in range(self.size):
                temp = []  # 가로
                for k in range(cont):
                    temp.append((i, j + k))  # 가로부터 쭉 확인
                    # i줄에 j번째 위치 쭉 확인
    # temp의 모든원소가 blacks whites 안에 있는지 확인
                flag_blacks = True
                for x in temp:
                    if not x in self.blacks:
                        flag_blacks = False
                if flag_blacks:
                    return flag_blacks

                temp = []  # 세로
                for k in range(cont):
                    temp.append((i + k, j))
                flag_blacks = True
                for x in temp:
                    if not x in self.blacks:
                        flag_blacks = False
                if flag_blacks:
                    return flag_blacks

                temp = []  # 대각위로
                for k in range(cont):
                    temp.append((i-k, j+k))
                flag_blacks = True
                for x in temp:
                    if not x in self.blacks:
                        flag_blacks = False
                if flag_blacks:
                    return flag_blacks

                temp = []  # 대각아래로
                for k in range(cont):
                    temp.append((i+k, j+k))
                flag_blacks = True
                for x in temp:
                    if not x in self.blacks:
                        flag_blacks = False
                if flag_blacks:
                    return flag_blacks
        return False


class Game:
    def __init__(self):
        # 오목판의 국제규격은 15 * 15
        self.board = Board()

        # 코드 짜다가 필요한 거 있으면 알아서 더 추가하기

    ############################################
    # 코드짜다가 필요한 함수 있으면 알아서 바꾸거나 더 추가하기
    ############################################

    def init_board(self):
        self.board = Board()
        self.whites = []
        self.blacks = []

    def __str__(self):
        return str(self.board)

    def print_board(self):
        print(self.board)

    def put_stone(self, location: Tuple[int, int]) -> None:  # 돌을 그자리에 놓는 함수
        if (len(self.board.whites) + len(self.board.blacks)) % 2 == 0:
            self.board.add_stone(location, 'black')

        elif (len(self.board.whites) + len(self.board.blacks)) % 2 == 1:  # 백돌
            self.board.add_stone(location, 'white')

    def is_finish(self):  # 게임이 끝났는지 확인하는 함수
        winner = self.board.stones_in_a_row(5)
        if winner == 'black win' or winner == 'white win':
            return True
        return False

    def remove_stone(self, location: Tuple[int, int]) -> None:
        if location in self.board.blacks:
            self.board.blacks.remove(location)
        elif location in self.board.whites:
            self.board.whites.remove(location)

    def remove_last_stone(self):
        if (len(self.board.whites) + len(self.board.blacks)) % 2 == 1:
            self.board.blacks.pop()
        else:
            self.board.whites.pop()

    def start_game(self):
        self.init_board()  # 초기화
        while not self.is_finish():
            self.print_board()

            try:
                location = input("돌의 위치를 입력하세요")
                print(location)
                if location == 'exit':
                    print('종료할끄야~')
                    return

                location = location.split(',')
                location = tuple(list(map(lambda x: int(x), location)))
                self.put_stone(location)
                is_six = self.board.sixmok_check()
                print(is_six)
                if is_six and (len(self.board.blacks) + len(self.board.whites)) % 2 == 1:
                    print('6목방지')
                    self.remove_stone(location)
                    raise Exception()

            except:
                print('잘못 입력 했습니다 다시 입력 하세요')

#             1. 사용자의 인풋을 받고 : input함수를 사용하도록 한다. 인풋을 받는 방식은 자율(ex. '1 1'로 받아도 되고, '1, 1'로 받아도 되고 )
#             2. 이상한 인풋이면 다시 인풋을 받고 : -1, -1과 같은 이상한 인풋이 주어졌을 때,
#             3. 매 순간 q를 입력받으면 게임을 종료할 수 있도록 한다.
        winner = self.board.stones_in_a_row(5)
        self.print_board()
        print(winner)


gomok = Game()
gomok.start_game()

# 프로그램종료가 안된 이유는 try ~ except 구문때문이다 전부 예외처리로 되서 컨+c가안먹음
