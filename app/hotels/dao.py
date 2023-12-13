from datetime import date

from sqlalchemy import insert, select, func, and_
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker, engine
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def search_for_hotels(
            cls,
            location,
            date_from,
            date_to
    ):
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.date_from <= date_to,
                    Bookings.date_to >= date_from
                )
            ).cte("booked_rooms")

            query = select(
                Hotels.id,
                Hotels.name,
                Hotels.location,
                Hotels.services,
                Hotels.rooms_quantity,
                Hotels.image_id,
                (Hotels.rooms_quantity - func.count(booked_rooms.c.id)).label("rooms_left")). \
                join(Rooms, Hotels.id == Rooms.id, isouter=True). \
                join(booked_rooms, Rooms.id == booked_rooms.c.room_id, isouter=True). \
                group_by(Hotels.id). \
                where(Hotels.location.like(f"%{location}%"))

            result = await session.execute(query)
            return result.mappings().all()

