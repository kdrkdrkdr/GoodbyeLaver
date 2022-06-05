from detector import Detector

d = Detector('weights.h5')
d.run_on_folder(
    input_folder='/content/image_original/',
    output_folder='/content/image_detected/', 
    is_video=False, 
    is_mosaic=False,
    dilation=3
)