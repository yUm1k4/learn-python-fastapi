### Buat Virtual Environment
```bash
python -m venv venv-fastapi
```

#### Aktifkan Virtual Environment
###### Windows
```bash
.\venv-fastapi\Scripts\activate
```
###### Linux/MacOS
```bash
source venv-fastapi/bin/activate
```

### Menonaktifkan Virtual Environment
```bash
deactivate
```

### Jalankan Aplikasi
```bash
uvicorn main:app --reload
```