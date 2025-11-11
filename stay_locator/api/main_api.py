from fastapi import FastAPI

from stay_locator.common.destination import Destination
from stay_locator.data_collection.common.utils import OriginSources, QueryDetails
from stay_locator.generate_origins import generate_origins

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "New msg"}


@app.get("/generate_orgins/")
async def generate_origins_api(origin_sources: OriginSources, query_details: QueryDetails):
    origins = generate_origins(origin_sources=origin_sources, query_details=query_details)

    return origins


@app.post("/add_dest/")
async def submit_dest(destination: Destination):
    # TODO
    return {"message": "submission suggessful", "new_id": id}
