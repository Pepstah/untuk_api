import requests

response = requests.get("https://jsonplaceholder.typicode.com/albums")

print(response)

# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/albums")

# print(response)

# # Kalau pengen lihat response codenya
# print(response.status_code)

# # Ini adalah hasilnya (kebetulan kita tau bentuknysa adalah JSON)
# print(response.json())

# Yang dibutuhin tadi ada
# pip install fastapi uvicorn

# import library
from fastapi import FastAPI

# Bikin instance FastAPI
# PERHATIKAN NAMA VARIABELNYA !
app = FastAPI()

# Tentukan dulu URLnya itu (Endpointnya) itu yang mana?
# https://localhost"/"
# GET /albums
@app.get("/")
def mengembalikan_data_dari_slash():
    return {"hello": "world"}

# GET /albums
@app.get("/albums")
def fetch_albums():
    return {"data": {"albums": [{"id": 1, "name": "Album A"}]}}

# GET /albums/"name" (name adalah variabel yang dinamis)
@app.get("/albums/{name}")
def fetch_albums_by_name(name): # name HARUS sama dengan yang di CURLY BRACKET
    return {
        "data": {
            "album_name": name,
            "id": "Id belum ada nih, kamu nanti bisa tambahin yah!",
        }
    }

# Ini list kosongan
albums = []

# Ini sekarang punya endpoint /albums TAPI PAKE POST
# POST /albums
@app.post("/albums")
# PERHATIKAN BAIK BAIK DI SINI ADA PARAMETER YANG KAMU DEFINISIKAN 
# DI SINI DIKASIH namanya adalah "album_baru"
def add_album_baru(album_baru):
    # Di sini tuh bagian logic, pengen diapain pun OK
    print(f"Album baru yang ditambahkan adalah: {album_baru}")

    # YANG PENTING JANGAN LUPA RETURN:
    # Ceritanya ini palsu, ga ditambahkan apa-apa
    return {"result": "Data berhasil ditambahkan"}


# Convention:
# untuk nama Endpoint, itu biasanya JANGAN ADA KATA PERINTAHNYA
# GET /albums
# GET /albums/{id}
# POST /albums

# GET /fetch-albums
# POST /add-albums

# GET /albums_top_10/ --> kurang tepat karena biasanya adalah -
# GET /albums-top-10

# Biasanya resourcenya itu di GROUPING
# GET /albums/
# GET /albums/top-ten

# Kalau udah tinggal "JALANIN"
# uvicorn nama_file_tanpa_py:nama_variabel_fast_api --reload