class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        endTime -= 1
        for s, e in self.booked:
            if s <= startTime <= e or s <= endTime <= e:
                return False
            if startTime < s and endTime > e:
                return False
        self.booked.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)