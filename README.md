# instagram_image_padding
Pad images to square ratio for instagram

# How to run the code?
- Make sure you have python;
- install pillow `pip install pillow` ;
- Update 2021/11/05 23:00
  - Run the code in command line with `python instagram_resize.py <folder_of_the_images_on_your_pc> <image_to_be_resized > <output_image_name>`, e.g. `python instagram_resize.py . test.jpg output.jpg` will run the code and resize the image `test.png` and save the padded image with the name of `output.png`. Both images are in the same folder as the python file.
  - The code will pad the image with black background color (R: 0, G:0, B:0). You can change to your fav color in the second last line of the code `im_new = expand2square(im, (0, 0, 0))` 
- Update 2021/11/05 22:45
  - Change the name of input and output image;
  - Run the code in command line with `python instagram_resize.py`

