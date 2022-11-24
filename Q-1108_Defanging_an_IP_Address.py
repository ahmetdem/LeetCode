class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address = list(map(lambda x: x.replace('.', '[.]'), address))
        
        return "".join(address)