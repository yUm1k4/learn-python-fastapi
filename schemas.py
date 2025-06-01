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
    ELECTRONIC = 'electronic'
    
class GenreChoices(Enum):
    ROCK = 'Rock'
    GRUNGE = 'Grunge'
    METAL = 'Metal'
    HIP_HOP = 'Hip-Hop'
    ELECTRONIC = 'Electronic'
    
    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            for member in cls:
                # Cocokkan dengan mengabaikan case
                if member.value.lower() == value.lower():
                    return member
        # Jika tidak ada yang cocok, biarkan Pydantic/Enum standar menangani error
        return None
    
class BandBase(BaseModel): # inherits dari BaseModel
    # contoh: 'id': 1, 'name': 'The Beatles', 'genre': 'Rock'
    # id: int
    name: str
    genre: GenreChoices # menggunakan Enum untuk genre musik, ini akan memberikan pilihan yang terbatas
    # 'Album' menggunakan 'Forward declaration' untuk menghindari error saat menggunakan tipe data yang belum didefinisikan
    albums: list['Album'] = []  # ini adalah daftar album yang dimiliki band, defaultnya adalah list kosong
    
class Album(BaseModel):
    # contoh: 'title': 'Abbey Road', 'release_date': '1969-09-26'
    title: str
    release_date: date
    
class BandCreate(BandBase): # BandCreate adalah turunan dari BandBase yang meng-inherit semua field dari BandBase
    pass # artinya tidak ada tambahan field, hanya untuk membuat model khusus untuk pembuatan band baru
    
    # tidak memerlukan @field_validator khusus untuk genre lagi
    # KARENA _missing_ sudah menangani case-insensitivity.
    # @field_validator('genre') # add validator utk genre
    # def title_case_genre(cls, value):
    #     # return value.title() if isinstance(value, str) else value.value # mengubah genre menjadi title case jika berupa string, atau mengambil value jika berupa Enum
    #     return value.title()

class BandWithID(BandBase):
    id: int # menambahkan field id untuk model yang memiliki ID