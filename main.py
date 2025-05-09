from abc import ABC, abstractmethod

## CLASSES FOR COMPOSITE DESIGN PATTERN
class FeatureComponent(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def display(self, indent: str = ""):
        pass

class CarFeature(FeatureComponent):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def display(self, indent: str = ""):
        print(f"{indent}- {self.name}: ${self.price:.2f}")

class FeatureGroup(FeatureComponent):
    def __init__(self, name:str):
        self.name = name
        self.features : list[FeatureComponent] = []

    def add_feature(self, feature: FeatureComponent):
        self.features.append(feature)

    def remove_feature(self, feature:FeatureComponent):
        self.features.remove(feature)

    def get_price(self):
        return sum(feature.get_price() for feature in self.features)

    def display(self, indent: str = ""):
        print(f"{indent}{self.name}:")
        for feature in self.features:
            feature.display(indent + "  ")

## CLASSES FOR BUILDER DESIGN PATTERN
class Car:
    def __init__(self, name: str =None, price: float =None, features: FeatureGroup =None):
        self.name = name
        self.base_price = price
        self.features : FeatureGroup = features

    def get_total_price(self):
        return self.base_price + self.features.get_price()

    def show_details(self):
        print(f"Car: {self.name}")
        print(f"Base Price: ${self.base_price:.2f}")
        self.features.display()
        print(f"Total: ${self.get_total_price():.2f}")

class CarBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_name(self, name:str):
        self.car.name = name
        return self

    def set_base_price(self, price:float):
        self.car.base_price = price
        return self

    def set_features(self, features: FeatureGroup):
        self.car.features = features
        return self

    def build(self):
        built_car = self.car
        self.reset()
        return built_car

class CarDirector:
    def __init__(self, builder:CarBuilder):
        self.builder = builder

    def construct_sports_car(self):
        return self.builder.set_name("Sports Car").set_base_price(60000).set_features(sportCarFeatures).build()

    def construct_family_car(self):
        return self.builder.set_name("Family Car").set_base_price(40000).set_features(familiyCarFeatures).build()

    def construct_electric_car(self):
        return self.builder.set_name("Electric Car").set_base_price(50000).set_features(electricCarFeatures).build()

## CLASSES FOR ITERATOR DESIGN PATTERN
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class CarOrder(Aggregate):
    def __init__(self):
        self.cars : list[Car] = []

    def add_item(self, car: Car):
        self.cars.append(car)

    def create_iterator(self):
        return OrderIterator(self)

class OrderIterator(Iterator):
    def __init__(self, car_order: CarOrder):
        self.car_order = car_order
        self.index: int = 0

    def has_next(self):
        return self.index < len(self.car_order.cars)

    def next(self):
        ordered_cars = sorted(self.car_order.cars, key=lambda car: car.name.lower())
        if self.has_next():
            car = ordered_cars[self.index]
            self.index += 1
            return car
        raise StopIteration

## CLASSES FOR ADAPTER DESIGN PATTERN
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Current Service
class LowPayment(PaymentProcessor):
    def pay(self, amount: float):
        if amount > 10000 or amount < 0:
            print("Payment failed! Too expensive.")
            return
        print(f"Successful payment of ${amount} with Low Payment")

# Current payment system
def checkout(processor:PaymentProcessor, amount):
    processor.pay(amount)

# New Service
class AnyPayment:
    def process_payment(self, amount: float, business_name: str):
        print("Processing...")
        if amount < 0:
            print("Process failed!")
            return
        print(f"Payment to {business_name} of ${amount} successful --- Any Payment")

class AnyPaymentAdapter(PaymentProcessor):
    def __init__(self, service: AnyPayment):
        self.service = service

    def pay(self, amount):
        self.service.process_payment(amount, "PERSONALIZED CARS")

### INDIVIDUAL FEATURES
premiumSound = CarFeature("Premium Sound System", 1500.99)
bluetooth = CarFeature("Bluetooth Connectivity", 1200.99)
proximitySensor = CarFeature("Proximity Sensor", 800.99)
screen = CarFeature("LCD Screen", 500.89)
bluePaint = CarFeature("Blue Paint", 1000.99)
redPaint = CarFeature("Red Paint", 1000.99)
turboEngine = CarFeature("Turbo Engine", 2000.50)
electricEngine = CarFeature("Electric Engine", 1399.99)
heatedSeats = CarFeature("Heated Seats", 1500.99)

## SPORTS CAR FEATURES
sportTechFeatures = FeatureGroup("Tech Features")
sportTechFeatures.add_feature(premiumSound)
sportTechFeatures.add_feature(bluetooth)

sportPaintJob = FeatureGroup("Paint Job")
sportPaintJob.add_feature(redPaint)
sportPaintJob.add_feature(bluePaint)

sportCarFeatures = FeatureGroup("Personalized Sports Car Features")
sportCarFeatures.add_feature(turboEngine)
sportCarFeatures.add_feature(sportTechFeatures)
sportCarFeatures.add_feature(sportPaintJob)

## FAMILY CAR FEATURES
familyTechFeatures = FeatureGroup("Tech Features")
familyTechFeatures.add_feature(bluetooth)

familiyCarFeatures = FeatureGroup("Personalized Family Car Features")
familiyCarFeatures.add_feature(heatedSeats)
familiyCarFeatures.add_feature(familyTechFeatures)

## ELECTRIC VEHICLE FEATURES
electricTechFeatures = FeatureGroup("Tech Features")
electricTechFeatures.add_feature(proximitySensor)
electricTechFeatures.add_feature(bluetooth)
electricTechFeatures.add_feature(screen)

electricCarFeatures = FeatureGroup("Personalized Electric Car Features")
electricCarFeatures.add_feature(electricEngine)
electricCarFeatures.add_feature(electricTechFeatures)

### BUILD CARS
builder = CarBuilder()
director = CarDirector(builder)

sportsCar = director.construct_sports_car()
familyCar = director.construct_family_car()

electricCar = director.construct_electric_car()


### MAKE ORDER AND CALCULATE TOTAL
order = CarOrder()
order.add_item(sportsCar)
order.add_item(familyCar)
order.add_item(electricCar)

iterator = order.create_iterator()

orderPrice = 0
print(f"\n------------------ ORDER -------------------")
while iterator.has_next():
    car = iterator.next()
    orderPrice += car.get_total_price()
    car.show_details()
    print()
print("--------------------------------------------")
print(f"ORDER TOTAL: ${orderPrice:.2f}\n")


### PROCESS PAYMENT
lowPayment = LowPayment()
anyPayment = AnyPayment()
adapter = AnyPaymentAdapter(anyPayment)

checkout(lowPayment, orderPrice)
checkout(adapter, orderPrice)
print()