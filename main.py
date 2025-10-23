from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    ItemNumber: int


app = FastAPI()
result = []

@app.post("/items/")
async def create_item(item: Item):
    global result
    result.append(item.__dict__)
    return {"message":"successfully Data inserted"}


@app.get("/items/")
async def get_items():
    global result
    return result


@app.delete("/item/")
async def delete_item(ItemNumber: int):
    global result
    for item in result:
        if (item['ItemNumber'] == ItemNumber):
            result.remove(item)
    return {"message":"Data successfully deleted"}


@app.patch("/item/")
async def update_item(saad: Item):
    global result
    for item in range(0,len(result)):
        if (result[item]['ItemNumber'] == saad.__dict__['ItemNumber']):
            result[item] = saad.__dict__
    return {"message":"Data successfully updated"}