def add_time(start, duration, weekday=False):

  return_time = ''

  # split the start time
  start_time_split = start.split(' ')
  start_hours = int(start_time_split[0].split(':')[0])
  start_minutes = int(start_time_split[0].split(':')[1])
  am_pm = start_time_split[1]

  print(start_hours)
  print(start_minutes)
  print(am_pm)

  # split the duration
  duration_hours = int(duration.split(':')[0])
  duration_minutes = int(duration.split(':')[1])

  print(duration_hours)
  print(duration_minutes)

  # add duration minutes to start minutes
  minutes = start_minutes + duration_minutes

  # if we reach more than 60 minutes we must increase the hour
  # nad keep the remaining minutes
  if minutes >= 60:
    start_hours += 1
    minutes = minutes % 60

  # add hours
  hours = start_hours + duration_hours

  return return_time
