# First FastAPI 

from fastapi import FastAPI
# from fastapi import FastAPI
from services.products import get_all_data

app = FastAPI()

@app.get("/")
def root_msg():
    return {"message":"hello world!"}

@app.get('/products/{id}')
def get_products(id:int):
    p_list = ["pro1","pro2","pro3","pro4"]
    return {"product is ":p_list[id]}

@app.get("/productlist")
def getProductList():
    # pass
    return get_all_data()