from datetime import date

from sqlalchemy import insert, select, func, and_
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all(
            cls,
            hotel_id,
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
                Rooms.id,
                Rooms.hotel_id,
                Rooms.name,
                Rooms.description,
                Rooms.services,
                Rooms.price,
                Rooms.quantity,
                Rooms.image_id,
                (Rooms.price * (date_to - date_from).days).label("total_cost"),
                (Rooms.quantity - func.count(booked_rooms.c.id)).label("rooms_left")). \
                join(Hotels, Hotels.id == Rooms.hotel_id, isouter=True). \
                join(booked_rooms, Rooms.id == booked_rooms.c.room_id, isouter=True). \
                group_by(Rooms.id). \
                where(Rooms.hotel_id == hotel_id)

            result = await session.execute(query)
            return result.mappings().all()
