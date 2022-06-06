def get_calendar(days: int, start_day: str) -> str:
    A = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    if not start_day in A:
        raise Exception(f'이상한 요일이 들어옴 {strat_day}')

    calendar_str = 'Sun Mon Tue Wed Thu Fri Sat\n'
    first_week = ''
    second_week_start = 0

    if start_day == 'Sun':
        first_week = '1   2   3   4   5   6   7   '
        second_week_start = 8
    elif start_day == 'Mon':
        first_week = '    1   2   3   4   5   6   '
        second_week_start = 7
    elif start_day == 'Tue':
        first_week = '        1   2   3   4   5   '
        second_week_start = 6
    elif start_day == 'Wed':
        first_week = '            1   2   3   4   '
        second_week_start = 5
    elif start_day == 'Thu':
        first_week = '                1   2   3   '
        second_week_start = 4
    elif start_day == 'Fri':
        first_week = '                    1   2   '
        second_week_start = 3
    elif starat_day == 'Sat':
        first_week = '                        1   '
        second_week_start = 2
    else:
        raise Exception(' 에 러 ')
    calendar_str = calendar_str + first_week + '\n'

    count = 0
    for i in range(second_week_start, days + 1):
        if i >= 10:
            calendar_str = calendar_str + str(i) + '  '
            print(f'달력 10이상 숫자 {i}')
        else:
            calendar_str = calendar_str + str(i) + '   '
            print(f'달력 10미만 숫자 {i}')

        count += 1
        print(f'count의 현재 개수 세기 {count}')
        if count >= 7:
            calendar_str = calendar_str + '\n'
            count = 0
            print(f'count 의 초기화 {count}')

    return calendar_str


january2022 = get_calendar(32, 'Mon')
print(january2022)


# 아래와 같은 리스트를 반환
# ex) n = 5
# [
#     [1, 2, 3, 4, 5],
#     [16, 0, 0, 0, 6],
#     [15, 0, 0, 0, 7],
#     [14, 0, 0, 0, 8],
#     [13, 12, 11, 10, 9]
# ]
def bingle(n: int) -> list:
    result = []
    for i in range(n):
        result.append([0] * n)

    cur_number = 1
    for i in range(n):  # 5개 0 1 2 3 4
        result[0][i] = cur_number
        cur_number += 1
    for i in range(1, n):  # 4개 1 2 3 4
        result[i][n-1] = cur_number
        cur_number += 1
    for i in range(n-2, -1, -1):  # 4개 3 2 1 0
        result[n-1][i] = cur_number
        cur_number += 1
    for i in range(n-2, 0, -1):  # 3개 3 2 1
        result[i][0] = cur_number
        cur_number += 1

    return result


bb = bingle(5)
print(bb)


def bubble_sort(lst):  # 모든정렬은 오름차순
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] < lst[j]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp


a = [2, 5, 1, 6]
bubble_sort(a)
print(a)

# bubble sort 시간복잡도 o n^2
# 서로 인접한 두 원소를 검사하여 정렬 하는 알고리즘


def selection_sort(lst):  # [2,5,1,6]
    for i in range(len(lst)):  # i = 0 1 2 3
        minimum = lst[i]  # lst 첫 위치부터 끝까지
        index = i  # 0 1 2 3

        for j in range(i+1, len(lst)):  # 1부터 4까지 / j = 1 2 3
            if minimum > lst[j]:  # lst 첫번째 원소부터 두번째 원소비교 / 결국엔 다비교
                minimum = lst[j]  # 최소값을 첫번째 원소에 넣어줌 현상태 [1,5,2,6]
                index = j  # 여기 까지 왔다는건 j = 2

        temp = lst[i]
        lst[i] = lst[index]
        lst[index] = temp


b = [2, 5, 1, 6]
selection_sort(b)
print(b)

# 선택정렬 시간복잡도 o(n^2)
# 첫번째 순서에는 첫번째 위치에 가장 최솟값넣고
# 두번째 순서에는 두번째 위치에 남은 값중에서의 최솟값 넣는다
