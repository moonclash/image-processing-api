import os
from datetime import datetime
from PIL import ImageFont
from services.image_processing_service import ImageProcessingService


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
  
  @staticmethod
  def good_morningfy(image):
    today_in_bulgarian = DateHelper.get_day_in_bulgarian()
    string_builder = f'Добро утро в {today_in_bulgarian}! \n Поднасям ви топло кафе и усмивки!'
    font_size = round(len(string_builder) * 1.5)
    font = ImageFont.truetype(os.path.join('fonts', 'adantino.ttf'), font_size)
    font_options = {
        'font': font,
        'align': 'center',
        'embedded_color': True,
        'fill': (255,0,166),
        'stroke_fill': 'white',
        'stroke_width': 3 
    }
    image_processing_service = ImageProcessingService(image)
    image_processing_service.adjust_contrast(3, 'new.jpeg')
    image_processing_service.adjust_brightness(0.3, 'new.jpeg')
    image_processing_service.add_text_to_image(string_builder, 'new.jpeg', font_options)
    image_processing_service.add_image_to_image(os.path.join('images', 'coffee.png'), 'bottom right', 'new.jpeg')
    image_processing_service.add_image_to_image(os.path.join('images', 'jesus.png'), 'top left', 'new.jpeg')
    image_processing_service.add_image_to_image(os.path.join('images', 'rose.png'), 'bottom left', 'new.jpeg')
    image_processing_service.resize_image('new.jpeg')
    












