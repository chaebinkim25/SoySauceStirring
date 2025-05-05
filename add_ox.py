import cv2
import os

in_folder = "white_background"
images = sorted(os.listdir(in_folder))

output_folder = "add_ox"
os.makedirs(output_folder, exist_ok=True)

# Read the first image to get dimensions
frame = cv2.imread(os.path.join(in_folder, images[76]))
height, width, layers = frame.shape

pad = 50
size = 300

def mark_x(img, size, pad, thickness):
    cv2.line(img, (width - size - pad, pad), (width - pad, size + pad ), (0, 0, 255), thickness)
    cv2.line(img, (width - size - pad, size + pad), (width - pad, pad ), (0, 0, 255), thickness)

def mark_o(img, size, pad, thickness):
    cv2.circle(img, (width - pad - size//2, pad + size//2), size//2, (0, 250, 0), thickness)

numbers = range(72, 80)
x_numbers = list(numbers) + [x + 76 for x in numbers]

o_numbers = [x + 76 * 2 for x in numbers]

print(x_numbers)
for i, img_name in enumerate(images):

    img = cv2.imread(os.path.join(in_folder, img_name))
    if i in x_numbers:
        mark_x(img, size, pad, 20)

    if i in o_numbers:
        mark_o(img, size, pad, 20)

    cv2.imwrite(os.path.join(output_folder, img_name), img)
