from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, Band  # Import GenreURLChoices dari file schemas.py

app = FastAPI()

# Band data
BANDS = [ # List of dictionaries representing bands
    {'id': 1, 'name': 'The Beatles', 'genre': 'Rock'},
    {'id': 2, 'name': 'Nirvana', 'genre': 'Grunge'},
    {'id': 3, 'name': 'Queen', 'genre': 'Rock', 'albums': [
        {'title': 'A Night at the Opera', 'release_date': '1975-11-21'},
        {'title': 'News of the World', 'release_date': '1977-10-28'}
    ]},
    {'id': 4, 'name': 'Metallica', 'genre': 'Metal', 'albums': [
        {'title': 'Master of Puppets', 'release_date': '1986-03-03'},
        {'title': 'The Black Album', 'release_date': '1991-08-12'}
    ]},
]

# route:
@app.get('/bands')
# async def bands() -> list[dict]: # sebelumnya seperti ini
# async def bands() -> list[Band]: # jadi seperti ini jika menggunakan model Band
async def bands(
    genre: GenreURLChoices = None,
    has_albums: bool = False
) -> list[Band]: # ketambahan query parameter genre
    # return BANDS

    band_list = [Band(**b) for b in BANDS]  # Menggunakan unpacking untuk mengonversi dictionary ke model Band
    # unpacking adalah proses mengambil nilai dari dictionary dan memasukkannya ke dalam model Band.

    if genre is not None:
        band_list = [
            b for b in band_list if b.genre.lower() == genre.value
        ]

    if has_albums:
        band_list = [
            # b for b in band_list if hasattr(b, 'albums') and b.albums
            # atau bisa dengan cara:
            b for b in band_list if len(b.albums) > 0
        ]

    return band_list  # Mengembalikan daftar band yang sesuai dengan filter genre dan has_albums

# Endpoint utk mendapatkan informasi band berdasarkan ID
@app.get('/bands/{band_id}', status_code=200)
# async def band(band_id: int) -> dict: # cara lama sebelum menggunakan model Band
async def band(band_id: int) -> Band:
    # # Looping melalui daftar band
    # for band in BANDS: 
    #     if band['id'] == band_id:
    #         return band
        
    # return {"error": "Band not found"}
    
    # ATAU bisa dengan cara:

    # next() digunakan untuk mendapatkan elemen pertama yang cocok dengan kondisi, atau None jika tidak ada yang cocok.
    # band = next((b for b in BANDS if b['id'] == band_id), None) # cara lama sebelum menggunakan model Band
    band = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found") # Jika band tidak ditemukan, mengembalikan respons dengan status code 404 dan pesan "Band not found"
    
    # raise HTTPException digunakan untuk mengembalikan respons HTTP dengan status code 200 dan detail berisi informasi band
    # raise HTTPException(status_code=200, detail=band) # HTTPException dari FastAPI digunakan untuk mengembalikan respons HTTP dengan status code tertentu
    return band