DAFTAR ISI
==========
- [LAPORAN PRAKTIKUM 6](#laporan-praktikum-6)   
    - [CODE PROGRAM DAFTAR NILAI](#code-program-daftar-nilai)
    - [FLOWCHART DAFTAR NILAI](#flowchart-daftar-nilai)
    - [KESIMPULAN](#kesimpulan)


# LAPORAN PRAKTIKUM 6


## CODE PROGRAM DAFTAR NILAI

### Step 1 : Inisialisasi Data
Tambahkan variabel data_mahasiswa sebagai list kosong yang digunakan untuk menyimpan data mahasiswa, setiap elemen dalam list adalah dictionary yang berisi informasi mahasiswa berupa Nilai Mahasiswa untuk kasus ini :

![gambar](ss/1.png)

### Step 2 : Fungsi tambah()
Fungsi ini untuk menambahkan data mahasiswa baru yang akan diproses sebagai :
- Meminta pengguna memasukkan nama dan nilai mahasiswa.
- Data yang dimasukkan disimpan dalam bentuk dictionary {"nama": nama, "nilai": nilai}.
- Dictionary ini ditambahkan ke dalam list data_mahasiswa menggunakan .append().

![gambar](ss/2.png)

### Step 3 : Fungsi tampilkan()
Fungsi ini digunakan untuk menampilkan data nilai mahasiswa ke dalam data_mahasiswa. Tujuan dapat menampilkan seluruh data mahasiswa. Menu ini mampu mengecek apakah data_mahasiswa kosong, Jika tidak kosong data ditampilkan dalam bentuk tabel sesuai data yang telah ditambahkan, Menggunakan enumerate untuk memberikan nomor pada setiap mahasiswa dalam daftar :

![gambar](ss/3.png)

### Step 4 : Fungsi hapus(nama)
Menghapus data mahasiswa berdasarkan nama yang dimasukan/input, sebagai proses menggunakan list comprehension untuk membuat daftar baru yang tidak berisi mahasiswa dengan nama yang dimasukkan, variabel data_mahasiswa diperbarui dengan daftar baru ini :

![gambar](ss/4.png)

### Step 5 : Fungsi ubah(nama)
Fungsi yang akan mengubah nilai mahasiswa berdasarkan nama yang dimasukan/input, mencari data mahasiswa dengan nama tertentu di dalam data_mahasiswa. Jika data ditemukan, maka nilai mahasiswa tersebut diperbarui sesuai input pengguna :

![gambar](ss/5.png)

### Step 6 : Fungsi menu()
Menyediakan Tampilan menu sebagai opsi pengguna, menggunakan perulangan while untuk terus menampilkan menu namun untuk menghentikan program masukan break sebagai perhentian :

Pilihan menu:
- 1: Memanggil fungsi tambah().
- 2: Memanggil fungsi tampilkan().
- 3: Memanggil fungsi hapus(nama).
- 4: Memanggil fungsi ubah(nama).
- 5: Menghentikan program.

![gambar](ss/6.png)

![gambar](ss/7.png)

### Step 7 : Closed Program
Pakai menu() untuk memulai sebuah program ketika dirun :

![gambar](ss/8.png)

### Step 8 : Run Program
Tahap akhir adalah uji coba code program yang sudah dibuat dengan mencoba berbagai kemungkinan yang ada.

#### Case 1 :
Kondisi pertama kita akan coba melihat tabel dengan inputkan 2 tampa menambahkan data/masih kosong, maka akan ditampilkan isi tabel masih belum ada datanya, akan ditampilkan 'Belum ada Data Mahasiswa' :

![gambar](ss/9.png)

#### Case 2 :
Kondisi kedua selanjutnya mencoba menambahkan data mahasiswa pada tabel, dengan menginputkan 1 untuk menambahkan data mahasiswa.

- Untuk perawalan, mencoba memasukan satu data mahasiswa :
    - Nama : Dafa Maulana
    - Nilai : 89

![gambar](ss/10.png)

#### Case 3 :
Selanjutnya, kondisi ketiga kembali dengan menginputkan 2 untuk melihat daftar data mahasiswa pada tabel, namun dari kondisi sebelumnya yang sudah menambahkan data mahasiswa saya coba tambahkan 3 data mahasiswa lagi. maka akan terlihat pada isi tabel :

![gambar](ss/11.png)

#### Case 4 :
Masuk kondisi keempat kita akan coba mengubah data, ada data yang salah diinputkan pada Nilai Mahasiswa 89 diubah menjadi 90, sebelum itu inputkan 4 untuk mengubah maka akan ditampilkan daftar nilai tabel dan diminta untuk memasukan nama mahasiswa yang ingin diubah data nilai -nya. User diminta memasukan kembali data valid yang akan diubah.

- Coba memasukan data mahasiswa berikut :
    - Nama : Dafa Maulana
    - Nilai : 90

![gambar](ss/12.png)

#### Case 5 : 
Kondisi keenam, kita mencoba menghapus sebuah data mahasiswa dengan menginputkan 3 untuk menghapuskan data mahasiswa lalu user diminta memasukan nama mahasiswa yang akan dihapus :

![gambar](ss/13.png)

#### Case 6 :
Jika semua data atau program input sudah selesai semua, user dapat menginputkan 5 untuk keluar dari progam :

![gambar](ss/14.png)



## FLOWCHART DAFTAR NILAI

![gambar](ss/15.png)


### Step 1 :
Titik mulai sebuah program atau alur.

### Step 2 :
lalu lakukan inisialisasi dengan menampilkan menu yang tersedia.

### Step 3 :
Inputkan code menu yang ingin dilakukan, setiap code berisi :
1. Tambah, 
2. Tampilkan, 
3. Hapus, 
4. Ubah, 
5. Keluar.

### Step 4 :
Dalam kasus ini semua kemgkinan dapat terjadi, kondisi yang diperlukan sesuai apa yang akan diinoutkan user.

- Jika Tampilkan, maka user akan di tampilkan sebuah tabel dari daftar nilai, namun jika tabel belum ada isi/kosong maka akan tampil Belum ada data, jika ada maka ditampilkan sebuah data nilai mahasiswa. Setelah tampilkan data maka akan kembali menuju inisialisasi menu. 

- Jika Tambah, user diminta memasukan sebuah data yang berupa :
    - Nama
    - Nilai

Lalu User akan diarahkan kembali ke inisialiasi menu.

- Jika Ubah, sama dengan Tampilkan jika tidak ada data nilai maka akan tampil tidak ada data nilai namun Ubah kalau ada data nilai user diminta menginputkan Nama Mahasiswa yang akan diubah, setelah itu diminta untuk mengisi atau menginputkan data valid yang diubah. Setelah itu user kembali ke inisialisasi menu.

- Jika Hapus, user akan ditampilkan daftar nilai lalu diminta memasukan sebuah Nama yang ingin dihapus dari daftar. Setelah itu kembali ke inisialisasi menu.

- jika Keluar, User akan keluar program dan program akan berhenti.


## KESIMPULAN
Dengan membuat code program daftar nilai ini saya pribadi dapat mengambil pelajaran, fungsi dapat memanggil sebuah data yang telah diberikan, dengan sub rutin ini kita menjadi dipermudah dengan baik. Melalui code program daftar nilai ini saya mampu memasukan sebuah data nama mahasiswa dan nilai. Adapun flowchart yang membantu saya dalam memahami alur sebuah code program yang telah saya buat.