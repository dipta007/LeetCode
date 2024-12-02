class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return False

            return True

        def biggest_prime_lt(n):
            for i in range(n-1, -1, -1):
                if prime(i):
                    return i
                
            return 0

        prev = 0
        for v in nums:
            if v <= prev:
                return False
            prime_v = biggest_prime_lt(v - prev)
            prev = v - prime_v

            # print(prime_v, prev)

        return True

