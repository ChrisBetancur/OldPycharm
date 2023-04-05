class Playlist:
    def __init__(self, playlist_name):
        self._playlist_name = playlist_name
        self._song_list = []
        self._shuffled_playlist = []

    def get_playlist_name(self):
        return self._playlist_name

    def set_playlist_name(self, playlist_name):
        self._playlist_name = playlist_name

    def get_playlist_size(self):
        return self._playlist_size

    def set_playlist_size(self, playlist_size):
        self._playlist_size = playlist_size

    def get_song_list(self):
        return self._song_list

    def set_song_list(self, play_list):
        self._song_list = play_list

    def get_shuffled_playlist(self):
        return self._shuffled_playlist

    def set_shuffled_playlist(self, shuffled_playlist):
        self._shuffled_playlist = shuffled_playlist
