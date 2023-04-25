from PIL import Image, ImageDraw

# Define image size and gradient color
width, height = 600, 350
color1 = (0, 0, 255)  # blue
color2 = (255, 0, 0)

# Create a new image with a white background
image = Image.new('RGB', (width, height), color1)

# Draw the gradient on the image
draw = ImageDraw.Draw(image)
for x in range(width):
    r = int((x / width) * (color2[0] - color1[0]) + color1[0])
    g = int((x / width) * (color2[1] - color1[1]) + color1[1])
    b = int((x / width) * (color2[2] - color1[2]) + color1[2])
    draw.line((x, 0, x, height), fill=(r, g, b))

# Save the image
image.save('gradient_horizontal_red.png')
