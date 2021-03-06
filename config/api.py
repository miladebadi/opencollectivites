from ninja import NinjaAPI
from core.api import router as core_router
from francesubdivisions.api import router as fs_router
from aspic.api import router as aspic_router

api = NinjaAPI()


api.add_router("/core/", core_router)
api.add_router("/france/", fs_router)
api.add_router("/aspic/", aspic_router)
