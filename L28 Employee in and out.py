class employee:
    #initiaizing constructor
    def __init__(self):
        print("employee created")

    #calling destrutor
    def __del__(self):
        print("destrutor called")

#function outside of class
def create_obj():
    print("making object...")
    obj = employee()

    print("function end...")
    return obj

print("calling create_obj() function...")
object_1 = create_obj()

print("program end...")