import urllib.parse

class Stocker():
    def __init__(self):
        self.stock = {}
        self.sales = 0

    def __call__(self, url):
        qs = urllib.parse.urlparse(url).query
        action = urllib.parse.parse_qs(qs) # dict

        func = action['function'][0]
        if func == 'addstock':
            self.addstock(action)
            ans = -1
        elif func == 'checkstock':
            ans = self.checkstock(action)
        elif func == 'sell':
            self.sell(action)
            ans = -1
        elif func == 'checksales':
            ans = 'sales: {}'.format(self.sales)
        elif func == 'deleteall':
            self.stock = {}
            self.price = {}
            self.sales = 0
            ans = -1

        #print(self.stock)
        return ans if ans != -1 else ''

    def addstock(self, action):
        key = action['name'][0]
        if key not in self.stock:
            self.stock[key] = 0
        amount = int(action['amount'][0]) if 'amount' in action else 1
        self.stock[key] += amount

    def checkstock(self, action):
        if 'name' in action:
            key = action['name'][0]
            ans = key + ': ' +  str(self.stock[key])
        else:
            ans = ''
            for key in self.stock:
                value = self.stock[key]
                ans += f'{key}: {value} \n'
        return ans

    def sell(self, action):
        key = action['name'][0]
        amount = int(action['amount'][0]) if 'amount' in action else 1
        price = int(action['price'][0]) if 'price' in action else 0
        self.stock[key] -= amount
        self.sales += amount * price
        #print('sales: ' + str(self.sales))
