def check(speed, limit):
    if speed > limit and limit:
        return False
    return True

print( check(130, 90) )
print( check(170, 0) )