print("Hello! This calculator computes how long will it take you to ride a given distance at a given speed.")

speed = float(input("Enter your speed in km/h: "))
distance = float(input("Enter your distance in km: "))

if speed <= 0:
    speed = float(input('Please enter an appropiate speed (km/h): '))
elif distance <0:
    distance = float(input('Please enter an appropiate distance (km): '))
    
seconds_speed = (distance / speed * 60) * 60

#import datetime
#time = str(datetime.timedelta(seconds=seconds_speed))

def sec_to_hours(seconds):
    hour = int(seconds//3600)
    minute = int((seconds%3600)//60)
    second = int((seconds%3600)%60)
    time = ["{} hours {} minutes {} seconds".format(hour, minute, second)]
    return time
    
duration = sec_to_hours(seconds_speed)

print(f"At that pace you will ride {distance} km in {duration}.")
