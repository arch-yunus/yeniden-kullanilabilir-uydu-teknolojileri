# 🌌 UYDU-101: Atmosferik Uzay Sınırı ve VLEO Dinamiği

Bu ders, **Very Low Earth Orbit (VLEO - Çok Düşük Dünya Yörüngesi)** olarak tanımlanan **200 km ile 450 km** irtifa aralığındaki sınır fiziksel koşullarını, seyreltilmiş gaz dinamiğini (Rarefied Gas Dynamics) ve bu bölgede operasyon yürüten uzay araçlarının yörünge ömrünü korumaya yönelik termo-aerodinamik tasarım parametrelerini ileri düzey matematiksel ve akademik modellerle ele alır.

---

## 📊 Ders Detayları ve Kredi Bilgileri
*   **Ders Kodu:** UYDU-101
*   **Dönem:** Güz (1. Dönem)
*   **Kredi Yapısı:** 3 Saat Teori + 2 Saat Uygulama
*   **AKTS (ECTS):** 7.5
*   **Ön Koşullar:** Akışkanlar Mekaniği, Diferansiyel Denklemler, Klasik Termodinamik

---

## 📅 Haftalık Ayrıntılı Ders Planı

### 🟦 Kısım I: Seyreltilmiş Gaz Dinamiği ve Atmosfer Fiziği

#### Haftalar 1-2: Karman Hattı ve Üst Atmosferin Termodinamik Profili
Karman Hattı ($100 \text{ km}$), havacılık uçuş mekaniği ile uzay yörünge mekaniği arasındaki geçiş sınırını tanımlar. Bu bölgede aerodinamik kaldırma (lift) kuvvetinin uzay aracının ağırlığını taşıyabilmesi için gereken çizgisel hız, dairesel yörünge hızına eşitlenir:
$$v_{\text{lift}} = \sqrt{\frac{2m g}{\rho C_L A}} \approx v_{\text{orbital}} = \sqrt{\frac{\mu}{R_E + z}}$$

Termosfer ve ekzosfer katmanlarının termodinamik yapısı, Güneş'in ekstrem ultraviyole (EUV) radyasyonu ve jeomanyetik fırtınalarla doğrudan ilişkilidir. Üst atmosferin hidrostatik dengesi, yükseklikle değişen sıcaklık gradyanına bağlı olarak modellenir:
$$\frac{dP}{dz} = -\rho(z) g(z) = - \frac{P(z) M(z) g(z)}{R_u T(z)}$$
Burada $M(z)$ ortalama moleküler ağırlık, $g(z)$ yüksekliğe bağlı yerçekimi ivmesi, $R_u$ evrensel gaz sabitidir. Sıcaklığın yüksek irtifalarda asimptotik olarak ekzosferik sıcaklığa ($T_{\infty}$) yakınsadığı Bates profili kullanılır:
$$T(z) = T_{\infty} - (T_{\infty} - T_0) \exp[-s(z - z_0)]$$
*Burada $s$ sıcaklık gradyan katsayısı, $T_0$ referans yüksekliği $z_0$ üzerindeki sıcaklıktır.*

#### Haftalar 3-4: Knudsen Sayısı ve Seyreltilmiş Akış Rejimleri
Sürekli ortam (continuum) kabullerinin çöktüğü VLEO bölgesinde, akış karakteristiği gaz moleküllerinin ortalama serbest yolu ($\lambda$) ile uzay aracının karakteristik boyutu ($L$) arasındaki oran olan **Knudsen Sayısı ($Kn$)** ile belirlenir.

Ortalama serbest yol formülü:
$$\lambda = \frac{k_B T}{\sqrt{2} \pi d^2 P}$$
Burada $k_B$ Boltzmann sabiti ($1.3806 \times 10^{-23} \text{ J/K}$), $T$ mutlak sıcaklık ($K$), $d$ gaz moleküllerinin kinetik çapı ($m$), $P$ ise lokal basınçtır ($Pa$).

Akış rejimleri Knudsen sayısına göre dört ana sınıfa ayrılır:
1.  **Sürekli Akış Rejimi ($Kn < 0.01$):** Navier-Stokes denklemleri geçerlidir. Yüzeyde kaymasızlık (no-slip) sınır şartı uygulanır.
2.  **Kayma Akış Rejimi ($0.01 < Kn < 0.1$):** Navier-Stokes denklemleri, yüzeyde hız kayması (velocity slip) ve sıcaklık sıçraması (temperature jump) düzeltme sınır şartları ile uygulanabilir.
3.  **Geçiş Akış Rejimi ($0.1 < Kn < 10$):** Moleküler çarpışmalar ile molekül-yüzey çarpışmaları benzer mertebededir. Navier-Stokes geçerliliğini yitirir; Boltzmann Taşıma Denklemi veya DSMC (Direct Simulation Monte Carlo) sayısal yöntemleri gereklidir.
4.  **Serbest Moleküler Akış Rejimi ($Kn > 10$):** Moleküller arası çarpışmalar tamamen ihmal edilebilir. Akış fiziği sadece moleküllerin yüzeye çarpma ve yansıma dinamiklerine dayanır.

---

### 🟩 Kısım II: VLEO Çevre Etkileri ve Aerodinamik Sürüklenme

#### Haftalar 5-6: Serbest Moleküler Akışta Aerodinamik Sürüklenme Modellemesi
VLEO'daki uzay araçları için sürüklenme katsayısı ($C_d$) sabit bir $2.0$ veya $2.2$ değeri değildir. Yüzey malzemesinin atomik pürüzlülüğü, yüzey sıcaklığı ($T_w$), gelen gazın sıcaklığı ($T_i$) ve moleküler hız oranı ($s$) ile sürekli değişir.

Yüzeye çarpan moleküllerin momentum transferi iki uç mekanizma ile açıklanır:
*   **Specular (Aynasal) Yansıma:** Molekül, yüzey normaline göre geliş açısıyla aynı açıda, enerjisini kaybetmeden yansır.
*   **Diffuse (Dağınık) Yansıma:** Yüzeyde adsorbe olan molekül, yüzeyle termal dengeye ulaştıktan sonra Lambert kosinüs yasasına uygun olarak rastgele yönlerde yansır.

Bu iki mekanizma Maxwell momentum uyum katsayıları ($\sigma_n, \sigma_t$) ile birleştirilir. Gelen ve yansıyan moleküllerin kinetik teorisine dayanan Schaaf ve Chambre analitik çözümüyle durma noktası sürüklenme katsayısı şu şekilde hesaplanır:
$$C_d = \frac{2 - \sigma_n}{\sqrt{\pi} s} \exp(-s^2 \cos^2\theta) + \left[ (2 - \sigma_n) \left( 1 + \frac{1}{2s^2} \right) + \sigma_n \frac{\sqrt{\pi}}{2s} \sqrt{\frac{T_w}{T_i}} \right] \text{erf}(s \cos\theta) + \frac{\sigma_t \cos\theta}{s} \left[ \frac{\sqrt{\pi}}{2} \sqrt{\frac{T_w}{T_i}} - s \cos\theta \text{erf}(s \cos\theta) \right]$$
Burada $s = V / \sqrt{2 R_g T_i}$ moleküler hız oranı, $R_g$ spesifik gaz sabiti, $\theta$ yüzey normali ile geliş doğrultusu arasındaki açıdır.

#### Haftalar 7-8: Atomik Oksijen (ATOX) Reaksiyonları ve Malzeme Bozunması
Termosferde Güneş'in sert UV fotonları çift atomlu oksijen bağlarını ($5.12 \text{ eV}$) parçalayarak son derece reaktif **Atomik Oksijen (ATOX)** radikalleri üretir:
$$O_2 + h\nu \rightarrow O(^3P) + O(^3P)$$

$200-450 \text{ km}$ irtifada uydunun yörünge hızı ($\sim 7.8 \text{ km/s}$) nedeniyle, ATOX atomları uydu yüzeylerine yaklaşık **$5 \text{ eV}$** kinetik çarpma enerjisiyle çarpar. Bu durum polimerik zincirleri koparır ve metalleri oksitleyerek ciddi kütle kayıplarına yol açar.

Aşınma ve kütle kaybı modeli:
$$\Delta m = E_y \cdot \Phi_{\text{ATOX}} \cdot A \cdot t \cdot \rho_{\text{malzeme}}$$
Burada $E_y$ aşınma verimi ($cm^3/\text{atom}$), $\Phi_{\text{ATOX}}$ birikimli ATOX akısı ($\text{atoms/cm}^2\cdot\text{s}$), $A$ maruz kalan alan ($cm^2$), $t$ süre ($s$), $\rho_{\text{malzeme}}$ ise malzeme yoğunluğudur ($g/cm^3$).

| Malzeme | Aşınma Verimi ($E_y \times 10^{-24} \text{ cm}^3/\text{atom}$) | Bozunma Karakteristiği |
| :--- | :--- | :--- |
| **Kapton (Poliimid)** | $3.0$ | Yüksek yüzey erozyonu, optik özellik kaybı |
| **Gümüş (Ag)** | $10.5$ | Hızlı oksitlenme, elektriksel iletkenlik kaybı |
| **Teflon (FEP)** | $0.3$ | Orta seviye dayanım, flor kaybı |
| **Karbon Fiber** | $2.1$ | Matris erozyonu, mekanik zayıflama |
| **Silicon Dioxide ($SiO_2$)** | $< 0.001$ | Tamamen kararlı (koruyucu kaplama olarak kullanılır) |

---

### 🟨 Kısım III: İtki ve Yörünge Kontrol Algoritmaları

#### Haftalar 9-10: RAM-EP (Air-Breathing Electric Propulsion) İtki Sistemleri
Geleneksel itki sistemlerinde uydu ömrünü taşıdığı xenon yakıt miktarı belirler. **RAM-EP (Atmosferik Elektrikli İtki)** sistemi, VLEO'daki seyreltilmiş havayı toplayarak yakıt olarak kullanır ve teorik olarak sınırsız yörünge ömrü sağlar.

Sistem üç ana bileşenden oluşur:
1.  **Aerodinamik Hava Alığı (Intake):** Gelen serbest moleküler akışı sıkıştırmak üzere tasarlanmış, aynasal yansımayı optimize eden geometri. Yakalama verimi:
    $$\eta_c = \frac{\dot{m}_{\text{toplanan}}}{\dot{m}_{\text{gelen}}}$$
2.  **Helikon Plazma Kaynağı:** Düşük basınçlı gazı iyonize etmek için radyo frekansı (RF) dalgaları ve manyetik alan kullanan yüksek verimli iyonizasyon hücresi.
3.  **Elektrostatik Hızlandırıcı (Gridded Ion Thruster):** İyonize azot ($N^+$) ve oksijen ($O^+$) iyonlarını yüksek voltajlı gridler arasından geçirerek yüksek özgül itkiyle ($I_{sp} > 3000 \text{ s}$) dışarı püskürten sistem.

#### Haftalar 11-12: Sürekli Düşük İtki ile Lyapunov Kontrolcü Tasarımı
Atmosferik sürüklenme altındaki yarı-büyük eksen ($a$) bozunmasını dengelemek için sürekli çalışan düşük itkili motorların kontrolünde Lyapunov kararlılık teorisi uygulanır.
Lyapunov fonksiyonu ($V_L$) yörünge enerjisinin hedef enerji düzeyinden sapması olarak tanımlanır:
$$V_L = \frac{1}{2} (a - a_{\text{hedef}})^2$$
Bu fonksiyonun zamana göre türevinin negatif tanımlı olması kararlılığı garanti eder:
$$\dot{V_L} = (a - a_{\text{hedef}}) \dot{a} = (a - a_{\text{hedef}}) \left[ \frac{2a^2 v}{\mu} (f_{\text{itki}} - f_{\text{sürüklenme}}) \right] < 0$$
Buradan elde edilen kontrol kanunu, itki kuvvetini anlık sürüklenme kuvvetine ve hedef irtifadan olan sapmaya bağlı olarak modüle eder:
$$f_{\text{itki}} = f_{\text{sürüklenme}} - K_{\text{kazanç}} \cdot (a - a_{\text{hedef}})$$

#### Haftalar 13-14: Yüksek Hızlı VLEO Haberleşmesi ve Doppler Yönetimi
Alçak yörüngede çizgisel hızın ($\sim 7.8 \text{ km/s}$) yüksek olması, yer istasyonları ile kurulan haberleşme pencerelerini **$5-7 \text{ dakika}$** gibi çok dar sürelerle sınırlandırır. Ayrıca taşıyıcı frekansta ciddi Doppler kaymaları oluşur.
Doppler kayması formülü:
$$f_{\text{alınan}}(t) = f_{\text{verilen}} \left( 1 - \frac{\vec{v}(t) \cdot \vec{r}(t)}{c \cdot ||\vec{r}(t)||} \right)$$
Burada $\vec{v}$ uydu hız vektörü, $\vec{r}$ uydudan yer istasyonuna uzanan konum vektörü, $c$ ışık hızıdır. Sistemler, frekans kaymasını gerçek zamanlı kompanse eden sayısal PLL (Phase-Locked Loop) mimarileriyle tasarlanır.

---

## 🔬 Laboratuvar Uygulamaları ve Ödevler

### Laboratuvar: Yüksek Sadakatli VLEO Yörünge Bozunması Simülasyonu
*   **Amaç:** `scripts/vleo_drag_calculator.py` betiğini genişleterek, uydunun zaman serisi boyunca irtifa kaybını Runge-Kutta 4. Derece (RK4) entegrasyon yöntemiyle çözmek.
*   **Girdiler:** $m = 150 \text{ kg}$, $A = 0.6 \text{ m}^2$, başlangıç irtifası $z_0 = 250 \text{ km}$, $C_d(t)$ Schaaf-Chambre modeli.
*   **Rapor Beklentisi:** İrtifa, sürüklenme kuvveti ve kalan yörünge ömrünün (days to decay) zaman grafiklerinin çıkarılması.

---

## 📚 Önerilen Akademik Kaynaklar
1.  **Bird, G. A. (1994).** *Molecular Gas Dynamics and the Direct Simulation of Gas Flows*. Oxford University Press. (DSMC simülasyonları için temel eser).
2.  **Shen, C. (2005).** *Rarefied Gas Dynamics: Fundamentals and Applications*. Springer.
3.  **AIAA S-111A-2019.** *Standard: Space Plug-and-Play Architecture*.
4.  **NASA/SP-2020-5002.** *NASA Systems Engineering Handbook*.
