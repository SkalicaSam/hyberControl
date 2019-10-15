
import time, os

y = 0
while y == 0:
    #time.sleep(15)
    # modul for hybernating
    os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')
    time.sleep(15)
