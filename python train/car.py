class Car:
    def __init__(self,model,years,color,for_sale):
        self.model = model
        self.years = years
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print("you drive the car",{self.model})
    
    def stop(self):
        print("you stop the car",{self.model})