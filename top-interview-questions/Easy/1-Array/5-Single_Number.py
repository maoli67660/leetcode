'''
136. 只出现一次的数字 (简单)
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import Counter
from  functools import reduce
from operator import xor

# 方法1 懒人做法，调用Counter
def singleNumber(nums):
    return min(Counter(nums).items(), key=lambda x:x[1])[0]


# 方法2
# 一个集合记录是否访问过元素
def singleNumber2(nums):
    _set = set()
    for item in nums:
        if item in _set:
            _set.remove(item)
        else:
            _set.add(item)
    return list(_set)[0]

# 方法3
# 使用异或

def singleNumber3(nums):
    return reduce(xor,nums)
if __name__ == '__main__':
    assert singleNumber([4, 1, 2, 1, 2]) == 4
    assert singleNumber([2,2,1]） == 1
                        
