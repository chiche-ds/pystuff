tesh_h = int(input("Height of the wall:  "))
test_w = int(input("Width of the wall: "))
coverage = 5


def number_of_can(height=tesh_h, width=test_w, cover=coverage):
    n = round((height*width) / cover)
    print(f"You will need {n} of paint")


number_of_can(tesh_h,test_w,coverage)