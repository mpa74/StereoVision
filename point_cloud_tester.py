from stereovision.stereo_cameras import StereoPair
from stereovision.stereo_cameras import CalibratedPair
from stereovision.calibration import StereoCalibration
from stereovision.blockmatchers import StereoBM
import numpy as np


# NOTE: INCLUDED CALIB FILES ARE FOR THE (LEFT, RIGHT) STEREOPAIR.
#       DO NOT USE (LEFT, CENTER)

# camera numbers
devices = (1, 2)
st_pair = StereoPair(devices)
st_bm = StereoBM(stereo_bm_preset=.0, search_range=80, window_size=21, settings=None)
load_calib = StereoCalibration(st_pair, input_folder='calib_leftright')
cal_pair = CalibratedPair(devices, load_calib, st_bm)

cal_pair.live_point_cloud(devices)
np.save("cloudtest.npy", np.ndarray(cal_pair.live_point_cloud(devices)))
