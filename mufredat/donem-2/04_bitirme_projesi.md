# 🚀 UYDU-202: Bitirme Projesi (Capstone)

UYDU-202 Capstone Projesi, öğrencilerin müfredat boyunca edindikleri tüm teorik, matematiksel ve pratik bilgileri, endüstri standartlarında kapsamlı bir uzay görevi senaryosunda birleştirdikleri ve uyguladıkları nihai ders aşamasıdır.

---

## 📊 Ders Detayları ve Kredi Bilgileri
*   **Ders Kodu:** UYDU-202
*   **Dönem:** Bahar (2. Dönem)
*   **Kredi Yapısı:** 1 Saat Teori + 4 Saat Laboratuvar ve Tasarım
*   **AKTS (ECTS):** 7.5
*   **Ön Koşullar:** UYDU-101, UYDU-102 ve UYDU-201 derslerinin başarıyla tamamlanmış olması.

---

## 🎯 Entegre Görev Senaryosu: "VLEO-OSAM-RETURN"

Öğrencilerden oluşan mühendislik takımları, aşağıdaki 4 aşamalı entegre görevi uçtan uca tasarlamak, analiz etmek, doğrulamak ve kod paketleriyle teslim etmekle yükümlüdür:

### 1. Aşama: VLEO Yörünge Analizi ve Bozunma Modellemesi
*   **Görev Tanımı:** Çok Düşük Dünya Yörüngesi'nde (VLEO) görev yürüten ve itki sisteminde (RAM-EP) arıza oluşan 100 kg'lık bir hedef uydunun (Target) serbest atmosferik sürüklenme etkisi altında irtifa bozunmasının modellenmesi.
*   **Uygulama:** Öğrenciler, uydunun maruz kaldığı sürüklenme kuvvetini yükseklikle değişen atmosferik yoğunluğa göre entegre edecek, uydunun kritik yörünge ömrünü (tahmini düşüş gününü) hesaplayacaktır.

### 2. Aşama: Otonom Yakınlaşma ve Yakalama (RPO & Grappling)
*   **Görev Tanımı:** Aktif bir servis aracının (Chaser), bozunan hedef uyduya güvenli ve yakıt-optimal şekilde yaklaşması ve robotik kolla yakalaması.
*   **Uygulama:** Clohessy-Wiltshire (CW) bağıntılı yörünge denklemlerini kullanarak optimal R-bar ve V-bar yörünge transferlerinin delta-V bütçeleri çözülecek, çarpışmadan kaçınma (collision avoidance) manevra planları ve 6-DOF EKF/UKF durum kestirimleri kodlanacaktır.

### 3. Aşama: Yörüngede Modüler Parça Değişimi (Servicing)
*   **Görev Tanımı:** Yakalanan hedef uydunun arızalı aviyonik modülünün otonom olarak yenisiyle değiştirilmesi.
*   **Uygulama:** Modül arayüzünün standart kılavuz ray (guide rail) toleransları, SPA/xTEDS veri entegrasyonu, mekanik kilitleme mekanizmaları ve elektriksel/akışkan konektörlerinin sıfır sızıntı sızdırmazlık tasarımları 3D CAD üzerinde detaylandırılacaktır.

### 4. Aşama: Kontrollü Geri Dönüş ve Dikey İniş
*   **Görev Tanımı:** Servis aracının (Chaser) hedef modülü aldıktan sonra kontrollü bir şekilde yörüngeden çıkması (De-orbit), atmosfere girmesi ve belirlenen koordinatlara dikey iniş yapması.
*   **Uygulama:** Sutton-Graves convective ısı akısı formülü kullanılarak hipersonik geçiş sırasındaki pik termal yükler hesaplanacak, seramik (HRSI) karo veya PICA-X kalınlığı 1-Boyutlu ısı iletimi ile doğrulanacaktır. TVC (Thrust Vector Control) ve G-fold konveks optimizasyon prensiplerine göre son dikey iniş yörüngesi simüle edilecektir.

---

## 📐 Somut Mühendislik Sınır Şartları (Boundary Conditions)

Takımlar, geliştirdikleri tasarımları ve yazdıkları Python simülasyonlarını aşağıdaki sert fiziksel sınırlar dahilinde doğrulamak zorundadır:

*   **Yörünge Başlangıç Parametreleri:**
    *   Yarı-büyük eksen yüksekliği: $z_0 = 350 \text{ km}$ (Dairesel yörünge)
    *   Yörünge Eğikliği: $i = 97.4^\circ$ (Güneş Eşzamanlı Yörünge - SSO)
*   **Aerodinamik Sürüklenme Kriterleri:**
    *   Uydu Kütlesi: $m = 100 \text{ kg}$
    *   Maksimum Sürüklenme Kesit Alanı: $A_{\text{drag}} = 0.5 \text{ m}^2$
    *   Sürüklenme Katsayısı: $C_d(z)$ (Schaaf-Chambre seyreltilmiş akış modeline uygun hesaplanacaktır)
*   **Kenetlenme ve Yakalama Koşulları:**
    *   Kenetlenme anındaki bağıl hız (Touchdown relative velocity): $\Delta V \le 0.05 \text{ m/s}$
    *   Maksimum açısal hizalama hatası: $\theta_{\text{hizalama}} \le 2.0^\circ$
    *   Maksimum yörünsel yaklaşma hatası (RPO Terminal Box): $\pm 5 \text{ cm}$
*   **Atmosfere Geri Dönüş Termal Kriterleri:**
    *   Burun Yarıçapı (Nose Radius): $R_n = 0.5 \text{ m}$ (Kapsül geometrisi)
    *   Maksimum Kabul Edilebilir Isı Akısı: $q_s \le 100 \text{ W/cm}^2$ (Sutton-Graves modeline göre)
    *   TPS Seçim Kriteri: Pik sıcaklık alüminyum gövdede $150^\circ\text{C}$'yi aşmayacak şekilde karo kalınlığı hesaplanacaktır.
*   **Dikey Dokunma Hızı (Touchdown Parameters):**
    *   Dikey Hız: $v_z \le 2.0 \text{ m/s}$ (Lander ayak dayanım limiti)
    *   Yatay Hız: $v_{xy} \le 0.5 \text{ m/s}$
    *   Maksimum Eğim Açısı: $\theta_{\text{tilt}} \le 3.0^\circ$

---

## 📅 Proje Aşamaları ve Kilometre Taşları (Milestones)

| Aşama / Kilometre Taşı | Teslim Süresi | Değerlendirme Çıktıları |
| :--- | :--- | :--- |
| **SDR (System Definition Review)** | Hafta 2 | Görev konseptinin tanımlanması, GMAT ile ilk yörünge analizi. |
| **PDR (Preliminary Design Review)** | Hafta 6 | İlk CAD modelleri, RPO yaklaşma stratejisi, Sutton-Graves ön hesabı. |
| **CDR (Critical Design Review)** | Hafta 10 | Detaylı parça arayüzleri, dikey iniş kontrol kararlılık analizleri. |
| **TRR (Test Readiness Review)** | Hafta 13 | Geliştirilen python simülasyon kodlarının (`scripts/`) test raporları. |
| **Final Defense & Poster** | Hafta 15 | Jüri önünde teknik sunum, simülasyon demoları ve rapor teslimi. |

---

## 📝 Teslim Edilecek Teknik Belgeler ve Kodlar

1.  **Teknik Tasarım Raporu:** ECSS (European Cooperation for Space Standardization) veya NASA Systems Engineering Handbook standartlarında hazırlanmış CDR (Critical Design Review) belgesi.
2.  **Simülasyon Paketleri:** 
    *   NASA GMAT (.script) yörünge dosyaları.
    *   `scripts/reentry_thermal_analysis.py` ve `scripts/vleo_drag_calculator.py` kullanılarak yapılmış analizlerin sayısal çıktıları ve grafik kodları.
3.  **CAD Dosyaları:** Standardize edilmiş SPA arayüzlerinin, kılavuz raylarının ve kenetlenme halkalarının 3D CAD modelleri (.STEP formatında).

---

## 🏆 Değerlendirme Kriterleri ve Puanlama Rubriği

Takımların projeleri akademik jüri tarafından şu 3 ana başlık altında puanlanacaktır:

### 1. Mühendislik Hesaplamalarının Doğruluğu ve Fiziksel Gerçekçilik (%40)
*   **VLEO Sürüklenme ve Yörünge Ömrü Hesabı (%10):** Atmosferik yoğunluğun yükseklikle üstel değişiminin doğruluğu ve bozunma entegrasyonu kalitesi.
*   **RPO Delta-V Bütçesi (%15):** Clohessy-Wiltshire modeline dayanan transferlerin yakıt-optimal çözümü ve gürültülü telemetri altında EKF/UKF performansı.
*   **Sutton-Graves Isı Akısı ve TPS Kalınlığı (%15):** Termal koruma kalkanı kalınlığı hesabı ve 1D ısı iletim diferansiyel denkleminin doğruluğu.

### 2. Modüler Tasarım ve Otonom Kontrol Mimarisi (%30)
*   **Modüler Platform Arayüz Standartları (%15):** Geliştirilen mekanik/elektriksel arayüzlerin SPA/xTEDS standartlarına uygunluğu ve robotik tolerans toleransı.
*   **Dikey İniş Algoritması (%15):** İniş kontrol sisteminin TVC gimbal kısıtları altında G-fold veya benzeri kararlı/optimal kontrol yöntemleriyle sürülmesi.

### 3. Belgeleme, Kod Kalitesi ve Akademik Sunum (%30)
*   **Kod Standartları ve Çalışabilirlik (%15):** Python kodlarının temiz yazım (PEP8), birim testler (unit tests) ve hata yakalama mekanizmaları barındırması.
*   **Sözlü Savunma ve Raporlama (%15):** Hazırlanan teknik raporun kalitesi ve jüri önünde yapılan mühendislik savunması kalitesi.
