
def week_time(week, time, prev):
    hour_miniute = time.split(":")
    final_minute = int(hour_miniute[0]) * 60 + int(hour_miniute[1])
    new_minute = final_minute - prev
    if new_minute > 0:
        new_week = week
    
    else:
        all_days, new_minute = divmod(new_minute, 1440)
        new_days = all_days % -7
        new_week = week + new_days
    
    new_hour, new_time = divmod(new_minute, 60)
    if new_hour < 10:
        new_hour = "0{0}".format(new_hour)
    if new_time < 10:
        new_time = "0{0}".format(new_time)
    return str(new_week), "{0}:{1}".format(new_hour, new_time)


if __name__ == "__main__":
    week = int(input())
    time = input()
    previous = int(input())
    new_week, new_time = week_time(week, time, previous)
    print(new_week)
    print(new_time)