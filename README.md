# Final Submission : Machine Learning Pipeline - Diabetes 
Nama: Ahmad Hasanuddin

Username dicoding: ahmad_hasanuddin_plMU



| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Diabetes prediction dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) |
| Masalah | Diabetes, atau sering disebut penyakit gula, adalah kondisi kronis yang ditandai dengan tingginya kadar gula darah (glukosa) melebihi ambang normal. Hal ini terjadi karena tubuh tidak dapat menyerap dan memanfaatkan gula sebagai energi, yang menyebabkan akumulasi gula dalam darah. Diabetes berkontribusi pada angka kematian global, dengan 6,7 juta kematian tercatat pada tahun 2021. |
| Solusi machine learning | Biasanya, diagnosis diabetes dilakukan dengan mengukur kadar gula dalam tubuh. Namun, dokter tidak dapat langsung memastikan apakah seseorang menderita diabetes hanya dari satu indikator. Sistem klasifikasi berbasis machine learning dapat memberikan wawasan tambahan bagi dokter untuk membantu pengambilan keputusan dan pemeriksaan lanjutan. |
| Metode pengolahan | Dataset ini memiliki sembilan fitur: delapan fitur digunakan untuk klasifikasi, sementara satu fitur menjadi target (class). Terdapat dua fitur kategori dan enam fitur numerik. Dataset dibagi menjadi 80% data pelatihan dan 20% data evaluasi. Selanjutnya, dilakukan transformasi seperti penggantian nama fitur, one-hot encoding pada fitur kategorikal, dan scaling pada data numerik. |
| Arsitektur model | Model menggunakan arsitektur dense dengan tiga hidden layer: Dense(256), Dense(64), dan Dense(16) dengan fungsi aktivasi ReLU. Layer terakhir berupa Dense(1) dengan fungsi aktivasi sigmoid untuk klasifikasi biner (diabetes atau tidak). Optimizer Adam digunakan dengan learning rate 0.001, loss function binary_crossentropy, dan metrik evaluasi BinaryAccuracy. |
| Metrik evaluasi | Metrik yang digunakan meliputi AUC, Precision, Recall, ExampleCount, dan BinaryAccuracy. |
| Performa model | Model menunjukkan performa yang baik dengan akurasi tinggi sebesar 0.97 pada data pelatihan dan validasi. Loss yang dihasilkan pada data pelatihan dan validasi adalah 0.0817, yang menunjukkan model dapat melakukan klasifikasi dengan efektif. |
| Opsi deployment | USistem akan dideploy menggunakan platform Railway untuk diakses secara online |
| Web app | [diabetes](streamlitbaru1-production.up.railway.app)|
| Monitoring |Sistem dimonitor menggunakan Prometheus dan Grafana. Proses monitoring mencakup pelacakan status setiap request yang masuk, seperti not found, invalid argument, atau request yang berhasil (ok).|
