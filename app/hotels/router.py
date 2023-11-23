from datetime import date

from fastapi import APIRouter

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
async def get_hotels(
        location: str,
        date_from: date,
        date_to: date
) -> list[SHotels]:
    return await HotelsDAO.find_all(location, date_from, date_to)

