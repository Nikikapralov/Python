def solution():

    def integers():
        current_int = 1
        while True:
            yield current_int
            current_int += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        nums = []
        counter = 1
        for halve in seq:
            nums.append(halve)
            if counter == n:
                break
            counter += 1
        return nums

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
