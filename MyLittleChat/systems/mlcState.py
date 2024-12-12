import reflex as rx

class State(rx.State):
    
    create_form: dict = {}

    num: int
    num_list = [3, 2, 1]

    def add_num(self):
        self.num_list.insert(0, self.num)
    def set_num(self, val):
        self.num = val