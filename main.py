from fastapi import FastAPI

app = FastAPI()

# route:
@app.get("/") # ini adalah route berdasarkan http method GET
async def index() -> dict[str, str]: # Fungsi ini akan dipanggil ketika ada request ke endpoint "/"
    return {"message": "Hello, World!"}

@app.get('/about')
async def about() -> str:
    return 'An exceptional FastAPI application'