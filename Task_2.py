import numpy as np


iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
t = 2.262
c = iq.mean()
a = c - (t * (iq.std(ddof=1)/(10**0,5))
b = c + (t * (iq.std(ddof=1)/(10**0,5))

print(f'Доверительный интервал для мат ожидания с надежностью 0,95 составляет [{a};{b}]')
