def average_speed():
    distance_1 = float(input("How far did you travel in the first half of the journey: "))
    distance_2 = float(input("How far did you travel in the second half of the journey: "))
    speed_1 = int(input("what was your average speed on the first half: "))
    speed_2 = int(input("what was your average speed ont he second half: "))

    total_time = distance_1/speed_1 + distance_2/speed_2
    average = (distance_1 + distance_2)/total_time
    average = round(average,2)
    print("your average speed was ",average,"mph")

def square_dimensions():
    top_left_x = int(input("enter top left x axis: "))
    top_left_y = int(input("enter top left y axis: "))

    top_right_x = top_left_x+100
    top_right_y = top_left_y
    print("the top right x and y coordinates are ", top_right_x, top_right_y)

 #def rectangle_perimeter():
