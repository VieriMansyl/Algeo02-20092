# Tugas Besar 2 IF2123 Aljabar Linier dan Geometri

> Membuat website yang dihost pada lokal yang dapat menerima inputan foto dan persentase kompresi lalu menghasilkan foto yang terkompres yang dapat didownload oleh pengguna.

## Daftar Anggota Kelompok

<table>

<tr><td colspan = 3 align = "center">KELOMPOK 15 ALGE-DEAD</td></tr>
<tr><td>No.</td><td>Nama</td><td>NIM</td></tr>
<tr><td>1.</td><td>Vieri Mansyl</td><td>13520092</td></tr>
<tr><td>2.</td><td>Vincent Prasetiya Atmadja</td><td>13520099</td></tr>
<tr><td>3.</td><td>Steven</td><td>13520131</td></tr>

</table>

## Teknologi yang digunakan
1. Python 3.8.0
2. click 8.0.3
3. colorama 0.4.4
4. Flask 2.0.2
5. itsdangerous 2.0.1
6. Jinja2 3.0.3
7. MarkupSafe 2.0.1
8. numpy 1.21.4
9. opencv-python 4.5.4.58
10. Werkzeug 2.0.2

## Cara Memakai

1. Download atau clone repo ini
2. Jalankan Windows PowerShell
3. Buka folder repo ini
4. Buat Virtual Environment Python

    ```bash
    py -m venv venv
    ./venv/Scripts/Activate.ps1
    ```

5. Install library yang akan digunakan

    ```bash
    pip3 install -r requirements.txt
    ```

6. Pastikan library yang telah diinstall sudah sesuai

    ```bash
    pip freeze
    ```

7. Jalankan program

    ```bash
    flask run
    ```

8. Copy IP address dan port yang tertera pada Windows PowerShell
    <br/>
    <br/>
    Misalnya Tertera:

    ```bash
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```

    Yang dicopy:
    `http://127.0.0.1:5000/`
    <br/>
    <br/>

9. Paste hasil copy-an tersebut pada browser

<br/>
<br/>

## Tampilan Cara Set-Up Virtual Environtment dan Download Library pada Windows PowerShell

![Tampilan pada windows powershell](./a-readme-related/wps.jpg)

## Tampilan Awal Pada Localhost

![Tampilan pada browser](./a-readme-related/blankweb.jpg)

## Tampilan Setelah Memilih File, Mengisi Image Compression Rate, dan Menekan Tombol Submit

![Tampilan pada browser](./a-readme-related/outputweb.jpg)

## Ucapan Terima Kasih

Kami mengucapkan terima kasih kepada

* Dr. Judhi S. Santoso (Dosen K1 IF2123 Tahun 2021/2022)
* Dr. Rinaldi Munir (Dosen K2 IF2123 Tahun 2021/2022)
* Dr. Rila Mandala (Dosen K3 IF2123 Tahun 2021/2022)
* Semua Asisten IF2123 Tahun 2021/2022
