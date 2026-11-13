---
arac: Open WebUI
repo: open-webui/open-webui
kategori: Yerel yapay zekâ
platformlar: [macOS, Linux, Windows]
zorluk: Başlangıç
son_dogrulama: 2026-11-13
---

# Open WebUI kurulumu

Open WebUI, kendi bilgisayarında çalışan bir yapay zekâ sohbet arayüzüdür. Tarayıcıda açılır, görünüşü bildiğin sohbet uygulamalarına benzer, ama modeller ve konuşmaların senin makinende kalır.

!!! info "Doğrulama notu"
    Bu rehberdeki komutlar 13 Kasım 2026'da aracın resmî README dosyasından alındı. Komutlar her platformda ayrıca denenmedi; bir adım sende çalışmazsa [hata bildir](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues/new/choose).

## Bu araç ne işe yarar?

Open WebUI tek başına bir model değildir; modellere bağlanan bir arayüzdür. İki tür kaynağa bağlanabilir:

- **Ollama:** Modelleri kendi bilgisayarında çalıştıran ücretsiz bir araç. İnternet olmadan da çalışır.
- **OpenAI uyumlu servisler:** API anahtarıyla eriştiğin bulut modelleri.

Örnek: Öğrenci verisi ya da şirket belgesi gibi dışarı çıkmaması gereken metinlerle çalışırken yerel bir modelle sohbet etmek.

## Ön koşullar

İki kurulum yolu var; birini seç.

- **Docker yolu (önerilen).** Bilgisayarında Docker Desktop kurulu ve çalışıyor olmalı. Kontrol et:

    ```bash
    docker --version
    ```

- **pip yolu.** Python 3.12 gerekir; resmî belge uyumluluk sorunlarından kaçınmak için bu sürümü öneriyor.

    ```bash
    python3 --version
    ```

- **Bir model kaynağı.** Yerel model kullanacaksan [Ollama](https://ollama.com) kurulu olmalı, ya da aşağıdaki "Ollama dahil" seçeneğini kullan.

## Kurulum

=== "Docker (Ollama bilgisayarda kurulu)"

    ```bash
    docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
    ```

=== "Docker (Ollama dahil)"

    Ollama'yı ayrıca kurmak istemiyorsan ikisini tek kapta çalıştır:

    ```bash
    docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
    ```

    Nvidia ekran kartın varsa komuta `--gpus=all` ekle.

=== "Docker (yalnızca OpenAI API)"

    ```bash
    docker run -d -p 3000:8080 -e OPENAI_API_KEY=anahtarin -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
    ```

    `anahtarin` yerine kendi API anahtarını yaz.

=== "pip"

    ```bash
    pip install open-webui
    open-webui serve
    ```

Komutlar macOS, Linux ve Windows'ta aynıdır. Windows'ta PowerShell kullan.

Komuttaki `-v open-webui:/app/backend/data` bölümünü silme. Bu bölüm konuşmalarını ve ayarlarını kalıcı bir alanda tutar; o olmadan kap silindiğinde veriler de gider.

## İlk kullanım

Tarayıcıda şu adresi aç:

- Docker ile kurduysan: `http://localhost:3000`
- pip ile kurduysan: `http://localhost:8080`

Sayfa açılıyorsa kurulum tamamdır. İlk açılışta bir hesap oluşturman istenir; bu hesap yalnızca senin bilgisayarındaki kurulum içindir.

Docker kabının çalışıp çalışmadığını görmek için:

```bash
docker ps
```

Listede `open-webui` adını görmelisin. Durdurmak ve yeniden başlatmak için:

```bash
docker stop open-webui
docker start open-webui
```

## Sık karşılaşılan sorunlar

### Arayüz açılıyor ama model listesi boş, Ollama'ya bağlanamıyor

Kap, bilgisayarındaki Ollama'ya ulaşamıyor. Kabı silip ağ ayarını değiştirerek yeniden başlat:

```bash
docker rm -f open-webui
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Bu kurulumda adres `http://localhost:8080` olur.

### `localhost:3000` açılmıyor

Kap ilk açılışta hazır olana kadar bir süre bekle, sonra `docker ps` ile çalıştığını kontrol et. Çalışmıyorsa `docker logs open-webui` hatayı gösterir.

### İnternetsiz ortamda açılışta takılıyor

Araç açılışta model dosyası indirmeye çalışır. Bunu kapatmak için ortam değişkenini ayarla:

```bash
export HF_HUB_OFFLINE=1
```

### pip kurulumu hata veriyor

Python sürümünü kontrol et. 3.12 dışındaki sürümlerde uyumsuzluk çıkabiliyor; Docker yolu bu sorunu tamamen ortadan kaldırır.

## Kaynaklar

- [Resmî depo](https://github.com/open-webui/open-webui)
- [Resmî belgeler](https://docs.openwebui.com/)
- [Güncelleme rehberi](https://docs.openwebui.com/getting-started/updating)
- Lisans: Open WebUI License (markanın korunmasını şart koşar; ayrıntı depodaki LICENSE dosyasında)
