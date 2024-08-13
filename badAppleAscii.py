from PIL import ImageDraw, ImageFont, Image
import cv2
import numpy as np
import math

def playBadApple():
    fileName = "~/dev/python/ytshell/BadApple.mp4"
    chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    charlist = list(chars)
    charlen = len(charlist)
    interval = charlen / 256
    scale_factor = 0.09
    charwidth = 10
    charheight = 10

    def get_char(i):
        return charlist[math.floor(i * interval)]

    cap = cv2.VideoCapture(fileName)

    # Use a font that is typically available on Linux systems
    Font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 15)
    
    while True:
        ret, img = cap.read()
        
        if not ret:  # Check if the frame was not read correctly
            print("Failed to grab frame")
            break
        
        img = Image.fromarray(img)

        width, height = img.size
        img = img.resize((int(scale_factor * width), int(scale_factor * height * (charwidth / charheight))), Image.NEAREST)
        width, height = img.size
        pixel = img.load()
        outputImage = Image.new("RGB", (charwidth * width, charheight * height), color=(0, 0, 0))
        dest = ImageDraw.Draw(outputImage)

        for i in range(height):
            for j in range(width):
                r, g, b = pixel[j, i]
                h = int(0.299 * r + 0.587 * g + 0.114 * b)
                pixel[j, i] = (h, h, h)
                dest.text((j * charwidth, i * charheight), get_char(h), font=Font, fill=(r, g, b))

        open_cv_image = np.array(outputImage)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        cv2.imshow("ASCII Art", open_cv_image)
    
    cap.release()
    cv2.destroyAllWindows()

playBadApple()
