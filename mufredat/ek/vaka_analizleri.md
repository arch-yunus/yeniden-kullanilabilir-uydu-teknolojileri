# 📂 OSAM Vaka Analizleri (Case Studies)

Bu bölüm, yörüngede otonom servis, bakım, yakıt ikmali ve montaj (OSAM) teknolojilerinin gerçek dünyadaki uygulamalarını, mühendislik detaylarını ve bu görevlerden elde edilen kritik kazanımları inceler.

---

## 1. Northrop Grumman MEV-1 & MEV-2 (Mission Extension Vehicle)

*   **Görev Hedefi:** GEO (Yer eşzamanlı yörünge) üzerindeki ticari haberleşme uydularına kenetlenerek, onların yörünge ve yönelim kontrolünü (attitude & orbit control) üstlenmek ve ömürlerini 5 yıl uzatmak.
*   **MEV-1 Operasyonu (Şubat 2020):** MEV-1, yakıtı tükenmek üzere olan **Intelsat 901** uydusu ile GEO mezarlık yörüngesinde buluştu ve başarıyla kenetlendi.
*   **MEV-2 Operasyonu (Nisan 2021):** MEV-2, aktif olarak çalışan ve hizmet vermeye devam eden **Intelsat 10-02** uydusuna doğrudan operasyonel GEO konumunda kenetlendi.
*   **Mühendislik ve Kenetlenme Mekanizması:**
    *   **Hazırlıksız Kenetlenme:** Intelsat uyduları üzerinde özel bir kenetlenme portu bulunmuyordu. MEV, uydunun arkasındaki sıvı yakıtlı motorun sıvı fırlatma nozülüne (Apogee Kick Motor - AKM) yerleşen özel bir mekanik sonda (probe) ve ardından uydunun halkasını kavrayan kilit mekanizması tasarladı.
    *   **RPO Yaklaşması:** Son yaklaşmada LiDAR ve termal kameralar kullanılarak bağıntılı pozisyon $\text{cm}$ hassasiyetinde tutuldu.

---

## 2. ClearSpace-1 (Avrupa Uzay Ajansı - ESA)

*   **Görev Hedefi:** Alçak Dünya Yörüngesi'ndeki (LEO) kontrolsüz ve dönen büyük bir uzay çöpünü yakalayarak kontrollü bir şekilde atmosfere sokup yok etmek.
*   **Hedef Nesne:** 2013 yılında fırlatılan Vega roketine ait yaklaşık $112 \text{ kg}$ kütleli **VESPA** (Vega Secondary Payload Adapter) üst aşama adaptörü.
*   **Mühendislik Zorlukları ve Yaklaşım:**
    *   **Tumbling (Kontrolsüz Dönüş):** Vespa adaptörü herhangi bir aktif yönelim kontrolüne sahip değildir ve kendi ekseni etrafında düzensiz dönmektedir.
    *   **Robotik Yakalama:** Chaser araç, hedefle kendi dönüş hızını senkronize ettikten sonra, 4 adet otonom kontrollü robotik kol yardımıyla Vespa'yı çevreleyerek kavrayacaktır.
    *   **Kazanım:** Kontrolsüz hedeflerin çoklu robot kollarla kavranması sırasında oluşan darbe sönümleme ve açısal momentum aktarımı dinamiklerinin doğrulanması.

---

## 3. NASA OSAM-1 (Eski Adıyla Restore-L)

*   **Görev Hedefi:** Yörüngede yakıt ikmali yapmak üzere tasarlanmamış olan **Landsat 7** uydusuna yakıt (sıvı hidrazin) doldurmak ve uzayda otonom modüler montaj (SPIDER anten projesi) gerçekleştirmek.
*   **Geliştirilen Kritik Teknolojiler:**
    *   **RRT (Robotic Refueling Tool):** Landsat 7'nin yakıt valfi koruyucu termal örtülerini (MLI) kesmek, emniyet tellerini robotik olarak sökmek, valfi açmak, hidrazin transfer etmek ve valfi sıfır sızıntıyla yeniden kapatıp mühürlemek için tasarlanan çok uçlu robotik alet başlığı.
    *   **Otonom Navigasyon:** Coğrafi olarak yeryüzünden kontrol edilemeyen, tamamen yapay zeka ve bilgisayarlı görüyle yönetilen otonom RPO sistemi.
*   **Tarihsel Not:** Proje, artan bütçe ve teknik takvim aşımı nedeniyle 2024 yılında NASA tarafından resmi olarak durdurulmuş olsa da, geliştirilen RRT ve bilgisayarlı görü teknolojileri gelecekteki uzay robotiği projelerine temel oluşturmuştur.

---

## 4. DARPA RSGS (Robotic Servicing of Geosynchronous Satellites)

*   **Görev Hedefi:** GEO yörüngesindeki askeri ve sivil uyduların robotik kollarla muayene edilmesi, mekanik arızalarının giderilmesi (örneğin sıkışmış güneş paneli veya antenlerin açılması) ve modüler bileşen yükseltmeleri yapılması.
*   **Teknik Mimari:**
    *   **Çift Robotik Kol:** İki adet yüksek serbestlik dereceli (multi-DOF), uzay ortamına uygun korumalı robotik manipülatör.
    *   **Uç Elemanı Deposu:** Robot kollarının yörüngede görev tipine göre (kesme, tutma, vidalama, lehimleme) uç başlıklarını otonom değiştirebilmesini sağlayan takım değiştirici depo.

---

## 🧐 Derinlemesine Analiz ve Vaka Çalışması Soruları

1.  **Soru:** MEV-1 görevi sırasında, hedef uydu üzerinde özel bir kenetlenme portu olmamasına rağmen, Apogee Kick Motor (AKM) nozülünün içine sonda yerleştirilerek yapılan mekanik kenetlenme sırasında servis uydusunun iticileri ve hedef uydunun yapısal bütünlüğü açısından ne tür riskler yönetilmiştir?
2.  **Soru:** OSAM-1 projesindeki "Robotik Yakıt İkmal Aleti" (RRT) tasarımının, yörüngede sıvı hidrazin ($N_2H_4$) transferi sırasında uzay vakumunda yaşanabilecek sıvı buharlaşması ve sızıntı risklerini engellemek için kullandığı contalama ve sızdırmazlık mimarisini açıklayınız.
3.  **Soru:** ClearSpace-1 görevi kapsamında, kendi ekseninde saniyede birkaç derece dönen ($Tumbling$) bir uzay çöpünü kavrayacak olan robotik kolların eklemlerinde empedans kontrolü ($Impedance\ Control$) yapılmasının mekanik çarpışma kuvvetlerini sönümlemedeki rolü nedir?
