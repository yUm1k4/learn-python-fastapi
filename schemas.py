# Schemas ini untuk mendefinisikan struktur data yang digunakan dalam aplikasi
# di Python, biasanya menggunakan Pydantic untuk membuat model data utk validasi dan serialisasi.
# Juga kalo pake Pydantic, dokomentasi API otomatis akan memiliki example value dan schema yang jelas.

from datetime import date
from enum import Enum
from pydantic import BaseModel

# Enum untuk genre musik yang digunakan dalam URL
class GenreURLChoices(Enum):
    ROCK = 'rock'
    GRUNGE = 'grunge'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'
    
class Band(BaseModel): # inherits dari BaseModel
    # contoh: 'id': 1, 'name': 'The Beatles', 'genre': 'Rock'
    id: int
    name: str
    genre: str
    albums: list['Album'] = []  # ini adalah daftar album yang dimiliki band, defaultnya adalah list kosong
# 'Alumb' menggunakan 'Forward declaration' untuk menghindari error saat menggunakan tipe data yang belum didefinisikan
    
class Album(BaseModel):
    # contoh: 'title': 'Abbey Road', 'release_date': '1969-09-26'
    title: str
    release_date: date