class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        # calculate the total waiting time
        # maintain a timer =0
        # waiting time for a customer = if timer > starting time then = timer - starting time + duration
        # else
        # waiting time for a customer = duration
        numCustomers = len(customers)
        waitTime = 0
        timer = 0
        for customer in customers:
            startTime = customer[0]
            duration = customer[1]
            if timer > startTime:
                waitTime += timer - startTime + duration
                timer = timer + duration
            else:
                waitTime += duration
                timer = startTime + duration
        
        return waitTime/numCustomers