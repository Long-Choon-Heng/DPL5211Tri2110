# Student ID : 1201200987
# Student Name : Loh Joo Sheng

def rectangle(w,l):
    area = w * l
    return area

def triangle(w,l):
    area = w * l / 2
    return area

i = 0
while(i<2):
    width = float(input("Enter width   : "))
    length = float(input("Enter length  : "))

    area_rec = rectangle(width,length)
    area_tri = triangle(width,length)

    print("Rectangle area : {:.2f}".format(area_rec))
    print("Triangle area  : {:.2f}".format(area_tri))
    i += 1