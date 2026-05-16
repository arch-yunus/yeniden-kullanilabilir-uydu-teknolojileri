# 🌌 UYDU-101: Atmosferik Uzay Sınırı ve VLEO Dinamiği

Bu ders, "Very Low Earth Orbit" (VLEO) olarak tanımlanan 200-450 km irtifa aralığındaki fiziksel zorlukları ve bu bölgede operasyon yapan uydu sistemlerinin dinamiklerini ele alır.

## 📅 Haftalık Ders Planı

### Haftalar 1-4: Karman Hattı ve Termosfer Fiziği
*   Atmosferin katmanları ve Karman Hattı'nın (100km) ötesindeki geçiş bölgesi.
*   Seyreltilmiş gaz dinamiği (Rarefied Gas Dynamics) prensipleri.
*   Knudsen sayısı ve akış rejimlerinin (Sürekli, Kayma, Serbest Moleküler) belirlenmesi.

### Haftalar 5-8: Aerodinamik Sürüklenme ve ATOX
*   Serbest moleküler akış rejiminde sürüklenme (drag) katsayısının hesaplanması.
*   **Atomik Oksijen (ATOX)** korozyonu: Malzeme bozunması ve hayatta kalma stratejileri.
*   Yüzey kaplama teknolojileri ve korozyon dirençli polimerler (Teflon, Kapton vb.).

### Haftalar 9-14: İtki ve Yörünge Koruma
*   **RAM-EP (Air-Breathing Electric Propulsion):** Atmosferden toplanan gazı yakıt olarak kullanan itki sistemleri.
*   VLEO yörünge koruma algoritmaları ve otomatik irtifa kontrolü.
*   VLEO uydularında haberleşme penceresi optimizasyonu ve Doppler kayması yönetimi.

## 🔬 Laboratuvar Uygulaması
*   `scripts/vleo_drag_calculator.py` scripti kullanılarak, farklı irtifalarda (250km, 300km, 350km) uydunun yörüngede kalma süresinin (orbital lifetime) tahmini.

## 📚 Kaynakça
1.  *Spacecraft Systems Engineering*, Peter Fortescue.
2.  *Aerodynamics of the Upper Atmosphere*, J.E. Anderson.
