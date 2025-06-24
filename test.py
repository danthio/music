from PIL import Image 

#38fca5 #125437 #071f14



def hex_to_rgb(hex_color: str) -> tuple:
    # Remove the '#' if it exists
    hex_color = hex_color.lstrip('#')
    # Convert to RGB
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def convert(file,output,col):


    im=Image.open(file)
    w,h=im.size

    rgb=hex_to_rgb(col)




    image = Image.new('RGB', (w, h), '#000000')
    pixels = image.load()


    for y in range(h):

        for x in range(w):


            color = im.getpixel((x, y))

            #print(mx)


            r=int(rgb[0]*color[1]/rgb[1])
            g=int(rgb[1]*color[1]/rgb[1])
            b=int(rgb[2]*color[1]/rgb[1])


            pixels[x,y]=(r,g,b)

    image.save(output)


"""
rgb=hex_to_rgb("#39fca7")
rgb=(int(rgb[0]*rgb[1]/255),rgb[1],int(rgb[2]*rgb[1]/255))

col="#%02x%02x%02x" % rgb


print(col)

"""


def darken_image(image_path, output_path,col, opacity=0.5):
    """
    Darkens an image by overlaying a semi-transparent black layer.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the darkened image.
        opacity (float): Opacity of the dark layer (0.0 to 1.0).
    """
    # Open the original image
    img = Image.open(image_path).convert("RGBA")
    
    # Create a black overlay with the same size as the image
    black_overlay = Image.new("RGBA", img.size, (*col, int(255 * opacity)))
    
    # Composite the black overlay onto the image
    darkened_img = Image.alpha_composite(img, black_overlay)
    
    # Save the result
    darkened_img.save(output_path)

# Example usage



"""
def hex_to_rgb(hex_color: str) -> tuple:
    # Remove the '#' if it exists
    hex_color = hex_color.lstrip('#')
    # Convert to RGB
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def compare(c1,c2):


    return c1[0]/c2[0]


col="#38fca5"

col_=hex_to_rgb(col)

#print(col_)

#col__="#%02x%02x%02x"%(int(col_[0]*255/col_[0]),int(col_[1]*255/col_[0]),int(col_[2]*255/col_[0]))

#print(col__)

r=compare(hex_to_rgb("#ff00ff"),hex_to_rgb("#550055"))

col2="#%02x%02x%02x"%(int(col_[0]/r),int(col_[1]/r),int(col_[2]/r))

r=compare(hex_to_rgb("#ff00ff"),hex_to_rgb("#200020"))

col3="#%02x%02x%02x"%(int(col_[0]/r),int(col_[1]/r),int(col_[2]/r))


r=compare(hex_to_rgb("#ff00ff"),hex_to_rgb("#550055"))

col4="#%02x%02x%02x"%(int(col_[0]/r),int(col_[1]/r),int(col_[2]/r))



print(col2,col3,col4)

"""

convert("data/bg_.jpg","data/bg.png","#38fca5")
#print(680*1.7)
im=Image.open("data/bg.png")
x,y=im.size 
im=im.resize((int(680*x/y),680))
x,y=im.size

xx=int((x-y*1.75)/2)

im=im.crop((xx,0,x-xx,y))
im.save("data/bg.png")

darken_image("data/bg.png", "data/bg.png",(0,0,0), opacity=0.4)
"""
im=Image.open("data/bg_ref2.png")
x,y=im.size 
im=im.resize((int(680*1.75),int(680*1.75*y/x)))
x,y=im.size

yy=int((y-680))

im=im.crop((0,yy,x,y))
im.save("data/bg_ref.png")"""

