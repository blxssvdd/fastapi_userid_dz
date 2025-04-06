from fastapi import FastAPI, Path, Query, Header
from typing import Optional
from datetime import datetime
import uvicorn


app = FastAPI()


@app.get("/users/{user_id}")
def get_user_info(
    user_id: int = Path(..., description="ID користувача"),
    timestamp: Optional[str] = Query(None, description="Час"),
    x_client_version: str = Header(..., description="Версія")
):

    current_time = timestamp or datetime.utcnow().isoformat()

    return {
        "user_id": user_id,
        "Час": current_time,
        "Версія": x_client_version,
        "Повідомлення": f"Hello, user {user_id}!"
    }



if __name__ == "__main__":
    uvicorn.run("main:app")