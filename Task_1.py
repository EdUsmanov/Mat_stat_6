import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

c1 = (zp * ks).mean() - zp.mean() * ks.mean()
c2 = np.cov(zp, ks, ddof=0)
std_zp = zp.std(ddof=0)
std_ks = ks.std(ddof=0)
corr = c1 / (std_zp * std_ks)

print(c1)
print(c2)
print(corr)
