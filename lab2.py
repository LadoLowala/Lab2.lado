Seconds= int(input('Numbers of seconds'))
hours=Seconds//3600
Seconds=Seconds%3600
mintue=Seconds//60
Seconds=Seconds%60
print(hours, mintue , Seconds)



Population=334205119
Seconds=1685720
birth=Seconds//7
death=Seconds//13
newimmigrant=Seconds//35

change=(birth+newimmigrant-death)
print(Population+change)

days=hours//24
hours=hours%24
print(days,hours,mintue,Seconds)

flapjacks=(((Population+350)**2)-12/50)
print("The number of FlapJacks eaten in the US")
round(flapjacks)