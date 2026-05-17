import random
import math
from PIL import Image, ImageDraw, ImageFont

width = 800
height = 250
num_nodes = 45
connection_distance = 90
drift_radius = 15
num_frames = 90
duration = 65  # 65ms per frame -> ~5.85s loop

bg_color = (13, 17, 23)        # #0D1117
accent_color = (14, 165, 233)  # #0EA5E9
accent_light = (56, 189, 248)  # #38BDF8
text_main = (248, 250, 252)    # #F8FAFC

random.seed(42)

nodes = []
for _ in range(num_nodes):
    bx = random.randint(0, width)
    by = random.randint(0, height)
    offset = random.uniform(0, 2 * math.pi)
    direction = random.choice([-1, 1])
    nodes.append({
        'bx': bx,
        'by': by,
        'offset': offset,
        'dir': direction
    })

try:
    title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 46)
    subtitle_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 15)
except:
    try:
        title_font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 46)
        subtitle_font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 15)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

frames = []

for frame_idx in range(num_frames):
    t = frame_idx / num_frames
    
    # Background
    img = Image.new('RGBA', (width, height), color=bg_color)
    
    # Layer for alpha blending (edges)
    edges_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    edges_draw = ImageDraw.Draw(edges_layer)
    
    # Compute current positions
    curr_nodes = []
    for node in nodes:
        angle = node['offset'] + node['dir'] * (2 * math.pi * t)
        nx = node['bx'] + drift_radius * math.cos(angle)
        ny = node['by'] + drift_radius * math.sin(angle)
        curr_nodes.append((nx, ny))
    
    # Draw edges
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            x1, y1 = curr_nodes[i]
            x2, y2 = curr_nodes[j]
            dist = math.hypot(x2 - x1, y2 - y1)
            if dist < connection_distance:
                opacity = 1.0 - (dist / connection_distance)
                # max opacity ~0.5 (128/255)
                alpha = int(opacity * 128)
                if alpha > 0:
                    edges_draw.line([(x1, y1), (x2, y2)], fill=(accent_color[0], accent_color[1], accent_color[2], alpha), width=1)
    
    # Composite edges
    img = Image.alpha_composite(img, edges_layer)
    draw = ImageDraw.Draw(img)
    
    # Draw nodes
    for x, y in curr_nodes:
        r = 1.5
        draw.ellipse([x - r, y - r, x + r, y + r], fill=accent_light)
    
    # Title
    title = "Tasfin Mahmud"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (width - tw) // 2
    ty = 120 - th
    
    # Draw text outline for legibility
    for dx, dy in [(-2,0), (2,0), (0,-2), (0,2), (-1,-1), (1,1), (-1,1), (1,-1)]:
        draw.text((tx + dx, ty + dy), title, fill=bg_color, font=title_font)
    draw.text((tx, ty), title, fill=text_main, font=title_font)
    
    # Subtitle
    subtitle = "AI/ML RESEARCHER • OPEN SOURCE DEVELOPER"
    bbox2 = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    sw = bbox2[2] - bbox2[0]
    sx = (width - sw) // 2
    sy = 150
    
    for dx, dy in [(-2,0), (2,0), (0,-2), (0,2)]:
        draw.text((sx + dx, sy + dy), subtitle, fill=bg_color, font=subtitle_font)
    draw.text((sx, sy), subtitle, fill=accent_light, font=subtitle_font)
    
    # Convert back to RGB for GIF saving
    frames.append(img.convert('RGB'))

frames[0].save('e:/301/TasfinMahmud/banner.gif', 
               save_all=True, 
               append_images=frames[1:], 
               duration=duration, 
               loop=0)

print("Generated animated banner.gif successfully!")
