import re
def check_day(weekday):
  week_list=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  day=weekday.lower().capitalize()
  try:    
    return week_list.index(day)
  except:
    return -1
    
def add_time(start, duration, weekday=""):
  new_time = duration
  hour,min,all_hour,all_min=0,0,0,0
  ampm=""
  ampm_f=1
  days=""
  day_list=[]
  day_count=0
  day_week=0
  f_min=""
  week_list=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", ""]
  day_week = check_day(weekday)
  if (re.fullmatch('^[1-9]:[0-5][0-9]\s[a|p]m$|^[1][0-2]:[0-5][0-9]\s[a|p]m$',start,re.IGNORECASE)): 
    
    if(re.fullmatch('^[0-9]*:[0-5][0-9]$',duration)):
      
      hour=int(start.split(" ")[0].split(":")[0])
      min=int(start.split(" ")[0].split(":")[1])
      ampm=start.split(" ")[1].lower()
      if hour==12:
        hour=0
      if(ampm=="am"):      
        ampm_f=1
      else:
        ampm_f=-1
        hour+=12
        
      dur_hour=int(duration.split(":")[0])
      dur_min=int(duration.split(":")[1])
      print("start time", hour, min, ampm,"duration:", dur_hour, dur_min, "ampm:", ampm_f)
      all_hour= hour + dur_hour
      all_min = min + dur_min
      
      if(all_min>59):
        all_min=all_min-60
        all_hour+=1
      print(all_hour, all_min,day_list)
      if(all_hour>=24):
        day_count=int(all_hour/24)
        all_hour = all_hour % 24
      """while(all_hour>=24):
        day_list.append(24)
        all_hour-=24
        print(all_hour)
        print(all_hour, all_min, day_list)
        """      
      print(all_hour, all_min, day_count)
      #format returnd hours
     
      if(all_hour>=12):
        if(all_hour>12):
          all_hour-=12
        ampm="pm"
      else:
        if(all_hour==0):
          all_hour=12
        ampm="am"
      #format returned minutes       
      if(re.match('^[0-9]$',str(all_min)))  :
        f_min = "0"+ str(all_min)
      else:
        f_min = str(all_min)
      new_time=str(all_hour) + ":" + f_min + " "+ ampm.upper() 
      """if(len(day_list)==1):
        day="next day"
        new_time+= f" ({day})"
      if(len(day_list)>1):
        new_time+= f" ({len(day_list)} days later)"
        """
      if(day_week>-1)  :
        day_week = day_week + day_count
        print("day_week: ", day_week)
        if day_week>6:
          day_week = day_week % 7.
        new_time+=f", {week_list[int(day_week)]}"
      if(day_count==1):
        day="next day"
        new_time+= f" ({day})"
      if(day_count>1):
        #new_time+= f" ({len(day_list)} days later)"
        new_time+= f" ({day_count} days later)"
      return new_time 
    else:
      return "invalid duration time, should be number:number between 0-59 format"
  else:
    return "invalid start time"    
  

  