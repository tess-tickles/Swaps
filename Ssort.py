def ssort(inlist):
    answer = inList[0]
    for number in inList:
        if number < answer:
            answer = number
    return (answer)
