import math
import random
from PIL import Image, ImageDraw, ImageFont
import colorsys

# Constants
WIDTH, HEIGHT = 1200, 800
TOP_MARGIN = int(HEIGHT * 0.2)
USABLE_HEIGHT = HEIGHT - TOP_MARGIN
CENTER_X, CENTER_Y = WIDTH // 2, TOP_MARGIN + (USABLE_HEIGHT // 2)

def generate_color_scheme(num_colors):
    hue = random.random()
    saturation = random.uniform(0.5, 0.8)
    lightness = random.uniform(0.5, 0.7)
    colors = []
    for i in range(num_colors):
        hue_i = (hue + i / num_colors) % 1.0
        rgb = colorsys.hls_to_rgb(hue_i, lightness, saturation)
        colors.append(tuple(int(x * 255) for x in rgb))
    return colors

def draw_shape(draw, shape, position, size, color, outline=None):
    x, y = position
    if shape == 'circle':
        draw.ellipse([x-size//2, y-size//2, x+size//2, y+size//2], fill=color, outline=outline)
    elif shape == 'square':
        draw.rectangle([x-size//2, y-size//2, x+size//2, y+size//2], fill=color, outline=outline)
    elif shape == 'hexagon':
        points = []
        for i in range(6):
            angle = i * math.pi / 3
            px = x + size//2 * math.cos(angle)
            py = y + size//2 * math.sin(angle)
            points.append((px, py))
        draw.polygon(points, fill=color, outline=outline)
    elif shape == 'triangle':
        points = [
            (x, y - size//2),
            (x - size//2, y + size//2),
            (x + size//2, y + size//2)
        ]
        draw.polygon(points, fill=color, outline=outline)
    elif shape == 'pentagon':
        points = []
        for i in range(5):
            angle = (i * 2 * math.pi / 5) - math.pi/2
            px = x + size//2 * math.cos(angle)
            py = y + size//2 * math.sin(angle)
            points.append((px, py))
        draw.polygon(points, fill=color, outline=outline)

def calculate_element_positions(num_elements, arrangement, radius, central_size, element_size):
    positions = []
    if arrangement == 'full_circle':
        for i in range(num_elements):
            angle = 2 * math.pi * i / num_elements
            x = CENTER_X + radius * math.cos(angle)
            y = CENTER_Y + radius * math.sin(angle)
            positions.append((x, y))
    elif arrangement == 'half_circle':
        for i in range(num_elements):
            angle = math.pi * (i / (num_elements - 1) - 0.5)
            x = CENTER_X + radius * math.cos(angle)
            y = CENTER_Y + radius * math.sin(angle)
            positions.append((x, y))
    elif arrangement == 'left_side':
        center_x = central_size
        available_width = WIDTH - central_size - element_size
        available_height = USABLE_HEIGHT - element_size
        for i in range(num_elements):
            x = center_x + available_width * ((i + 1) / (num_elements + 1))
            y = TOP_MARGIN + available_height * ((i % 2 + 1) / 3)
            positions.append((x, y))
    return positions

def draw_connection_lines(draw, center, positions, element_size):
    for pos in positions:
        # Check if the line would overlap with any element
        if not any(math.dist(center, p) + math.dist(p, pos) <= math.dist(center, pos) + element_size for p in positions if p != pos):
            draw.line([center, pos], fill='gray', width=2)

def generate_spoke_slide():
    img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
    draw = ImageDraw.Draw(img)

    # Choose random parameters
    num_elements = random.randint(3, 8)
    arrangement = random.choice(['full_circle', 'half_circle', 'left_side'])
    central_shape = random.choice(['circle', 'square', 'hexagon', 'triangle', 'pentagon'])
    surrounding_shape = random.choice(['circle', 'square', 'hexagon', 'pentagon'])

    # Generate color scheme
    colors = generate_color_scheme(num_elements + 1)

    # Calculate sizes
    available_space = min(WIDTH, USABLE_HEIGHT)
    if arrangement == 'left_side':
        central_size = int(USABLE_HEIGHT * 0.6)
        max_element_size = int((WIDTH - central_size) / (num_elements + 1))
    else:
        max_element_size = int(available_space / (num_elements + 3))
        central_size = int(max_element_size * 2)

    surrounding_size = int(max_element_size * 0.8)

    # Draw central element
    if arrangement == 'left_side':
        central_pos = (central_size // 2, CENTER_Y)
    else:
        central_pos = (CENTER_X, CENTER_Y)
    draw_shape(draw, central_shape, central_pos, central_size, colors[0])

    # Calculate and draw surrounding elements
    if arrangement == 'left_side':
        radius = 0  # Not used for left_side arrangement
    else:
        radius = (available_space - central_size - surrounding_size) // 2
    positions = calculate_element_positions(num_elements, arrangement, radius, central_size, surrounding_size)
    for i, pos in enumerate(positions):
        draw_shape(draw, surrounding_shape, pos, surrounding_size, colors[i+1])

    # # Draw connection lines
    # draw_connection_lines(draw, central_pos, positions, surrounding_size)

    return img

def generate_dataset(num_images):
    for i in range(num_images):
        img = generate_spoke_slide()
        img.save(f'spoke_slide_{i:04d}.png')


if __name__ == "__main__":
    # Generate 10,000 unique spoke slide images
    generate_dataset(10)