import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import rehber_denetle as rd

BUGUN = dt.date(2026, 11, 12)

GECERLI = """---
arac: Örnek
repo: sahip/depo
kategori: Git
platformlar: [macOS, Linux]
zorluk: Başlangıç
son_dogrulama: 2026-11-01
---

# Örnek kurulumu

## Bu araç ne işe yarar?
## Ön koşullar
## Kurulum

```bash
komut
```

## İlk kullanım
## Sık karşılaşılan sorunlar
## Kaynaklar
"""


def denetle(tmp_path, metin):
    yol = tmp_path / "ornek.md"
    yol.write_text(metin, encoding="utf-8")
    return rd.rehberi_denetle(yol, BUGUN)


def test_gecerli_rehber_hatasiz(tmp_path):
    veri, hatalar, uyarilar = denetle(tmp_path, GECERLI)
    assert hatalar == [] and uyarilar == []
    assert veri["arac"] == "Örnek"


def test_on_bilgi_yoksa_hata(tmp_path):
    _, hatalar, _ = denetle(tmp_path, "# Başlık\n")
    assert any("ön bilgi" in h for h in hatalar)


def test_eksik_alan_ve_baslik(tmp_path):
    metin = GECERLI.replace("kategori: Git\n", "").replace("## Kaynaklar\n", "")
    _, hatalar, _ = denetle(tmp_path, metin)
    assert "ön bilgide 'kategori' alanı eksik" in hatalar
    assert "başlık eksik: ## Kaynaklar" in hatalar


def test_gecersiz_platform_ve_repo(tmp_path):
    metin = GECERLI.replace("[macOS, Linux]", "[macOS, BeOS]").replace("sahip/depo", "https://github.com/a/b")
    _, hatalar, _ = denetle(tmp_path, metin)
    assert any("bilinmeyen platform: BeOS" in h for h in hatalar)
    assert any("sahip/depo biçiminde" in h for h in hatalar)


def test_baslik_sirasi(tmp_path):
    metin = GECERLI.replace("## Ön koşullar\n## Kurulum\n", "## Kurulum\n## Ön koşullar\n")
    _, hatalar, _ = denetle(tmp_path, metin)
    assert any("başlık sırası yanlış" in h for h in hatalar)


def test_gelecek_tarih_hata_eski_tarih_uyari(tmp_path):
    _, hatalar, _ = denetle(tmp_path, GECERLI.replace("2026-11-01", "2027-01-01"))
    assert any("gelecekte" in h for h in hatalar)
    _, hatalar, uyarilar = denetle(tmp_path, GECERLI.replace("2026-11-01", "2026-01-01"))
    assert hatalar == [] and len(uyarilar) == 1


def test_liste_alfabetik(tmp_path):
    a = {"arac": "zeta", "kategori": "K", "platformlar": ["Linux"], "zorluk": "Orta", "son_dogrulama": BUGUN}
    b = dict(a, arac="Alfa")
    liste = rd.listeyi_uret([(tmp_path / "zeta.md", a), (tmp_path / "alfa.md", b)])
    assert liste.index("[Alfa](alfa.md)") < liste.index("[zeta](zeta.md)")


def test_bos_liste():
    assert "Henüz yayımlanmış rehber yok" in rd.listeyi_uret([])
