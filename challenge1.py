def convert_to_24_hour(hour, minute, period):
    #Check if it's in the morning (am) and adjust hour if necessary
    if period.lower() == 'am':
        if hour == 12:
            hour = 0
    
    #Check if it's in the afternoon/evening (pm) and adjust hour if necessary
    elif period.lower() == 'pm':
        if hour != 12:
            hour += 12

    #Format the hour and minute as a four digit string
    formatted_hour = "{:02d}".format(hour)
    formatted_minute = "{:02d}".format(minute)
    return formatted_hour + ":" + formatted_minute

print(convert_to_24_hour(8, 30, 'pm'))