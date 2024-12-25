class Solution:
    def summaryRanges(self, nums: list) -> list:
        if len(nums) == 0:
            return nums
        if len(nums) < 2:
            return [str(x) for x in nums]
        current = nums[0]
        before = nums[0]
        out = []
        # if the v is current + 1 and not the end of the list, keep going
        # if the v is not current + 1 and not the end of the list:
        ## check does it have before or not, if not then append the number
        ## if yes append before->current
        # if the we are in the end of the list:
        ## check if v == current + 1 or not, if yes append before->current+1
        ## if not check again does current have different value than before
        ### if current != before then append before -> current, and then append v
        ### if current == before, append current, append v
        for i, v in enumerate(nums[1:]):
            if i != len(nums) - 2:
                if v == current + 1:
                    current = v
                elif v != current + 1:
                    if current == before:
                        out.append(str(current))
                    else:
                        out.append(f"{before}->{current}")
                    before = v
                    current = v
            else:
                if v == current + 1:
                    out.append(f"{before}->{v}")
                else:
                    if current == before:
                        out.append(str(current))
                    else:
                        out.append(f"{before}->{current}")
                    out.append(str(v))
        return out
