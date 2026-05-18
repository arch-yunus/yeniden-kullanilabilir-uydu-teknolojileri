# 🤖 UYDU-201: Yörüngede Servis, Bakım ve Tamirat (OSAM)

Bu ders, otonom uzay operasyonlarının en kritik aşaması olan "yakınlaşma, bağıntılı konum kontrolü ve robotik müdahale" teknolojilerini en üst düzey mühendislik ve matematik modelleriyle ele alır. 

---

## 📊 Ders Detayları ve Kredi Bilgileri
*   **Ders Kodu:** UYDU-201
*   **Dönem:** Bahar (2. Dönem)
*   **Kredi Yapısı:** 3 Saat Teori + 2 Saat Uygulama
*   **AKTS (ECTS):** 7.5
*   **Ön Koşullar:** Robotik Kinematik, İleri Kontrol Sistemleri, Yörünge Mekaniği

---

## 📅 Haftalık Ayrıntılı Ders Planı

### 🟦 Kısım I: RPO ve Bağıntılı Yörünge Mekaniği

#### Haftalar 1-2: Hill / Clohessy-Wiltshire (CW) Denklemlerinin Analitik Çözümleri
Hedef dairesel yörüngedeki uyduya (Target) yaklaşan servis uydusunun (Chaser) göreceli hareket dinamikleri, doğrusal **Clohessy-Wiltshire (CW)** diferansiyel denklemleri ile modellenir.

Yerçekimsel alanın doğrusallaştırılmasıyla elde edilen diferansiyel sistem:
$$\ddot{x} - 3n^2x - 2n\dot{y} = f_x$$
$$\ddot{y} + 2n\dot{x} = f_y$$
$$\ddot{z} + n^2z = f_z$$
*   $x$: Radyal eksen (R-bar: Yer merkezinden dışarı doğru)
*   $y$: Teğetsel eksen (V-bar: Yörünge hızı doğrultusu)
*   $z$: Yörünge düzlemine dik eksen (H-bar: Açısal momentum yönü)
*   $n = \sqrt{\mu / a^3}$: Hedef uydunun ortalama hareketi (mean motion)

Bu sistemin sıfır kontrol girdisi ($f_x = f_y = f_z = 0$) altındaki homojen zamansal analitik çözümü matrisel formda şu şekilde ifade edilir:
$$\begin{bmatrix} x(t) \\ y(t) \\ z(t) \\ \dot{x}(t) \\ \dot{y}(t) \\ \dot{z}(t) \end{bmatrix} = \begin{bmatrix} 4-3\cos(nt) & 0 & 0 & \frac{1}{n}\sin(nt) & \frac{2}{n}(1-\cos(nt)) & 0 \\ 6(\sin(nt)-nt) & 1 & 0 & -\frac{2}{n}(1-\cos(nt)) & \frac{1}{n}(4\sin(nt)-3nt) & 0 \\ 0 & 0 & \cos(nt) & 0 & 0 & \frac{1}{n}\sin(nt) \\ 3n\sin(nt) & 0 & 0 & \cos(nt) & 2\sin(nt) & 0 \\ -6n(1-\cos(nt)) & 0 & 0 & -2\sin(nt) & 4\cos(nt)-3 & 0 \\ 0 & 0 & -n\sin(nt) & 0 & 0 & \cos(nt) \end{bmatrix} \begin{bmatrix} x_0 \\ y_0 \\ z_0 \\ \dot{x}_0 \\ \dot{y}_0 \\ \dot{z}_0 \end{bmatrix}$$
Bu çözüm kullanılarak, servis uydusunun hedefi gözlemleyebilmesi ve güvenle kenetlenebilmesi için gereken teğetsel ($V$-bar) ve radyal ($R$-bar) eksenli optimal yaklaşma manevra adımları ($\Delta V$ bütçesi) planlanır.

#### Haftalar 3-4: 6-DOF Göreceli Konum ve Yönelim (Pose) Kestirimi ve Sensör Entegrasyonu
Hazırlıksız (non-cooperative) hedeflere yanaşırken LiDAR, stereoskopik kameralar ve kızılötesi (IR) sensörlerden alınan gürültülü telemetri verileri füzyon edilerek hedefin **6-DOF (Konum ve Yönelim)** parametreleri tahmin edilir.

Bu amaçla **Genişletilmiş Kalman Filtresi (EKF)** ve doğrusal olmayan yüksek mertebeden dinamikler için Sigma noktalarını kullanan **Kokusuz Kalman Filtresi (UKF)** algoritmaları uygulanır.
Filtre tahmin (prediction) ve güncelleme (update) adımları:
*   **Tahmin Adımı:**
    $$\hat{\boldsymbol{x}}_{k|k-1} = f(\hat{\boldsymbol{x}}_{k-1|k-1}, \boldsymbol{u}_{k-1})$$
    $$\boldsymbol{P}_{k|k-1} = \boldsymbol{F}_{k-1} \boldsymbol{P}_{k-1|k-1} \boldsymbol{F}_{k-1}^T + \boldsymbol{Q}_{k-1}$$
*   **Güncelleme Adımı:**
    $$\boldsymbol{K}_k = \boldsymbol{P}_{k|k-1} \boldsymbol{H}_k^T (\boldsymbol{H}_k \boldsymbol{P}_{k|k-1} \boldsymbol{H}_k^T + \boldsymbol{R}_k)^{-1}$$
    $$\hat{\boldsymbol{x}}_{k|k} = \hat{\boldsymbol{x}}_{k|k-1} + \boldsymbol{K}_k (\boldsymbol{z}_k - h(\hat{\boldsymbol{x}}_{k|k-1}))$$
    $$\boldsymbol{P}_{k|k} = (\boldsymbol{I} - \boldsymbol{K}_k \boldsymbol{H}_k) \boldsymbol{P}_{k|k-1}$$
*Burada $\boldsymbol{P}$ hata kovaryans matrisi, $\boldsymbol{Q}$ sistem gürültü kovaryansı, $\boldsymbol{R}$ ölçüm gürültü kovaryansıdır.*

---

### 🟩 Kısım II: Uzay Robotiği, Kinematik ve Yakalama (Grappling)

#### Haftalar 5-6: Serbest-Yüzen (Free-Floating) Uzay Manipülatör Kinematiği
Uzay manipülatörlerinin kinematiği yerde çalışan robotlar gibi sabit bir tabana dayanmaz. Reaksiyon tekerlekleri kapatılmış **Serbest-Yüzen (Free-floating)** modda, robot kol hareket ettikçe açısal ve çizgisel momentum korunumu nedeniyle uydunun ana gövdesi zıt yönde döner ve ötelenir:
$$\begin{bmatrix} \boldsymbol{P}_{\text{çizgisel}} \\ \boldsymbol{L}_{\text{açısal}} \end{bmatrix} = \boldsymbol{H}_b \dot{\boldsymbol{x}}_b + \boldsymbol{H}_m \dot{\boldsymbol{\theta}} = \mathbf{0}$$
Burada $\dot{\boldsymbol{x}}_b$ gövdenin çizgisel ve açısal hız vektörleri, $\dot{\boldsymbol{\theta}}$ robot kollarının eklem hız vektörüdür. Gövdenin hareketini sönümleyen ve robot ucunun (end-effector) atalet uzayındaki konumunu kontrol eden **Etkin Jacobian Matrisi ($J^*$ veya $J_{eff}$)** şu şekilde türetilir:
$$\boldsymbol{v}_{ee} = \boldsymbol{J}^*(\boldsymbol{\theta}) \dot{\boldsymbol{\theta}} \quad \text{burada} \quad \boldsymbol{J}^* = \boldsymbol{J}_m - \boldsymbol{J}_b \boldsymbol{H}_b^{-1} \boldsymbol{H}_m$$
*   $\boldsymbol{J}_m$: Kola ait klasik Jacobian matrisi.
*   $\boldsymbol{J}_b$: Taban hareketinin uç noktaya etkisini tanımlayan Jacobian matrisi.

#### Haftalar 7-8: Hazırlıksız ve Dönen Hedeflerin Yakalanması (Tumbling Target Grappling)
Kontrolden çıkmış ve kendi ekseninde dönen (tumbling) hedeflerin robotik kolla yakalanması yüksek riskli bir darbe mekaniği problemidir.
*   **Darbe Sönümleme (Impedance Control):** Robotik kolun eklemlerinde sanal kütle-yay-sönümleyici sistemi modellenerek çarpışma anındaki darbe kuvvetleri absorbe edilir.
*   **Geri-Reaksiyon Kontrolü:** Yakalama sonrası, hedefin sahip olduğu açısal momentumun servis aracına zarar vermemesi için servis aracının reaksiyon tekerlekleri ve kontrol iticileriyle (ACS) ortak momentum sönümleme (De-tumbling) manevraları uygulanır.

---

### 🟨 Kısım III: Yörüngede Akışkan Transferi ve Büyük Montaj

#### Haftalar 9-10: Sıfır Yerçekiminde Akışkan Yönetimi ve Yakıt İkmali
Mikro-yerçekimi ortamında yerçekimi ivmesi olmadığından sıvılar depoda serbestçe yüzer ve tank çıkış valfinde gaz birikerek pompalara zarar verebilir (vapor lock). Bu durumun engellenmesi için kılcallık kuvvetlerine dayanan **PMD (Propellant Management Devices)** donanımları kullanılır.

Kılcal yükselme ve yüzey gerilimi dengesi **Young-Laplace** denklemi ile modellenir:
$$\Delta P = P_{\text{gaz}} - P_{\text{sıvı}} = \frac{2 \gamma \cos\theta_c}{R_c}$$
Burada $\gamma$ akışkanın yüzey gerilim sabiti, $\theta_c$ malzemenin ıslanma (temas) açısı, $R_c$ ise kılcal kanal yarıçapıdır. Tank içi metal kanallar ve gözenekli sünger benzeri metal mesh yapılar yardımıyla sıvı yakıt sürekli olarak tankın çıkış boğazında toplanır.

#### Haftalar 11-12: Yörüngede Modüler Montaj (OOA) ve Uzayda Üretim
*   **OOA (On-Orbit Assembly):** Fırlatma rüzgar korumalarına sığmayan devasa radyo teleskop aynaları veya mega uzay istasyonlarının robotik kollar yardımıyla modül modül yörüngede birleştirilmesi.
*   **Uzayda İmalat (In-Space Manufacturing):** Uzay boşluğunun ultra-vakum ve mikro-yerçekimi avantajlarını kullanarak hatasız kristal yapıların, biyoteknolojik dokuların veya 3D yazıcılarla devasa karbon fiber kafes kirişlerin (truss) üretilmesi.

#### Haftalar 13-14: Aktif Uzay Çöpü Temizleme (ADR) ve Uzay Hukuku
*   **ADR (Active Debris Removal):** Kontrolden çıkmış eski uyduların robotik kollar, ağlar veya zıpkınlar kullanılarak yakalanması ve Pasifik Okyanusu'ndaki "Point Nemo" mezarlığına kontrollü düşürülmesi (De-orbit).
*   **Uzay Hukuku ve Sorumluluk:** Outer Space Treaty (1967) ve Liability Convention (1972) çerçevesinde, uzay çöplerinin temizlenmesi esnasında oluşabilecek kaza ve hasarların yasal sorumluluklarının analizi.

---

## 💻 Simülasyon Uygulaması ve Ödevler

### Proje Görevi: Clohessy-Wiltshire Tabanlı R-bar ve V-bar Yaklaşma Manevraları
*   **Görev:** Öğrenciler, hedef uyduya bağıntılı koordinatlarda $y_0 = -1000 \text{ m}$ (V-bar üzerinde arkada) konumunda bulunan bir servis uydusunun, hedef ile çarpışmadan güvenli kenetlenme alanına ($\pm 5 \text{ cm}$ tolerans) gelebilmesi için gereken optimal çift itkili (two-impulse) manevralarını planlayacak ve gerekli $\Delta V$ bütçesini sayısal olarak hesaplayan Python kodunu yazacaktır.

---

## 📚 Önerilen Akademik Kaynaklar
1.  **Vallado, D. A. (2013).** *Fundamentals of Astrodynamics and Applications* (4. Baskı). Microcosm Press.
2.  **Yoshida, K. (2003).** *Space robot dynamics and control: To grasp a tumbling satellite*. Space Technology and Applications International Forum.
3.  **ISO 24330:2022.** *Space systems — Rendezvous and Proximity Operations (RPO) and On-Orbit Servicing (OOS)*.
