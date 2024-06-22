from fastapi import FastAPI, Depends
from database import startup_db_client, shutdown_db_client, get_database

app = FastAPI()

app.add_event_handler("startup", startup_db_client)
app.add_event_handler("shutdown", shutdown_db_client)

@app.post("/send_data")
async def insert_sample_data(sample_data: dict, db=Depends(get_database)):
    try:
        collection = db['sample-users']
        result = await collection.insert_one(sample_data)
        return {"id of inserted record": str(result.inserted_id)}
    except Exception as e:
        return {"error": str(e)}
