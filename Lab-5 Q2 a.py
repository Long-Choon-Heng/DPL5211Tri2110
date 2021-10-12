def rectangle(width,length):
    area = width * length
    return area

def triangle(width,length):
    area = width * length / 2
    return area

width = float(input("Enter width: "))
length = float(input("Enter length: "))

area_rec = rectangle(width,length)
print("Rectangle area: {:.2f}".format(area_rec))

area_tri = triangle(width,length)
print("Triangle area: {:.2f}".format(area_tri))



