import calendar  # 日历模块
import io

try:
    c = calendar.calendar(2022)
    file = open("F:/zzz/calendar.txt", "w")
    file.write(c)
    #read = open("F:/zzz/calendar.txt", "r")
    #print(file.read())
finally:
    file.close()
    #read.close()
