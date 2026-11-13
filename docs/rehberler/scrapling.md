---
arac: Scrapling
repo: D4Vinci/Scrapling
kategori: Veri toplama
platformlar: [macOS, Linux, Windows]
zorluk: Orta
son_dogrulama: 2026-11-13
---

# Scrapling kurulumu

Scrapling, web sayfalarından veri toplamak için kullanılan bir Python kütüphanesidir. Sayfayı indirir, içinden istediğin bölümleri seçmeni sağlar ve sonucu dosyaya yazar.

!!! info "Doğrulama notu"
    Bu rehberdeki komutlar 13 Kasım 2026'da aracın resmî README dosyasından alındı. Komutlar her platformda ayrıca denenmedi; bir adım sende çalışmazsa [hata bildir](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues/new/choose).

## Bu araç ne işe yarar?

Bir sitedeki bilgiyi elle kopyalamak yerine programla toplamaya **web kazıma** (web scraping) denir. Scrapling bu işin üç adımını tek pakette toplar:

- **İndirme:** Sayfayı sıradan bir HTTP isteğiyle ya da gerçek bir tarayıcıyla açar. JavaScript ile dolan sayfalar için tarayıcı gerekir.
- **Seçme:** CSS ya da XPath seçicileriyle sayfadan istediğin öğeleri alır.
- **Dışa aktarma:** Sonuçları JSON, CSV gibi biçimlerde kaydeder.

Örnek: Ders için bir alıntı sitesinden bütün alıntıları çekip analiz etmek, ya da kendi sitendeki bozuk bağlantıları taramak.

!!! warning "Kullanmadan önce"
    Bir siteden veri toplamadan önce kullanım koşullarına ve `robots.txt` dosyasına bak. Kişisel veri topluyorsan KVKK kapsamındaki yükümlülükler sana aittir. Bu rehberdeki örnekler, kazıma alıştırması için yayımlanmış `quotes.toscrape.com` sitesini kullanır.

## Ön koşullar

- **Python 3.10 ya da üstü.** Kontrol et:

    ```bash
    python3 --version
    ```

    Windows'ta komut `python --version` olur.

- **pip.** Python ile birlikte gelir.

## Kurulum

Komutlar bütün işletim sistemlerinde aynıdır.

Sayfa indirme özellikleriyle birlikte kur:

```bash
pip install "scrapling[fetchers]"
```

Yalnızca `pip install scrapling` yazarsan sadece ayrıştırıcı kurulur; sayfa indiremezsin.

Tarayıcı gerektiren sayfalar için tarayıcı dosyalarını indir:

```bash
scrapling install
```

Bu adım yalnızca tarayıcıyla açılan sayfalar için gerekir. Düz HTTP istekleriyle çalışacaksan atlayabilirsin.

Komut satırından kod yazmadan kullanmak istersen kabuk eklentisini de kur:

```bash
pip install "scrapling[shell]"
```

## İlk kullanım

### Kod yazmadan

Bir sayfayı Markdown dosyası olarak kaydet:

```bash
scrapling extract get 'https://quotes.toscrape.com/' alintilar.md
```

Sayfanın yalnızca belli bir bölümünü al:

```bash
scrapling extract get 'https://quotes.toscrape.com/' alintilar.txt --css-selector '.quote'
```

`--css-selector` seçeneği sayfadaki hangi öğelerin alınacağını belirler. Burada `quote` sınıfını taşıyan öğeler seçiliyor.

### Python ile

`alintilar.py` adında bir dosya oluştur:

```python
from scrapling.fetchers import Fetcher

sayfa = Fetcher.get("https://quotes.toscrape.com/")
alintilar = sayfa.css(".quote .text::text").getall()

for alinti in alintilar:
    print(alinti)
```

Çalıştır:

```bash
python3 alintilar.py
```

Terminalde sayfadaki alıntıların listesini görmelisin. `Fetcher.get` sayfayı indirir, `css` seçiciye uyan öğeleri bulur, `getall` hepsini liste olarak verir.

Aynı seçimi XPath ile de yapabilirsin:

```python
alintilar = sayfa.xpath('//div[@class="quote"]')
```

## Sık karşılaşılan sorunlar

### `ModuleNotFoundError: No module named 'scrapling.fetchers'` ya da eksik bağımlılık hatası

Temel paket kurulmuş, indirme eklentisi kurulmamış. Şunu çalıştır:

```bash
pip install "scrapling[fetchers]"
```

### zsh'te `no matches found: scrapling[fetchers]`

macOS'un varsayılan kabuğu köşeli parantezleri özel karakter sayar. Paket adını rehberdeki gibi tırnak içinde yaz.

### Tarayıcıyla açılan sayfalarda tarayıcı bulunamadı hatası

`scrapling install` adımı atlanmış. Çalıştır; dosyalar bozulduysa `scrapling install --force` ile yeniden indir.

### Liste boş dönüyor

Seçici sayfadaki yapıyla uyuşmuyor ya da içerik JavaScript ile sonradan yükleniyor. Tarayıcında sayfaya sağ tıklayıp "İncele" ile öğenin sınıf adını kontrol et.

### `scrapling: command not found`

Terminali yeniden aç. Sorun sürerse komutu `python3 -m pip install ...` biçiminde kurduğun Python ile aynı ortamda çalıştırdığından emin ol.

## Kaynaklar

- [Resmî depo](https://github.com/D4Vinci/Scrapling)
- [Resmî belgeler](https://scrapling.readthedocs.io/en/latest/)
- Lisans: BSD-3-Clause
