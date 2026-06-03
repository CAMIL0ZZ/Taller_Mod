from fastapi import HTTPException


def get_or_404(obj):

    if obj is None:
        raise HTTPException(
            status_code=404,
            detail="Mascota no encontrada"
        )

    return obj