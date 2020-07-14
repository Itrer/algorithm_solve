# 재귀로 순열을 만드는 구나!!!

# 중복을 허용하는 순열
class Solution:
    def recombi(self,n,k,result):  # 가능한 숫자, 뽑는 갯수
        path=[]
        index=0  # 위치 파악
        nums=[i for i in range(1,n+1)]
        self.dfs(nums,n,k,index,path,result)

    def dfs(self,nums,n,k,index,path,res):  # path는 경우의 수들, index는 현위치, k는 뽑아야 하는 갯수
        print(f"탐색 중: {index}")
        print(f"경우의 수 탐색: {path}")
        if k==0:
            res.append(path)
            return
        for i in range(index,n):
            self.dfs(nums,n,k-1,i,path+[nums[i]],res)


an1=[]
possible_num,length = map(int,input().split())

list1 = Solution()
list1.recombi(possible_num,length,an1)
for i in an1:
    print(*i)


'''
Combination questions can be solved with dfs most of the time. I'm following caikehe's approach. Also, 
if you want to fully understand this concept and backtracking, try to finish this post and do all the examples.

We have an array [1, 2, ..., n], if k == 0, meaning combination of zero numbers which is nothing (lines #7, 8, 9), right? Return [[]].

def combine(self, n, k):
    res = [] #1
    self.dfs(range(1,n+1), k, 0, [], res) #2
    return res #3
    
def dfs(self, nums, k, index, path, res):  #4
	print('index is:', index)
    print('path is:', path)
    if k == 0:  #7
        res.append(path)  #8
        return # backtracking  #9 
    for i in range(index, len(nums)):  #10
        self.dfs(nums, k-1, i+1, path+[nums[i]], res)  #11
        
Lines #1, 2, 3 are the main function, where you initialize res = []. Also, you call the dfs function to find all the combinations, and finally, 
you return the res. The dfs function is the main part of the code. Lines #7, 8 were explained before. 
dfsfuction goes into deeper levels until these two lines get activated. 
Keep reading.

Let's do an example for the rest! I define levels as the number of times dfs gets called recursively before moving on in the for loop of line #10.

---- Level 0 (input: nums, k=2, index = 0, path = [], res = []).
The idea of dfs is that it starts from first entry of nums = [1, 2, ..., n]. At first, nums[0] gets chosen in line #10, 
it calls the dfs again in line #11 with updated inputs and goes basically one level deer to choose the second number in the combination 
(note that his combination would look something like [1, ...], right? nums doesn't change, but since we have already chosen one entry, variables get updated k = k - 1. 
Also, since we're already chosen entry 0, index variable becomes i = i +1 to go one step deeper.

---- Level 1 (input: nums, k=1, index = 1, path = [1], res = []).
Now, in line #10, the range changes. It starts from 1 to len(nums). It goes in and calls dfs one more time.

--- Level 2 (input: nums, k=0, index = 2, path = [1,2]], res = []).
This time it gets stuck in line #7, and appends path to res. Now, res = [[1,2]].

Does this make sense?

All these level just return one combination, right? ( res = [[1,2]]). \
Remember going into deeper levels happened when we were in line #10 and called dfs for the first time in line #11, 
and then for the second time in level 1, and we ended up in level 2 and got stuck in line #7. 
Now, we go back one step to level 1 and move on in line #10. This time, i = 1 and index = 2. Again we go back to level 2 and return path = [1,3]. 
This will be appended to res to get to res = [[1,2],[1,3]]. Finally, we exhaust all indices in level 1. We end up with res = [[1,2],[1,3],[1,4]]. 
We go up one level, to level 0. Move on in line #10, this time, we'll get to path = [[2,3],[2,4]], and will update res = [[1,2],[1,3],[1,3],[2,3],[2,4]].
 We keep going to get the final combination, we're done.

If you want to fully understand how this works, try to print some variables at the start of your dfs function. I printed index and path and this is the outcome.

index is: 0
path is: []
index is: 1
path is: [1]
index is: 2
path is: [1, 2]
index is: 3
path is: [1, 3]
index is: 4
path is: [1, 4]
index is: 2
path is: [2]
index is: 3
path is: [2, 3]
index is: 4
path is: [2, 4]
index is: 3
path is: [3]
index is: 4
path is: [3, 4]
index is: 4
path is: [4]

Final output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
That's it!'''


