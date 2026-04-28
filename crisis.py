import numpy as np
from landlab import Component


class Crisis(Component):
    """
    Landlab component for CRISIS model (Kassem et al., 2026).
    """

    _name = "Crisis"

    _unit_agnostic = True

    _info = {
        "topographic__elevation": {
            "dtype": float,
            "intent": "in",
            "optional": False,
            "units": "m",
            "mapping": "node",
            "doc": "Land surface topographic elevation",
        },
        "soil__depth": {
            "dtype": float,
            "intent": "in",
            "optional": False,
            "units": "m",
            "mapping": "node",
            "doc": "Depth of soil or weathered bedrock",
        },
        "bedrock__elevation": {
            "dtype": float,
            "intent": "in",
            "optional": False,
            "units": "m",
            "mapping": "node",
            "doc": "Bedrock surface elevation",
        },
        "topographic__slope": {
            "dtype": float,
            "intent": "in",
            "optional": False,
            "units": "m/m",
            "mapping": "node",
            "doc": "Topographic slope",
        },
    }

    def __init__(
        self,
        grid,
        cohesion=0.0,
        friction_angle=30.0,
    ):
        """
        Initialize the Crisis component.

        Parameters
        ----------
        grid : ModelGrid
            Landlab ModelGrid object
        cohesion : float, optional
            Cohesion parameter (default: 0.0)
        friction_angle : float, optional
            Friction angle parameter in degrees (default: 30.0)
        """
        super().__init__(grid)

        self._cohesion = cohesion
        self._friction_angle = friction_angle

        # Get references to grid fields
        self._topographic_elevation = self.grid.at_node["topographic__elevation"]
        self._soil_depth = self.grid.at_node["soil__depth"]
        self._bedrock_elevation = self.grid.at_node["bedrock__elevation"]
        self._topographic_slope = self.grid.at_node["topographic__slope"]
