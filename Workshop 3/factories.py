from abc import ABC, abstractmethod
from engines import ElectricEngine, GasEngine
from vehicles import VehicleFlyweight

class AbstractEngineFactory(ABC):
    """
    This class is an abstract factory to create both gas and electric engines.
    """

    @abstractmethod
    def create_electric_engine(self) -> ElectricEngine:
        """
        This method creates an electric engine.

        Returns:
        ElectricEngine: An electric engine object.
        """

    @abstractmethod
    def create_gas_engine(self) -> GasEngine:
        """
        This method creates a gas engine.

        Returns:
        GasEngine: A gas engine object.
        """

class HighEngineFactory(AbstractEngineFactory):
    """
    This class is a concrete factory to create expensive versions of engines.
    """

    def create_electric_engine(self) -> ElectricEngine:
        """
        Create a high-end electric engine.

        Returns:
        ElectricEngine: A high-end electric engine object.
        """
        return ElectricEngine(
            torque=180,
            maximum_speed=300,
            dimensions="200x200x200",
            power=200,
            stability="high",
            weight=100.9
        )

    def create_gas_engine(self) -> GasEngine:
        """
        Create a high-end gas engine.

        Returns:
        GasEngine: A high-end gas engine object.
        """
        return GasEngine(
            torque=210,
            maximum_speed=400,
            dimensions="210x200x250",
            power=250,
            stability="medium",
            weight=120.5
        )

class PoorEngineFactory(AbstractEngineFactory):
    """
    This class is a concrete factory to create cheap versions of engines.
    """

    def create_electric_engine(self) -> ElectricEngine:
        """
        Create a low-end electric engine.

        Returns:
        ElectricEngine: A low-end electric engine object.
        """
        return ElectricEngine(
            torque=90,
            maximum_speed=100,
            dimensions="100x100x100",
            power=50,
            stability="low",
            weight=63.4
        )

    def create_gas_engine(self) -> GasEngine:
        """
        Create a low-end gas engine.

        Returns:
        GasEngine: A low-end gas engine object.
        """
        return GasEngine(
            torque=100,
            maximum_speed=150,
            dimensions="110x100x150",
            power=100,
            stability="low",
            weight=80.5
        )

class VehicleFactory:
    """
    This class is responsible for creating vehicles using an engine factory.
    """

    def __init__(self, engine_factory: AbstractEngineFactory):
        """
        Constructor for the VehicleFactory class.

        Parameters:
        - engine_factory: An instance of an engine factory to create engines for vehicles.
        """
        self.__engine_factory = engine_factory
        self.__vehicles = {}

    def get_vehicle(self, make: str, model: str, year: int, engine_type: str):
        """
        Get a vehicle with the specified make, model, year, and engine type.

        Parameters:
        - make: Make of the vehicle.
        - model: Model of the vehicle.
        - year: Year of the vehicle.
        - engine_type: Type of engine for the vehicle (electric or gas).

        Returns:
        VehicleFlyweight: A vehicle object.
        """
        key = f"{make}-{model}-{year}-{engine_type}"
        if key not in self.__vehicles:
            engine = self.__get_engine(engine_type)
            vehicle = VehicleFlyweight(make, model, year, engine)
            self.__vehicles[key] = vehicle
        return self.__vehicles[key]

    def __get_engine(self, engine_type: str):
        """
        Get an engine of the specified type.

        Parameters:
        - engine_type: Type of engine (electric or gas).

        Returns:
        Engine: An engine object.
        """
        if engine_type == "electric":
            return self.__engine_factory.create_electric_engine()
        elif engine_type == "gas":
            return self.__engine_factory.create_gas_engine()
        else:
            raise ValueError("Invalid engine type")
