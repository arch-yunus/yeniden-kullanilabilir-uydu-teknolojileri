# 🛰️ UYDU-102: Yeniden Kullanılabilir Uydu Platform Tasarımı

Bu ders, havacılık ve uzay endüstrisindeki geleneksel "fırlat ve unut" modelinden, sürdürülebilir "bakım yapılabilir, modüler ve dünyaya geri döndürülebilir" platform modeline geçişin yapısal, aviyonik ve malzeme mühendisliği esaslarını inceler. Uydu ömrünü uzatan ve donanım bileşenlerinin yörüngede otonom olarak yenilenmesini sağlayan modüler mimarileri kapsar.

---

## 📊 Ders Detayları ve Kredi Bilgileri
*   **Ders Kodu:** UYDU-102
*   **Dönem:** Güz (1. Dönem)
*   **Kredi Yapısı:** 3 Saat Teori + 2 Saat Uygulama
*   **AKTS (ECTS):** 7.5
*   **Ön Koşullar:** Isı Transferi, Kontrol Sistemleri, Malzeme Bilimi

---

## 📅 Haftalık Ayrıntılı Ders Planı

### 🟦 Kısım I: Modüler Bus Mimarileri ve Standartları

#### Haftalar 1-2: Space Plug-and-Play Architecture (SPA) ve Veri Standartları
*   **Teorik Odak:** Modüler uzay aracı konsepti. Donanımların sistem entegrasyon süresini aylardan günlere düşüren **SPA** standartları (SPA-S: SpaceWire, SPA-U: USB, SPA-I: I2C).
*   **Aviyonik Modelleme:** **xTEDS** (eXtensible Transducer Electronic Data Sheet) XML şemaları ile sensörlerin ve eyleyicilerin kendilerini ana uçuş bilgisayarına otomatik olarak tanıtması (Self-describing hardware).
*   **Okumalar:** *AIAA Standard: Space Plug-and-Play Architecture*.

#### Haftalar 3-4: Mekanik ve Elektriksel Standart Arayüzler (Standard Interfaces)
*   **Teorik Odak:** Robotik manipülatörlerin uyduyu yakalaması için standart kenetlenme halkaları (Grapple Fixtures: FRGF, PDGF) ve güç-veri aktarımı sağlayan arayüzler.
*   **Tasarım Kriterleri:** Modül değişimi sırasında oluşan mekanik hizalama hatalarını absorbe eden kılavuz kanallı (Guide Rails) kilit mekanizmaları.
*   **Yörüngede Yakıt İkmal Portları:** Sıfır sızıntılı, basınç ve vakum altında çalışan hızlı ayrılabilir (Quick Disconnect) akışkan port tasarımları.

---

### 🟩 Kısım II: Atmosfere Geri Dönüş ve Isıl Koruma Sistemleri (TPS)

#### Haftalar 5-6: Atmosfere Geri Dönüş Mekaniği ve Balistik Katsayısı
*   **Teorik Odak:** Atmosfere giriş yörüngeleri, giriş açısı ve yavaşlama sınırları.
*   **Matematiksel Modelleme:** Balistik Katsayısı ($B_c$) denklemi:
    $$B_c = \frac{m}{C_d \cdot A}$$
    *Düşük $B_c$ değerine sahip araçlar atmosferin üst katmanlarında daha hızlı yavaşlayarak pik ısı akısını düşürür.*

#### Haftalar 7-8: Sutton-Graves Isı Akısı Modellemesi
*   **Teorik Odak:** Durma noktasında (stagnation point) oluşan şok dalgaları ve konvektif ısı akısı.
*   **Matematiksel Modelleme:** Sutton-Graves Isı Akısı formülü:
    $$q_s = k \sqrt{\frac{\rho}{R_n}} \cdot V^3$$
    *   $q_s$: Durma noktası convective ısı akısı ($W/\text{m}^2$)
    *   $k$: Gezegensel sabit (Dünya atmosferi için $1.7415 \times 10^{-4} \text{ kg}^{0.5}/\text{m}$)
    *   $\rho$: Atmosferik freestream yoğunluğu ($\text{kg/m}^3$)
    *   $R_n$: Araç burun (nose) yarıçapı ($\text{m}$)
    *   $V$: Giriş hızı ($\text{m/s}$)

#### Haftalar 9-10: Termal Koruma Malzemeleri (TPS) Karşılaştırmalı Analizi
Geri dönüş araçlarının yapısal bütünlüğünü korumak için tasarlanan malzemelerin özellikleri:

| Malzeme Sınıfı | Örnek Tip | Maksimum Sıcaklık Limit (°C) | Isıl İletkenlik Sabiti ($W/m\cdot K$) | Mekanizma Tipi |
| :--- | :--- | :--- | :--- | :--- |
| **Ablatif (Tek Kullanımlık)** | PICA-X, Avcoat | > 2000 | 0.2 - 0.4 (Aşınma esnasında) | Kimyasal bozunma (erime/buharlaşma) |
| **Yeniden Kullanılabilir Karolar** | HRSI (Silika) | ~ 1260 | 0.05 - 0.08 | Yüksek yalıtım ve yansıtıcılık |
| **Ultra-Yüksek Isı Seramikleri** | RCC (Reinforced Carbon-Carbon) | ~ 1650 | 25 - 45 (Yüksek iletkenlik) | Yapısal dayanım (Burun ve kanat uçları) |

---

### 🟨 Kısım III: Kontrollü Dikey İniş ve Yenileme (Refurbishment)

#### Haftalar 11-12: İtki Yönlendirme (TVC) ve Dikey İniş Algoritmaları
*   **Teorik Odak:** Dikey iniş yapan roket ve uzay araçlarının kontrolü. Güvenli iniş koridoru sınırları.
*   **Matematiksel Modelleme:** **G-fold** (Guidance for Fuel-Optimal Descent) konveks optimizasyon algoritması. Sınır şartlarının ve itki sınırlarının tanımlanarak gerçek zamanlı yörünge çözülmesi:
    $$\min_{u(t)} \int_{0}^{t_f} ||u(t)|| dt \quad \text{s.t.} \quad \ddot{r} = g + \frac{u(t)}{m(t)}, \quad ||u(t)|| \le U_{\max}$$

#### Haftalar 13-14: Malzeme Yorgunluğu ve Yeniden Sertifikalandırma (Refurbishment)
*   **Teorik Odak:** Uzay ortamından dönen yapıların radyasyon, mikro-meteoroid çarpması ve termal döngü altındaki yorgunluğu. Hasarsızlık testleri (NDT - Non-Destructive Testing) ve yeniden uçuş sertifikasyon süreçleri.

---

## 📐 Tasarım Projesi ve Uygulama

### Proje Görevi: Yeniden Kullanılabilir Isı Kalkanı Kalınlık Analizi
*   **Detay:** Öğrenciler, `scripts/reentry_thermal_analysis.py` betiğini kullanarak farklı atmosfere giriş senaryolarında oluşan Sutton-Graves pik ısı akısını hesaplayacaktır. Elde edilen verilere göre, erime sıcaklığı 1400°C olan bir platform için gerekli minimum HRSI karo kalınlığını 1D ısı iletim denklemi ile hesaplayacaklardır:
    $$\frac{dT}{dt} = \alpha \frac{d^2T}{dx^2}$$

---

## 📚 Önerilen Akademik Kaynaklar
1.  **Griffin, M. D., & French, J. R. (2004).** *Space Vehicle Design* (2. Baskı). AIAA Education Series.
2.  **Sutton, K., & Graves, R. A. (1971).** *A Practical Numerical Method for Determining Convective Heat-Transfer Rates to Rapidly Deforming Bodies*. NASA TR R-376.
3.  **Acikmese, B., & Blackmore, L. (2013).** *Lossless Convexification of Nonconvex Control Bound and Pointing Constraints of the Fuel-Optimal Powered Descent Guidance*. IEEE Transactions on Control Systems Technology.
