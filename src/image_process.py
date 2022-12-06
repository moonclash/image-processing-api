from services.image_processing_service import ImageProcessingService
from services.file_io_service import FileIOService
from services.helper_services import DateHelper
import os
from PIL import ImageFont


today_in_bulgarian = DateHelper.get_day_in_bulgarian()
string_builder = f'Добро утро в {today_in_bulgarian}! \n Поднасям ви топло кафе и усмивки!'
font_size = round(len(string_builder) * 1.5)

image_processing_service = ImageProcessingService('test.jpeg')
image_processing_service.adjust_contrast(3, 'new.jpeg')
image_processing_service.adjust_brightness(0.3, 'new.jpeg')
image_processing_service.add_text_to_image(string_builder, 'new.jpeg', font=ImageFont.truetype(os.path.join('fonts', 'adantino.ttf'), font_size))
image_processing_service.add_image_to_image(os.path.join('images', 'coffee.png'), 'bottom right', 'new.jpeg')
image_processing_service.add_image_to_image(os.path.join('images', 'jesus.png'), 'top left', 'new.jpeg')
image_processing_service.add_image_to_image(os.path.join('images', 'rose.png'), 'bottom left', 'new.jpeg')
image_processing_service.resize_image('new.jpeg')

