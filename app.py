from flask import Flask
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(
    host="db",
    database="mydatabase",
    user="postgres",
    password="admin123"
)

cur = conn.cursor()


@app.route("/")
def home():

    return "<h1>Hello DevOps!</h1>"


@app.route("/mahasiswa")
def mahasiswa():

    cur.execute("SELECT * FROM mahastudent")

    data = cur.fetchall()

    hasil = "<h2>Data Mahasiswa</h2>"

    for row in data:

        hasil += f"""
        <p>
        ID : {row[0]} <br>
        Nama : {row[1]} <br>
        Jurusan : {row[2]}
        </p>
        <hr>
        """

    return hasil


@app.route("/tambah")
def tambah():

    cur.execute(
        """
        INSERT INTO mahastudent(nama,jurusan)
        VALUES(%s,%s)
        """,
        ("Andi", "Teknologi Informasi")
    )

    conn.commit()

    return "Data berhasil ditambahkan."


app.run(host="0.0.0.0", port=5000)