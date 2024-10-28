from sqlmodel import SQLModel, Field

class MovieModel(SQLModel, table = True):
    __tablename__ = "movies"
    
    id: int = Field(primary_key = True)
    nombre_pelicula: str
    anio_estreno: int
    duracion: float
    director: str
    clasificacion: str
    genero: str