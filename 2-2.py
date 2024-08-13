def km_to_miles(km):
    return km * 0.621371

def calculate_speed(minutes, seconds, distance_km):
    distance_miles = km_to_miles(distance_km)
    total_hours = (minutes * 60 + seconds) / 3600
    speed_mph = distance_miles / total_hours
    return round(speed_mph, 1)

minutes = int(input("跑步時間（分鐘）："))
seconds = int(input("跑步時間（秒數）："))
distance_km = float(input("跑步距離（公里）："))
speed = calculate_speed(minutes, seconds, distance_km)
print(f"\nyour speed: {speed} mph")
