try:
    print("Hello World")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Execution completed.")


try:
    f = open("demofile.txt", "r")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file.")
    finally:
        f.close()
        print("File closed.")
except FileNotFoundError:
    print("The file was not found.")

x = -1
if x < 0:
    # raise Exception("Sorry, no numbers below zero")
    pass

x = "hello"
if not isinstance(x, int):
    raise TypeError("Only integers are allowed")