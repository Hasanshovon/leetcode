class Solution:
    def convertDateToBinary(self, date: str) -> str:
        temp = [int(i) for i in date.split("-")]
        bin_ = [bin(n).replace("0b", "") for n in temp]
        up = ""
        for loc,val in enumerate(bin_):
            if loc == 0:
                up+=val
            else:
                up = up+"-"+val
        print(up)
        
# give me summary of the sudo code
# split the date into a list
# convert the date into binary
# remove the 0b from the binary
# join the binary into a string
# return the string

# write a note about the integer to binray conversion
# bin() function converts an integer to binary
# bin(5) = 0b101
# bin(5).replace("0b", "") = 101
# bin(5)[2:] = 101
# bin(5)[2:] is faster than bin(5).replace("0b", "")
