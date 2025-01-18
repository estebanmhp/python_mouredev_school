from fastapi import APIRouter

# Default URL -> prefix="/products"

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"Error": "Not found"}}) 

products_list = ["Item_01", "Item_02", "Item_03", "Item_04", "Item_05"] 

# "/" = "/products"

@router.get("/") 
async def products():
    return products_list

@router.get("/{id}")
async def products_id(id: int):
    return products_list[id]