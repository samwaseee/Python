day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

match day:
    case 1 | 2 | 3:
        print("Weekday")
    case 4 | 5:
        print("Thursday or Friday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid day")