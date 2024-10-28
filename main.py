from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from moviesmodel import MovieModel
from schemas import UserSchema
from sqlmodel import select

app = FastAPI()

#? fastapi dev .\main.py

create_db_and_tables()

@app.post("/movies")
async def create_movies(movies_data: UserSchema, database: SessionDep):
    movies = MovieModel(
        nombre_pelicula= movies_data.nombre_pelicula,
        anio_estreno= movies_data.anio_estreno,
        duracion= movies_data.duracion,
        director= movies_data.director,
        clasificacion= movies_data.clasificacion,
        genero= movies_data.genero
    )
    
    database.add(movies)
    database.commit()
    database.refresh(movies)
    
    return movies

@app.get("/movies")
async def get_movies(database: SessionDep):
    statement = select(MovieModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/movies/{movie_id}")
async def get_movie_by_id(movie_id: int, database: SessionDep):
    movie = database.get(MovieModel, movie_id)
    
    if not movie:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Pelicula no encontrada")
    
    return movie