class Vehicle:
    premium_amount=0
    def __init__(self,vehicle_id,type,cost):
        self.vehicle_id=vehicle_id
        self.type=type
        self.cost=cost
        
    def calculate_premium_amount(self):
        if(self.type=="Two Wheeler"):
            self.premium_amount=self.cost*(2/100)
        elif(self.type=="Four Wheeler"):
            self.premium_amount=self.cost*(6/100)
            
        return self.premium_amount
    def displaydetails(self):
        self.premium_amount=int(self.premium_amount)
        print(self.vehicle_id)
        print(self.type)
        print(self.cost)
        print(self.premium_amount)
v1=Vehicle(1,"Two Wheeler",1000)

v1.calculate_premium_amount()
v1.displaydetails()