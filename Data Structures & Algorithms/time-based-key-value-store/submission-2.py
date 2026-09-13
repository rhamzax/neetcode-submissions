class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        l, r = 0, len(self.timeMap[key]) - 1
        person = self.timeMap[key]
        res = ""
        while l <= r:
            mid = (l + r) // 2
            time = person[mid][0]
            if time > timestamp:
                r = mid - 1
            elif time <= timestamp:
                l = mid + 1
                res = person[mid][1]
        return res
