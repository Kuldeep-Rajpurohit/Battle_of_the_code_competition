"""
Jesse loves cookies. He wants the sweetness of all his cookies to be greater than value k. To do this, Jesse repeatedly mixes two cookies with the least sweetness. He creates a special combined cookie with:

sweetness =(1*Least sweet cookie + 2*2nd least sweet cookie).

He repeats this procedure until all the cookies in his collection have a sweetness >= k .
You are given Jesse's cookies. Print the number of operations required to give the cookies a sweetness >= k. Print -1 if this isn't possible.

Input Format

The first line consists of nintegers n, the number of cookies and k, the minimum required sweetness, separated by a space.
The next line contains n integers describing the array A where Ai is the sweetness of the ith cookie in Jesse's collection.
"""


import heapq

[no_of_cookies, min_sness] = map(int,input().split())
sness = map(int, input().split())
sness = list(sness)
heapq.heapify(sness)
no_of_opp = 0
if sum(sness) >= min_sness:
    while sness[0] < min_sness and no_of_opp <= no_of_cookies:
        no_of_opp += 1
        temp1 = heapq.heappop(sness)
        temp2 = heapq.heappop(sness)
        heapq.heappush(sness, temp1 + 2 * temp2)
    print (no_of_opp) if no_of_opp <= no_of_cookies else -1
else:
    print -1
