# Data types

age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if (police_check(12)):
    print("You're old enough to drive, on your way")
else: 
    print("Woah! Get out of the car! You're going to jail kid!")

