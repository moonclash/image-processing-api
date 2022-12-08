import os
import re
import uuid
from datetime import datetime
from PIL import ImageFont
from ..services.image_processing_service import ImageProcessingService


class DateHelper(object):

    bulgarian_days = [
      'понеделник',
      'вторник',
      'сряда',
      'четвъртък',
      'петък',
      'събота',
      'неделя'
    ]

    @staticmethod
    def get_day():
        return datetime.today().weekday()
    
    @classmethod
    def get_day_in_bulgarian(cls):
        day = cls.get_day()
        return cls.bulgarian_days[day].capitalize()


class GoodMorningImage(object):

#  TODO - this is kinda shitty, clean it up
  @staticmethod
  def good_morningfy(image, file_name):
    image_processing_service = ImageProcessingService(image)
    static_dir = os.path.dirname(__file__)
    fonts_dir = os.path.join(static_dir, '../fonts/')
    images_dir = os.path.join(static_dir, '../images/')
    today_in_bulgarian = DateHelper.get_day_in_bulgarian()
    ext_regex = re.compile('\.[a-z]*', re.IGNORECASE)
    image_ext, *_ = re.findall(ext_regex, file_name)
    new_image_name = f'{str(uuid.uuid4())}{image_ext}'
    string_builder = f'Добро утро в {today_in_bulgarian}! \n Поднасям ви топло кафе и усмивки!'
    w, h = image_processing_service.get_image_dimensions()
    font_size = round(w / 17)
    font = ImageFont.truetype(os.path.join(fonts_dir, 'adantino.ttf'), font_size)
    font_options = {
        'font': font,
        'align': 'center',
        'embedded_color': True,
        'fill': (255,0,166),
        'stroke_fill': 'white',
        'stroke_width': 3 
    }
    
    image_processing_service.rotate_image_if_landscape()
    image_processing_service.adjust_contrast(3, new_image_name)
    image_processing_service.adjust_brightness(0.3, new_image_name)
    image_processing_service.add_text_to_image(string_builder, new_image_name, font_options)
    image_processing_service.add_text_to_image('www.dobroutro.net', new_image_name, {
      'fill': (255,255,255),
      'stroke_fill': 'black',
      'embedded_color': True,
      'align': 'center',
      'font': ImageFont.truetype(os.path.join(fonts_dir, 'poppins.ttf'), round(font_size / 2))
    },
    position='top'
    )
    image_processing_service.add_image_to_image(os.path.join(images_dir, 'coffee.png'), 'bottom right', new_image_name)
    image_processing_service.add_image_to_image(os.path.join(images_dir, 'jesus.png'), 'top left', new_image_name)
    image_processing_service.add_image_to_image(os.path.join(images_dir, 'rose.png'), 'bottom left', new_image_name)
    image_processing_service.resize_image(new_image_name)
    return new_image_name
    












