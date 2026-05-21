class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return("")
        else:
            l, r = 0, len(self.store[key]) - 1
            most_recent = ""
            while l <= r:
                m = (l + r)//2
                if self.store[key][m][1] == timestamp:
                    return self.store[key][m][0]
                elif self.store[key][m][1] < timestamp:
                    l = m + 1
                    most_recent = self.store[key][m][0]
                elif self.store[key][m][1] > timestamp:
                    r = m - 1
            return most_recent

