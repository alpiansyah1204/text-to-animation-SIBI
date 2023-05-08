import imageio.v3 as iio
import numpy as np

# make sure pyav is installed (pip install av)

frames = np.vstack([
    iio.imread(
        "a.mp4",
        plugin="pyav",
        # normalize the GIF to 50 FPS
        filter_sequence=[("fps", "24")]
    ),
    # iio.imread(
    #     "testing_2.gif",
    #     plugin="pyav",
    #     # normalize the GIF to 50 FPS
    #     filter_sequence=[("fps", "50")]
    # ),
])

iio.imwrite("a.gif", frames, duration=20)