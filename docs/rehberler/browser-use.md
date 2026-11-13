---
arac: Browser Use
repo: browser-use/browser-use
kategori: Tarayıcı otomasyonu
platformlar: [macOS, Linux, Windows]
zorluk: Orta
son_dogrulama: 2026-11-13
---

# Browser Use kurulumu

Browser Use, bir yapay zekâ modeline tarayıcıyı kullandıran açık kaynak bir Python kütüphanesidir. Görevi düz cümleyle yazarsın; ajan sayfaları açar, tıklar, okur ve sonucu sana döndürür.

!!! info "Doğrulama notu"
    Bu rehberdeki komutlar 13 Kasım 2026'da aracın resmî README dosyasından alındı. Komutlar her platformda ayrıca denenmedi; bir adım sende çalışmazsa [hata bildir](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues/new/choose).

## Bu araç ne işe yarar?

Klasik tarayıcı otomasyonunda her tıklamayı kodla tarif edersin ve site değişince kod bozulur. Browser Use'da adımları değil hedefi yazarsın: "şu deponun yıldız sayısını bul" gibi. Hangi düğmeye basılacağına model karar verir.

Kütüphane iki şeye ihtiyaç duyar: tarayıcıyı süren Python kodu ve kararları veren bir dil modeli. Modeli sen seçersin; resmî örnek OpenAI ile verilir, bu yüzden bir API anahtarı gerekir.

[agent-browser](agent-browser.md) rehberindeki araçtan farkı şudur: agent-browser bir ajanın kullandığı komut satırı aracıdır, Browser Use ise ajanın kendisini Python içinde kurmanı sağlar.

## Ön koşullar

- **Python 3.11 ya da üstü.**
- **uv.** Resmî belgenin önerdiği paket yöneticisi. Kurulu değilse:

    === "macOS ve Linux"

        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```

    === "Windows"

        ```powershell
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        ```

- **Bir model API anahtarı.** Hızlı başlangıç örneği için OpenAI API anahtarı. Bu anahtarın kullanımı ücretlidir; ajan her adımda modele istek gönderir.

## Kurulum

Bu adımlar bütün işletim sistemlerinde aynıdır. Önce proje için boş bir klasör aç ve içine gir:

```bash
mkdir tarayici-ajani
cd tarayici-ajani
```

Projeyi başlat ve kütüphaneyi ekle:

```bash
uv init --python 3.12
uv add browser-use
```

İlk komut klasörü bir Python projesine çevirir, ikincisi Browser Use'u kurar.

Sonra aynı klasörde `.env` adında bir dosya oluştur ve API anahtarını içine yaz:

```text
OPENAI_API_KEY=anahtarin
```

`.env` dosyasını kimseyle paylaşma ve Git'e ekleme.

## İlk kullanım

Klasörde `agent.py` adında bir dosya oluştur ve şunu yapıştır:

```python
import asyncio

from browser_use import Agent, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


async def main():
    llm = ChatOpenAI(model="gpt-5.6-luna")
    agent = Agent(
        task="browser-use deposunun yıldız sayısını bul",
        llm=llm,
    )
    gecmis = await agent.run()
    print(gecmis.final_result())


if __name__ == "__main__":
    asyncio.run(main())
```

Model adı resmî örnekten alındı; hesabında erişimin olan başka bir modeli de yazabilirsin.

Çalıştır:

```bash
uv run agent.py
```

Bir tarayıcı penceresi açılır, ajan depoyu arayıp bulur ve sonucu terminale yazar. `task` satırını değiştirerek başka görevler deneyebilirsin.

## Sık karşılaşılan sorunlar

### API anahtarı hatası (401 ya da "api key" içeren mesaj)

`.env` dosyası `agent.py` ile aynı klasörde olmalı ve satır `OPENAI_API_KEY=` ile başlamalı. Anahtarın başında ya da sonunda boşluk, tırnak bırakma.

### Model bulunamadı hatası

Koddaki model adına hesabının erişimi yok. Sağlayıcının model listesinden erişebildiğin bir modeli yaz.

### `uv: command not found`

uv kurulumundan sonra terminali kapatıp yeniden aç.

### Windows'ta Claude araç seti bütünleşmesi çalışmıyor

Resmî belgeye göre bu bütünleşme `/bin/bash` bulunan Linux ya da macOS ister. Windows'ta WSL içinde çalıştır. Bu rehberdeki temel kullanım için WSL gerekmez.

### Ajan çok adım atıyor, maliyet artıyor

Görevi dar ve net yaz. "Şu sayfadaki fiyatı oku" gibi tek hedefli görevler hem daha hızlı biter hem daha az istek harcar.

## Kaynaklar

- [Resmî depo](https://github.com/browser-use/browser-use)
- [Kütüphane belgeleri](https://docs.browser-use.com/open-source/introduction)
- [uv kurulum belgeleri](https://docs.astral.sh/uv/getting-started/installation/)
- Lisans: MIT
