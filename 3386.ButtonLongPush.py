events = [[1,2],[2,5],[3,9],[1,15]]
def abs(x,y): 
    if x>=y: 
        return x-y 
    else: 
        return y-x

diff = events[0][1]
index = events[0][0]
for i in range(1,len(events)): 
    if abs(events[i-1][1],events[i][1])>diff: 
        diff = abs(events[i-1][1],events[i][1])
        index = events[i][0]
print(index)
