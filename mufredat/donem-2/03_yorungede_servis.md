# 🤖 UYDU-201: Yörüngede Servis, Bakım ve Tamirat (OSAM)

Bu ders, otonom uzay operasyonlarının en karmaşık aşaması olan "yakınlaşma ve fiziksel müdahale" teknolojilerini en üst düzey mühendislik ve matematik modelleriyle ele alır. OSAM (On-Orbit Servicing, Assembly, and Manufacturing) operasyonları; yörünge mekaniği, robotik kontrol, sensör füzyonu ve mikro-yerçekimi akışkanlar mekaniğinin kesişim noktasında yer alır.

---

## 📊 Ders Detayları ve Kredi Bilgileri
*   **Ders Kodu:** UYDU-201
*   **Dönem:** Bahar (2. Dönem)
*   **Kredi Yapısı:** 3 Saat Teori + 2 Saat Uygulama
*   **AKTS (ECTS):** 7.5
*   **Ön Koşullar:** Robotik Kinematik, İleri Kontrol Sistemleri, Yörünge Mekaniği

---

## 📅 Haftalık Ayrıntılı Ders Planı

### 🟦 Kısım I: RPO (Rendezvous & Proximity Operations) ve Bağıntılı Yörünge Mekaniği

#### Haftalar 1-2: Clohessy-Wiltshire (Hill) Denklemleri ve Göreceli Hareket
*   **Teorik Odak:** Dairesel bir yörüngedeki hedef uyduya (Target/Leader) yaklaşan servis uydusunun (Chaser) göreceli hareket dinamikleri.
*   **Matematiksel Modelleme:** Clohessy-Wiltshire (CW) lineer diferansiyel denklem sistemi:
    $$\ddot{x} - 3n^2x - 2n\dot{y} = f_x$$
    $$\ddot{y} + 2n\dot{x} = f_y$$
    $$\ddot{z} + n^2z = f_z$$
    *   $x$: Radyal eksen (Radial - Dünya merkezinden dışarıya doğru)
    *   $y$: Teğetsel eksen (In-track - Hareket doğrultusu)
    *   $z$: Yörünge düzlemine dik eksen (Cross-track - Açısal momentum doğrultusu)
    *   $n = \sqrt{\mu / a^3}$: Hedef uydunun ortalama hareketi (Mean motion)
    *   $f_x, f_y, f_z$: Birim kütle başına etki eden kontrol veya perturbasyon ivmeleri.

#### Haftalar 3-4: 6-DOF Göreceli Navigasyon ve Sensör Füzyonu
*   **Teorik Odak:** Otonom yakınlaşma için sensor entegrasyonu (LiDAR, Star Tracker, Optik ve IR Kameralar). Hedef uydunun 6 serbestlik dereceli (6-DOF) konum ve yönelim (Pose) kestirimi.
*   **Algoritmik Altyapı:** Durum kestirimi için **Genişletilmiş Kalman Filtresi (EKF)** ve doğrusal olmayan sistemler için **Kokusuz Kalman Filtresi (UKF)** uygulamaları. Çarpışmadan kaçınma manevraları için pasif güvenli yörünge (Passive Safety Orbit) tasarımı.

---

### 🟩 Kısım II: Uzay Robotiği, Kinematik ve Yakalama (Grappling)

#### Haftalar 5-6: Mikro-Yerçekiminde Uzay Robotiği Kinematiği
*   **Teorik Odak:** Yerdeki sabit robotik kolların aksine, uzayda "tabanı serbest" (floating base) hareket eden robotik sistemler.
*   **Kontrol Rejimleri:**
    *   **Free-Flying (Serbest Uçan):** Ana gövdenin (Chaser) yönelimi reaksiyon tekerlekleri veya iticiler (ACS) ile sürekli sabit tutulur.
    *   **Free-Floating (Serbest Yüzen):** İtki sistemleri kapatılır. Robotik kol hareket ettikçe açısal momentumun korunumu nedeniyle gövde zıt yönde döner. Yakıt tasarrufu sağlar ancak kinematiği non-holonomiktir.
*   **Matematiksel Modelleme:** Açısal momentumun korunumu denklemi:
    $$I_b \cdot \omega_b + I_m(\theta) \cdot \dot{\theta} = 0$$
    *Burada $I_b$ gövde eylemsizlik matrisi, $\omega_b$ gövde açısal hızı, $I_m(\theta)$ kola ait eylemsizlik matrisi ve $\dot{\theta}$ eklem hızları vektörüdür.*

#### Haftalar 7-8: Hazırlıksız Hedef Yakalama ve Momentum Yönetimi
*   **Teorik Odak:** Landsat 7 (OSAM-1) örneğindeki gibi üzerinde kenetlenme portu bulunmayan uyduların (non-cooperative unprepared targets) kavranması.
*   **Mühendislik Dinamikleri:** Robotik kol hedefe temas ettiği andaki darbe mekaniği ve momentum transferi. Temas sonrası hedef uydunun dönüş hareketini (tumbling) sönümleme algoritmaları.

---

### 🟨 Kısım III: Yörüngede Akışkan Transferi ve Büyük Montaj

#### Haftalar 9-10: Sıfır Yerçekiminde Akışkan Transferi ve Yakıt İkmali
*   **Teorik Odak:** Mikro-yerçekimi ortamında sıvıların davranışı. Kılcallık etkisi, yüzey gerilimi ve gaz-sıvı ayrışması problemleri (vapor lock riski).
*   **Donanım Mimarileri:** Depodaki sıvıyı yerçekimi olmadan motor valflerine yönlendiren **Akışkan Yönetim Cihazları (PMD - Propellant Management Devices)** sünger ve galeri tasarımları. Hidrazin ($N_2H_4$) ve Ksenon ($Xe$) transfer protokolleri.

#### Haftalar 11-12: Yörüngede Modüler Montaj (OOA) ve Üretim (ISM)
*   **Teorik Odak:** Yeryüzünden fırlatılamayacak büyüklükteki devasa radyo teleskop antenlerinin ve güneş panellerinin robotik kollarla yörüngede birleştirilmesi. Uzay ortamında 3D yazıcılarla karbon fiber ve polimer bazlı yapısal eleman üretimi.

#### Haftalar 13-14: Aktif Uzay Çöpü Temizleme (ADR)
*   **Teorik Odak:** Kessler sendromunun önlenmesi için OSAM tekniklerinin çöp uyduların yörüngeden indirilmesinde (De-orbit) kullanılması.

---

## 💻 Simülasyon Uygulaması ve Ödevler

### Proje Görevi: Clohessy-Wiltshire Tabanlı Kenetlenme Delta-V Analizi
*   **Detay:** Öğrenciler, `scripts/mission_control_cli.py` betiğinde yer alan yörünge parametrelerini kullanarak, hedef uyduya 1 km mesafeden yaklaşan bir servis uydusunun (Chaser) optimal V-bar ve R-bar yaklaşma manevralarını planlayacak, gerekli toplam delta-V bütçesini sayısal olarak hesaplayacaklardır.

---

## 📚 Önerilen Akademik Kaynaklar
1.  **Spong, M. W., Hutchinson, S., & Vidyasagar, M. (2005).** *Robot Dynamics and Control* (2. Baskı). John Wiley & Sons.
2.  **Sidi, M. J. (1997).** *Spacecraft Dynamics and Control: A Practical Engineering Approach*. Cambridge University Press.
3.  **NASA OSAM-1 Mission Reference Guide (2022).** *On-Orbit Servicing, Assembly, and Manufacturing 1*.
