
# Questiion

1. Remove Duplicates
Giving a sorted array, remove the duplicated elements and keep the uniques elements only. 
For example, if the array is [1,1,3,3,3,3,5,5,9,9,9,9]. The unique elements should be [1,3,5,9]
Solution:

```python
arr = [1,1,3,3,3,3,5,5,9,9,9,9]
print set(arr)
Consider situation with only 1 element
def removeDuplicates(arr):
    if arr is None or len(arr)<=1:
        return arr
    
    res = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            res.append(arr[i])
    
    return res
    
print removeDuplicates(arr)

//Inplace, not allocation
def removeDuplicates(arr):
    if arr is None or len(arr)<=1:
        return arr
    
    i = 0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i += 1
            arr[i] =arr[j]
        j += 1
    
    return arr[:i+1][:]
    
    
    print removeDuplicates(arr)
```

2. Maximium continues subarry
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    newSum = nums[0]
    maxSum = nums[0]
    
    for v in nums[1:]:
        newSum = max(newSum+v,v)
        maxSum = max(maxSum,newSum)
        
    return maxSum

print maxSubArray(nums)
```

3. The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

```python
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

for i in range(10):
    print(fib(i))
```

Fast Solution
```python
//(Public) Returns F(n).
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]

// Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)
			
print fibonacci(100)
```


4. Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
```python
prices = []

def maxProfit(prices):
    minVal = prices[0]
    maxProfit = float('-inf')
    
    for i in prices:
        minVal = min(minVal, i)
        maxProfit = max(maxProfit,i-minVal)
	
	return maxProfit

print maxProfit(prices)
```


