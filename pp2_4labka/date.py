1#

# import datetime
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days = 5)
# print(tday - tdelta)


2## import datetime
# tday  = datetime.date.today()
# tdelta = datetime.timedelta(days = 1)
# yest = (datetime.date.today()   - tdelta)
# tmrw = (datetime.date.today() + tdelta)
# print(f"Yesterday : {yest}")
# print(f"Today : {datetime.date.today()}")
# print(f"Tomorrow : {tmrw}")


#3
# import datetime
# dt =  datetime.datetime.today()
# print(dt.microsecond)


#4
# import datetime
# one =datetime.datetime.now()
# two = datetime.datetime(2023,12,28,2,3,4)
# differential_equation = one-two
# print(differential_equation.total_seconds())
# print(differential_equation.total_seconds()/60) #-> for minute difference 
# print(differential_equation.total_seconds()/60**2) #-> for hour difference