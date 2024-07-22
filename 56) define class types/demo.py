

class My_class:
    def __init__(self, name:str) -> None:
        self.name = name

    def name_change(self,new_name:str) -> None:
        self.name = new_name 


Person: My_class = My_class("Samar Saeed")