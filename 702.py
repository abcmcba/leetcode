class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 1
        while reader.get(right) < target:
            left = right
            right *=2

        while left <= right:
            mid = right - (right - left)//2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) >= target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
