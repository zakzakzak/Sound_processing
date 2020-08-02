import pydub
import numpy as np
from random import randint

def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

def write(f, sr, x, normalized=False):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")


sr, x = read('D:/boku no projecto/python/sound/sound1.wav')
# print(x)

x_baru = x.copy()
# for i in x:
#     print(i)
#
#     a = randint(-1000,1000)
#     b = randint(-1000,1000)
#     x_baru.append([i[0]+a, i[1]+b])
#

print(len(x))
# for i in range(10000, 500000):
#     print(x[i])
#
#     a = randint(-1000,1000)
#     b = randint(-1000,1000)
#     x_baru[i] = [x[i][0]+a, x[i][1]+b]
#
#
#
# print(x_baru)
# write('D:/boku no projecto/python/sound/out2.mp3', sr, x_baru)



# write
# write('out2.mp3', sr, x)
