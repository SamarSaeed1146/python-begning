from typing import Optional

name: Optional[str] = "Samar"

if name is not None:
    print(name.upper())
else:
    print("name value is none")