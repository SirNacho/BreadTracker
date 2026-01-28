from pydantic import ConfigDict, BaseModel
from pydantic.alias_generators import to_camel

# from models.camel_model import CamelModel

class SerpSearchRequest(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    
    grocery_list: str