import datetime
def convertTimestamp(input):
    if input[len(input)-1] == 'Z':
        newTime = datetime.datetime.fromisoformat(input[:-1])
        return newTime.strftime("%Y/%m/%d, %H:%M:%S")+" (UTC)"
