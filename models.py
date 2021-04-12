from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4


class Contact(BaseModel):
    cid: UUID = Field(default_factory=uuid4)
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone: Optional[str]
    mail: Optional[str]


class Contacts(BaseModel):
    contacts: List[Contact] = []
