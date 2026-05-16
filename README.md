# 🛰️ Yeniden Kullanılabilir Uydu Teknolojileri ve Yörüngede Tamirat Mühendisliği

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Academic Grade](https://img.shields.io/badge/Status-Academic--Grade-blue.svg)](#)
[![Field](https://img.shields.io/badge/Field-Aerospace--Engineering-orange.svg)](#)

Bu portal; atmosferik uzay sınırı (**VLEO**), yeniden kullanılabilir uydu mimarileri ve yörüngede otonom servis, bakım ve tamirat (**OSAM**) teknolojilerini kapsayan, ileri düzey bir mühendislik müfredatı ve açık kaynaklı kaynak havuzudur.

Havacılık, uzay, kontrol ve robotik mühendisliği disiplinlerinin kesişim noktasında yer alan yeni nesil uzay operasyonları için akademik ve pratik bir rehber sunmaktadır.

---

## 🎯 Projenin Amacı ve Kapsamı

Geleneksel uzay görevleri, uyduların ömrü bittiğinde sistemlerin uzay çöpüne dönüşmesi üzerine kuruludur. Bu müfredat; uzay sürdürülebilirliği ve maliyet optimizasyonu için üç ana sütuna odaklanır:

1.  **VLEO (Very Low Earth Orbit):** 200-450 km arası irtifada aerodinamik etkiler ve Atomik Oksijen (ATOX) korozyonu altında operasyon.
2.  **Yeniden Kullanılabilirlik (Reusability):** Görevini tamamlayan bileşenlerin kontrollü geri dönüşü (re-entry) ve dikey iniş mekanizmaları.
3.  **OSAM (On-Orbit Servicing, Assembly, and Manufacturing):** Robotik kollarla yakalama, yörüngede yakıt ikmali ve modüler parça değişimi.

---

## 📂 Depo Yapısı

| Klasör / Dosya | Açıklama |
| :--- | :--- |
| [**mufredat/**](./mufredat/) | Akademik ders içerikleri, haftalık planlar ve AKTS detayları. |
| [**scripts/**](./scripts/) | Yörünge mekaniği, ATOX ve yakıt bütçesi simülasyonları. |
| [**dashboard/**](./dashboard/) | Müfredatı görselleştiren interaktif web arayüzü. |
| [**TERIMLER.md**](./TERIMLER.md) | Kapsamlı uzay ve havacılık teknik terimler sözlüğü. |
| [**Vaka Analizleri**](./mufredat/ek/vaka_analizleri.md) | MEV-1, ClearSpace-1 gibi gerçek görev incelemeleri. |
| [**Sürdürülebilirlik**](./mufredat/ek/surdurulebilirlik_ve_cop.md) | Uzay çöpü yönetimi ve Kessler Sendromu analizi. |

---

## 🎓 Müfredat Özeti

### 🟦 1. Dönem: Sınır Fiziği ve Platform Mimarisi
*   **VLEO Dinamiği:** Karman Hattı fiziği ve seyreltilmiş gaz aerodinamiği.
*   **Platform Tasarımı:** Modüler bus mimarileri ve Termal Koruma Sistemleri (TPS).

### 🟩 2. Dönem: Otonom Uzay Robotiği ve Müdahale
*   **OSAM Teknikleri:** RPO (Rendezvous and Proximity Operations) kinematiği.
*   **Robotik Müdahale:** Sıfır yerçekimi ortamında çok eklemli kol kontrolü.

---

## 🛠️ Teknik Araçlar
*   **NASA GMAT:** Yörünge analizi ve RPO doğrulaması.
*   **ROS 2:** Robotik kol kinematiği ve otonom çevre algılama.
*   **Orekit & Spice:** Python tabanlı düşük seviyeli uzay dinamiği kütüphaneleri.

---

## 🚀 Başlangıç

Proje içeriklerini incelemek için [Müfredat Ana Sayfası](./mufredat/README.md) dosyasından başlayabilir veya [Dashboard](./dashboard/index.html) üzerinden görsel bir tura çıkabilirsiniz.

---

## 📜 Lisans
Bu proje **MIT Lisansı** altında korunmaktadır. Detaylar için [LICENSE](./LICENSE) dosyasına bakınız.