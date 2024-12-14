import re
from dataclasses import dataclass
import math

# OK this is mostly ChatGPT's work but I fixed some bugs
# Don't beat me

def calculate_deviation(positions):
    # Calculate the mean of x and y positions
    mean_x = sum(x for x, y in positions) / len(positions)
    mean_y = sum(y for x, y in positions) / len(positions)

    # Calculate the variance for x and y
    variance_x = sum((x - mean_x) ** 2 for x, y in positions) / len(positions)
    variance_y = sum((y - mean_y) ** 2 for x, y in positions) / len(positions)

    return math.sqrt(variance_x + variance_y)

@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int

def parse_input(file_path):
    robots = []
    pattern = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            match = pattern.match(line)
            if match:
                x, y, vx, vy = map(int, match.groups())
                robots.append(Robot(x, y, vx, vy))
            else:
                print(f"Invalid line format: {line}")
    return robots

def simulate(robots, seconds, width, height):
    final_positions = []
    for robot in robots:
        final_x = (robot.x + robot.vx * seconds) % width
        final_y = (robot.y + robot.vy * seconds) % height
        final_positions.append((final_x, final_y))
    return final_positions

def assign_quadrants(positions, width, height):
    # Define center points
    center_x = (width - 1) // 2  
    center_y = (height - 1) // 2  

    Q1 = Q2 = Q3 = Q4 = 0

    for x, y in positions:
        if x < center_x and y < center_y:
            Q1 +=1
        elif x > center_x and y < center_y:
            Q2 +=1
        elif x < center_x and y > center_y:
            Q3 +=1
        elif x > center_x and y > center_y:
            Q4 +=1
        # Robots exactly on the dividing lines (x=50.5 or y=51.5) are not possible since positions are integers
    return Q1, Q2, Q3, Q4


def calculate_safety_factor(quadrants):
    Q1, Q2, Q3, Q4 = quadrants
    return Q1 * Q2 * Q3 * Q4

def save_positions_image(positions, i, width, height):
    from PIL import Image, ImageDraw
    img_size = (width * 5, height * 5)
    img = Image.new('RGB', img_size, 'white')
    draw = ImageDraw.Draw(img)
    for x, y in positions:
        draw.rectangle([x*5, y*5, x*5+4, y*5+4], fill='black')
    img.save(f'imgs/{i}.png')

def main():
    # Grid dimensions as per the problem statement
    width = 101
    height = 103
    seconds = 100
    robots = parse_input("../input/14.in")
    final_positions = simulate(robots, seconds, width, height)
    quadrants = assign_quadrants(final_positions, width, height)
    safety_factor = calculate_safety_factor(quadrants)
    
    # Part 1
    print(safety_factor)

    # Part 2, then eyeball it
    for i in range(10000):
        final_positions = simulate(robots, i, width, height)
        d = calculate_deviation(final_positions)
        if d < 37:
            save_positions_image(final_positions, i, width, height)

if __name__ == "__main__":
    main()
