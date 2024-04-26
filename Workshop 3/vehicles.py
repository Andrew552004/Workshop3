from engines import Engine

class VehicleFlyweight:
    """
    This class represents the intrinsic data of a vehicle.
    """

    def __init__(self, make: str, model: str, year: int, engine: Engine):
        """
        Constructor for the VehicleFlyweight class.

        Parameters:
        - make: Make of the vehicle.
        - model: Model of the vehicle.
        - year: Year of the vehicle.
        - engine: Engine object associated with the vehicle.
        """
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

class Vehicle:
    """
    This class represents a complete vehicle object.
    """

    def __init__(self, flyweight: VehicleFlyweight, chassis: str, price: float, consumption: float):
        """
        Constructor for the Vehicle class.

        Parameters:
        - flyweight: VehicleFlyweight object representing the intrinsic data of the vehicle.
        - chassis: Chassis type of the vehicle.
        - price: Price of the vehicle.
        - consumption: Fuel consumption of the vehicle.
        """
        self.flyweight = flyweight
        self.chassis = chassis
        self.price = price
        self.consumption = consumption

    def __str__(self):
        """
        String representation of the Vehicle object.

        Returns:
        - str: String representation of the Vehicle object.
        """
        return f"Vehicle: {self.flyweight.model} - {self.flyweight.year} - {self.price} - {self.consumption} - {self.flyweight.engine} - {self.chassis}"

class Truck(Vehicle):
    """
    This class is a concrete implementation of a truck.
    """

    def calculate_gas_consumption(self) -> float:
        """
        Calculate gas consumption based on engine values.

        Returns:
        - float: Fuel consumption of the truck.
        """
        consumption = (
            (1.1 * self.flyweight.engine.power)
            + (0.2 * self.flyweight.engine.weight)
            + (0.3 if self.chassis == "A" else 0.5)
        )
        return consumption
