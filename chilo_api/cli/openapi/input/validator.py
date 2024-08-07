import os


class InputValidator:
    
    def validate_arguments(self, input_args):
        self.__check_directory(input_args.output)

    def __check_directory(self, possible_dir):
        if not os.path.exists(possible_dir):
            raise Exception(f'{possible_dir} is not a valid directory path')
