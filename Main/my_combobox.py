from tkinter.ttk import Combobox


class MyCombobox(Combobox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_user_info = None
        self.current_index = 0

    def save_user_info(self, info):
        self.list_user_info = info
        print(self.list_user_info)
        if len(self.list_user_info) <= self.current_index:
            self.current_index = 0
        values = [item.get('assignment_detail') for item in info]
        self['values'] = values
        self.current(self.current_index)