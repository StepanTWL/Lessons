s: int = 100#в vscode не работает
s = True
print(s)

def add_numbers(a:int, b:int) -> int:
    return a+b

add_numbers(False, True)
print(add_numbers.__annotations__)#{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

from typing import List, Any, Optional, Union

e: Any = 12
f: Optional[list] = None#или [1,23]
h: Union[str, int] = 12#или '12'   !!!!!для версий <3.10
#h: int | str = '12' #тоже самое что и выше для версий 3.10+
def list_upper(lst: List[str]):#проанонсировать коллекцию с указанием анотации ее элементов
    for elem in lst:
        print(elem.upper())