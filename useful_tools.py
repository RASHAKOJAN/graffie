import random

feet_in_mile = 5800
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul mcCartney", "George Harrison", "Ringo Star"]

def get_file_ext(fileName):
    return fileName[fileName.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)

if __name__ == '__main__':
    pass