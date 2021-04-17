import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# I2C display address
ADDRESS = 0x21

# Display dimensions
W = 128
H = 32

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(W, H, i2c, addr=ADDRESS)

image = Image.new('1', (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

def clear():
    oled.fill(0)
    oled.show()

def draw_text(text):
    clear()

    (fw, _fh) = font.getsize(text)
    draw.text(
        (oled.width // 4, oled.height // 2 - fh // 2),
        text,
        font=font,
        fill=255
    )

    oled.image(image)
    oled.show()
