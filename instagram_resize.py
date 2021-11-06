import sys
from PIL import Image

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

if __name__ == '__main__':
    # folder of the images you want to pad
    folder = sys.argv[1]
    # filename of the image you want to change ratio
    image_to_be_resized = folder + "/" + sys.argv[2]
    # filename of the output image
    image_to_be_saved = folder + "/" +  sys.argv[3]

    # function calls
    im = Image.open(image_to_be_resized)
    im_new = expand2square(im, (0, 0, 0))
    im_new.save(image_to_be_saved, quality=100)
