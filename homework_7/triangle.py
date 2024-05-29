"""Triangle"""
# pylint: disable-msg=C0103

star = "*"
N = 10
for i in range(N):
    print((star + star * i * 2).center(N * 2 + 1))
