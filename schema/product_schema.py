from pydantic import BaseModel, Field
from typing import Annotated


class Product(BaseModel):
    id: str
    sku: Annotated[str,Field(min_length=6,max_length=36,title="SKU",description="Stock keeping Unit",examples=["SHAR-235GB-003","SAMS-253GB-003"])]
    name: str
