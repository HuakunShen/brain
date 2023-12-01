# 1396. Design Underground System

https://leetcode.com/problems/design-underground-system/

Level: Medium

This is quite easy.

## Solution

This solution used 3 hash maps to store average travelling time, number of travels from one station to another, and
the starting time and station of a ongoing travel.

Every method takes constant time, preventing storing all travel records and linear search.

The `self.traveling` hash map is designed to store the station and start time of the current travel of a person, using
a nested dictinary structure, the inner dictionary can be replaced by a tuple to save more memory. I used a dictionary 
just to make it easier to understand.

```python
class UndergroundSystem:

    def __init__(self):
        self.traveling = {} # {id: {stationName: str, t: int}}
        self.count = defaultdict(lambda: 0) # {(station1, station2): number_of_travel}
        self.average_time = defaultdict(lambda: 0)  # {(station1, station2): time}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.traveling[id] = {"stationName": stationName, "t": t}
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time_taken = t - self.traveling[id]['t']
        start_station = self.traveling[id]['stationName']
        total_history_travel_time = self.average_time[(start_station, stationName)] * self.count[(start_station, stationName)]
        self.count[(start_station, stationName)] += 1
        self.average_time[(start_station, stationName)] = (total_history_travel_time + time_taken) / self.count[(start_station, stationName)]
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average_time[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```