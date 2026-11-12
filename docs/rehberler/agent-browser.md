---
arac: agent-browser
repo: vercel-labs/agent-browser
kategori: Tarayıcı otomasyonu
platformlar: [macOS, Linux, Windows]
zorluk: Başlangıç
son_dogrulama: 2026-11-12
---

# agent-browser kurulumu

agent-browser, yapay zekâ ajanlarının bir web tarayıcısını komut satırından kullanmasını sağlayan bir araçtır. Sayfa açar, içeriğini okur, tıklar, form doldurur ve ekran görüntüsü alır.

!!! info "Doğrulama notu"
    Bu rehberdeki komutlar 12 Kasım 2026'da aracın resmî README dosyasından alındı. Komutlar her platformda ayrıca denenmedi; bir adım sende çalışmazsa [hata bildir](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues/new/choose).

## Bu araç ne işe yarar?

Claude Code gibi kodlama ajanları terminalde çalışır ve kendi başlarına bir web sayfasını göremez. agent-browser bu boşluğu doldurur: ajan terminale kısa komutlar yazar, araç da gerçek bir Chrome penceresinde bu işlemleri yapar.

Aracın ajanlara uygun olmasının nedeni sayfayı okuma biçimidir. Sayfanın bütün HTML'ini dökmek yerine **erişilebilirlik ağacını** verir: düğmeler, bağlantılar ve giriş alanları kısa bir liste olarak gelir, her birinin `@e1`, `@e2` gibi bir etiketi olur. Ajan "`@e2`'ye tıkla" demekle yetinir.

Örnek: Yazdığın web sitesinin giriş formunu ajana test ettirmek, ya da bir sayfadaki tabloyu okutup özet çıkarttırmak.

## Ön koşullar

- **Node.js ve npm.** En yaygın kurulum yolu npm'dir. Kontrol et:

    ```bash
    node --version
    npm --version
    ```

    Sürüm numarası çıkmıyorsa Node.js'i [nodejs.org](https://nodejs.org) adresinden kur. macOS'ta Homebrew kullanıyorsan Node.js'e gerek kalmadan da kurabilirsin.

- **Chrome.** Bilgisayarında Chrome, Brave ya da daha önce kurulmuş bir Playwright tarayıcısı varsa araç onu kendiliğinden bulur. Yoksa kurulumun ikinci adımı uygun bir Chrome indirir.

## Kurulum

=== "macOS"

    Homebrew ile:

    ```bash
    brew install agent-browser
    agent-browser install
    ```

    Ya da npm ile:

    ```bash
    npm install -g agent-browser
    agent-browser install
    ```

=== "Linux"

    ```bash
    npm install -g agent-browser
    agent-browser install --with-deps
    ```

    `--with-deps` seçeneği Chrome'un ihtiyaç duyduğu sistem kütüphanelerini de kurar. Yönetici yetkisi gerektirir; root değilsen komutun başına `sudo` ekle.

=== "Windows"

    PowerShell'i aç:

    ```powershell
    npm install -g agent-browser
    agent-browser install
    ```

İlk komut aracı kurar. İkinci komut olan `agent-browser install`, test amaçlı bir Chrome sürümü (Chrome for Testing) indirir ve yalnızca ilk kurulumda gerekir.

Aracı ileride güncellemek için:

```bash
agent-browser upgrade
```

## İlk kullanım

Aşağıdaki komutları sırayla dene. Bunları ajan da aynı biçimde kullanır.

Bir sayfa aç:

```bash
agent-browser open example.com
```

Tarayıcı başlar ve adrese gider.

Sayfada neler olduğunu listele:

```bash
agent-browser snapshot
```

Çıktıda sayfadaki öğeler `@e1`, `@e2` gibi etiketlerle gelir. Sonraki komutlarda bu etiketleri kullanırsın.

Bir öğenin metnini oku, bir bağlantıya tıkla:

```bash
agent-browser get text @e1
agent-browser click @e2
```

Bir giriş alanını doldur:

```bash
agent-browser fill @e3 "ornek@example.com"
```

Ekran görüntüsü al ve tarayıcıyı kapat:

```bash
agent-browser screenshot sayfa.png
agent-browser close
```

Etiketler her `snapshot` çıktısına göre değişebilir. Sayfa değiştikten sonra yeniden `snapshot` al.

## Sık karşılaşılan sorunlar

### macOS 12 ya da daha eski sürümde `agent-browser install` Chrome indiremiyor

Chrome for Testing macOS 13'ten eski sürümleri desteklemiyor. Chrome'u [google.com/chrome](https://www.google.com/chrome/) adresinden elle kur; araç kurulu Chrome'u kendiliğinden bulur.

### Linux'ta tarayıcı açılmıyor, eksik kütüphane hatası veriyor

Kurulumu `agent-browser install --with-deps` ile yeniden çalıştır. Komut gereken kütüphanelerin tamamını kuramazsa hata koduyla çıkar; bu durumda komutu `sudo` ile dene.

### `npm install -g` izin hatası veriyor (EACCES)

macOS ve Linux'ta npm'in genel klasörüne yazma iznin olmadığında görülür. Node.js'i `nvm` gibi bir sürüm yöneticisiyle kurmak bu sorunu kalıcı olarak çözer.

### `agent-browser: command not found`

Terminali kapatıp yeniden aç. Sorun sürerse `npm config get prefix` çıktısındaki klasörün PATH'te olduğunu kontrol et.

## Kaynaklar

- [Resmî depo](https://github.com/vercel-labs/agent-browser)
- [Resmî belgeler](https://agent-browser.dev)
- Lisans: Apache-2.0
