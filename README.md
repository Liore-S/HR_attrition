# Proyek: Pencegahan kenaikan *attrition rate* karyawan pada Jaya Jaya Maju


## Business Understanding

Jaya Jaya Maju meupakan sebuah perusahaan multinasional yang telah berdiri sejak tahun 2000.
Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

### Permasalahan Bisnis

Jaya Jaya Maju memiliki permasalahan terkait dengan kenaikan *attrition rate* karyawan yang cukup tinggi yaitu lebih dari 10%.

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
pip install plotly==5.22.0 scipy==1.13.1 imbalanced-learn==0.12.2
```

## Business Dashboard

```
# Metabase Account
Email: root@mail.com
Password: root123
```
### Dashboard Preview
![Dasbor Screenshot](/app/notebook/template-data-science/liore-s-dashboard.png)

### Penjelasan
Pada bagian atas dashboard terdapat beberapa filter seperti *Department*, *Gender*, *OverTime*, dan *JuniorRole*. Filter ini dapat digunakan untuk melihat *attrition rate* karyawan berdasarkan kriteria tertentu. Misalnya, Anda dapat memilih untuk melihat data attrition hanya untuk karyawan di departemen tertentu atau hanya untuk karyawan yang bekerja lembur. Dengan menggunakan filter ini, pengguna dapat memperoleh wawasan yang lebih spesifik dan mendetail mengenai faktor-faktor yang mempengaruhi keluarnya karyawan dari perusahaan.

Selanjutnya, terdapat beberapa plot yang menggambarkan distribusi *attrition rate* karyawan berdasarkan beberapa faktor yang dinilai berkorelasi dengan *attrition rate* tersebut. Contohnya, distribusi *attrition rate* berdasarkan *Job Role* menunjukkan bagaimana tingkat keluar karyawan bervariasi di antara berbagai posisi pekerjaan. Plot ini memungkinkan untuk mengidentifikasi posisi atau departemen mana yang memiliki tingkat keluar karyawan yang tinggi, sehingga perusahaan dapat mengambil tindakan yang lebih tepat sasaran.

Sedangkan yang paling bawah merupakan sebuah plot yang menunjukkan hubungan antara rata-rata *Monthly Income* dan rata-rata *Total Working Years* yang dikelompokkan berdasarkan *Job Level*. Plot ini menunjukkan bahwa semakin tinggi Job Level, semakin tinggi pula Monthly Income dan Total Working Years. Ini mengindikasikan bahwa dengan kenaikan level pekerjaan, karyawan cenderung mendapatkan penghasilan yang lebih tinggi dan memiliki pengalaman kerja yang lebih banyak.

Plot ini penting untuk memahami bagaimana peningkatan karir dan kompensasi dapat mempengaruhi retensi karyawan, dan dapat digunakan untuk mengidentifikasi area dimana perusahaan perlu fokus dalam upaya mempertahankan karyawan.

## Conclusion

Berdasarak analisis yang dilakukan terdapat beberapa faktor yang menyebabkan kenaikan *attrition rate* karyawan pada Jaya Jaya Maju. Beberapa faktor tersebut antara lain:
- Over Time, dimana karyawan yang bekerja lembur cenderung memiliki *attrition rate* yang lebih tinggi.
- JuniorRole dan First Job, dimana karyawan yang memiliki posisi junior dan first job cenderung memiliki *attrition rate* yang lebih tinggi
- Karyawan dengan gaji di atas rata-rata memiliki tingkat *attrition rate* yang lebih rendah. 

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- **Kurangi Overtime**: Perbaiki manajemen waktu dan distribusi tugas untuk mengurangi kebutuhan akan lembur.
- **Karyawan Junior**: Buat rencana karir yang jelas dan transparan untuk karyawan junior. Tunjukkan jalur promosi dan peluang pengembangan karir dalam perusahaan untuk meningkatkan motivasi dan komitmen mereka.
- **Tinjau dan Sesuaikan Gaji**: Pastikan struktur gaji kompetitif untuk mempertahankan karyawan, terutama bagi mereka yang berada di posisi kritis.