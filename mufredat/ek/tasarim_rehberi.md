# 📐 Modüler Uydu Tasarım ve Arayüz Standartları Rehberi

Yeniden kullanılabilir ve yörüngede servis edilebilir uydular için tasarım standartları, bileşenlerin mekanik, elektriksel, akışkan ve veri arayüzlerinin yörüngede otonom robotik kollarla müdahale edilebilecek düzeyde uyumlu ve toleranslı olmasına dayanır.

---

## 1. Mekanik Arayüz Standartları (Mechanical & Docking Interfaces)

Robotik manipülatörlerin (robot kolları) uyduları yakalaması ve modülleri takıp çıkarması için arayüz tasarımlarının standartlaştırılması gerekir:

*   **Androjen Kenetlenme Mekanizmaları (Androgynous Docking):** Servis aracının (Chaser) hedef uyduya kilitlenmesini sağlayan, iki tarafın da hem aktif hem pasif rol alabildiği **LIDS (Low Impact Docking System)** veya **IDSS (International Docking System Standard)** uyumlu arayüz halkaları.
*   **Robotik Tutamaçlar (Grapple Fixtures):** Uzay istasyonlarındaki standart **FRGF (Flight Releasable Grapple Fixture)** ve veri/güç aktarımlı **PDGF (Payload Data Grapple Fixture)** pimleri. Bu pimler, robot ucunun (end-effector) kaymadan sıkıca kenetlenmesini sağlar.
*   **Kılavuz Kanallar ve Konik Yuvalar (Guide Rails & Alignment Cones):** Robotik kolların mikro-yerçekimi altındaki $\pm 5 \text{ mm}$ mertebesindeki konumlandırma hatalarını mekanik olarak sönümleyen ve modülü yuvaya kendiliğinden yerleştiren açılı kılavuz rayları ve konik kılavuz delikleri.
*   **Görsel İşaretçiler (Visual & Fiducial Markers):** Bilgisayarlı görü (Computer Vision) ve LiDAR sistemlerinin hedefin yönünü (pose) anlık kestirebilmesi için modül etrafına yerleştirilen yüksek kontrastlı **AprilTag** veya **ArUco** görsel kodları.

---

## 2. Elektriksel, Akışkan ve Termal Arayüzler

Modül değişimi veya yakıt transferi esnasında bağlantı güvenliğini sağlayan alt arayüz parametreleri:

*   **Pogo-Pin Elektriksel Arayüzleri:** Sık sık takılıp sökülen modüller arasında esnek, yay baskılı altın kaplama pogo-pin dizilimleri kullanılır. Uzay vakumunda metallerin soğuk kaynaklanmasını (Cold Welding) engellemek için konektör gövdeleri PEEK (Polieter eter keton) gibi yüksek performanslı polimerlerden imal edilir.
*   **Sıfır-Sızıntılı Yakıt İkmal Portları (Zero-Leak Quick Disconnect):** Yörüngede yakıt ikmali için basınç altındaki sıvı veya gazların sızmasını önleyen, bilyeli kilit sistemine sahip yaylı valfler. İki valf tamamen birbirine kilitlenmeden akışkan yolu açılmaz, ayrılma anında ise mililitre mertebesinde dahi kaçak yaşanmaz.
*   **Termal Arayüz Malzemeleri (TIM):** Güç üreten modüllerin ürettiği ısının ana uydu radyatörlerine iletilebilmesi için, modül birleşme yüzeylerinde yüksek ısıl iletkenlik sağlayan esnek ve vakuma dayanıklı termal pedler veya grafit folyo arayüzleri.

---

## 3. Veri ve Yazılım Entegrasyon Protokolleri

Aviyonik sistemlerin modül değişimini anlık algılaması ve yazılımsal konfigüre etmesi:

*   **SpaceWire ve SpaceFibre Veri Yolu:** Yüksek hızlı görüntü ve sensör verilerini aktarmak için geliştirilen, hata töleranslı (fail-safe) standart veri yolları.
*   **xTEDS Standartları:** Her modülün veri tanımlarını, komut setlerini ve çalışma frekanslarını içeren XML tabanlı **xTEDS (eXtensible Transducer Electronic Data Sheet)** dosyası uçuş bilgisayarına otomatik yüklenir.
*   **Hot-Swappable (Sıcak Tak-Çıkar) Altyapısı:** Enerji kesilmeden modül takılıp söküldüğünde veri hattında oluşabilecek elektriksel arkları ve akım piklerini engelleyen koruyucu tampon devreler.

---

## 🛠️ Tasarım Mühendisliği Gereksinimleri (Design Requirements - DR)

Takımların tasarımlarında uyması gereken temel kurallar:

1.  **[DR-01] Tolerans Yönetimi:** Tüm değiştirilebilir aviyonik modüller, robotik kolun uç konumlandırma hatasını kompanse edecek şekilde giriş ağzında en az $15^\circ$ eğimli kılavuz pahlarına (chamfers) sahip olmalıdır.
2.  **[DR-02] Soğuk Kaynak Önleme:** Birbiriyle temas eden metalik yüzeyler (özellikle alüminyum ve titanyum parçalar), uzay vakumunda moleküler olarak birbirine kaynamaması için **Anodik Oksidasyon (Eloksal)** veya kuru yağlayıcı (MoS2 - Molibden Disülfür) kaplamalara sahip olmalıdır.
3.  **[DR-03] Acil Durum Bırakma (Emergency Release):** Tüm kilit mekanizmaları, motor arızası veya kilit sıkışması ihtimaline karşı robotik kolun mekanik olarak tetikleyebileceği bir acil durum yaylı bırakma (redundant pyrotechnic or mechanical spring release) sistemine sahip olmalıdır.
4.  **[DR-04] EMI/EMC Koruma:** Modüler arayüz hatları, uzay radyasyonu ve elektromanyetik parazitlerden (EMI) korunmak için alüminyum gövde üzerinden ortak şasiye topraklanmalıdır.

---

## 📖 İleri Okuma ve Mühendislik Standartları
*   **ISO 24330:2022:** *Space systems — Rendezvous and Proximity Operations (RPO) and On-Orbit Servicing (OOS) Requirements*.
*   **NASA OSAM-1 Reference:** *On-Orbit Servicing, Assembly, and Manufacturing 1 Hardware Standards*.
*   **AIAA S-111A:** *Space Plug-and-Play Architecture Standard Series*.
