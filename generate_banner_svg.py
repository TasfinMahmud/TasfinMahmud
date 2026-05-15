import random
import math

width = 800
height = 250
num_nodes = 75
connection_distance = 110
drift_radius = 25
duration = "20s"

# Cool professional tech palette
bg_color = "#0D1117"
accent_color = "#0ea5e9"  # Tech Blue/Cyan
accent_light = "#38bdf8"
text_main = "#f8fafc"

nodes = []
for _ in range(num_nodes):
    bx = random.randint(0, width)
    by = random.randint(0, height)
    
    # Generate random drift points for smooth animation
    points = []
    for _ in range(4):
        dx = random.randint(-drift_radius, drift_radius)
        dy = random.randint(-drift_radius, drift_radius)
        points.append((bx + dx, by + dy))
    
    # Close the loop for continuous animation
    points.append(points[0])
    
    # Format values for SVG SMIL animation
    x_vals = ";".join([f"{p[0]}" for p in points])
    y_vals = ";".join([f"{p[1]}" for p in points])
    
    nodes.append({
        'bx': bx,
        'by': by,
        'x_vals': x_vals,
        'y_vals': y_vals
    })

svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
# Background
svg += f'  <rect width="100%" height="100%" fill="{bg_color}" />\n'

# Edges
svg += f'  <g stroke="{accent_color}" stroke-width="0.6">\n'
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        bx1, by1 = nodes[i]['bx'], nodes[i]['by']
        bx2, by2 = nodes[j]['bx'], nodes[j]['by']
        dist = math.hypot(bx2 - bx1, by2 - by1)
        if dist < connection_distance:
            # Base opacity relative to distance
            opacity = 1.0 - (dist / connection_distance)
            opacity = max(0.05, min(0.6, opacity))
            
            x1_vals = nodes[i]['x_vals']
            y1_vals = nodes[i]['y_vals']
            x2_vals = nodes[j]['x_vals']
            y2_vals = nodes[j]['y_vals']
            
            svg += f'    <line stroke-opacity="{opacity:.2f}">\n'
            svg += f'      <animate attributeName="x1" values="{x1_vals}" dur="{duration}" repeatCount="indefinite" />\n'
            svg += f'      <animate attributeName="y1" values="{y1_vals}" dur="{duration}" repeatCount="indefinite" />\n'
            svg += f'      <animate attributeName="x2" values="{x2_vals}" dur="{duration}" repeatCount="indefinite" />\n'
            svg += f'      <animate attributeName="y2" values="{y2_vals}" dur="{duration}" repeatCount="indefinite" />\n'
            svg += f'    </line>\n'
svg += '  </g>\n'

# Nodes
svg += f'  <g fill="{accent_light}">\n'
for node in nodes:
    x_vals = node['x_vals']
    y_vals = node['y_vals']
    
    svg += f'    <circle r="1.5" opacity="0.7">\n'
    svg += f'      <animate attributeName="cx" values="{x_vals}" dur="{duration}" repeatCount="indefinite" />\n'
    svg += f'      <animate attributeName="cy" values="{y_vals}" dur="{duration}" repeatCount="indefinite" />\n'
    # Adding a slight pulse effect to nodes
    pulse_dur = f"{(random.random() * 3 + 4):.1f}s"
    svg += f'      <animate attributeName="r" values="1;2;1" dur="{pulse_dur}" repeatCount="indefinite" />\n'
    svg += f'      <animate attributeName="opacity" values="0.3;0.8;0.3" dur="{pulse_dur}" repeatCount="indefinite" />\n'
    svg += f'    </circle>\n'
svg += '  </g>\n'

# Text
svg += '  <g text-anchor="middle" font-family="system-ui, -apple-system, sans-serif">\n'
# Subtitle outline (for legibility against moving lines)
svg += f'    <text x="400" y="160" font-size="15" fill="{bg_color}" stroke="{bg_color}" stroke-width="5" stroke-linejoin="round" font-weight="600" letter-spacing="2">AI/ML RESEARCHER • OPEN SOURCE DEVELOPER</text>\n'
# Subtitle fill
svg += f'    <text x="400" y="160" font-size="15" fill="{accent_light}" font-weight="600" letter-spacing="2">AI/ML RESEARCHER • OPEN SOURCE DEVELOPER</text>\n'

# Title outline
svg += f'    <text x="400" y="125" font-size="48" font-weight="800" fill="{bg_color}" stroke="{bg_color}" stroke-width="8" stroke-linejoin="round" letter-spacing="-0.5">Tasfin Mahmud</text>\n'
# Title fill
svg += f'    <text x="400" y="125" font-size="48" font-weight="800" fill="{text_main}" letter-spacing="-0.5">Tasfin Mahmud</text>\n'
svg += '  </g>\n'

svg += '</svg>'

with open('e:/301/TasfinMahmud/banner.svg', 'w') as f:
    f.write(svg)

print("Generated animated banner.svg")
