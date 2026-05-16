# 📐 Modüler Uydu Tasarım ve Arayüz Rehberi

Yeniden kullanılabilir ve yörüngede servis edilebilir uydular için tasarım standartları, bileşenlerin mekanik, elektriksel ve veri arayüzlerinin uyumluluğuna dayanır.

---

## 1. Mekanik Arayüzler (Docking & Berthing)
*   **Standart Kenetlenme Portu (SSID):** Servis aracının uyduya fiziksel olarak kilitlendiği ana nokta. 
*   **Robotik Tutamaçlar (Grapple Fixtures):** Robotik kolun uyduda güvenle tutunabileceği standart noktalar.
*   **Alignment Markers:** Bilgisayarlı görü sistemleri için yüksek kontrastlı optik işaretçiler.

## 2. Elektriksel ve Akışkan Arayüzleri
*   **Yörüngede Yakıt İkmali (Refueling):** Sızdırmazlığı garanti eden, basınçlı akışkan transfer valfleri.
*   **Güç Aktarımı:** Servis aracından hedef uyduya acil durum güç aktarımı sağlayan endüktif veya temaslı konektörler.
*   **Termal Bağlantılar:** Modül değişiminde termal iletkenliği koruyan yüzey tasarımları.

## 3. Veri ve Yazılım Arayüzleri
*   **SpaceWire / SpaceFibre:** Modüller arası yüksek hızlı veri iletişimi.
*   **PnP (Plug-and-Play) Yazılım:** Yeni takılan bir sensörün veya batarya modülünün sistem tarafından otomatik tanınması (Self-describing modules).

---

## 🛠️ Tasarım Gereksinimleri (DR)
1.  **DR-01:** Tüm değiştirilebilir modüller, robotik kolun hata payını tolere edebilecek "kılavuz kanallara" (guide rails) sahip olmalıdır.
2.  **DR-02:** Elektriksel konektörler, uzay vakumunda kaynaklanmayı önlemek için özel kaplamalara sahip olmalıdır.
3.  **DR-03:** Modül kilit mekanizmaları, manuel (robotik) acil durum bırakma (emergency release) özelliğine sahip olmalıdır.

---

## 📖 İleri Okuma
*   *ISO 24330:2022 - Space systems — Rendezvous and Proximity Operations (RPO) and On-Orbit Servicing (OOS)*.
*   *NASA On-orbit Servicing, Assembly, and Manufacturing (OSAM) Standards*.
