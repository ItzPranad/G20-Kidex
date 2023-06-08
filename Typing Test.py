from time import *
import random as r
def Mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1

    return error


def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)

test = ["A paragrph is a self-contained unit of discourse in writing with a particular point or a idea ",
"Typing speed is measured by the number of words you can type correctly in a set amount of time", "A skilled typist is able to finish a writing task within a specific length of time and is not hindered by their slower typing speed"]
print("***** Typing Speed *****")
test1 = r.choice(test)
print(test1)
print()
print()
time_1 = time()
testinput = input(" Enter:")
time_2 = time()

print('Speed : ', speed_time(time_1, time_2, testinput)," w/sec")
print("Error : ", Mistake(test1, testinput))