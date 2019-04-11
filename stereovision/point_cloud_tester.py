from stereovision.stereo_cameras import StereoPair
from stereovision.stereo_cameras import CalibratedPair
from stereovision.calibration import StereoCalibration as StereoCalibration

calibration = StereoCalibration(input_folder="calib")

if calibration:
    calibration.export("calibrated_cameras")
