std = 5
n = 27
mu = 174.2
z_t = 1.96
a = mu - (z_t * std/(27 ** 0.5))
b = mu + (z_t * std/(27 ** 0.5))

print(f'Доверительный интервал для мат ожидания с надежностью 0,95 составляет [{a};{b}]')
