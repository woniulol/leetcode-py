class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            str_x = str(x)
            len_x = len(str_x)
            largest = 2**31 - 1

            digit = 1
            cur_sum = 0

            for i in range(len_x):
                size = int(str_x[i]) * digit
                remaining = largest - cur_sum
                if remaining >= size:
                    cur_sum += size
                    digit *= 10
                else:
                    return 0

            return cur_sum

        else:
            str_x = str(x)[1:]
            len_x = len(str_x)
            smallest = -(2**31)

            digit = -1
            cur_sum = 0

            for i in range(len_x):
                size = int(str_x[i]) * digit
                remaining = smallest - cur_sum
                if remaining <= size:
                    cur_sum += size
                    digit *= 10
                else:
                    return 0

            return cur_sum
