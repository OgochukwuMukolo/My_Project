# Volume of a prism

def vol(length=10, width=8, height=15):
    return length * width * height


print("The volume of the rectangular prism is " + str(vol()) + " cubic feet.")



length = int(input("Enter an integer for length."))
width = int(input("Enter an integer for with."))
height = int(input("Enter an integer for height."))


def vol(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(vol(length, width, height)) + " cubic feet.")