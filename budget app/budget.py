class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.wt_amount_count = []
        
    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": self.amount, "description": self.description})
        
    def withdraw(self, wt_amount, wt_description=""):
        
        if self.check_funds(wt_amount):
            self.wt_amount = wt_amount
            self.wt_description = wt_description
            self.ledger.append({"amount": -abs(self.wt_amount), "description": self.wt_description})
            self.wt_amount_count.append(self.wt_amount)
            return True
        
        else: return False
        
    def get_balance(self):
        
        balance = 0
        
        for item in self.ledger:
            for k, v in item.items():
                if k == "amount":
                    balance += v
                
        return balance
        
    def transfer(self, tn_amount, tn_destination):
        self.tn_amount = tn_amount
        self.tn_destination = tn_destination
                
        if self.check_funds(tn_amount):
            self.ledger.append({"amount": -abs(self.tn_amount), "description": f"Transfer to {self.tn_destination.category}"})
            self.tn_destination.ledger.append({"amount": self.tn_amount, "description": f"Transfer from {self.category}"})
            self.wt_amount_count.append(self.tn_amount)
            return True
        
        else: return False
        
    def check_funds(self, amount):
        
        if amount > self.get_balance():
            return False
        else:
            return True 

    def __str__(self):
        
        title = self.category.center(30, "*")
        
        description_list = []
        amount_list = []
        
        nl = "\n"
        
        for item in self.ledger:
            for k, v in item.items():
                if k == "amount":
                    if len("{:.2f}".format(v)) > 7:
                        v_split = "{:.2f}".format(v).split(".")
                        amount_list.append(v_split[0][:4] + "." + v_split[1])
                    else:
                        amount_list.append("{:.2f}".format(v))
                else:
                    if k == "description":
                        if len(v) > 23:
                            description_list.append(v[:23])
                        else:
                            description_list.append(v)
                    
        dictionary = dict(zip(description_list, amount_list))
        
        for k, v in dictionary.items():
            dictionary[k] = str(v).rjust(30 - (len(k) + 1))
        
        total = self.get_balance()

        return title + nl + f'{nl.join(f"{key} {value}" for key, value in dictionary.items())}\nTotal: {total}'
      


def create_spend_chart(categories):
    balance = []
    category_name = []
    for category in categories:
        balance.append(round(sum(category.wt_amount_count),2))
        category_name.append(category.category.capitalize())

    bl_amnt = dict(zip(category_name, balance))
    
    total = 0
    nl = '\n'
    
    for value in bl_amnt.values():
        total += value
            
    for k, v in bl_amnt.items():
        bl_amnt[k] = round((v/total) * 100)

    
    chart = "Percentage spent by category"
    chart += nl

    for i in reversed(range(0,110, 10)):
        chart += str(i).rjust(3) + "| "
        for k, v in bl_amnt.items():
            if v >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += nl

    chart += "----------".rjust(14, " ")

    chart += nl + '     '
    
    maxLen = max(len(i) for i in category_name)
    
    for i in range(maxLen):
        for category in category_name:
            if len(category) > i:
                chart +=  category[i] + "  "
            else:
                chart += '   '
        if i < maxLen - 1:
            chart += nl + '     '

                
    return chart
    