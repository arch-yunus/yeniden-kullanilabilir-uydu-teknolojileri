# 🤖 UYDU-201: Yörüngede Servis, Bakım ve Tamirat (OSAM)

Bu ders, otonom uzay operasyonlarının en karmaşık aşaması olan "yakınlaşma ve fiziksel müdahale" teknolojilerine odaklanır. OSAM (On-Orbit Servicing, Assembly, and Manufacturing) operasyonları, uydu ömrünü uzatmanın ve yörüngede sürdürülebilirliğin anahtarıdır.

## 📅 Haftalık Ders Planı

### Haftalar 1-4: RPO ve Göreceli Navigasyon
*   **RPO (Rendezvous and Proximity Operations):** Clohessy-Wiltshire (Hill's) denklemleri ve bağıntılı yörünge mekaniği.
*   **Sensör Füzyonu:** LiDAR, Star Tracker ve IR kameralar ile otonom hedef tanıma ve takip.
*   **Göreceli Navigasyon:** Hedefin 6-DOF (Degrees of Freedom) poz ve oryantasyon kestirimi.
*   **Yaklaşma Güvenliği:** Pasif güvenli yörüngeler ve çarpışmadan kaçınma manevraları.

### Haftalar 5-8: Uzay Robotiği ve Yakalama (Grappling)
*   **Mikro-yerçekimi Kinematiği:** "Floating base" robotik sistemler ve kütle merkezi dinamikleri.
*   **Hazırlıksız Hedef Yakalama (Unprepared Targets):** Landsat 7 (OSAM-1) örneğinde olduğu gibi, yakalama kolu veya handle bulunmayan uyduların robotik kolla kavranması.
*   **Momentum Yönetimi:** Robotik kol hareketinin ana gövde (servicer) üzerindeki perturbasyonlarını dengeleme (Attitude Control System entegrasyonu).
*   **Dexterous Manipulation:** Çok eklemli kollar ile hassas cıvata sökme, kablo kesme ve vana erişim operasyonları.

### Haftalar 9-14: Yörüngede Yakıt İkmali ve Montaj
*   **Fluid Transfer:** Yörüngede yakıt (Hidrazin, Ksenon vb.) transferi için basınçlandırma ve sızdırmazlık protokolleri.
*   **On-Orbit Assembly (OOA):** Modüler antenlerin ve büyük ölçekli güneş panellerinin yörüngede birleştirilmesi.
*   **In-Space Manufacturing (ISM):** 3D baskı (additive manufacturing) teknikleri ile uzayda parça üretimi.
*   **Sürdürülebilirlik:** Aktif Çöp Kaldırma (ADR - Active Debris Removal) görevlerinde OSAM tekniklerinin kullanımı.

## 💻 Simülasyon Uygulaması
*   **Proje:** `scripts/mission_control_cli.py` üzerinden erişilebilen, bir servis uydusunun yakıtı bitmiş bir hedefle senkronizasyon ve kenetlenme Delta-V bütçesi analizi.
*   **Araçlar:** ROS 2 (MoveIt 2) ile robotik kol yörünge planlaması.

## 📚 Kaynakça
1.  *Robot Dynamics and Control*, Spong, Hutchinson, Vidyasagar.
2.  *Space Robotics*, Yaobing Wang.
3.  *NASA OSAM-1 Mission Reference Guide*.
4.  *Spacecraft Dynamics and Control*, Marcel J. Sidi.
