from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI KT",
    description="This is a test FastAPI application",
    version="1.0.0"
)

data = {
    "user": "dore",
    "phone": 125252525
}

def verify_token(token: str = Header(None)):
    if token != "apoloo565555sds":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return {
        "user": "Authorized"
    }

@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return {
        "message": "Access granted",
        "user": user,
        "data": data
    }