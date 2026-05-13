from typing import Literal

from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    rainfall: float = Field(gt=0, description="Rainfall in mm")
    slope: float = Field(ge=0, le=90, description="Slope in degrees")
    soil_type: Literal["clay", "sand", "gravel", "silt"] = Field(description="Type of soil")