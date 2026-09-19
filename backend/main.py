from fastapi import FastAPI

app = FastAPI(title="Lyria OS API")


@app.get("/")
def root():
    return {"message": "Lyria OS Backend Running 🚀"}