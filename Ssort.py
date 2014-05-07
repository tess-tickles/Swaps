inList = [5,3,4,2,0,1]
answer = inList[0]
for number in inList:
    if number < answer:
        answer = number
print(answer)
