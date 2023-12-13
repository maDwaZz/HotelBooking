import asyncio
from datetime import date, datetime

from fastapi import APIRouter, Query

from fastapi_cache.decorator import cache

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotels, SHotel

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("/id/{hotel_id}")
async def get_hotel(
        hotel_id: int
) -> SHotel:
    return await HotelsDAO.find_by_id(hotel_id)


@router.get("/{location}")
@cache(expire=20)
async def get_hotels_by_location_and_time(
        location: str,
        date_from: date = Query(..., description=f"Например: {datetime.now().date()}"),
        date_to: date = Query(..., description=f"Например: {datetime.now().date()}")
) -> list[SHotels]:
    return await HotelsDAO.search_for_hotels(location, date_from, date_to)

