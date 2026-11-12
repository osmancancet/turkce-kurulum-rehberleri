# Katkı rehberi

Bu depo, GitHub'da yükselen açık kaynak araçlar için Türkçe kurulum rehberleri toplar. Katkının her türü değerli: yeni rehber, hata düzeltmesi, eksik bir işletim sistemi adımı, daha anlaşılır bir cümle.

## Yeni rehber yazmak

1. Aynı araç için açık bir istek ya da rehber var mı diye [issue listesine](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues) bak. Yoksa "Rehber isteği" şablonuyla bir tane aç ve üstlendiğini yaz.
2. Depoyu fork'la, `sablonlar/rehber-sablonu.md` dosyasını `docs/rehberler/arac-adi.md` olarak kopyala.
3. Şablondaki bütün başlıkları doldur. Başlık adlarını değiştirme; otomatik denetim bunlara bakar.
4. `python scripts/rehber_denetle.py` çalıştır. Betik rehberi denetler ve rehber listesini günceller.
5. `mkdocs.yml` içindeki `nav` bölümüne rehberi ekle.
6. Pull request aç ve açıklamaya `Closes #istek-numarası` yaz.

## Yazım kuralları

- Okurun daha önce terminal kullanmadığını varsay. Bir komutu yazmadan önce nereye yazılacağını söyle.
- Komutları aracın resmî belgelerinden al, kaynağı "Kaynaklar" başlığında ver. Denemediğin bir platform için adım yazıyorsan bunu belirt.
- Her komuttan sonra ne olması gerektiğini yaz: beklenen çıktı ya da kontrol komutu.
- Teknik terimin yerleşik Türkçesi varsa onu kullan, yoksa İngilizcesini bırak ve ilk geçtiği yerde açıkla.
- `son_dogrulama` alanına komutları en son kontrol ettiğin tarihi yaz.

## Yerelde önizleme

```bash
pip install -r requirements-dev.txt
python scripts/rehber_denetle.py
pytest -q
mkdocs serve
```

Tarayıcıda `http://127.0.0.1:8000` adresini aç.

## Hata bildirmek

Bir rehberdeki adım çalışmıyorsa "Rehberde hata" şablonuyla issue aç. İşletim sistemini, aracın sürümünü ve hata mesajını ekle.

## Soru sormak

Kurulum soruları için [Tartışmalar](https://github.com/osmancancet/turkce-kurulum-rehberleri/discussions) bölümünü kullan. Issue'lar rehber istekleri ve hatalar içindir.
