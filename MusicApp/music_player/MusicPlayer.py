from music_player_properties.Model import Model
from music_player_properties.Song import Song


class MusicPlayer:

    def __int__(self, model_head):
        self._model_head = model_head

    def get_model_head(self):
        return self._model_head

    def set_model_head(self, model_head):
        self._model_head = model_head


