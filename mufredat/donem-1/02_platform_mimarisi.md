# 🛰️ UYDU-102: Yeniden Kullanılabilir Uydu Platform Tasarımı

Geleneksel "fırlat ve unut" modelinden "bakım yapılabilir ve geri döndürülebilir" modeline geçişin mühendislik esaslarını inceler. Bu ders, uydu ömrünü uzatan ve maliyetleri düşüren donanım mimarilerine odaklanır.

## 📅 Haftalık Ders Planı

### Haftalar 1-4: Modüler Bus ve Standartlar
*   **Plug-and-Play (PnP) Aviyonik:** SPA (Space Plug-and-Play Architecture) standartları ve veri yolları.
*   **Modüler Mekanik Arayüzler:** Robotik kollar için standart yakalama noktaları (Grapple Fixtures) ve yakıt transfer portları.
*   **Yazılım Tanımlı Uydu:** Donanım bağımsız görev güncellemeleri ve yörüngede yazılım tabanlı hata giderme.
*   **Açık Sistem Mimarisi:** Bileşen seviyesinde "hot-swap" (çalışırken değiştirme) kabiliyeti.

### Haftalar 5-8: Geri Dönüş ve Termal Koruma (TPS)
*   **Atmosfere Geri Dönüş Mekaniği:** Balistik katsayısı (Ballistic Coefficient) ve ısıl yük korelasyonları.
*   **Sutton-Graves Isı Akısı Modellemesi:** Durma noktası (stagnation point) konvektif ısınma hesaplamaları.
*   **TPS (Thermal Protection Systems) Seçimi:**
    *   **Ablatif Sistemler:** PICA-X ve Avcoat gibi kendini feda eden karbon bazlı yapılar.
    *   **Yeniden Kullanılabilir Sistemler:** HRSI (High-temperature Reusable Surface Insulation) seramik karolar ve RCC.
*   **Aerobraking ve Aerocapture:** Yakıt tasarrufu için atmosferin üst katmanlarını kullanma stratejileri.

### Haftalar 9-14: İniş ve Kurtarma Teknolojileri
*   **Yörüngeden Çıkarma (De-orbit):** Aktif itki vs. pasif yöntemler (Drag Sails).
*   **Dikey İniş (Vertical Landing):** İtki yönlendirme (Thrust Vector Control) ve G-fold algoritması gibi hassas iniş teknikleri.
*   **Refurbishment (Yenileme):** Uzay ortamının malzeme yorgunluğu üzerindeki etkisi ve yeniden sertifikalandırma süreçleri.

## 📐 Tasarım Projesi
*   **Görev:** Modüler bir sensör paketinin (Payload) yörüngede otonom olarak değiştirilmesini sağlayan mekanik ve elektriksel arayüz tasarımı.
*   **Araçlar:** CAD tasarımı ve `scripts/reentry_thermal_analysis.py` kullanılarak ısı kalkanı kalınlık analizi.

## 📚 Kaynakça
1.  *Satellite Technology: Principles and Applications*, Anil K. Maini.
2.  *Space Vehicle Design*, Michael D. Griffin.
3.  *Elements of Propulsion: Gas Turbines and Rockets*, Jack D. Mattingly.
