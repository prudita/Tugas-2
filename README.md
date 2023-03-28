Tautan Railway: https://study-tr4cker.up.railway.app/

Tugas 2

Bagan: https://drive.google.com/file/d/1o02IlTSM4H7CsEXhLdmjzeFF_tKhiJvM/view?usp=sharing

Tugas 3 

Data dapat di-input dengan tag . Namun data yang di-input dengan tag ini tidak disimpan dalam server, sedangkan data yang di-input dengan tag

dapat disimpan dalam server.
HTML menampilkan data dan mendeskripsikan struktur suatu halaman (webpage), sedangkan XML dan JSON menyimpan dan mentransfer data yang akan ditampilkan

JSON dan XML dapat digunakan untuk menyimpan dan mentransfer data. Objek dalam JSON berupa data dengan type string, angka, array, atau Boolean, sedangkan semua data dalam XML berupa string XML lebih mudah dibaca oleh manusia, sedangkan JSON lebih mudah dibaca oleh oleh mesin JSON dapat disimpan sebagai file JavaScript, sedangkan XML hanya dapat disimpan sebagai file teks.

Membuat file forms.py pada folder study_tracker yang memiliki AssignmentForm yang memiliki 2 atribut, yaitu model dan fields yang masing-masing menyimpan class Assignment dari models.py dan list yang berisi atribut-atribut pada class Assignment
Membuat fungsi create_assignment pada views.py yang menerima parameter request. Fungsi ini memiliki variabel form yang merupakan objek AssignmentForm dan variabel context yang memiliki nilai {‘form’ : form}. Fungsi ini memanggil fungsi render dengan parameter berupa request, file create_assignment.html, dan context.
Membuat file create_assignment.html pada folder main/templates. File ini berisi tabel yang dapat diisi oleh pengguna. Lalu meng-impor fungsi create_assignment dari views.py ke file urls.py yang terdapat pada folder study_tracker dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi tersebut.
Menambahkan kode yang diawali tag dan diakhiri tag pada file home.html yang terdapat pada main/templates.
Membuat fungsi show_xml dan show_json pada views.py yang masing-masing menerima parameter request dan memiliki variabel data yang menyimpan semua object dari class Assignment dan me-return data dalam format xml dan json. Lalu, meng-import kedua fungsi tersebut ke urls.py pada study_tracker dan menambahkan path url ke urlpatterns untuk mengakses fungsi-fungsi tersebut.


Tugas 5
Internal CSS adalah kode CSS yang diletakkan di dalam <head> dari file HTML. CSS internal diletakkan di dalam tag <style></style>.
Kelebihan internal CSS:

1. Perubahan hanya terjadi pada 1 halaman

2. Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.

Kekurangan menggunakan Internal CSS:

1. Meningkatkan waktu akses website
2. Tidak efisien jika CSS yang sama ingin digunakan pada beberapa file.

External CSS adalah kode CSS yang diletakkan dalam file CSS eksternal, bukan dalam file HTML. File CSS eksternal diletakkan setelah bagian <head> pada halaman HTML.
Kelebihan CSS eksternal:

1. Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi
2. Kecepatan loading menjadi lebih cepat
3. File CSS yang sama bisa digunakan di banyak halaman.

Kekurangan CSS eksternal:
1. Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.


Inline CSS adalah kode CSS yang digunakan untuk tag HTML tertentu.
Kelebiha  Inline CSS:
1. Membuat perbaikan menjadi cepat
2. Permintaan HTTP yang lebih kecil
Kekurangan inline CSS:

1. Inline CSS harus diterapkan pada setiap tag

Tipe-Tipe CSS selector
1. Element Selector
Selector yang mengelompokkan elemen berdasarkan nama elemennya. Misalnya, h1, p, table, dan lain-lain.
2. Class Selector
Selector yang mengelompokkan elemen berdasarkan class-nya. Semua elemen anggota suatu class akan dipengaruhi oleh kode CSS dalam class selector
3. ID Selector
Selector yang mengelompokkan elemen berdasarkan id yang diberikan kepadanya. Id bersifat unik. Dalam kode CSS, id diawali dengan "#".

Tugas 6
* Perbedaaan synchronous programming dan asynchronous programming 
Dalam synchronous programming, setiap operasi tergantung pada operasi sebelumnya , sehingga setiap tugas dijalankan secara berurutan. Suatu tugas hanya akan dijalankan setelah tugas sebelumnya selesai berjalan. Sedangkan dalam asynchronous programming, operasi tidak tergantung satu sama lain, sehingga setiap tugas dapat berjalan tanpa urutan tertentu, bahkan dapat berjalan pada waktu yang sama

* Dalam penerapan paradigma event-driven programming, alur dari program ditentukan oleh kejadian seperti tindakan user (menekan tombol mouse, menekan key di keyboard, dan lain-lain), output sensor, dan penerimaan pesan dari program lain. 

* Penerapan asynchronous programming pada AJAX:
Pada saat page HTML me-load, data diakses dari web server.
Ketika user melakukan suatu tindakan, JavaScript akan membuat suatu object XMLHttpRequest. Object tersebut akan membuat request ke web server. Lalu, web server akan mengirim response ke browser. JavaScript membaca response tersebut dan melakukan tindakan yang sesuai sehingga web page akan diperbarui sesuai tindakan user. Hanya bagian web page yang diperbarui akan di-refresh, sehingga tidak seluruh web page harus di-refresh dan web page tidak harus di-reload. 

Referensi:
* Slide 2 Kuliah Pemrograman Berbasis Platform Genap 2022/2023

* https://www.guru99.com/xml-vs-html-difference.html#:~:text=XML%20is%20abbreviation%20for%20extensible,while%20HTML%20is%20Case%20insensitive

* https://byjus.com/free-ias-prep/difference-between-xml-and-html/

* https://www.guru99.com/json-vs-xml-difference.html#:~:text=Key%20Difference%20Between%20JSON%20and,more%20secure%20compared%20to%20JSON

* https://appmaster.io/blog/json-vs-xml

* https://stackoverflow.com/questions/3294572/is-input-well-formed-without-a-form

* https://www.hostinger.co.id/tutorial/perbedaan-inline-css-external-css-dan-internal-css

* https://datamyte.com/synchronous-vs-asynchronous/

* https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/

* https://www.theserverside.com/definition/Ajax-Asynchronous-JavaScript-and-XML

