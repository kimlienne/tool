from tkinter import StringVar, IntVar


class VariableManager:
    string_var_manager = {}
    int_var_manager = {}

    def __init__(self):
        pass

    def set_svm(self, key, value) -> StringVar:
        if key in self.string_var_manager.keys():
            raise ValueError(f'Key {key} is existed')
        else:
            self.string_var_manager.update({key: StringVar(value=value)})
            return self.string_var_manager.get(key)

    def get_svm(self, key) -> StringVar:
        if key not in self.string_var_manager.keys():
            raise ValueError(f'Key {key} is not existed')
        else:
            return self.string_var_manager.get(key)

    def get_svm_value(self, key) -> str:
        if key not in self.string_var_manager.keys():
            raise ValueError(f'Key {key} is not existed')
        else:
            return self.get_svm(key).get()

    def set_svm_value(self, key, value) -> None:
        if key not in self.string_var_manager.keys():
            raise ValueError(f'Key {key} is not existed')
        else:
            self.get_svm(key).set(value)

    def set_ivm(self, key, value=0) -> IntVar:
        if key in self.int_var_manager.keys():
            raise ValueError(f'Key {key} is existed')
        else:
            self.int_var_manager.update({key: IntVar(value=value)})
            return self.int_var_manager.get(key)

    def get_ivm(self, key) -> IntVar:
        if key not in self.int_var_manager.keys():
            raise ValueError(f'Key {key} is not existed')
        else:
            return self.int_var_manager.get(key)

    def set_ivm_value(self, key, value) -> None:
        if key not in self.int_var_manager.keys():
            raise ValueError(f'Key {key} is not existed')
        else:
            self.int_var_manager.get(key).set(value)

    def get_ivm_value(self, key) -> int:
        if key not in self.int_var_manager.keys():
            raise ValueError(f'Key {key} is not existed')
        else:
            try:
                return self.int_var_manager.get(key).get()
            except Exception:
                print('Error when get IntVar. Return 0')
                return 0

    def __str__(self) -> str:
        return {'String variable': self.string_var_manager,
                'Int variable': self.int_var_manager}.__str__()


variable_manager = VariableManager()