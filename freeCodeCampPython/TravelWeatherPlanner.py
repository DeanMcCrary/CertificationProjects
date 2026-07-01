distance_mi = 3
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if is_raining:
        print(False)
    else:
        print(True)
elif (distance_mi > 1) and (distance_mi <= 6): 
#raining with no bike should print false
    if is_raining:
        print(False)
    elif not has_bike:
        print(False)
    else:
        print(True)
else:
    if has_car or has_ride_share_app:
        print(True)
    elif not has_car and not has_ride_share_app:
        print(False)