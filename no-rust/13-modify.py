# Open the file for reading and writing
with open('../input/13.in', 'r') as file:
    # Read the entire content of the file
    content = file.read()
    
content = content.replace('Button A: X+', ' ')
content = content.replace('Button B: X+', ' ')
content = content.replace(', Y+', ' ')
content = content.replace('Prize: X=', ' ')
content = content.replace(', Y=', ' ')

with open('../input/13-modified.in', 'w') as file:
    file.write(content)
