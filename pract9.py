primes = [2, 3, 5, 7, 11, 13, 17, 19]
primes[0]  # 2
primes[7]  # 19
primes[8]  # IndexError: list index out of range
primes[-1]  # 19
primes[-9]  # IndexError: list index out of range

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekdays[1] = "Tue"

temperatures = [14.5, 8.0, -2.5, 15.0]
temperatures[-2] = 10.0

type(primes)  # <class 'list'>
type(weekdays)  # <class 'list'>
type(temperatures)  # <class 'list'>

[2, 4, 6, 8] * 3  # [2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]
[0] * 3  # [0, 0, 0]
weekdays * 2  # ['Mon', 'Tue', 'Wed', 'Thu', 'Mon', 'Tue', 'Wed', 'Thu']

weekend = ["Sat", "Sun"]
daysOfWeek = weekdays + weekend
daysOfWeek  # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

primes2 = primes + [23, 29]