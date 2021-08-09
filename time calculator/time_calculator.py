import math as m

def add_time(strt_time, dur_time, day=" "):

    lst1 = strt_time.split()
    
    AM_or_PM = lst1[1]
    s_time = lst1[0]
    s_time = s_time.split(":")
    
    strt_hr = int(s_time[0])
    strt_min = int(s_time[1])
    
    lst2 = dur_time.split(":")
        
    dur_hr = int(lst2[0])
    dur_min = int(lst2[1])
    
    fin_hr = strt_hr + dur_hr
    fin_min = strt_min + dur_min
    
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        

    if fin_hr < 12 and fin_min < 60 and AM_or_PM == "PM":
        fin_hr = fin_hr
        fin_min = fin_min
        AM_or_PM = "PM"
                
        if day in weekdays:
            return ("{}:{:02d} {}, {}".format(fin_hr, fin_min, AM_or_PM, day))
        else:
            return ("{}:{:02d} {}".format(fin_hr, fin_min, AM_or_PM))   
        
    elif fin_hr < 12 and fin_min < 60 and AM_or_PM == "AM":
        fin_hr = fin_hr
        fin_min = fin_min
        AM_or_PM = "AM"
        return ("{}:{:02d} {}".format(fin_hr, fin_min, AM_or_PM))        
    
    elif fin_hr > 12 and fin_min > 60 and AM_or_PM == "AM":
        fin_min = abs(fin_min - 60)
        AM_or_PM = "PM"
        days_later = 0
        while fin_hr > 12:
            fin_hr = abs(fin_hr - 12)
            days_later += 1
        fin_hr += 1
        if days_later == 1:
            return ("{}:{:02d} {}".format(fin_hr, fin_min, AM_or_PM))
        
    if fin_hr > 12 and fin_min > 60 and AM_or_PM == "PM":
        fin_min = abs(fin_min - 60)
        AM_or_PM = "AM"
        days_later = 0
        while fin_hr > 12:
            fin_hr = abs(fin_hr - 12)
            days_later += 1
        fin_hr += 1
        new_day = ""
        for i in range(len(weekdays)):
            if weekdays[i].lower() == day.lower():
                new_day = i + days_later
                new_day = weekdays[new_day]

                
        if days_later > 1 and day in weekdays:
            return ("{}:{:02d} {}, {} ({} days later)".format(fin_hr, fin_min, AM_or_PM, new_day, days_later))
        else:
            return ("{}:{:02d} {} ({} days later)".format(fin_hr, fin_min, AM_or_PM, days_later))     
    
    
    elif fin_hr < 12 and fin_min > 60 and AM_or_PM == "AM":
        fin_hr = fin_hr + 1
        AM_or_PM = "PM"
        fin_min = abs(fin_min - 60)
        return ("{}:{:02d} {}".format(fin_hr, fin_min, AM_or_PM))
    
    
    if fin_hr > 12 and fin_min < 60 and AM_or_PM == "PM":
        fin_min = fin_min
        AM_or_PM = "AM"
        days_later = 0
        while fin_hr > 12:
            fin_hr = abs(fin_hr - 12)
            days_later += .5
        days_later = m.ceil(days_later)
        new_day = ""
                        
        # for i in range(len(weekdays)):
        #     if weekdays[i].lower() == day.lower():
        #         new_day = i + days_later
        #         new_day = weekdays[new_day]
                
        if days_later == 1:
            return ("{}:{:02d} {} (next day)".format(fin_hr, fin_min, AM_or_PM))
        elif day == " ":
            return ("{}:{:02d} {} ({} days later)".format(fin_hr, fin_min, AM_or_PM, days_later))
        else:
            return ("{}:{:02d} {}, {} ({} days later)".format(fin_hr, fin_min, AM_or_PM, weekdays[0], days_later))     
            
    elif fin_hr > 12 and fin_min < 60 and AM_or_PM == "AM":
        fin_min = fin_min
        AM_or_PM = "AM"
        days_later = 0
        while fin_hr > 12:
            fin_hr = abs(fin_hr - 12)
        days_later += .5
        days_later = m.ceil(days_later)

        
        new_day = ""
        
        for i in range(len(weekdays)):
            if weekdays[i].lower() == day.lower():
                new_day = i + days_later
                new_day = weekdays[new_day]
                
   
        if day == " ":
            return ("{}:{:02d} {} (next day)".format(fin_hr, fin_min, AM_or_PM))
        else:
            return ("{}:{:02d} {}, {} (next day)".format(fin_hr, fin_min, AM_or_PM, new_day))