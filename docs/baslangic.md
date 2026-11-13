# Terminale giriş

Rehberlerdeki komutların hepsi terminale yazılır. Daha önce terminal kullanmadıysan bu sayfa beş dakikada yetecek kadarını anlatır.

## Terminal nedir?

Terminal, bilgisayara fareyle tıklamak yerine yazıyla komut verdiğin penceredir. Bir satır yazarsın, Enter'a basarsın, bilgisayar yapar ve sonucu altına yazar.

## Terminali açmak

=== "macOS"

    ++cmd+space++ tuşlarına bas, `Terminal` yaz ve Enter'a bas.

=== "Windows"

    Başlat menüsünü aç, `PowerShell` yaz ve Enter'a bas. Rehberlerde "PowerShell'i aç" denen yer burasıdır.

=== "Linux"

    Çoğu dağıtımda ++ctrl+alt+t++ kısayolu terminali açar.

## Komut yazarken bilmen gerekenler

- **Komutu kopyala, yapıştır.** Elle yazarken yapılan tek harf hatası komutu bozar. Rehberlerdeki kod kutularının sağ üstünde kopyalama düğmesi var.
- **Enter'a basmadan komut çalışmaz.**
- **Çıktıyı oku.** Komut bir şey yazdıysa çoğu zaman ne olduğunu söylüyordur. `error` ya da `not found` geçiyorsa bir sorun var demektir.
- **Hiçbir şey yazmaması çoğu zaman iyi haberdir.** Birçok komut başarılı olduğunda sessiz kalır.
- **Satır başındaki `$` işaretini yazma.** Bazı kaynaklarda komutların başında görürsün; komutun parçası değildir.

## Sık kullanacağın üç komut

Hangi klasörde olduğunu gör:

```bash
pwd
```

Klasördeki dosyaları listele (`dir` Windows'ta da çalışır):

```bash
ls
```

Başka bir klasöre geç:

```bash
cd klasor-adi
```

Bir üst klasöre dönmek için `cd ..` yaz.

## Sık geçen terimler

**Paket yöneticisi**
:   Programları tek komutla kuran araç. macOS'ta Homebrew (`brew`), Windows'ta Winget (`winget`), Python dünyasında `pip` ve `uv`, JavaScript dünyasında `npm` en yaygın olanlardır.

**PATH**
:   Bilgisayarın, yazdığın komutu aradığı klasörlerin listesi. Bir aracı kurduktan sonra `command not found` hatası alıyorsan çoğu zaman aracın klasörü bu listede değildir. İlk denenecek şey terminali kapatıp yeniden açmaktır.

**sudo**
:   macOS ve Linux'ta bir komutu yönetici yetkisiyle çalıştırır ve parolanı sorar. Parolayı yazarken ekranda hiçbir şey görünmez; bu normaldir.

**Depo (repository)**
:   Bir projenin dosyalarının ve geçmişinin tutulduğu yer. GitHub'daki her proje bir depodur.

**Ortam değişkeni**
:   Programların okuduğu, ada bağlı bir ayar. API anahtarları çoğu zaman böyle verilir.

## Bir şey ters giderse

1. Hata mesajının tamamını kopyala.
2. Terminali kapatıp yeniden aç ve komutu bir kez daha dene.
3. Olmazsa hangi işletim sistemini kullandığını ve hata mesajını ekleyerek [Tartışmalar](https://github.com/osmancancet/turkce-kurulum-rehberleri/discussions) bölümüne yaz.
