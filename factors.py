def temp_felt(t,v): #t denotes temperature in farenheit and # v denotes wind speed in mph
    s= v**0.16
    wind_chill = 35.74+ 0.6215*t - 35.75*s + 0.4275*t*s
    print("temperature felt by human body is ",round(wind_chill),"F")
temp_felt(37,55)