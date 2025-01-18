from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
async def products():
    return ["Item_01", "Item_02", "Item_03", "Item_04", "Item_05"] 