def lcm(nums):
    multiples = []
    while True:
        multiplier = 1
        for num in nums:
            product = num * multiplier
            if product in multiples:
                break
            multiples.append(product)
        multiplier += 1

    return multiples[-1]

if __name__ == "__main__":
    print(lcm([3,4,6]))