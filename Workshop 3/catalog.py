from typing import List
from vehicles import VehicleFlyweight

class Catalog:
    def __init__(self, vehicle_factory):
        """
        Constructor for the Catalog class.

        Parameters:
        - vehicle_factory: An instance of the vehicle factory used to create new vehicles in the catalog.
        """
        self.__vehicles = []  # List to store vehicles in the catalog
        self.__vehicle_factory = vehicle_factory  # Vehicle factory instance

    def get_all_vehicles(self) -> List[VehicleFlyweight]:
        """
        Get all vehicles in the catalog.

        Returns:
        - List of all vehicles in the catalog.
        """
        return self.__vehicles

    def get_price_by_range(self, min_price: float, max_price: float) -> List[VehicleFlyweight]:
        """
        Get vehicles within a price range.

        Parameters:
        - min_price: Minimum price of the vehicles.
        - max_price: Maximum price of the vehicles.

        Returns:
        - List of vehicles within the specified price range.
        """
        return [vehicle for vehicle in self.__vehicles if min_price <= vehicle.price <= max_price]

    def add_vehicle(self, make, model, year, engine):
        """
        Add a new vehicle to the catalog.

        Parameters:
        - make: Make of the vehicle.
        - model: Model of the vehicle.
        - year: Year of the vehicle.
        - engine: Engine of the vehicle.
        """
        # Create a new vehicle using the vehicle factory and add it to the catalog
        vehicle = self.__vehicle_factory.get_vehicle(make, model, year, engine)
        self.__vehicles.append(vehicle)
