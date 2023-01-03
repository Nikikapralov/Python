def recursive_drawing(number_of_stars):
    if number_of_stars == 0:
        return
    print("*" * number_of_stars)
    recursive_drawing(number_of_stars - 1)
    print("#" * number_of_stars)


recursive_drawing(5)