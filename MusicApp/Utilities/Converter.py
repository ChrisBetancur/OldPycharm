import math

def get_song_length_str(seconds):
    arr = seconds_to_min(seconds)
    if arr[1] < 10:
        return str(arr[0]) + ":0" + str(arr[1])
    return str(arr[0]) + ":" + str(arr[1])

def seconds_to_min(seconds):
    rounded_seconds = round(seconds)
    minutes = rounded_seconds / 60
    minutes = math.floor(minutes)
    remaining = rounded_seconds % 60
    return (minutes, remaining)


def calculate_ratio_milliseconds(song, image):
    #print(image.get_rect().size[0], ":", song.get_song_length())
    dimensions = image.get_rect().size
    width_of_image = dimensions[0]
    song_length = song.get_song_length() * 1000

    ratio_image_to_song = width_of_image / song_length

    return ratio_image_to_song
