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

im = Image.open("./7.jpeg")
im_new = expand2square(im, (0, 0, 0))
im_new.save('./new7.jpeg', quality=100)


# if __name__ == '__main__':
#     # 待修改尺寸的图片的路径
#     image_to_be_resized = sys.argv[1]
#     # 修改尺寸后保存图片的名称
#     image_to_be_saved = sys.argv[2]
