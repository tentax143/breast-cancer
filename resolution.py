from PIL import Image

def change_resolution(input_image_path, output_image_path, new_resolution):
    # Open the image
    img = Image.open(input_image_path)
    
    # Resize the image to the new resolution
    img_resized = img.resize(new_resolution, Image.ANTIALIAS)
    
    # Save the resized image
    img_resized.save(output_image_path)

for i in range in range Image:
    input_image_path = "input_image.jpg"
    output_image_path = "output_image.jpg"
    new_resolution = (800, 600)  # Specify the new resolution (width, height) in pixels
change_resolution(input_image_path, output_image_path, new_resolution)
