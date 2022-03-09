from datetime import time

print('min: ', time.min)
print('max: ', time.max)
print('resolution: ', time.resolution)

time_var = time(hour=20, minute=1, second=1, microsecond=1)
print(time_var, type(time_var))
