import math
from PIL import ImageFont, ImageDraw, Image

class draw_somethig_to_pic:

    def __init__(self, raw_image_name):
        self.raw_image_name = raw_image_name
        self.fillcolor = '#ff0000'
        self.font_color = '#ffffff'

    def init_image(self):
        self.image = Image.open(self.raw_image_name)
        self.image_draw_handle = ImageDraw.Draw(self.image)
        self.raw_image_width, self.raw_image_height = self.image.size

    def init_font(self, text, font_size):
        self.font_size = font_size
        self.font_handle = ImageFont.truetype("./Monaco.ttf", size=self.font_size)
        self.font_width, self.font_height = self.font_handle.getsize(text)
    
    def save_pic(self, file_name):
        self.image.save(file_name)
    
    def add_text_to_pic(self, text, font_size, reload_pic=True, reload_font=True, bound=0):
        if reload_pic:
            self.init_image()
        if reload_font:
            self.init_font(text, font_size)

        font_position = (self.raw_image_width - self.font_width - bound, bound - 2)
        
        self.image_draw_handle.text(font_position,
                                    text, font=self.font_handle, fill=self.font_color)
        
    
    def draw_a_circle(self):
        self.init_image()

        color = 128
        self.image_draw_handle.ellipse((50, 50, 140, 140), fill=self.fillcolor)
    
        self.image.save('3.jpg', 'jpeg')

    def draw_a_num_in_circle(self, text, font_size, bound=20):
        self.init_image()
        self.init_font(text, font_size)

        # 计算出半径
        circle_r = (math.sqrt(pow(self.font_height, 2) + pow(self.font_width, 2))) / 2
        # 计算圆心位置,预留边界
        # circle_x = (self.raw_image_width - circle_r) - bound
        # circle_y = circle_r + bound
        circle_x = (self.raw_image_width - self.font_width / 2) - bound
        circle_y = (self.font_height / 2) + bound
        

        circle_size = (circle_x - circle_r,
                        circle_y - circle_r,
                        circle_x + circle_r,
                        circle_y + circle_r)
        # 画圆
        self.image_draw_handle.ellipse(circle_size, fill=self.fillcolor)

        self.add_text_to_pic(text, font_size, reload_pic=False, reload_font=False, bound=bound)

if __name__ == '__main__':
    a = draw_somethig_to_pic('1.jpg')
    # a.add_text_to_pic('hello', 40)
    # a.draw_a_circle()
    a.draw_a_num_in_circle('2', 30)
    a.save_pic('4.png')
