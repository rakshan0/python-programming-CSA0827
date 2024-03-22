def get_season(month, day):
    
    seasons = {
        "Spring": ("Mar", 20),
        "Summer": ("Jun", 21),
        "Fall": ("Sep", 22),
        "Winter": ("Dec", 21)
    }

   
    for season, (start_month, start_day) in seasons.items():
        if (month == start_month and day >= start_day) or (month > start_month):
            return season
    
   
    return None


month = input("Enter the month (first three letters capitalized): ")
day = int(input("Enter the day within the month: "))


season = get_season(month, day)


if season:
    print(f"The season associated with {month} {day} is {season}.")
else:
    print("Invalid input or date not associated with any season.")
