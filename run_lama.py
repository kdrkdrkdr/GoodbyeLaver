import requests
from PIL import Image
from os import listdir

def run_inpaint(image_path, mask_path, output_path):
    w, h = Image.open(image_path).size
    r = requests.post(
        url = 'http://127.0.0.1:5003/inpaint',
        files={
            'image':open(image_path, 'rb'),
            'mask':open(mask_path, 'rb'),
        },
        data={
            'ldmSteps':'50',
            'hdStrategy':'Resize',
            'hdStrategyCropMargin':'128',
            'hdStrategyCropTrigerSize':'2048',
            'hdStrategyResizeLimit':'2048',
            'sizeLimit': '%s' %(w if w>h else h),
        },
    )
    open(output_path, 'wb').write(r.content)


def make_mask(detected_image):
    img = Image.open(detected_image)
    img_pixels = img.load()
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img_pixels[i, j] == (0, 255, 0):
                img_pixels[i, j] = (255, 255, 255)
            else:
                img_pixels[i, j] = (0, 0, 0)
                
    mask_fname = '%s_mask.png' %detected_image[:-4]
    img.save(mask_fname)
    return mask_fname






if __name__ == '__main__':

    for i in listdir('/content/image_detected/'):
        mask = make_mask(f'/content/image_detected/{i}')
        print('mask 완료')

        run_inpaint(
            image_path=f'/content/image_original/{i}',
            mask_path=mask,
            output_path=f'/content/image_uncensored/{i}'
        )
        print('inpaint 완료')
