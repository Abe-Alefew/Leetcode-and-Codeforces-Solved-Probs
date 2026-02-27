class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        len_output = len(output)
        for word in strs[1:]:
            while output != word[0:len_output]:
                len_output -=1
                if len_output == 0:
                    return ""
                

                output = output [0:len_output]
        
        return output


