# Türkçe Kurulum Rehberleri

GitHub'da hızla yükselen açık kaynak araçlar için, yeni başlayanlara yönelik Türkçe kurulum rehberleri.

Çoğu yeni aracın belgesi yalnızca İngilizce ve okurun terminale, paket yöneticilerine alışkın olduğunu varsayıyor. Buradaki rehberler aynı kurulumu sıfırdan, işletim sistemine göre ayrılmış adımlarla ve sık görülen hataların çözümleriyle anlatır.

**Site:** https://osmancancet.github.io/turkce-kurulum-rehberleri/

## Rehberler

| Araç | Ne işe yarar? |
|---|---|
| [agent-browser](docs/rehberler/agent-browser.md) | Yapay zekâ ajanları için komut satırından tarayıcı otomasyonu |
| [Browser Use](docs/rehberler/browser-use.md) | Yapay zekâ modeline tarayıcı kullandıran Python kütüphanesi |
| [Open WebUI](docs/rehberler/open-webui.md) | Yerel ve bulut modeller için tarayıcıda çalışan sohbet arayüzü |
| [Spec Kit](docs/rehberler/spec-kit.md) | Kodlama ajanlarıyla şartname odaklı geliştirme süreci |
| [Worktrunk](docs/rehberler/worktrunk.md) | Git worktree yönetimi; birden fazla dalda aynı anda çalışma |

## Nasıl katkı verilir?

- **Araç öner:** [Rehber isteği aç](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues/new/choose).
- **Rehber yaz:** [Katkı rehberini](CONTRIBUTING.md) oku, `sablonlar/rehber-sablonu.md` dosyasından başla.
- **Soru sor:** Kurulumda takıldıysan [Tartışmalar](https://github.com/osmancancet/turkce-kurulum-rehberleri/discussions) bölümüne yaz.

## Yerelde çalıştırma

```bash
pip install -r requirements.txt
mkdocs serve
```

## Rehber kalıbı

Her rehber aynı başlıkları taşır: aracın ne işe yaradığı, ön koşullar, kurulum, ilk kullanım, sık karşılaşılan sorunlar ve kaynaklar. Rehberin başındaki `son_dogrulama` alanı komutların en son ne zaman kontrol edildiğini gösterir.
