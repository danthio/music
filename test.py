from PIL import Image,ImageTk,ImageDraw,ImageGrab
import tkinter as tk

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

            mx=max(rgb)

            c_=max(color)#color[rgb.index(mx)]



            r=int(c_*rgb[0]/mx)
            g=int(c_*rgb[1]/mx)
            b=int(c_*rgb[2]/mx)


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

convert("data/bg_.png","data/bg.png","#38fca5")
#print(680*1.7)
im=Image.open("data/bg.png")
x,y=im.size 
im=im.resize((int(680*x/y),680))
x,y=im.size

xx=int((x-y*1.75)/2)

im=im.crop((xx,0,x-xx,y))
im.save("data/bg.png")

darken_image("data/bg.png", "data/bg.png",(0,0,0), opacity=0.5)

"""
im=Image.open("data/bg_ref2.png")
x,y=im.size 
im=im.resize((int(680*1.75),int(680*1.75*y/x)))
x,y=im.size

yy=int((y-680))

im=im.crop((0,yy,x,y))
im.save("data/bg_ref.png")"""





images = []  # to hold the newly created image

def create_rectangle(can,x1, y1, x2, y2, **kwargs):
    global images
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images.append(ImageTk.PhotoImage(image))
        can.create_image(x1, y1, image=images[-1], anchor='nw')



def hex_to_rgba(hex_color, alpha):
    """Convert hex color like '#38fca5' to RGBA tuple."""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (r, g, b, int(alpha * 255))


def create_polygon(*args, **kwargs):
    global can





    if "alpha" in kwargs:         
        if "fill" in kwargs:
            # Get and process the input data
            c=kwargs.pop("can")
            outline = kwargs.pop("outline") if "outline" in kwargs else None

            # We need to find a rectangle the polygon is inscribed in
            # (max(args[::2]), max(args[1::2])) are x and y of the bottom right point of this rectangle
            # and they also are the width and height of it respectively (the image will be inserted into
            # (0, 0) coords for simplicity)
            image = Image.new("RGBA", (max(args[::2])+1, max(args[1::2])+1))

            fill=hex_to_rgba(kwargs.pop("fill"), kwargs.pop("alpha"))

            ImageDraw.Draw(image).polygon(args, fill=fill, outline=outline)



            images.append(ImageTk.PhotoImage(image))  # prevent the Image from being garbage-collected


            return c.create_image(0, 0, image=images[-1], anchor="nw")  # insert the Image to the 0, 0 coords

def capture_canvas(e):

    global can
    # Ensure Tkinter updates before capturing
    root.update_idletasks()

    # Get the absolute coordinates of the canvas
    x = root.winfo_rootx() + can.winfo_x()
    y = root.winfo_rooty() + can.winfo_y()
    x1 = x + can.winfo_width()
    y1 = y + can.winfo_height()

    # Capture the specified screen region
    image = ImageGrab.grab(bbox=(x, y, x1, y1))

    # Convert and save as high-quality image
    image = image.convert("RGB")  
    image.save("data/bg.png", quality=10000)





w,h=int(680*1.75),680

root=tk.Tk()
root.geometry(str(w)+"x"+str(h)+"+0+0")

can=tk.Canvas(width=w,height=h,relief="flat",highlightthickness=0,border=0,bg="#000000")
can.place(in_=root,x=0,y=0)

bg=ImageTk.PhotoImage(file="data/bg.png")

can.create_image(0,0,image=bg,anchor="nw")


#create_polygon(*[0,559, w,559, w,h, 0,h], fill="#000000", alpha=0.6,can=can)


can.bind("<Button-1>",capture_canvas)

root.mainloop()

