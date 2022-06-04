# 파이썬 typing modul

from typing import List, Dict, Tuple, Set, Optional, Union
nums: List[int] = [1, 2, 3]

print(nums)

countries: Dict[str, str] = {'KR': 'South Korea',
                             'US': 'United states', 'CN': 'China'}
print(countries)

user: Tuple[int, str, bool] = (3, 'Dale', True)
print(user)

chars: Set[str] = {'a', 'b', 'c'}
print(chars)

# Union 여러개의 타입이 허용될수있는 상황에서 사용


def toString(num: Union[int, float]) -> str:
    return str(num)


toString(1)  # -> '1'
toString(1.5)  # -> '1.5'

# None이 허용되는 함수의 매개변수에 대한 타입을 명시할때 사용


def repeat(message: str, times: Optional[int] = None) -> list:
    if times:
        return [message] * times
    else:
        return [message]

# Optional[int] 랑 Union[int, None] 은 같은 효력이다
# Optional은 None이 나올수있는 ? 상황에 고려해서 사용한다
