# 🌌 UYDU-101: Atmosferik Uzay Sınırı ve VLEO Dinamiği

Bu ders, "Very Low Earth Orbit" (VLEO) olarak tanımlanan **200-450 km** irtifa aralığındaki fiziksel zorlukları, üst atmosfer dinamiğini, seyreltilmiş gaz akış rejimlerini ve bu bölgede operasyon yapan uydu sistemlerinin yörünge ömrü koruma stratejilerini ileri düzey akademik ve matematiksel modellerle ele alır.

---

## 📊 Ders Detayları ve Kredi Bilgileri
*   **Ders Kodu:** UYDU-101
*   **Dönem:** Güz (1. Dönem)
*   **Kredi Yapısı:** 3 Saat Teori + 2 Saat Uygulama
*   **AKTS (ECTS):** 7.5
*   **Ön Koşullar:** Akışkanlar Mekaniği, Diferansiyel Denklemler, Temel Fizik-II

---

## 📅 Haftalık Ayrıntılı Ders Planı

### 🟦 Kısım I: Seyreltilmiş Gaz Dinamiği ve Atmosfer Fiziği

#### Haftalar 1-2: Karman Hattı ve Termosfer/Ekzosfer Sınır Fiziği
*   **Teorik Odak:** Karman Hattı'nın ($100 \text{ km}$) fiziksel ve aerodinamik tanımı. Yerçekimi kuvveti ile aerodinamik kaldırma kuvveti arasındaki denge limiti. Üst atmosferin termodinamik yapısı.
*   **Matematiksel Modelleme:** Hidrostatik denge denklemi ve sıcaklık gradyanına bağlı basınç dağılımları:
    $$\frac{dP}{dz} = -\rho(z) \cdot g(z)$$
*   **Okumalar:** Fortescue, Bölüm 3: *The Space Environment*.

#### Haftalar 3-4: Knudsen Sayısı ve Akış Rejimleri
*   **Teorik Odak:** Süreklilik (Continuum) modelinin geçerliliğini yitirmesi. Moleküler ortalama serbest yol ($\lambda$) kavramı. Akış rejimlerinin sınıflandırılması.
*   **Matematiksel Modelleme:** Knudsen Sayısı ($Kn$) formülü:
    $$Kn = \frac{\lambda}{L} = \frac{k_B \cdot T}{\sqrt{2} \cdot \pi \cdot d^2 \cdot P \cdot L}$$
    *   $Kn < 0.01$: Sürekli Akış Rejimi (Continuum Flow)
    *   $0.01 < Kn < 0.1$: Kayma Akışı Rejimi (Slip Flow)
    *   $0.1 < Kn < 10$: Geçiş Rejimi (Transition Flow)
    *   $Kn > 10$: Serbest Moleküler Akış Rejimi (Free Molecular Flow)
*   **Laboratuvar Uygulaması:** İrtifaya bağlı Knudsen sayısı hesaplama simülasyonları.

---

### 🟩 Kısım II: VLEO Çevre Etkileri ve Aerodinamik Sürüklenme

#### Haftalar 5-6: Serbest Moleküler Akışta Aerodinamik Sürüklenme Modellemesi
*   **Teorik Odak:** VLEO irtifasında sürüklenme katsayısının ($C_d$) klasik $2.0$ değerinden farklılaşması. Moleküllerin uydu yüzeyi ile etkileşimi (Specular vs. Diffuse Yansıma). Sentetik momentum transfer katsayıları ($\sigma$).
*   **Matematiksel Modelleme:** Sürüklenme kuvveti ($F_d$) ve sürüklenme katsayısı ($C_d$) entegrasyonu:
    $$F_d = \frac{1}{2} \rho V^2 C_d A$$
    $$C_d = \frac{2}{\sqrt{\pi} \cdot s} \exp(-s^2 \cos^2\theta) + \left(\frac{2s^2 + 1}{s^2}\right) \text{erf}(s \cos\theta) + \frac{\sqrt{\pi}}{s} \left(\frac{T_w}{T_i}\right)^{1/2} \cos\theta$$
    *Burada $s = V / \sqrt{2 R T}$ moleküler hız oranı, $T_w$ duvar sıcaklığı, $T_i$ gelen gaz sıcaklığıdır.*

#### Haftalar 7-8: Atomik Oksijen (ATOX) Reaksiyonları ve Korozyon Mekanizmaları
*   **Teorik Odak:** Güneş UV radyasyonu etkisiyle çift atomlu oksijenin parçalanması ve yüksek enerjili tekli oksijen radikallerinin (ATOX) oluşumu. Malzemelerin kimyasal olarak oksitlenmesi ve kütle kaybı.
*   **Matematiksel Modelleme:** Aşınma Hızı ve Kütle Kaybı formülü:
    $$\Delta m = E_y \cdot F_{\text{ATOX}} \cdot A \cdot t$$
    *   $E_y$: Aşınma Verimi ($cm^3/\text{atom}$) (Örn: Kapton için $3.0 \times 10^{-24} \text{ cm}^3/\text{atom}$)
    *   $F_{\text{ATOX}}$: Yıllık birikimli ATOX akısı ($\text{atoms/cm}^2\cdot\text{s}$)
*   **Korunma Teknolojileri:** $SiO_2$, Teflon (FEP), Kapton-AOD gibi koruyucu yüzey kaplamaları.

---

### 🟨 Kısım III: İtki ve Yörünge Kontrol Algoritmaları

#### Haftalar 9-10: RAM-EP (Air-Breathing Electric Propulsion) Teknolojisi
*   **Teorik Odak:** VLEO'da yakıt taşımadan sonsuz yörünge ömrü sağlama vizyonu. Atmosferik sürüklenme gazını toplayan özel difüzör (intake) tasarımları. Gazın iyonlaştırılması ve hızlandırılması.
*   **Mühendislik Parametreleri:** Gaz yakalama verimliliği ($\eta_{in}$), Helikon iyonizasyon odası tasarımı ve Izgaralı İyon İticisi (Gridded Ion Thruster) verimlilik limitleri.

#### Haftalar 11-12: Sürekli Düşük İtki (Low-Thrust) ile Yörünge Koruma Algoritmaları
*   **Teorik Odak:** Sürüklenme kuvvetini anlık olarak dengeleyen aktif kontrol algoritmaları. Lyapunov tabanlı kapalı çevrim kontrolcü tasarımı.
*   **Matematiksel Modelleme:** Gauss varyasyonel denklemleri çerçevesinde yarı-büyük eksen ($a$) değişimi:
    $$\frac{da}{dt} = \frac{2 a^2 V}{\mu} \cdot (a_{\text{itki}} - a_{\text{sürüklenme}})$$

#### Haftalar 13-14: VLEO Haberleşme ve Doppler Kayması Yönetimi
*   **Teorik Odak:** Yüksek yörünge hızından kaynaklanan Doppler etkisi. Yer istasyonları ile haberleşme pencerelerinin kısıtlı süresi (geçi sürelerinin optimize edilmesi).
*   **Formülasyon:**
    $$f_{\text{alınan}} = f_{\text{yayınlanan}} \left(1 - \frac{\vec{v} \cdot \vec{r}}{c \cdot |\vec{r}|}\right)$$

---

## 🔬 Laboratuvar Uygulamaları ve Ödevler

### Laboratuvar 1: VLEO İrtifa Kaybı Modellemesi (Sayısal Entegrasyon)
*   **Hedef:** `scripts/vleo_drag_calculator.py` betiğini temel alarak, Euler-Cromer veya Runge-Kutta 4 (RK4) sayısal yöntemleriyle uydunun 250 km, 300 km ve 350 km başlangıç yörüngelerinden itibaren serbest düşüş sürelerini tahmin etmek.
*   **Beklenen Rapor:** İrtifaya bağlı sürüklenme kuvveti grafikleri ve yörünge ömrü eğrileri.

---

## 📚 Önerilen Akademik Kaynaklar
1.  **Fortescue, P., Swinerd, G., & Stark, J. (2011).** *Spacecraft Systems Engineering* (4. Baskı). John Wiley & Sons.
2.  **Koppenwallner, G. (2009).** *Rarefied Gas Dynamics for Space Technology*. Springer.
3.  **NASA Goddard Space Flight Center (2018).** *Atomic Oxygen Erosion in Low Earth Orbit (LEO)* - Teknik Bülten.
