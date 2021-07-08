# [공유기 설치](https://www.acmicpc.net/problem/2110)
def fn(param):
    count = 1
    gong = 0
    print(f"[houses[gong], houses[i]] = ", end=" ")
    for i in range(1, n):
        if houses[i] - houses[gong] >= param:
            print(f"[{houses[gong]}, {houses[i]}]",end=", ")
            count += 1
            gong = i
    print(f"\ncount = {count} -> {count >= c}")
    return count >= c


def search():
    lo = 0
    hi = houses[n - 1] + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        print(f"[lo, hi] = [{lo}, {hi}], mid = {mid}")
        if fn(mid):
            lo = mid
        else:
            hi = mid
    return lo


n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()
print(houses)
print(search())
