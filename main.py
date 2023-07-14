def imt_count():
    try:
        weight = int(input("Enter your weight in kilos: "))
        height = int(input("Enter your height in centimetres: "))
        if weight and height < 1:
            raise TypeError
        imt = round((weight / ((height / 100) ** 2)), 1)
        if imt < 16.5:
            print(f"Your index is: {imt}. It's huge underweight, so close to death")
        elif 16 < imt < 18.6:
            print(f"Your index is: {imt}.It's underweight")
        elif 18.5< imt < 26:
            print(f"Your index is: {imt}. It's normal weight")
        elif 24 < imt < 31:
            print(f"Your index is: {imt}. It's overweight")
        elif 29 < imt < 35:
            print(f"Your index is: {imt}. It's obesity (First class)")
        elif 34 < imt < 40:
            print(f"Your index is: {imt}. It's obesity (Second class - severe)")
        elif 40 < imt:
            print(f"Your index is: {imt}. It's obesity (Second class - very severe)")
    except ValueError:
        print("Enter only numbers, without coma")
        return imt_count()
    except ZeroDivisionError:
        print("You be zero in your life but not in numbers")
        return imt_count()


imt_count()
