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
Öğrencilerden oluşan mühendislik takımları, aşağıdaki 4 aşamalı entegre görevi uçtan uca tasarlamak, analiz etmek ve doğrulamakla yükümlüdür:

1.  **Aşama 1: VLEO Yörünge Analizi:** Çok Düşük Dünya Yörüngesi'nde (350 km) görev yapan ve itki sisteminde arıza oluştuğu için hızla irtifa kaybeden bir uydunun (Target) yörünge ömrünün modellenmesi.
2.  **Aşama 2: Otonom Yakınlaşma ve Yakalama (RPO & Grappling):** Bir otonom servis aracının (Chaser) hedef uyduya güvenli bir şekilde yaklaşması, Clohessy-Wiltshire denklemlerine göre relative yörünge kontrolü yapması ve robotik kol ile hazırlıksız hedefi yakalaması.
3.  **Aşama 3: Yörüngede Modüler Parça Değişimi:** Servis aracının, hedefin arızalı aviyonik modülünü standard SPA/xTEDS kılavuz ray arayüzlerini kullanarak otonom olarak yenisiyle değiştirmesi.
4.  **Aşama 4: Kontrollü Geri Dönüş ve Dikey İniş:** Servis aracının yörüngeden çıkarılması (De-orbit), Sutton-Graves formüllerine göre atmosfere geri dönüş ısıl yük analizinin yapılması ve yeryüzüne dikey inişinin kontrol edilmesi.

---

## 📐 Somut Mühendislik Sınır Şartları (Boundary Conditions)
Takımlar tasarımlarını şu fiziksel ve operasyonel limitler dahilinde gerçekleştirmelidir:

*   **Yörünge Başlangıç İrtifası:** $350 \text{ km}$ (Dairesel yörünge, eğiklik $i = 97.4^\circ$)
*   **Maksimum Sürüklenme Alanı:** $A_{\text{drag}} = 0.5 \text{ m}^2$ (Uydu kütlesi $m = 100 \text{ kg}$)
*   **Hedef Yakalama Relative Hızı:** Kenetlenme anında bağıl hız $\Delta V \le 0.05 \text{ m/s}$ ve açısal sapma $\le 2^\circ$
*   **Geri Dönüş Burun Yarıçapı:** $R_n = 0.5 \text{ m}$ (Kapsül geometrisi)
*   **Maksimum Isı Akısı Sınırı:** Sutton-Graves modeline göre durma noktası ısı akısı $q_s \le 100 \text{ W/cm}^2$ (TPS malzemesi HRSI Karo veya PICA-X seçimine uygun olmalıdır).
*   **Dikey Dokunma Hızı (Touchdown):** Yere temas anında dikey hız $v_z \le 2.0 \text{ m/s}$, yatay hız $v_{xy} \le 0.5 \text{ m/s}$.

---

## 📅 Proje Aşamaları ve Kilometre Taşları (Milestones)

| Hafta | Aşama / Kilometre Taşı | Açıklama |
| :--- | :--- | :--- |
| **Hafta 2** | **SDR (System Definition Review)** | Görev mimarisinin tanımlanması, GMAT ile ilk yörünge analizi. |
| **Hafta 6** | **PDR (Preliminary Design Review)** | İlk CAD modelleri, RPO yaklaşma stratejisi, Sutton-Graves ön hesabı. |
| **Hafta 10** | **CDR (Critical Design Review)** | Detaylı parça arayüzleri, dikey iniş kontrol kararlılık analizleri. |
| **Hafta 13** | **TRR (Test Readiness Review)** | Geliştirilen python simülasyon kodlarının (`scripts/`) test raporları. |
| **Hafta 15** | **Final Defense & Poster** | Jüri önünde teknik sunum, simülasyon demoları ve rapor teslimi. |

---

## 📝 Teslim Edilecek Teknik Belgeler ve Kodlar
*   **Tasarım Raporu:** NASA Systems Engineering standardında CDR Raporu (PDF formatında).
*   **Simülasyon Paketleri:** 
    *   NASA GMAT (.script) dosyaları.
    *   `scripts/reentry_thermal_analysis.py` ve `scripts/vleo_drag_calculator.py` kullanılarak yapılmış analizlerin sayısal çıktıları ve grafik kodları.
*   **CAD Dosyaları:** Modüler uydu arayüzü ve kılavuz raylarının 3D CAD modelleri (.STEP formatında).

---

## 🏆 Değerlendirme Kriterleri ve Puanlama Rubriği

*   **1. Mühendislik Hesaplamalarının Doğruluğu (%40):**
    *   Sürüklenme ve yörünge ömrü hesaplarının doğruluğu (%10)
    *   RPO Delta-V bütçesinin Clohessy-Wiltshire modeline uygunluğu (%15)
    *   Sutton-Graves Isı Akısı ve TPS kalınlığı hesaplarının doğruluğu (%15)
*   **2. Modülerlik ve Yenilikçilik (%30):**
    *   Uydu platformunun modüler arayüz tasarımı ve standartlara (SPA/xTEDS) uygunluğu (%15)
    *   Dikey iniş kontrol sisteminin konveks optimizasyon (G-fold) veya benzeri modern kontrolcü kalitesi (%15)
*   **3. Belgeleme, Kod ve Sunum Kalitesi (%30):**
    *   Açık kaynak standartlarında yazılmış, hata içermeyen Python analiz kodları (%15)
    *   Teknik rapor kalitesi ve jüri önündeki sözlü savunma performansı (%15)
