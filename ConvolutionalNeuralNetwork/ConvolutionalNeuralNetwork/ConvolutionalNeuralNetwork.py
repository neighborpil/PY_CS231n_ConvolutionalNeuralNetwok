"""
# string 편집
s = "hello"
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(10))
print(s.center(7))
print(s.replace('l', '(ell)'))
print('  world'.strip()) # trim




# list : array와 비슷하나, 사이즈를 조정 할 수 있고, 다른 타입을 담을 수 있다
xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1]) # result : 2
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)
x = xs.pop() # stack처럼 사용 가능
print(x, xs)



# list는 slicing기술이 강려크
nums = list(range(5))
print(nums)
print(nums[2:4]) # 2, 3
print(nums[2:]) # 2, 3, 4
print(nums[:2]) # 0, 1
print(nums[:]) # 전체 출력 : 0, 1, 2, 3, 4
print(nums[:-1]) # 0, 1, 2, 3
nums[2:4] = [8, 9]
print(nums) # 0, 1, 8, 9, 4



# enumrate
animals = ['cat', 'dog', 'bird']

for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

#results
#1: cat
#2: dog
#3: bird


# list comprehension
nums = list(range(5))
squares = []
for num in nums:
    squares.append(num ** 2)
print(squares)

# list comprehension containg conditions
nums = list(range(5))
even_square = [x ** 2 for x in nums if x % 2 == 0]
print(even_square)

"""

# dictionaries
d = {'cat' : 'cute', 'dog' : 'furry'}
print(d['cat'])
print ('cat' in d) # True : 딕셔너리에 키가 있는지 체크
print('cute' in d) # False : Value는 체크하지 않는다
d['fish'] = 'wet'
print(d['fish'])
print(d.get('monkey', 'N/A')) # 기본값을 'N/A'로 값이 없으면 출력
print(d.get('fish', 'N/A'))
del d['fish']
print(d.get('fish', 'N/A'))

# iteration
d = {'person' : 2, 'cat' : 4, 'spider' : 8}
for animal in d: # key 반환
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))

































