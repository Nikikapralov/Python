def powersOf2(n):
    # print("n:"+str(n))
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2))
        # print("prev:"+str(prev))
        print(prev)
        curr = prev*2
        print(curr)
        return curr

powersOf2(50)

"""So since we are dividing and taking the result of this division,
this will be a time complexity of O(log N)"""