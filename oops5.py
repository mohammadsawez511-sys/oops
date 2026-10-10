class product:
    def __init__(self,pid):
        self.pid = pid 


class category(product):
    def __init__(self, pid,pname,pcategory,price):
        super().__init__(pid)
        self.pname = pname
        self.pcategory = pcategory
        self.price = price 

class order(category):
    def __init__(self, pid, pname, pcategory, price,qty,payment_method):

        super().__init__(pid, pname, pcategory, price)
        self.qty = qty
        self.payment_method = payment_method

    def amount(self):
        print("ORDER DETAILS ")
        print(self.pid, self.pname, self.pcategory, self.price,self.qty,self.payment_method,sep="\t")
        return self.qty*self.price

S1 = order(101,"phone","electronic",10000,2,"CASh")
S2 = order(102,"computer","electronic",2500,1,"UPI")
S3 = order(103,"ear phone","electronic",2500,4,"credit card")

orders = [S1,S2,S3]
total_amount=0
print("TOTAL BILL")
for i in orders:
    total_amount+=i.amount()
print("TOTAL AMOUNT :",total_amount)    
