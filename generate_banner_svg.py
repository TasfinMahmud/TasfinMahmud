import random
import math

width = 800
height = 250
num_nodes = 80
connection_distance = 100

nodes = []
for _ in range(num_nodes):
    x = random.randint(0, width)
    y = random.randint(0, height)
    nodes.append((x, y))

svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
# CSS Animation
svg += '''
  <style>
    @keyframes float {
      0% { transform: translateY(0px) translateX(0px); }
      33% { transform: translateY(-5px) translateX(5px); }
      66% { transform: translateY(5px) translateX(-5px); }
      100% { transform: translateY(0px) translateX(0px); }
    }
    @keyframes pulse {
      0% { opacity: 0.4; }
      50% { opacity: 0.8; }
      100% { opacity: 0.4; }
    }
    .node { animation: float 10s ease-in-out infinite; }
    .edge { animation: pulse 4s ease-in-out infinite; }
  </style>
'''
# Background
svg += f'  <rect width="100%" height="100%" fill="#0D1117" />\n'

# Edges
svg += '  <g stroke="#A855F7" stroke-width="1" opacity="0.4">\n'
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        x1, y1 = nodes[i]
        x2, y2 = nodes[j]
        dist = math.hypot(x2 - x1, y2 - y1)
        if dist < connection_distance:
            opacity = 1.0 - (dist / connection_distance)
            delay = random.uniform(0, 5)
            svg += f'    <line class="edge" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-opacity="{opacity:.2f}" style="animation-delay: -{delay:.1f}s" />\n'
svg += '  </g>\n'

# Nodes
svg += '  <g fill="#A855F7">\n'
for x, y in nodes:
    delay = random.uniform(0, 10)
    svg += f'    <circle class="node" cx="{x}" cy="{y}" r="2" opacity="0.8" style="animation-delay: -{delay:.1f}s" />\n'
svg += '  </g>\n'

# Text
svg += '  <g text-anchor="middle" font-family="system-ui, -apple-system, sans-serif">\n'
svg += '    <text x="400" y="120" font-size="46" font-weight="bold" fill="#ffffff" filter="drop-shadow(0px 4px 6px rgba(0,0,0,0.5))">Tasfin Mahmud</text>\n'
svg += '    <text x="400" y="160" font-size="16" fill="#A855F7" font-weight="500" letter-spacing="1">AI/ML RESEARCHER • OPEN SOURCE DEVELOPER</text>\n'
svg += '  </g>\n'

svg += '</svg>'

with open('e:/301/TasfinMahmud/banner.svg', 'w') as f:
    f.write(svg)

print("Generated animated banner.svg")
