from PIL import Image, ImageDraw, ImageEnhance

class ImageProcessingService(object):

    def __init__(self, image) -> None:
        self.image = Image.open(image)
        
    def get_image_dimensions(self):
        return self.image.size
    
    def calculate_sub_image_position(self, sub_image, position: str):
        width, height = self.get_image_dimensions()
        w, h = sub_image.size
        x_pos = y_pos = 0
        if position == 'top left':
            x_pos = round(width / w)
            y_pos = round(height / h)
        if position == 'bottom right':
            x_pos = round((width - w))
            y_pos = round((height - h))
        if position == 'bottom left':
           x_pos = round(width / w)
           y_pos = round(height - h)
        return (x_pos, y_pos)

    def adjust_contrast(self, value: int, out_dir: str) -> None:
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(value)
        self.image.save(out_dir)
    
    def adjust_brightness(self, value: int, out_dir: str) -> None:
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(value)
        self.image.save(out_dir)

    def add_text_to_image(self, text: str, out_dir: str, font_options) -> None:
        width, height = self.get_image_dimensions()
        drawer = ImageDraw.Draw(self.image)
        textbox = drawer.textbbox((10, 10), text, font_options.get('font'))
        _, _, w, h = textbox
        drawer.multiline_text(((width - w) / 2, (height - h) / 2), text, **font_options)
        self.image.save(out_dir)
    
    def add_image_to_image(self, img, position: str, out_dir: str) -> None:
        img_to_paste = Image.open(img)
        width, height = self.get_image_dimensions()
        img_to_paste = img_to_paste.resize((round(width / 4), round(height / 4)))
        x_pos, y_pos = self.calculate_sub_image_position(img_to_paste, position)
        self.image.paste(img_to_paste, (x_pos, y_pos), img_to_paste)
        self.image.save(out_dir)
    
    def resize_image(self, out_dir):
        width, height = self.get_image_dimensions()
        w = round(width / 2)
        h = round(height / 2)
        self.image = self.image.resize((w, h), Image.ANTIALIAS)
        self.image.save(out_dir, optimize=True, quality=95)

