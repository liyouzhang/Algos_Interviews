# 717. 1-bit and 2-bit Characters
# We have two special characters. The first character can be represented by one bit 0. 
# The second character can be represented by two bits (10 or 11).
# Now given a string represented by several bits. 
# Return whether the last character must be a one-bit character or not. 
# The given string will always end with a zero.

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
    def one_bits(bits):
        ### 20200401 - solution 1
        if len(bits) == 1 & bits[0] == 0:
                return True
        else:
            new_bits = "".join(str(x) for x in bits)
            e = []
            for i in new_bits.split('11'):
                e.extend(i.split('10')) ## note extend vs append
            if set(e[-1]) == '0': ## set is important here
                return True
            else:
                return False 



        ### 20200410 -- try
        # if the first bit = 0, then it is one-bit
        # if the first bit = 1, then it is two-bit
        # iterate through all the bits in the list 
        # the last two bits if start with 1 then False
        # the last two bits if start with 0 then True
        for i in range(len(bits)):
            if bits[i] == 0:
                
        
        # maybe only need to check the last two bits?
        ## have to consider edge cases where len(bits) <=0
        ## wrong. [1,1,0] 
        ## wrong. [1,1,1,0]
        if len(bits) == 1: #has to be zero
            return True
        if len(bits) == 2:
            if bits[0] == 1:
                return False
            if bits[0] == 0:
                return True
        else:
            if bits[-2] == 0:
                return True
            if bits[-2] == 1:
                if bits[-3] == 1:
                    return True
                if bits[-3] == 0:
                    return False
        
        