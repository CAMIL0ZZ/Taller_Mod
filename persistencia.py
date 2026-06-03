from mascota_model import *
from sqlmodel import Session, select


def create_mascota(session: Session, mascota: MascotaBase):

    db_mascota = Mascota.model_validate(mascota)

    session.add(db_mascota)
    session.commit()
    session.refresh(db_mascota)

    return db_mascota


def get_one_mascota(session: Session, id: int):

    return session.get(Mascota, id)


def update_mascota(session: Session, id: int, mascota: MascotaUpdate):

    db_mascota = session.get(Mascota, id)

    if db_mascota is None:
        return None

    data = mascota.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(db_mascota, key, value)

    session.add(db_mascota)
    session.commit()
    session.refresh(db_mascota)

    return db_mascota


def delete_mascota(session: Session, id: int):

    db_mascota = session.get(Mascota, id)

    if db_mascota is None:
        return None

    session.delete(db_mascota)
    session.commit()

    return db_mascota