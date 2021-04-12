from fastapi import Body, FastAPI, status, HTTPException, Response
from models import Contact, Contacts
from uuid import UUID

from cache import DictCache
from exceptions import ContactAlreadyExistsError, ContactNotExistsError

app = FastAPI()
app_cache = DictCache()


@app.get("/contacts", response_model=Contacts, status_code=status.HTTP_200_OK)
def get_all_contacts():
    return Contacts(contacts=[app_cache.get(key) for key in app_cache.get_keys()])


@app.post("/contacts", response_model=Contact, status_code=status.HTTP_201_CREATED)
def create_contact(
        contact: Contact = Body(
            Contact(first_name="John", last_name="Doe", phone="0123456789", mail="john.doe@mail.com"))
):
    try:
        app_cache.add(contact.cid, contact)
        return contact
    except ContactAlreadyExistsError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contact already exits")


@app.get("/contacts/{cid}", response_model=Contact, status_code=status.HTTP_200_OK)
def get_contact(
        cid: UUID
):
    try:
        return app_cache.get(cid)
    except ContactNotExistsError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")


@app.put("/contacts/{cid}", response_model=Contact, status_code=status.HTTP_200_OK)
def update_contact(
        cid: UUID,
        contact: Contact = Body(
            default=Contact(first_name="John", last_name="Doe", phone="0123456789", mail="john.doe@mail.com"))
):
    try:
        app_cache.update(cid, contact)
        return contact
    except ContactNotExistsError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")


@app.delete("/contacts/{cid}", response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(
        cid: UUID
):
    try:
        app_cache.delete(cid)
    except ContactNotExistsError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
