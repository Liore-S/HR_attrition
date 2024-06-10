# Proyek: Pencegahan kenaikan *attrition rate* karyawan pada Jaya Jaya Maju


## Business Understanding

Jaya Jaya Maju meupakan sebuah perusahaan multinasional yang telah berdiri sejak tahun 2000.
Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

### Permasalahan Bisnis

Jaya Jaya Maju memiliki permasalahan terkait dengan kenaikan *attrition rate* karyawan yang cukup tinggi. Hal ini menyebabkan perusahaan mengalami kerugian yang signifikan, baik dari segi finansial maupun operasional. Oleh karena itu, perusahaan membutuhkan solusi untuk mengatasi permasalahan ini dan mempertahankan karyawan yang ada.

### Cakupan Proyek

Membuat sebuah Dashboard yang dapat digunakan untuk melihat *attrition rate* karyawan, membuat model prediksi *attrition* karyawan, dan melakukan analisis pada faktor penyebab *attrition* karyawan.

### Persiapan

Sumber data: [GitHub](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)<br>
Hardware: GPU NVIDIA Volta™ or higher with compute capability 7.0+. ([list](https://developer.nvidia.com/cuda-gpus))<br>
Software:
- Docker
- Visual Studio Code


#### Setup environment:

Docker Container:
- Metabase Container: <u>metabase/metabase:v0.49.6</u> **(Docker Hub)**
- Rapids Notebook Container: <u>nvcr.io/nvidia/rapidsai/notebooks:24.04-cuda12.2-py3.11</u> **(Nvidia NGC)**

```bash
docker run -d -p 4000:3000 --name metabase metabase/metabase:v0.49.6

# Ubah parameter --gpus sesuai dengan GPU ID yang digunakan
docker run -d --name rapids-vs --gpus '"device=1"' -v ~/data-science:/app nvcr.io/nvidia/rapidsai/notebooks:24.04-cuda12.2-py3.11
```

Python Library:
```bash
# Jalankan perintah tersebut pada container rapids-vs
pip install -r requirements.txt
```

## Model Usage

Untuk menggunakan model prediksi *attrition* karyawan, Anda dapat menjalankan kode berikut:

```py
python predict.py
```
> Pastikan Anda telah mengubah parameter `input_data` dan `file_name` pada kode tersebut sesuai dengan nama/path data yang ingin anda prediksi.

## Business Dashboard

```
# Metabase Account
Email: root@mail.com
Password: root123
```
### Dashboard Preview
![Dasbor Screenshot](https://i.ibb.co.com/0KX1crx/liore-s-dashboard.png)

### Penjelasan
Pada bagian atas dashboard terdapat beberapa filter seperti *Department*, *Gender*, *OverTime*, dan *JuniorRole*. Filter ini dapat digunakan untuk melihat *attrition rate* karyawan berdasarkan kriteria tertentu. Misalnya, Anda dapat memilih untuk melihat data attrition hanya untuk karyawan di departemen tertentu atau hanya untuk karyawan yang bekerja lembur. Dengan menggunakan filter ini, pengguna dapat memperoleh wawasan yang lebih spesifik dan mendetail mengenai faktor-faktor yang mempengaruhi keluarnya karyawan dari perusahaan.

Selanjutnya, terdapat beberapa plot yang menggambarkan distribusi *attrition rate* karyawan berdasarkan beberapa faktor yang dinilai berkorelasi dengan *attrition rate* tersebut. Contohnya, distribusi *attrition rate* berdasarkan *Job Role* menunjukkan bagaimana tingkat keluar karyawan bervariasi di antara berbagai posisi pekerjaan. Plot ini memungkinkan untuk mengidentifikasi posisi atau departemen mana yang memiliki tingkat keluar karyawan yang tinggi, sehingga perusahaan dapat mengambil tindakan yang lebih tepat sasaran.

Sedangkan yang paling bawah merupakan sebuah plot yang menunjukkan hubungan antara rata-rata *Monthly Income* dan rata-rata *Total Working Years* yang dikelompokkan berdasarkan *Job Level*. Plot ini menunjukkan bahwa semakin tinggi Job Level, semakin tinggi pula Monthly Income dan Total Working Years. Ini mengindikasikan bahwa dengan kenaikan level pekerjaan, karyawan cenderung mendapatkan penghasilan yang lebih tinggi dan memiliki pengalaman kerja yang lebih banyak.

Plot ini penting untuk memahami bagaimana peningkatan karir dan kompensasi dapat mempengaruhi retensi karyawan, dan dapat digunakan untuk mengidentifikasi area dimana perusahaan perlu fokus dalam upaya mempertahankan karyawan.

## Conclusion

Berdasarak analisis yang dilakukan terdapat beberapa faktor yang menyebabkan kenaikan *attrition rate* karyawan pada Jaya Jaya Maju. Beberapa faktor tersebut antara lain:
- **Over Time**  
  - Karyawan yang sering bekerja lembur cenderung memiliki attrition rate yang lebih tinggi. Ini bisa disebabkan oleh beberapa alasan, termasuk kelelahan, kurangnya keseimbangan antara kehidupan kerja dan pribadi, serta tekanan pekerjaan yang tinggi. Karyawan yang bekerja lembur mungkin merasa terbebani dan kurang memiliki waktu untuk beristirahat atau berinteraksi dengan keluarga dan teman-teman, yang akhirnya dapat menyebabkan mereka meninggalkan perusahaan. 
- **JuniorRole** dan **First Job**  
  - Ekspektasi Karir: Karyawan di posisi junior mungkin memiliki ekspektasi yang tinggi terhadap perkembangan karir mereka dan mungkin merasa frustrasi jika mereka tidak melihat adanya peluang promosi atau perkembangan karir yang cepat.
  - Adaptasi Lingkungan Kerja: Karyawan yang baru pertama kali bekerja mungkin memerlukan waktu lebih lama untuk menyesuaikan diri dengan budaya dan lingkungan kerja, yang bisa menjadi faktor penyebab ketidakpuasan dan akhirnya attrition.
- **MonthlySalary**
  -  Kepuasan Finansial: Gaji yang lebih tinggi dapat memberikan kepuasan finansial yang lebih besar, yang bisa mengurangi keinginan karyawan untuk mencari pekerjaan lain dengan imbalan yang lebih baik.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- **Kurangi Overtime**
  - Kebijakan Overtime: Implementasikan kebijakan yang membatasi jumlah lembur yang diperbolehkan. Misalnya, batasi lembur maksimal 10 jam per minggu per karyawan.
  - Manajemen Waktu: Tingkatkan manajemen waktu dan distribusi tugas sehingga pekerjaan dapat diselesaikan dalam jam kerja normal. Pertimbangkan untuk menambah jumlah karyawan atau menggunakan sistem shift jika beban kerja tinggi.
- **Karyawan Junior**
  - Rencana Karir: Buat rencana karir yang jelas dan transparan untuk karyawan junior. Tampilkan jalur promosi dan peluang pengembangan karir dalam perusahaan untuk meningkatkan motivasi dan komitmen mereka.
  - Evaluasi Berkala: Lakukan evaluasi kinerja secara berkala dan berikan umpan balik konstruktif. Diskusikan tujuan karir karyawan dan langkah-langkah yang diperlukan untuk mencapainya.
- **Tinjau dan Sesuaikan Gaji**
  - Struktur Gaji Kompetitif: Pastikan struktur gaji yang kompetitif dengan melakukan benchmarking terhadap industri sejenis. Periksa apakah gaji yang ditawarkan sudah sesuai dengan standar pasar.
  - Insentif dan Bonus: Tawarkan insentif dan bonus berbasis kinerja untuk mendorong produktivitas dan loyalitas karyawan.