from time import strftime, gmtime

formatted_time = strftime("%a, %d %b %Y %H:%M:%S , %Z", gmtime())
print(formatted_time)