Tautan aplikasi Railway: https://study-tr4cker.up.railway.app/



Bagan: https://drive.google.com/file/d/1o02IlTSM4H7CsEXhLdmjzeFF_tKhiJvM/view?usp=sharing

Tugas 3
Data dapat di-input dengan tag <input>. Namun data yang di-input dengan tag ini tidak disimpan dalam server, sedangkan data yang di-input dengan tag <form> dapat disimpan dalam server.

HTML menampilkan data dan mendeskripsikan struktur suatu halaman (webpage), sedangkan XML dan JSON menyimpan dan mentransfer data yang akan ditampilkan

JSON dan XML dapat digunakan untuk menyimpan dan mentransfer data. Objek dalam JSON berupa data dengan type string, angka, array, atau Boolean, sedangkan semua data dalam XML berupa string
XML lebih mudah dibaca oleh manusia, sedangkan JSON lebih mudah dibaca oleh oleh mesin
JSON dapat disimpan sebagai file JavaScript, sedangkan XML hanya dapat disimpan sebagai file teks.




1. Membuat file forms.py pada folder study_tracker yang memiliki AssignmentForm yang memiliki 2 atribut, yaitu model dan fields yang masing-masing menyimpan class Assignment dari models.py dan list yang berisi atribut-atribut pada class Assignment
2. Membuat fungsi create_assignment pada views.py yang menerima parameter request. Fungsi ini memiliki variabel form yang merupakan objek AssignmentForm dan variabel context yang memiliki nilai {‘form’ : form}. Fungsi ini memanggil fungsi render dengan parameter berupa request, file create_assignment.html, dan context.
3. Membuat file  create_assignment.html pada folder main/templates. File ini berisi tabel yang dapat diisi oleh pengguna. Lalu meng-impor fungsi create_assignment dari views.py ke file urls.py yang terdapat pada folder study_tracker dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi tersebut.
4. Menambahkan kode yang diawali tag <button > dan diakhiri tag  </button > pada file home.html yang terdapat pada main/templates.
5. Membuat fungsi show_xml dan show_json pada views.py yang masing-masing menerima parameter request dan memiliki variabel data yang menyimpan semua object dari class Assignment dan me-return data dalam format xml dan json. Lalu, meng-import kedua fungsi tersebut ke urls.py pada study_tracker dan menambahkan path url ke urlpatterns untuk mengakses fungsi-fungsi tersebut.

Referensi:
* Slide 2 Kuliah Pemrograman Berbasis Platform Genap 2022/2023

* https://www.guru99.com/xml-vs-html-difference.html#:~:text=XML%20is%20abbreviation%20for%20extensible,while%20HTML%20is%20Case%20insensitive

* https://byjus.com/free-ias-prep/difference-between-xml-and-html/

* https://www.guru99.com/json-vs-xml-difference.html#:~:text=Key%20Difference%20Between%20JSON%20and,more%20secure%20compared%20to%20JSON

* https://appmaster.io/blog/json-vs-xml

* https://stackoverflow.com/questions/3294572/is-input-well-formed-without-a-form