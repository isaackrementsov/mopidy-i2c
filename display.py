import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# I2C display address, change
ADDRESS = 0x21

# Display dimensions (px)
W = 128
H = 32

# Connect to display via I2C
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(W, H, i2c, addr=ADDRESS)

# Initialize displayed image & font
image = Image.new('1', (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Clear display
def clear():
    oled.fill(0)
    oled.show()

# Draw text on display
def draw_text(text):
    # Clear whatever was already on the screen
    clear()

    # Align text horizontally left (with padding) and vertically center
    (fw, _fh) = font.getsize(text)
    draw.text(
        (oled.width // 8, oled.height // 2 - fh // 2),
        text,
        font=font,
        fill=255
    )

    # Show the text on the display
    oled.image(image)
    oled.show()
