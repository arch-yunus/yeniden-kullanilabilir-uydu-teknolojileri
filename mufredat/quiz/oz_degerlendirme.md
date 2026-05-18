# 📝 Öz Değerlendirme Testleri

Müfredatın her dersi ve bölümü için hazırlanmış, hem teorik kavramları pekiştirmeyi hem de matematiksel hesaplama yeteneklerini test etmeyi amaçlayan ileri düzey soru setleri.

---

## 🟦 Ders UYDU-101: VLEO ve Sınır Fiziği

### 1. Teorik Soru
**Soru:** Knudsen sayısı ($Kn$), L karakteristik boyutu $2.0 \text{ m}$ olan bir uydu için $Kn = 15$ olarak hesaplanmıştır. Bu akış hangi rejimdedir ve bu rejimde aerodinamik hesaplamalarda Navier-Stokes denklemleri neden kullanılamaz?
*   **Cevap:** Akış, **Serbest Moleküler Akış (Free Molecular Flow)** rejimindedir ($Kn > 10$). Bu rejimde moleküller arası çarpışmalar ihmal edilecek düzeyde azdır ve gaz sürekli bir ortam olarak kabul edilemez. Navier-Stokes denklemleri süreklilik (continuum) kabullerine dayandığı için bu rejimde fiziksel olarak geçersizdir; yerine Boltzmann Taşıma Denklemi veya DSMC sayısal yöntemleri kullanılmalıdır.

### 2. Matematiksel Hesaplama Sorusu
**Soru:** VLEO'da $250 \text{ km}$ irtifada uçan bir uydunun yüzeyindeki birikimli yıllık Atomik Oksijen (ATOX) akısı $\Phi_{\text{ATOX}} = 6.0 \times 10^{14} \text{ atoms/cm}^2\cdot\text{s}$ olarak verilmiştir. Bu uydu üzerindeki Kapton koruyucu örtünün alanı $A = 500 \text{ cm}^2$ ve Kapton'un aşınma verimi $E_y = 3.0 \times 10^{-24} \text{ cm}^3/\text{atom}$'dur. Kapton malzemenin yoğunluğu $\rho = 1.42 \text{ g/cm}^3$ olduğuna göre, 1 yıllık ($365 \text{ gün}$) maruz kalma süresi sonunda oluşacak **aşınma derinliğini (mm)** ve **toplam kütle kaybını (gram)** hesaplayınız.
*   **Çözüm Adımları:**
    1.  **Toplam Saniye ($t$):** $365 \times 86400 = 31,536,000 \text{ s}$
    2.  **Toplam Fluence ($F$):** $\Phi_{\text{ATOX}} \cdot t = (6.0 \times 10^{14}) \cdot (3.1536 \times 10^7) = 1.892 \times 10^{22} \text{ atoms/cm}^2$
    3.  **Aşınma Derinliği ($d$):** $F \cdot E_y = (1.892 \times 10^{22}) \cdot (3.0 \times 10^{-24}) = 0.05676 \text{ cm} = \mathbf{0.5676 \text{ mm}}$
    4.  **Kütle Kaybı ($\Delta m$):** $d \cdot A \cdot \rho = 0.05676 \text{ cm} \cdot 500 \text{ cm}^2 \cdot 1.42 \text{ g/cm}^3 = \mathbf{40.2996 \text{ gram}}$

---

## 🟩 Ders UYDU-102: Yeniden Kullanılabilirlik ve Termal Tasarım

### 1. Teorik Soru
**Soru:** Atmosfere dikey iniş yapan bir roketin kontrol sisteminde **G-fold** algoritmasının tercih edilmesinin temel nedeni nedir? Klasik PID kontrolcülere göre üstünlüğü nedir?
*   **Cevap:** G-fold, doğrusal olmayan ve konveks olmayan itki limitleri ile açısal kısıtları barındıran yörünge planlama problemini gerçek zamanlı olarak **Konveks Optimizasyon** formuna dönüştürür. Bu sayede, uçuş bilgisayarı anlık olarak "küresel en iyi" (globally optimal) çözümü milisaniyeler seviyesinde bulmayı garanti eder. Klasik PID kontrolcüler bu tür karmaşık çoklu girdi-çıktı kısıtlarını (örneğin gimbal limitleri, minimum/maksimum itki kısıtları) aynı anda ve optimal olarak yönetemez.

### 2. Matematiksel Hesaplama Sorusu
**Soru:** Dünyaya geri dönüş yapan bir kapsülün burun yarıçapı $R_n = 0.8 \text{ m}$'dir. Kapsül, yoğunluğu $\rho = 2.0 \times 10^{-4} \text{ kg/m}^3$ olan bir atmosfer tabakasından $V = 6000 \text{ m/s}$ hızla geçmektedir. Dünya için Sutton-Graves sabiti $k = 1.7415 \times 10^{-4} \text{ kg}^{0.5}/\text{m}$ olduğuna göre, durma noktasında oluşan konvektif **ısı akısını ($W/cm^2$ mertebesinde)** hesaplayınız ve bu ısı akısı için uygun **TPS malzeme sınıfını** seçiniz.
*   **Çözüm Adımları:**
    1.  **Sutton-Graves Formülü:** $q_s = k \sqrt{\rho / R_n} V^3$
    2.  $\sqrt{\rho / R_n} = \sqrt{2.0 \times 10^{-4} / 0.8} = \sqrt{2.5 \times 10^{-4}} = 0.015811$
    3.  $V^3 = (6000)^3 = 2.16 \times 10^{11} \text{ m}^3/\text{s}^3$
    4.  $q_s = (1.7415 \times 10^{-4}) \cdot (0.015811) \cdot (2.16 \times 10^{11}) = 5.947 \times 10^5 \text{ W/m}^2$
    5.  **$W/cm^2$ Dönüşümü:** $q_s / 10000 = \mathbf{59.47 \text{ W/cm}^2}$
    6.  **TPS Malzeme Tavsiyesi:** Bu seviye ($50 - 100 \text{ W/cm}^2$ arası) yüksek ısı yalıtımı gerektirir; bu nedenle **HRSI (High-temperature Reusable Surface Insulation - Yüksek Sıcaklık Yeniden Kullanılabilir Yüzey Yalıtımı) Silika Karoları** veya hafif ablatif malzemeler (PICA-X limit başlangıcı) tercih edilmelidir.

---

## 🤖 Ders UYDU-201: OSAM ve Robotik Yaklaşma

### 1. Teorik Soru
**Soru:** Serbest-Yüzen (Free-Floating) uzay robotlarında eklemler hareket ettirildiğinde gövdede oluşan dönme reaksiyonunun nedeni nedir? Uç işlevcinin (end-effector) konumlandırılmasında hangi matematiksel matris kullanılır?
*   **Cevap:** Mikro-yerçekiminde uydunun tabanı uzaya sabitlenmediği için, robot kolun hareketinden kaynaklanan reaksiyon torkları, **Açısal Momentumun Korunumu Yasası** gereğince ana gövdenin zıt yönde dönmesine neden olur. Uç işlevcinin hedefe göre bağımsız konumlandırılmasını çözebilmek için gövde ve kol atalet matrislerini birleştiren **Etkin Jacobian Matrisi ($J^*$ veya $J_{eff}$)** kullanılır.

### 2. Matematiksel Hesaplama Sorusu
**Soru:** Bir dairesel yörüngede ($a = 6800 \text{ km}$ yarıçap, $\mu = 3.986 \times 10^5 \text{ km}^3/\text{s}^2$) bulunan hedef uyduya yaklaşan bir servis uydusu, hedef uydunun $100 \text{ m}$ arkasındadır ($y_0 = -100 \text{ m}, x_0 = 0, z_0 = 0$).
1. Hedef uydunun **ortalama hareketini ($n$, rad/s)** hesaplayınız.
2. Servis uydusu hiç kontrol manevrası yapmazsa, yörünge mekaniği nedeniyle hedefe göre konumu zamanla nasıl değişir?
*   **Çözüm Adımları:**
    1.  **Ortalama Hareket ($n$):**
        $$n = \sqrt{\frac{\mu}{a^3}} = \sqrt{\frac{3.986 \times 10^5}{(6800)^3}} = \sqrt{\frac{398600}{3.14432 \times 10^{11}}} = \sqrt{1.26767 \times 10^{-6}} \approx \mathbf{0.001126 \text{ rad/s}}$$
    2.  **Yörüngesel Davranış:** Hedef ile servis uydusu aynı yarı-büyük eksende ($x_0 = 0$) ve dairesel yörüngede olduğu için, homojen Clohessy-Wiltshire denklemlerine göre aralarındaki bağıl teğetsel mesafe ($y(t)$) sabit kalır, radyal salınım yapmazlar. Ancak herhangi bir bozucu kuvvet veya başlangıç bağıl hızı ($\dot{y}_0$) verilirse, doğrusal bir sürüklenme başlar.

---

## 🌍 Ders UYDU-202: Sürdürülebilirlik ve Çöp Yönetimi

### 1. Teorik Soru
**Soru:** Bir uyduda görevi bittiğinde açılan "Elektrodinamik Kablo" (EDT - Electrodynamic Tether) sisteminin yakıt harcamadan yörünge düşürmeyi başarmasındaki temel elektromanyetik prensip nedir?
*   **Cevap:** EDT sistemi, uydudan sarkıtılan kilometrelerce uzunluktaki iletken kablonun Dünya'nın iyonosfer plazması ve manyetik alanı ($\vec{B}$) içinden yörünge hızıyla geçmesi prensibine dayanır. Bu hareket kablo üzerinde Faraday kanununa göre bir elektrik akımı ($I$) indükler. İndüklenen akım ile Dünya'nın manyetik alanı arasındaki etkileşim, kablo üzerinde yörünge hareket yönünün zıttı yönünde bir **Lorentz Kuvveti ($\vec{F}_L = I \vec{L} \times \vec{B}$)** üretir. Bu elektromanyetik frenleme kuvveti, uydunun hızını keserek yörüngesini düşürür.

### 2. Çoktan Seçmeli Test Sorusu
**Soru:** FCC'nin 2022 yılında aldığı karara göre, LEO yörüngesinde görev yapan ve lisansı yeni verilen uyduların görev süreleri bittikten sonra en geç kaç yıl içinde yörüngeden çıkarılması (De-orbit) yasal olarak zorunludur?
*   A) 25 Yıl
*   B) 10 Yıl
*   **C) 5 Yıl** (Doğru Cevap)
*   D) 1 Yıl
*   *Açıklama:* Eski IADC kuralı 25 yıl iken, mega takımyıldızların yarattığı kirlilik nedeniyle FCC bu süreyi yasal olarak 5 yıla indirmiştir.
