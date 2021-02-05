class Category:
    category_name = ""

    def __init__(self, category_name_init):
        self.balance = 0
        self.category_name = category_name_init
        self.ledger = list()

    def deposit(self, amount, description=None):
        if description == None:
            description = ""
        self.depositData = dict()
        self.depositData["amount"] = amount
        self.depositData["description"] = description
        self.ledger.append(self.depositData)

    def withdraw(self, amount, description=None):
        if description == None:
            description = ""
        if self.check_funds(amount) == True:
            self.withdrawData = dict()
            self.withdrawData["amount"] = amount * (-1)
            self.withdrawData["description"] = description
            self.ledger.append(self.withdrawData)
            return True
        else:
            return False

    def get_balance(self):
        self.list_for_balance = list()
        for item in self.ledger:
            self.list_for_balance.append(item["amount"])
        self.balance = sum(self.list_for_balance)
        return self.balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " +
                          budget_category.category_name)
            budget_category.deposit(
                amount, 'Transfer from '+self.category_name)
            return True
        else:
            return False

    def check_funds(self, amount):
        self.get_balance()
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        self.elements = ""
        self.spaces = " "
        self.get_balance()
        for item in self.ledger:
            self.new_elem = item["description"][0:23] + \
                self.spaces+str('{0:.2f}'.format(float(item["amount"])))
            if len(self.new_elem) < 30:
                self.newspaces = " " * (30 - len(self.new_elem)+1)
                self.new_elem = item["description"][0:23] + \
                    self.newspaces+str('{0:.2f}'.format(float(item["amount"])))
            self.elements = self.elements + self.new_elem + '\n'
        return self.category_name.center(30, '*') + '\n' + str(self.elements).rstrip() + '\n' + "Total: " + str(self.balance).rstrip()


def create_spend_chart(categories):
    data_spend_chart = dict()
    total_spend = list()
    list_spend_bis = list()
    list_spend = list()

    for item in categories:
        list_spend_bis = list()
        for amount in item.ledger:
            if amount['amount'] < 0:
                list_spend_bis.append(amount['amount'])
                list_spend.append(amount['amount'])

        data_spend_chart[item.category_name] = sum(list_spend_bis)
    total_spend.append(list_spend_bis)
    total = sum(list_spend)

    list_cat = list()
    list_spend = list()
    list_percent = list()
    for cat, spend in data_spend_chart.items():
        list_cat.append(cat)
        list_spend.append(spend)
    for item in list_spend:
        list_percent.append((round((item/total)*100)))

    first_line = "Percentage spent by category"

    # While loop pour dérouler les pourcentages verticalement tout en acolant les "o" au bon moment
    i = 100
    full_string = ""
    percent_stg = ""
    while i >= 0:
        left_area = str(i).rjust(3, " ")+'| '

        dot_area = ""
        for item in list_percent:
            if item < i:
                dot_area += '   '
            else:
                dot_area += 'o  '
        full_string = left_area + str(dot_area)
        percent_stg = percent_stg+full_string+'\n'

        i -= 10

    length_line = len(list_cat)
    longest_cat_len = len(max(list_cat, key=len))

    # Faire les tirets
    line_tiret = "    " + ((len(dot_area)+1) * "-")

    # while pour construire les nom de categories
    y = 0
    leftblank = "     "
    string_cat_name = ""
    total_cat_stg = ""

    while y != longest_cat_len:
        x = 0
        name_area = ""
        while x < length_line:
            try:
                name_area = name_area + list_cat[x][y] + "  "
            except:
                name_area = name_area + "   "
            x = x + 1
        string_cat_name = leftblank+name_area
        total_cat_stg = total_cat_stg+string_cat_name+'\n'
        y += 1

    complete_stg = first_line+'\n'+percent_stg + \
        line_tiret+'\n'+total_cat_stg.rstrip() + "  "
    return complete_stg
