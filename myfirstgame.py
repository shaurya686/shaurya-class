import math
import os
import time

# Define the vertices of a cube (8 corners in 3D space)
vertices = [
    [-1, -1, -1],
    [-1, -1,  1],
    [-1,  1, -1],
    [-1,  1,  1],
    [ 1, -1, -1],
    [ 1, -1,  1],
    [ 1,  1, -1],
    [ 1,  1,  1]
]

# Edges connecting the vertices
edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),  # Front face
    (4, 5), (5, 7), (7, 6), (6, 4),  # Back face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]

def rotate_x(point, angle):
    """Rotate a point around the X-axis."""
    x, y, z = point
    y_rot = y * math.cos(angle) - z * math.sin(angle)
    z_rot = y * math.sin(angle) + z * math.cos(angle)
    return [x, y_rot, z_rot]

def rotate_y(point, angle):
    """Rotate a point around the Y-axis."""
    x, y, z = point
    x_rot = x * math.cos(angle) + z * math.sin(angle)
    z_rot = -x * math.sin(angle) + z * math.cos(angle)
    return [x_rot, y, z_rot]

def project(point, screen_width, screen_height, fov, viewer_distance):
    """Project a 3D point onto a 2D screen."""
    x, y, z = point
    factor = fov / (viewer_distance + z)
    x_proj = int(screen_width / 2 + x * factor)
    y_proj = int(screen_height / 2 - y * factor)
    return [x_proj, y_proj]

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Screen size and settings
screen_width, screen_height = 80, 40
fov = 500  # Field of view
viewer_distance = 4  # Distance of the viewer from the object
angle = 0

# Main loop
while True:
    clear_screen()
    transformed_vertices = []

    # Rotate and project each vertex
    for vertex in vertices:
        rotated_x = rotate_x(vertex, angle)
        rotated_y = rotate_y(rotated_x, angle)
        projected = project(rotated_y, screen_width, screen_height, fov, viewer_distance)
        transformed_vertices.append(projected)

    # Draw the edges
    screen = [[' ' for _ in range(screen_width)] for _ in range(screen_height)]
    for edge in edges:
        start, end = edge
        x1, y1 = transformed_vertices[start]
        x2, y2 = transformed_vertices[end]

        # Simple line drawing algorithm (Bresenham's algorithm)
        dx, dy = x2 - x1, y2 - y1
        steps = max(abs(dx), abs(dy))
        for i in range(steps + 1):
            x = int(x1 + i * dx / steps)
            y = int(y1 + i * dy / steps)
            if 0 <= x < screen_width and 0 <= y < screen_height:
                screen[y][x] = 'O'

    # Print the screen
    for row in screen:
        print("".join(row))

    # Update angle and pause
    angle += 0.05
    time.sleep(0.03)
