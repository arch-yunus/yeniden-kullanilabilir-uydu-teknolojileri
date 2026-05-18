# 🛰️ UYDU-102: Yeniden Kullanılabilir Uydu Platform Tasarımı

Bu ders, havacılık ve uzay endüstrisindeki geleneksel "fırlat ve unut" modelinden, sürdürülebilir "yörüngede servis edilebilir, modüler, yükseltilebilir ve dünyaya geri döndürülebilir" yeni nesil platform modeline geçişin yapısal, aviyonik, malzeme ve kontrol mühendisliği esaslarını inceler.

---

## 📊 Ders Detayları ve Kredi Bilgileri
*   **Ders Kodu:** UYDU-102
*   **Dönem:** Güz (1. Dönem)
*   **Kredi Yapısı:** 3 Saat Teori + 2 Saat Uygulama
*   **AKTS (ECTS):** 7.5
*   **Ön Koşullar:** Isı Transferi, Kontrol Sistemleri, Yapısal Mekanik, Malzeme Bilimi

---

## 📅 Haftalık Ayrıntılı Ders Planı

### 🟦 Kısım I: Modüler Uzay Aracı Mimarileri ve Standartları

#### Haftalar 1-2: Space Plug-and-Play Architecture (SPA) ve xTEDS Aviyonik Veri Yapıları
Aviyonik entegrasyon sürelerini dramatik şekilde düşüren **SPA (Space Plug-and-Play Architecture)** standartları (AIAA S-111 ve devamı), uydudaki her alt bileşenin kendini uçuş bilgisayarına tanıtmasını sağlayan **xTEDS (eXtensible Transducer Electronic Data Sheet)** XML şemalarına dayanır.

Aşağıda, modüler bir Güneş Sensörünün (Sun Sensor) sisteme tanıtılması için hazırlanan örnek bir **xTEDS XML** kod yapısı verilmiştir:
```xml
<?xml version="1.0" encoding="utf-8"?>
<xTEDS xmlns="http://www.aiaa.org/standards/spa" name="CSS_Modular_Sensor" uuid="f81d4fae-7dec-11d0-a765-00a0c91e6bf6">
  <DeviceDescription>
    <Manufacturer>Reusat Aviyonik A.Ş.</Manufacturer>
    <Model>CSS-V2-Modular</Model>
    <DeviceType>SunSensor</DeviceType>
  </DeviceDescription>
  <Interface name="TelemetryInterface" type="DataQuery">
    <Command name="GetSunVector">
      <Output name="SunVector" type="float" length="3" unit="dimensionless"/>
      <Output name="Confidence" type="float" range="0.0,1.0"/>
    </Command>
    <DataStream name="ContinuousAngle" rate="10Hz">
      <Variable name="AngleX" type="float" unit="degrees"/>
      <Variable name="AngleY" type="float" unit="degrees"/>
    </DataStream>
  </Interface>
</xTEDS>
```
Bu sayede, uçuş yazılımı (Flight Software) kaynak kod derlemesine ihtiyaç duymadan, yeni takılan modülün fonksiyonlarını ve veri arayüzlerini dinamik olarak tanımlar ve veri yollarını (SpaceWire, I2C veya USB) otomatik olarak konfigüre eder.

#### Haftalar 3-4: Mekanik, Elektriksel ve Akışkan Transfer Standart Arayüzleri
Yörüngede otonom robotik kollarla parça değiştirebilmek için arayüz tasarımlarının standartlaştırılması şarttır.
*   **Mekanik Arayüzler:** Robotik manipülatörlerin uyduyu stabil yakalayabilmesi için **FRGF (Flight Releasable Grapple Fixture)** ve veri/güç aktarımlı **PDGF (Payload Data Grapple Fixture)** mimarileri. Modüllerin kayma eksenlerinde $\pm 5 \text{ mm}$ hizalama hatalarını tolere edebilen kılavuz ray (guide rail) ve konik yuvalı kenetleyiciler.
*   **Elektriksel ve Veri Konektörleri:** Uzay vakumunda metallerin birbiriyle moleküler olarak kaynaşmasını (Cold Welding) önlemek amacıyla nitrürlenmiş ve altın kaplamalı, yay baskılı "pogo-pin" veya temassız endüktif güç aktarım arayüzleri.
*   **Akışkan Arayüzleri:** Kimyasal yakıt (Hidrazin) veya elektrikli itki yakıtı (sıvı/süperkritik Xenon) ikmali için sıfır-sızıntılı (zero-leakage), çift kilitlemeli **Quick Disconnect (QD - Hızlı Ayrılabilir)** valf mekanizmaları.

---

### 🟩 Kısım II: Atmosfere Geri Dönüş Fiziği ve Isıl Koruma Tasarımı

#### Haftalar 5-6: Atmosfere Giriş Dinamiği ve Balistik Katsayısı
Uzay aracının atmosferik re-entry (geri dönüş) sırasında maruz kaldığı pik yavaşlama ve pik ısı akısı, aracın **Balistik Katsayısı ($B_c$)** ile belirlenir:
$$B_c = \frac{m}{C_d A}$$
Burada $m$ araç kütlesi ($kg$), $C_d$ sürüklenme katsayısı, $A$ ise referans kesit alanıdır ($m^2$). Düşük balistik katsayılı (örneğin şişirilebilir aerodinamik yavaşlatıcılar - IRDT) araçlar atmosferin daha ince üst tabakalarında yavaşlayarak pik ısı yüklerini düşürürler.

#### Haftalar 7-8: Sutton-Graves Isı Akısı Modellemesi
Durma noktasındaki (stagnation point) konvektif ısı transfer oranı, hipersonik şok dalgalarının arkasındaki gaz iyonizasyonu ve termal uyarılmalar çerçevesinde **Sutton-Graves** denklemiyle hesaplanır:
$$q_s = k \sqrt{\frac{\rho}{R_n}} V^3$$
Burada $q_s$ durma noktası ısı akısı ($W/m^2$), $\rho$ serbest akış yoğunluğu ($kg/m^3$), $R_n$ burun eğrilik yarıçapı ($m$), $V$ ise hipersonik giriş hızıdır ($m/s$).

Sutton-Graves gezegensel katsayısı ($k$), gezegen atmosferinin kimyasal kompozisyonuna göre değişir:

| Gezegen | Atmosfer Kompozisyonu | $k$ Katsayısı ($\text{kg}^{0.5}/\text{m}$) |
| :--- | :--- | :--- |
| **Dünya** | $\%78 N_2, \%21 O_2$ | $1.7415 \times 10^{-4}$ |
| **Mars** | $\%95.3 CO_2, \%2.7 N_2$ | $1.8900 \times 10^{-4}$ |
| **Venüs** | $\%96.5 CO_2, \%3.5 N_2$ | $1.9100 \times 10^{-4}$ |

#### Haftalar 9-10: Termal Koruma Sistemleri (TPS) Karşılaştırma Matrisi
Re-entry aracının yapısal gövdesini $1500^\circ\text{C}$'yi aşan sıcaklıklardan korumak için üç temel malzeme grubu kullanılır:

| Malzeme Sınıfı | Örnek Sistemler | Sıcaklık Limiti ($^\circ\text{C}$) | Mekanik / Fiziksel Süreç | Yeniden Kullanılabilirlik |
| :--- | :--- | :--- | :--- | :--- |
| **Ablatif (Aşınmalı)** | PICA-X, Avcoat, Phenolic | $> 2500$ | Isıyı absorbe ederek erime, süblimleşme, piroliz gazı salınımı ve karbonlaşma. | **Hayır** (Her uçuştan sonra tamamen değiştirilmelidir) |
| **Yalıtımlı Seramik Karolar** | HRSI, LI-900 (Silika) | $\sim 1260 - 1500$ | Çok düşük ısıl iletkenlik ($< 0.06 \text{ W/mK}$) sayesinde ısıyı bünyesinde bloke etme. | **Evet** (Hasar görmedikçe binlerce döngü dayanır) |
| **Ultra-Yüksek Sıcaklık Seramikleri** | RCC (Karbon-Karbon), $ZrB_2, HfB_2$ | $> 1650$ | Yüksek ısıl iletkenlikle ısıyı geniş alana yayarak ışıma (radyasyon) ile geri gönderme. | **Evet** (Burun ve kanat hücum kenarlarında kullanılır) |

---

### 🟨 Kısım III: Kontrollü Dikey İniş ve Yenileme (Refurbishment)

#### Haftalar 11-12: İtki Yönlendirme (TVC) ve G-fold Konveks Optimizasyon Algoritması
Dikey iniş manevrasının yakıt-optimal olarak ve sıfır hata ile gerçekleştirilmesi için doğrusal olmayan itki ve hareket denklemleri **G-fold** algoritması ile konveksleştirilerek gerçek zamanlı çözülür:

Uçuş bilgisayarında anlık çözülen konveks optimizasyon problemi formulasyonu:
$$\min_{\boldsymbol{u}(t), t_f} \int_{0}^{t_f} \eta(t) dt$$
Sınır şartları altında (Subject to):
1.  **Dinamik Hareket Denklemi:** $\ddot{\boldsymbol{r}}(t) = \boldsymbol{g} + \frac{\boldsymbol{u}(t)}{m(t)}$
2.  **İtki Yönlendirme Sınırı (Gimbal):** $\boldsymbol{u}(t) \cdot \hat{\boldsymbol{n}}_{\text{motor}} \ge ||\boldsymbol{u}(t)|| \cos\theta_{\max}$
3.  **Minimum ve Maksimum İtki Limitleri:** $0 < U_{\min} \le ||\boldsymbol{u}(t)|| \le U_{\max}$
4.  **Zemin Temas Koşulu (Touchdown):** $\boldsymbol{r}(t_f) = \mathbf{0}, \quad \dot{\boldsymbol{r}}(t_f) = \boldsymbol{v}_{\text{hedef}}$
*Burada $\boldsymbol{u}(t)$ itki vektörü, $\theta_{\max}$ maksimum gimbal açısı, $t_f$ ise iniş süresidir.*

#### Haftalar 13-14: Malzeme Yorgunluğu ve Yeniden Sertifikasyon Protokolleri
Uzaydan geri dönen platformların yeniden uçuşa hazırlanması sürecinde yapısal ve aviyonik yorgunluklar analiz edilir.
*   **Hasarsız Muayene (NDT):** Ultrasonik tarama, girdap akımları (Eddy Current) testi ve X-ışını tomografisi ile mikroskobik çatlak tespiti.
*   **Sertifikasyon:** Termal vakum odası (TVAC) döngü testleri ve titreşim (vibration shaker) tablaları ile yapısal rezonans doğrulaması.

---

## 📐 Tasarım Projesi ve Uygulama

### Proje Görevi: Sutton-Graves Isı Akısı ve 1D Isı İletim Entegrasyonu
*   **Görev:** Öğrenciler, `scripts/reentry_thermal_analysis.py` betiğini kullanarak hipersonik bir re-entry kapsülünün durma noktası ısı akısı profilini ($q_s(t)$) çıkaracaktır. Bu ısı akısını üst sınır şartı olarak kabul ederek, $10 \text{ cm}$ kalınlığındaki bir HRSI silika karosunun arkasındaki alüminyum uydu gövdesine iletilen sıcaklığı 1-Boyutlu Zamana Bağlı Isı İletim Denklemi ile sayısal (Sonlu Farklar Yöntemi - Crank-Nicolson veya FTCS) olarak çözeceklerdir:
    $$\rho C_p \frac{\partial T}{\partial t} = K_{\text{iletkenlik}} \frac{\partial^2 T}{\partial x^2}$$

---

## 📚 Önerilen Akademik Kaynaklar
1.  **Anderson, J. D. (2006).** *Hypersonic and High-Temperature Gas Dynamics*. AIAA Education Series.
2.  **Acikmese, B., & Blackmore, L. (2007).** *Convex programming approach to powered descent guidance for mars landing*. Journal of Guidance, Control, and Dynamics, 30(5), 1353-1366.
3.  **ISO 19683:2017.** *Space systems — Design qualification and acceptance tests of small spacecraft and units*.
