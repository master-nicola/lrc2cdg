# Generating Unicode bit masks
# You can:
#  - use your favorite font
#  - select size of font and bit mask
#  - select a range of Unicod points

from PIL import Image, ImageFont, ImageDraw
import json

def generate_char_mask(char, font_path="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", font_size=20):
    # Dimensions of bit mask
    width, height = 12, 24
    
    # Empty monochrome image (mode 'L' - grayscale)
    image = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(image)
    
    # Load a font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
        
    # Calculate center of symbol in mask
    bbox = draw.textbbox((0, 0), char, font=font)
    char_w = bbox[2] - bbox[0]
    char_h = bbox[3] - bbox[1]
    
    x_offset = 0
    y_offset = 0
    
    # Draw symbol white color (255)
    draw.text((x_offset, y_offset), char, fill=255, font=font)
    
    # Convert image into 2D matrix (True - line, False - background)
    mask_2d = []
    pixels = list(image.getdata())
    
    for y in range(height):
        row = []
        for x in range(width):
            pixel_val = pixels[y * width + x]
            # Pixel lighter than 128 - it's line (True)
            row.append(True if pixel_val > 128 else False)
        mask_2d.append(row)
        
    return mask_2d

json_masks=json.loads("{}")

fontSize=20

# Cyrillic
for code in range(1040, 1104):
    char_mask = generate_char_mask(chr(code), font_size=fontSize)
    json_masks[str(code)]=char_mask

# Draw mask into console
    for row in char_mask:
        print(" ".join(['█' if pixel == True else '.' for pixel in row]))
    print()

# Symbols 'ё' and 'Ё'
code=1105
char_mask = generate_char_mask(chr(code), font_size=fontSize)
json_masks[str(code)]=char_mask
for row in char_mask:
        print(" ".join(['█' if pixel == True else '.' for pixel in row]))
print()
code=1025
char_mask = generate_char_mask(chr(1025), font_size=fontSize)
json_masks[str(code)]=char_mask
for row in char_mask:
        print(" ".join(['█' if pixel == True else '.' for pixel in row]))
print()

# English symbols and special symbols
for code in range(32, 127):
    char_mask = generate_char_mask(chr(code), font_size=fontSize)
    json_masks[str(code)]=char_mask

    for row in char_mask:
        print(" ".join(['█' if pixel == True else '.' for pixel in row]))
    print()

# Save result to JSON file
with open("alphabet.json", "w", encoding="utf-8") as f:
    json.dump(json_masks, f)