from detector import Detector

d = Detector('weights.h5')
d.run_on_folder(
    input_folder='.\\gray_scale\\',
    output_folder='./gray_scale_detected/', 
    is_video=False, 
    is_mosaic=False,
    dilation=3
)