class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_dict = {
        'O' : 0,
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000}
        
        num_str = s

        total = 0
        num_str += 'O'
        to_add = numeral_dict[num_str[0]]
        for i in range(1, len(num_str)):
            next_char = numeral_dict[num_str[i]]    
            if to_add < next_char:
                to_add *= -1
            total += to_add
            to_add = next_char
        return total