from typing import Callable

def my_func(name:str,age:int) -> str:
    return name

a: Callable[[str,int],str] = my_func

def abc() -> None:
    print("Hello One")

b: Callable = abc