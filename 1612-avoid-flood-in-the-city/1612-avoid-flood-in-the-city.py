class Solution(object):
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1] * n              # default for rainy days
        full = {}                   # lake -> index of the last day it rained
        dry_days = []               # indices of days we can use to dry
        import bisect               # for binary search

        for i, lake in enumerate(rains):
            if lake == 0:
                # It's a sunny day, we can dry later
                dry_days.append(i)
                ans[i] = 1          # temporarily mark (will adjust later)
            else:
                # It's raining on a lake
                if lake in full:
                    # This lake is already full — must have been dried before now
                    last_rain = full[lake]
                    # Find a dry day after the last rain
                    idx = bisect.bisect_right(dry_days, last_rain)
                    if idx == len(dry_days):
                        # No available dry day after last rain — flood
                        return []
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake   # dry this lake on that day
                    dry_days.pop(idx)     # remove that dry day (used)
                # Update last rain day
                full[lake] = i
        return ans