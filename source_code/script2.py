from fastapi import FastAPI, HTTPException, Query, Path
from services.products import get_all_data
from schema.product_schema import Product


app = FastAPI()

@app.get("/")
def root():
    return({"message":"welcome to FastAPI course"})

@app.get("/products")
def list_products(
name:str=Query(default=None, max_length=50, min_length=1, description="search by product name(case insensitive)"),
sort_by_price:bool=Query(default=False,description="want to see products by its price 'max-lower' or 'lower-max'"),
price_order:str = Query(default="asc",description="see all products by ascending order (need descending order just write 'desc')"),
limit: int = Query(
    default=10, ge=1,le=100, description="number of items to return."
),
offset: int = Query(
    default=0,ge=0,description="paggination offset!"
)
):
    # n_ = name.strip().lower()
    products = get_all_data()
    # return products
    if name:
        n_ = name.strip().lower()
        products = [p for p in products if n_ in p.get("name").lower()]
        if not products:
            raise HTTPException(status_code=404, detail=f"No products by {name}")
        else:
            len_products = len(products)
    if sort_by_price:
        is_reversed = (price_order.lower() == "desc")
        products = sorted(products,key=lambda p:p.get("price",0),reverse=is_reversed)
    
    products = products[offset:offset+limit]
    return {"total_products":len_products,"limit":limit, "items":products}

@app.get("/products/{product_id}")
def product_id(
    product_id:str = Path(...,min_length=36,max_length=36,examples="394d40e7-2ad5-335d-8738-c6af6be5a97f",description="UUID of the products"),

):
    products = get_all_data()

    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="page not found!")
    


@app.post("/products",status_code=201)
def create_product(product: Product):
    return product



