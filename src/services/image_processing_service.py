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

    def add_text_to_image(self, text: str, out_dir: str, font=None) -> None:
        font = font if font else None
        width, height = self.get_image_dimensions()
        drawer = ImageDraw.Draw(self.image)
        _, _, w, h = drawer.textbbox((0, 0), (text.encode('utf-8').decode('utf-8')), font=font)
        drawer.multiline_text(((width-w)/2, (height-h)/2), text, font=font, align='center', embedded_color=True, fill=(255,0,166))
        self.image.save(out_dir)
    
    def add_image_to_image(self, img, position: str, out_dir: str) -> None:
        img_to_paste = Image.open(img)
        x_pos, y_pos = self.calculate_sub_image_position(img_to_paste, position)
        self.image.paste(img_to_paste, (x_pos, y_pos), img_to_paste)
        self.image.save(out_dir)
