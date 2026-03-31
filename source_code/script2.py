from fastapi import FastAPI, HTTPException, Query
from services.products import get_all_data

app = FastAPI()

@app.get("/")
def root():
    return({"message":"welcome to FastAPI course"})

@app.get("/products")
def list_products(
name:str=Query(default=None, max_length=50, min_length=1, description="search by product name(case insensitive)"),
sort_by_price:bool=Query(default=False,description="want to see products by its price 'max-lower' or 'lower-max'"),
price_order:str = Query(default="asc",description="see all products by ascending order (need descending order just write 'desc')")
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
    
    return {"total_products":len_products, "items":products}
        
        
        






