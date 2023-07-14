def imt_count():
    try:
        weight = int(input("Enter your weight in kilos: "))
        height = int(input("Enter your height in centimetres: "))
        if weight and height < 1:
            raise TypeError
        imt = (weight / ((height / 100) ** 2))
        if imt < 17:
            print("Bad news, you need to eat a lot")
        elif 16 < imt < 18.6:
            print("Not so good, you need additional breakfast, lunch and double dinner")
        elif 18.5< imt < 26:
            print("Keep on that's way")
        elif 24 < imt < 31:
            print("Just a little bit and you'll become fat ass")
        elif
    except ValueError:
        print("Enter only numbers, without coma")
        return imt_count()
    except ZeroDivisionError:
        print("You be zero in your life but not in numbers")
        return imt_count()


imt_count()
