class Solution:
    def findComplement(self, num: int) -> int:
        outl = list(bin(num))
        l = outl[2:]
        for i in range(len(l)):
            if l[i] == '1':
                l[i] = '0'
            else:
                l[i] = '1'
        b = ''.join(l)
        return(int(b,2))

# Number complement