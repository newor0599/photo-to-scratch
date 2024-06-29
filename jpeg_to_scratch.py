import cv2

image_dimension = (200,200)
export_raw_image = f"{image_dimension[0]}\n{image_dimension[1]}\n"
image = None

try:
    image_path = input("Enter image path (jpg/jpeg only!):\n")
    image = cv2.imread(image_path)
    image = cv2.resize(image,image_dimension)
except:
    print("Invalid image")
    quit()
print("Converting...")

rows,cols,_ = image.shape

for i in range(rows):
    for j in range(cols):
        k = image[i,j]
        r = format(k[0],'x')
        g = format(k[1],'x')
        b = format(k[2],'x')
        export_raw_image += f'{b+g+r}\n'
export_raw_image += " "
with open('output.txt','w') as f:
    f.write(export_raw_image)
print("Data has been saved to output.txt")
