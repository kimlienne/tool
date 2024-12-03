from Main.connect import read_user_txt
from Utilizes.sentence import SentenceInfo
from Utilizes.var_manager import variable_manager as vm


class EnginUnderground:
    def __init__(self) -> None:
        self.next_sentence = SentenceInfo(0, '', '', '', '', '', '')
        self.current_sentence = SentenceInfo(0, '', '', '', '', '', '')
        self.previous_sentence = SentenceInfo(0, '', '', '', '', '', '')
        self.main_ui = None
        self.start_time = None
        self.end_time = None
        self.user = None

    def get_user(self):
        self.user = read_user_txt(vm.get_svm_value('knox_id'))
        vm.set_svm_value('knox_id', self.user.get('knox_id'))
        vm.set_ivm_value('start_index_info', self.user.get('start'))
        vm.set_ivm_value('end_index_info', self.user.get('end'))
        print(self.user)


eu = EnginUnderground()