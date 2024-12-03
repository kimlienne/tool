import re
import os
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.font import Font
from tkinter.ttk import Notebook

from Main.back_end import eu
from Main.connect import read_user_txt

from Utilizes.var_manager import variable_manager as vm

class MainUI(Tk):
    def __init__(self):
        super().__init__()
        eu.main_ui = self

        self.title('Tone Tool')
        default_font = Font(family='Times New Roman', size=14)
        self.option_add("*Font", default_font)
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.config(family='Times New Roman', size=14)

        self.notebook = Notebook(self)
        self.notebook.grid(row = 0, column = 0)

        self.edit_text_tone = Frame()
        self.notebook.add(self.edit_text_tone, text='Chỉnh sửa tone')

        main_frame = Frame(self.edit_text_tone, highlightbackground='black', highlightthickness=1, padx = 10, pady = 10)
        main_frame.grid(row = 0, column = 0)
        main_frame.pack(padx = 10, pady = 10)

        user_frame = LabelFrame(main_frame, text='Thông tin user', padx = 10, pady = 10)
        user_frame.grid(row = 0, column = 0, sticky = W)


        Label(user_frame, text='Knox ID:').grid(row = 0, column = 0)
        knox_id_entry = Entry(user_frame, textvariable=vm.set_svm('knox_id', ''))
        knox_id_entry.grid(row = 0, column = 1, sticky = W)

        Button(user_frame, text='Load', command=lambda: eu.get_user()).grid(row = 0, column = 2)

        Label(user_frame, text='Bắt đầu: ').grid(row=1, column=0)
        Label(user_frame, textvariable=vm.set_ivm('start_index_info')).grid(row=1, column=1)
        Label(user_frame, text='Kết thúc: ').grid(row=1, column=2)
        Label(user_frame, textvariable=vm.set_ivm('end_index_info')).grid(row=1, column=3)
        Label(user_frame, text='Hiện tại: ').grid(row=1, column=4)
        Label(user_frame, textvariable=vm.set_ivm('current_index_info')).grid(row=1, column=5)

        hot_key_frame = LabelFrame(main_frame, text='Hướng dẫn điều khiển', padx = 10, pady = 10)
        hot_key_frame.grid(row=1, column=0)
        Label(hot_key_frame, text='- Enter để next').grid(row=0, column=0, sticky=W)
        Label(hot_key_frame, text='- F4 để back').grid(row=1, column=0, sticky=W)

        load_sentence_frame = LabelFrame(main_frame, text='Thông tin sentence', padx = 10, pady = 10)
        load_sentence_frame.grid(row = 2, column = 0, sticky = W)

        stt_frame = Frame(load_sentence_frame)
        stt_frame.grid(row=0, column=0, sticky=W)
        Label(stt_frame, text='Index', width=10).grid(row=0, column=0, sticky=W)
        index_entry = Entry(stt_frame, textvariable=vm.set_ivm('index_value', 1))
        index_entry.grid(row=0, column=1, sticky=W)

        sentence_frame = Frame(load_sentence_frame)
        sentence_frame.grid(row = 1, column = 0)

        Label(sentence_frame, text='Input', width=10).grid(row = 0, column = 0, sticky =W)
        self.input_area = Text(sentence_frame, wrap='word', width=100, height=5)
        self.input_area.grid(row = 0, column = 1, sticky = W, columnspan = 3)
        self.input_area.config(state='disabled')

        Label(sentence_frame, text='Professional', width=10).grid(row = 1, column = 0, sticky =W)
        self.professional_area = Text(sentence_frame, wrap='word', width=100, height=5)
        self.professional_area.grid(row=1, column=1, sticky=W, columnspan=3)



if __name__ == '__main__':
    MainUI().mainloop()
