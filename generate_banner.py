import random
import math
from PIL import Image, ImageDraw, ImageFont

width = 1200
height = 350
num_nodes = 120
connection_distance = 120

# Generate random node positions
random.seed(42)  # Fixed seed for reproducibility
nodes = []
for _ in range(num_nodes):
    x = random.randint(0, width)
    y = random.randint(0, height)
    nodes.append((x, y))

# Create image
img = Image.new('RGB', (width, height), color=(13, 17, 23))  # #0D1117
draw = ImageDraw.Draw(img)

# Draw edges
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        x1, y1 = nodes[i]
        x2, y2 = nodes[j]
        dist = math.hypot(x2 - x1, y2 - y1)
        if dist < connection_distance:
            opacity = 1.0 - (dist / connection_distance)
            alpha = int(opacity * 80)  # max ~80 out of 255
            color = (168, 85, 247, alpha)  # #A855F7 with alpha
            draw.line([(x1, y1), (x2, y2)], fill=(168, 85, 247), width=1)

# Draw nodes
for x, y in nodes:
    r = 3
    draw.ellipse([x - r, y - r, x + r, y + r], fill=(168, 85, 247))

# Draw text - try to use a good font, fallback to default
try:
    title_font = ImageFont.truetype("arial.ttf", 56)
    subtitle_font = ImageFont.truetype("arial.ttf", 20)
except:
    try:
        title_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 56)
        subtitle_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

# Title - "Tasfin Mahmud"
title = "Tasfin Mahmud"
bbox = draw.textbbox((0, 0), title, font=title_font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
tx = (width - tw) // 2
ty = (height // 2) - th - 10

# Draw text shadow
draw.text((tx + 2, ty + 2), title, fill=(0, 0, 0), font=title_font)
draw.text((tx, ty), title, fill=(255, 255, 255), font=title_font)

# Subtitle
subtitle = "AI/ML RESEARCHER  |  OPEN SOURCE DEVELOPER"
bbox2 = draw.textbbox((0, 0), subtitle, font=subtitle_font)
sw = bbox2[2] - bbox2[0]
sx = (width - sw) // 2
sy = ty + th + 20

draw.text((sx, sy), subtitle, fill=(168, 85, 247), font=subtitle_font)

# Save
img.save('e:/301/TasfinMahmud/banner.png', 'PNG')
print("Generated banner.png successfully!")
