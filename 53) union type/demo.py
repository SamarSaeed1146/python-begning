from typing import List, Union

a: List[Union[str,int]] = ["Samar", "One", 100]

b: List[str | int | List[str | int]] = ["Samar", "One", 100, ["Samar", "One", 100]]