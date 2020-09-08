#Given a valid (IPv4) IP address, return a defanged version of that IP address.

#A defanged IP address replaces every period "." with "[.]".

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")

# Time Complexity : O(n)
# Space Complexity : O(1)
