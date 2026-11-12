---
arac: Spec Kit
repo: github/spec-kit
kategori: Yapay zekâ ile geliştirme
platformlar: [macOS, Linux, Windows]
zorluk: Orta
son_dogrulama: 2026-11-12
---

# Spec Kit kurulumu

Spec Kit, GitHub'ın yayımladığı açık kaynak bir araç setidir. Yapay zekâ kodlama ajanına "şunu yap" demek yerine önce ne istediğini yazdırır, sonra plana, görevlere ve koda adım adım ilerletir.

!!! info "Doğrulama notu"
    Bu rehberdeki komutlar 12 Kasım 2026'da aracın resmî README dosyasından alındı. Komutlar her platformda ayrıca denenmedi; bir adım sende çalışmazsa [hata bildir](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues/new/choose).

## Bu araç ne işe yarar?

Bir ajana tek cümlelik istek verdiğinde çoğu zaman çalışan ama istediğin gibi olmayan bir sonuç alırsın. Spec Kit'in önerdiği yöntemin adı **şartname odaklı geliştirme**dir (Spec-Driven Development): önce projenin ilkeleri, sonra özelliğin ne yapacağı, sonra teknik plan yazılır. Kod en son gelir ve bu belgelere göre üretilir.

Araç iki parçadan oluşur:

- `specify` adında bir komut satırı aracı. Projeyi hazırlar, gerekli şablonları klasöre yerleştirir.
- Ajanın sohbet penceresinde kullandığın `/speckit-...` komutları. Süreç bu komutlarla ilerler.

Çekirdek sürecin yanında iki hazır eklenti gelir: hata düzeltme ve bir fikrin yapılmaya değer olup olmadığını değerlendirme.

## Ön koşullar

- **Python 3.11 ya da üstü.** Kontrol et:

    ```bash
    python3 --version
    ```

    Windows'ta komut `python --version` olur.

- **uv.** Python araçlarını kuran bir paket yöneticisi. Aşağıda kurulumu var.
- **Desteklenen bir kodlama ajanı.** Resmî örnek GitHub Copilot ile verilir; diğer ajanlar için [resmî belgelerdeki](https://github.github.io/spec-kit/) entegrasyon listesine bak.

## Kurulum

### 1. uv'yi kur

=== "macOS ve Linux"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    PowerShell'de:

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

Terminali kapatıp yeniden aç ve kontrol et:

```bash
uv --version
```

### 2. Spec Kit'i kur

Bu adım bütün işletim sistemlerinde aynıdır:

```bash
uv tool install specify-cli
```

İsteğe bağlı iki eklentiyi de kurmak istersen:

```bash
specify extension add bug
specify extension add assess
```

İlki hata düzeltme sürecini, ikincisi fikir değerlendirme sürecini ekler.

## İlk kullanım

Yeni bir proje oluştur. Örnekte ajan olarak GitHub Copilot seçiliyor:

```bash
specify init benim-projem --integration copilot
cd benim-projem
```

`specify init` bir klasör açar ve seçtiğin ajan için gerekli dosyaları içine koyar.

Şimdi kodlama ajanını bu klasörde başlat. Aşağıdaki komutları terminale değil, **ajanın sohbet penceresine** tek tek yaz:

| Sıra | Komut | Ne yapar? |
|---|---|---|
| 1 | `/speckit-constitution` | Projenin ilkelerini yazar. Proje başına bir kez çalıştırılır. |
| 2 | `/speckit-specify` | Özelliğin ne yapacağını tarif edersin; şartnameyi çıkarır. |
| 3 | `/speckit-plan` | Hangi teknolojilerle yapılacağını söylersin; teknik planı yazar. |
| 4 | `/speckit-tasks` | Planı yapılacak işler listesine böler. |
| 5 | `/speckit-implement` | Görevleri uygular, kodu yazar. |
| 6 | `/speckit-converge` | Kodun şartnameyle örtüşüp örtüşmediğini kontrol eder. |

Komutların yanına isteğini düz metin olarak yazarsın. Örneğin:

```text
/speckit-constitution Kod kalitesine, teste ve bakım kolaylığına odaklanan ilkeler oluştur.
/speckit-specify Fotoğrafları tarihe göre albümlere ayıran bir fotoğraf düzenleyici yap.
/speckit-plan Vite ve sade JavaScript kullan. Görseller yerelde kalsın.
```

5. ve 6. adımları, `/speckit-converge` çıktısında `Converged` yazana kadar tekrarla. Yeni bir özellik eklerken 2. adımdan yeniden başlarsın; ilkeleri baştan yazmana gerek yoktur.

## Sık karşılaşılan sorunlar

### `specify: command not found`

uv'nin araçları kurduğu klasör PATH'te değil. Şunu çalıştır, sonra terminali yeniden aç:

```bash
uv tool update-shell
```

### `uv: command not found`

uv kurulumundan sonra terminal yeniden açılmamış. Kapatıp aç; sorun sürerse kurulum komutunu yeniden çalıştır ve çıktının sonundaki PATH uyarısını izle.

### Python sürümü eski olduğu için kurulum başarısız

Spec Kit Python 3.11 ya da üstünü ister. uv uygun sürümü senin yerine indirebilir:

```bash
uv python install 3.12
```

### `/speckit-...` komutları ajanda görünmüyor

Ajanı `specify init` ile oluşturulan proje klasörünün içinde başlattığından emin ol. Projeyi başka bir ajan için hazırladıysan komutlar o ajana göre yerleştirilmiştir; `--integration` değerini kullandığın ajana göre seç.

## Kaynaklar

- [Resmî depo](https://github.com/github/spec-kit)
- [Resmî belgeler](https://github.github.io/spec-kit/)
- [uv kurulum belgeleri](https://docs.astral.sh/uv/getting-started/installation/)
- Lisans: MIT
