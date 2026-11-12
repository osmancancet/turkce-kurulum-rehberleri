---
arac: Worktrunk
repo: max-sixty/worktrunk
kategori: Git
platformlar: [macOS, Linux, Windows]
zorluk: Orta
son_dogrulama: 2026-11-12
---

# Worktrunk kurulumu

Worktrunk, aynı projede birden fazla dalda aynı anda çalışmayı kolaylaştıran bir komut satırı aracıdır. Özellikle birkaç yapay zekâ kodlama ajanını yan yana çalıştıranlar için yazılmıştır.

!!! info "Doğrulama notu"
    Bu rehberdeki komutlar 12 Kasım 2026'da aracın resmî README dosyasından alındı. Komutlar her platformda ayrıca denenmedi; bir adım sende çalışmazsa [hata bildir](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues/new/choose).

## Bu araç ne işe yarar?

Git'te normalde tek klasörde tek dal açıktır. Başka bir dala geçmek için elindeki işi kaydetmen ya da bir kenara koyman gerekir. Git'in **worktree** özelliği bu sınırı kaldırır: aynı deponun her dalı ayrı bir klasörde açık durur, birinden ötekine geçerken hiçbir şey kaybolmaz.

Sorun, `git worktree` komutlarının uzun ve akılda tutması zor olmasıdır. Worktrunk bunları kısaltır. Dalın adını yazarsın, klasörü o oluşturur ve seni içine götürür.

Örnek: Bir ajan `giris-ekrani` dalında çalışırken sen `hata-duzeltme` dalında başka bir işe bakabilirsin. İkisi ayrı klasörlerde durduğu için birbirinin dosyalarını bozmaz.

## Ön koşullar

- **Git.** Terminale şunu yaz, sürüm numarası görüyorsan kuruludur:

    ```bash
    git --version
    ```

- **Bir paket yöneticisi.** macOS ve Linux'ta Homebrew, Windows'ta Winget en kısa yoldur. Windows 11'de Winget hazır gelir.
- **Bir Git deposu.** Worktrunk komutları bir deponun içinde çalışır.

## Kurulum

=== "macOS"

    Terminal uygulamasını aç ve şunu çalıştır:

    ```bash
    brew install worktrunk && wt config shell install
    ```

=== "Linux"

    Homebrew kuruluysa:

    ```bash
    brew install worktrunk && wt config shell install
    ```

    Arch Linux'ta:

    ```bash
    sudo pacman -S worktrunk && wt config shell install
    ```

=== "Windows"

    PowerShell'i aç ve sırayla çalıştır:

    ```powershell
    winget install max-sixty.worktrunk
    git-wt config shell install
    ```

    Windows'ta komutun adı `wt` değil `git-wt` olur, çünkü `wt` adı Windows Terminal tarafından kullanılıyor. Bu rehberin geri kalanında `wt` gördüğün her yere `git-wt` yaz.

=== "Diğer yollar"

    Rust kuruluysa her platformda:

    ```bash
    cargo install worktrunk && wt config shell install
    ```

    Conda ile:

    ```bash
    conda install -c conda-forge worktrunk && wt config shell install
    ```

İkinci komut olan `wt config shell install` atlanmamalı. Bu adım kabuk bütünleşmesini kurar; o olmadan Worktrunk seni yeni klasöre taşıyamaz.

Kurulumdan sonra terminali kapatıp yeniden aç ve kontrol et:

```bash
wt --help
```

Komut listesi görünüyorsa kurulum tamamdır.

## İlk kullanım

Önce bir Git deposunun klasörüne gir. Sonra yeni bir dal ve ona ait klasörü tek komutla oluştur:

```bash
wt switch --create giris-ekrani
```

Bu komut ana daldan `giris-ekrani` adında bir dal açar, ona ayrı bir klasör oluşturur ve seni o klasöre geçirir.

Açık olan bütün çalışma klasörlerini gör:

```bash
wt list
```

Listede `@` işareti şu an içinde bulunduğun klasörü, `+` işareti commit'lenmeyi bekleyen değişiklikleri gösterir.

İşin bitince, pull request birleştirildikten sonra klasörü temizle:

```bash
wt remove
```

Pull request açmadan, işi doğrudan ana dala almak istersen:

```bash
wt merge main
```

Bu komut commit'leri tek commit'te toplar, ana dalın üstüne taşır, birleştirir ve klasörü kaldırır.

Claude Code kullanıyorsan dalı açıp ajanı aynı anda başlatabilirsin:

```bash
wt switch -x claude -c giris-ekrani -- 'Kullanıcı girişi ekle'
```

## Sık karşılaşılan sorunlar

### Windows'ta `wt` yazınca Windows Terminal açılıyor

Beklenen davranış. Winget aracı `git-wt` adıyla kurar. Komutları `git-wt` ile yaz. `wt` adını kullanmak istersen Windows ayarlarında "Uygulama yürütme diğer adları" bölümünden Terminal'in diğer adını kapatman gerekir.

### `wt switch` çalışıyor ama klasör değişmiyor

Kabuk bütünleşmesi kurulmamış. `wt config shell install` komutunu çalıştır, terminali kapatıp yeniden aç.

### `wt: command not found`

Terminali kurulumdan sonra yeniden açmadıysan önce onu dene. Cargo ile kurduysan `~/.cargo/bin` klasörünün PATH'te olduğundan emin ol.

## Kaynaklar

- [Resmî depo](https://github.com/max-sixty/worktrunk)
- [Resmî belgeler](https://worktrunk.dev)
- Lisans: MIT ya da Apache-2.0
