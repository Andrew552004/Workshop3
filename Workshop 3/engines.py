class Engine:
    """
    This class represents an abstraction of an engine for any vehicle.
    """

    def __init__(self, torque: float, maximum_speed: float, dimensions: str,
                 power: float, stability: str, weight: float):
        """
        Constructor for the Engine class.

        Parameters:
        - torque: Torque of the engine.
        - maximum_speed: Maximum speed of the engine.
        - dimensions: Dimensions of the engine.
        - power: Power output of the engine.
        - stability: Stability of the engine.
        - weight: Weight of the engine.
        """
        self.torque = torque
        self.maximum_speed = maximum_speed
        self.dimensions = dimensions
        self.power = power
        self.stability = stability
        self.weight = weight

class GasEngine(Engine):
    """
    This class represents the behavior of a gas engine.
    """

class ElectricEngine(Engine):
    """
    This class represents the behavior of an electric engine.
    """
