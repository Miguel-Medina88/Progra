from pydantic import BaseModel

class UserSchema(BaseModel):

    nombre_pelicula: str
    anio_estreno: int
    duracion: float
    director: str
    clasificacion: str
    genero: str