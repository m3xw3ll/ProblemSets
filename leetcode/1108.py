#https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address):
        output = address.replace(".", "[.]")
        return output
