class Model:
    def __init__(self, song):
        self._song = song
        self._prev_model = None
        self._next_model = None

    def get_song(self):
        return self._song

    def set_song(self, song):
        self._song = song

    def get_prev_model(self):
        return self._prev_model

    def set_prev_model(self, prev_model):
        self._prev_model = prev_model

    def get_next_model(self):
        return self._next_model

    def set_next_model(self, next_model):
        self._next_model = next_model
