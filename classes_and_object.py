

print('=========================One==========================')

import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data
    
    def mean(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
    
    def mode(self):
        c = Counter(self.data)
        mode_freq = max(c.values())
        return [k for k, v in c.items() if v == mode_freq]
    
    def range(self):
        return max(self.data) - min(self.data)
    
    def variance(self):
        mean = self.mean()
        return sum((x - mean)**2 for x in self.data) / (len(self.data) - 1)
    
    def standard_deviation(self):
        return math.sqrt(self.variance())
    
    def minimum(self):
        return min(self.data)
    
    def maximum(self):
        return max(self.data)
    
    def count(self):
        return len(self.data)
    
    def percentile(self, p):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        k = (n - 1) * (p / 100)
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return sorted_data[int(k)]
        else:
            d0 = sorted_data[int(f)] * (c - k)
            d1 = sorted_data[int(c)] * (k - f)
            return d0 + d1
    
    def frequency_distribution(self):
        c = Counter(self.data)
        total = sum(c.values())
        return {k: v/total for k, v in c.items()}

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


print('=================================Two==========================')

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        return sum(income[0] for income in self.incomes)

    def total_expense(self):
        return sum(expense[0] for expense in self.expenses)

    def account_info(self):
        print(f"{self.firstname} {self.lastname}'s Account Balance\n")
        print(f"Total Income: {self.total_income()}\n")
        print(f"Total Expense: {self.total_expense()}\n")
        print(f"Account Balance: {self.account_balance()}\n")

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()


