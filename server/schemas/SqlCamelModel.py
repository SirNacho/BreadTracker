from pydantic import ConfigDict, AliasGenerator
from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel

class SqlCamelModel(SQLModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_camel,
            serialization_alias=to_camel,
        ),
        populate_by_name=True,
        from_attributes=True
    )