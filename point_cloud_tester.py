from stereovision.stereo_cameras import StereoPair
from stereovision.stereo_cameras import CalibratedPair
from stereovision.calibration import StereoCalibration as StereoCalibration
from stereovision.blockmatchers import BlockMatcher as Blockmatcher
from pathlib import Path

file_path = '~/StereoVision/calib'

calibration = StereoCalibration(input_folder=file_path)

devices = (1, 2)
st_pair = StereoPair(devices)
bl_match = Blockmatcher(calibration)
cal_pair = CalibratedPair(st_pair, calibration, bl_match)

if calibration:
    calibration.export("calibrated_cameras")
