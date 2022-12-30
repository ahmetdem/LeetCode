class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        valid = set()
        def fix(email):
            email = email.split("@")
            email[0] = email[0].split("+")
            
            if len(email[0]) == 2:
                del email[0][1]
            
            email[0] = email[0][0].replace(".", "")
            
            return "@".join(email)

        for email in emails:
            valid.add(fix(email))
            
        return len(valid)