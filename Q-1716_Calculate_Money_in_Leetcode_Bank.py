class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Initialize the total amount of money in the bank to 0
        total = 0

        # Initialize the amount of money Hercy puts in on Monday to 1
        monday_amount = 1
        normal_amount = 1

        # Loop through the days
        for day in range(1, n+1):

            if day % 7 == 1:
                total += monday_amount
                monday_amount += 1
                normal_amount = monday_amount
            else:
                total += normal_amount
                normal_amount += 1


        return total