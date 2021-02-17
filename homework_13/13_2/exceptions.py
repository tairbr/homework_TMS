class Layout_error(Exception):
    def __init__(self, mess='Поменяй раскладку клавиатуры'):
        super().__init__(mess)