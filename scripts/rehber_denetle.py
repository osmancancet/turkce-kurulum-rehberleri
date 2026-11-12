#!/usr/bin/env python3
"""Rehber dosyalarını denetler ve rehber listesini üretir.

Kullanım:
    python scripts/rehber_denetle.py            # denetle, listeyi yeniden yaz
    python scripts/rehber_denetle.py --kontrol  # denetle, liste güncel değilse hata ver
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

KOK = Path(__file__).resolve().parent.parent
REHBER_KLASORU = KOK / "docs" / "rehberler"
LISTE_DOSYASI = REHBER_KLASORU / "index.md"

ZORUNLU_ALANLAR = ("arac", "repo", "kategori", "platformlar", "zorluk", "son_dogrulama")
ZORUNLU_BASLIKLAR = (
    "## Bu araç ne işe yarar?",
    "## Ön koşullar",
    "## Kurulum",
    "## İlk kullanım",
    "## Sık karşılaşılan sorunlar",
    "## Kaynaklar",
)
GECERLI_PLATFORMLAR = {"macOS", "Linux", "Windows"}
GECERLI_ZORLUKLAR = {"Başlangıç", "Orta", "İleri"}
REPO_KALIBI = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
ESKIME_GUN = 180

LISTE_BASI = """# Rehberler

Bu sayfa `scripts/rehber_denetle.py` tarafından üretilir; elle düzenleme.

"""
LISTE_SONU = """
Bir aracın rehberini görmek istiyorsan [rehber isteği aç](https://github.com/osmancancet/turkce-kurulum-rehberleri/issues/new/choose).
"""


def on_bilgiyi_oku(metin: str) -> tuple[dict, str]:
    """Dosyanın başındaki YAML bloğunu ve gövdeyi ayırır."""
    if not metin.startswith("---\n"):
        raise ValueError("dosya '---' ile başlayan ön bilgi bloğu içermiyor")
    try:
        _, blok, govde = metin.split("---\n", 2)
    except ValueError as hata:
        raise ValueError("ön bilgi bloğu '---' ile kapatılmamış") from hata
    veri = yaml.safe_load(blok) or {}
    if not isinstance(veri, dict):
        raise ValueError("ön bilgi bloğu anahtar-değer biçiminde değil")
    return veri, govde


def rehberi_denetle(yol: Path, bugun: dt.date) -> tuple[dict | None, list[str], list[str]]:
    """Tek rehberi denetler; (ön bilgi, hatalar, uyarılar) döndürür."""
    hatalar: list[str] = []
    uyarilar: list[str] = []
    try:
        veri, govde = on_bilgiyi_oku(yol.read_text(encoding="utf-8"))
    except (ValueError, yaml.YAMLError) as hata:
        return None, [str(hata)], uyarilar

    for alan in ZORUNLU_ALANLAR:
        if veri.get(alan) in (None, "", []):
            hatalar.append(f"ön bilgide '{alan}' alanı eksik")

    repo = str(veri.get("repo", ""))
    if repo and not REPO_KALIBI.match(repo):
        hatalar.append(f"'repo' alanı sahip/depo biçiminde olmalı: {repo!r}")

    platformlar = veri.get("platformlar") or []
    if not isinstance(platformlar, list):
        hatalar.append("'platformlar' alanı liste olmalı")
    else:
        bilinmeyen = [p for p in platformlar if p not in GECERLI_PLATFORMLAR]
        if bilinmeyen:
            hatalar.append(f"bilinmeyen platform: {', '.join(map(str, bilinmeyen))}")

    zorluk = veri.get("zorluk")
    if zorluk and zorluk not in GECERLI_ZORLUKLAR:
        hatalar.append(f"'zorluk' şunlardan biri olmalı: {', '.join(sorted(GECERLI_ZORLUKLAR))}")

    tarih = veri.get("son_dogrulama")
    if tarih is not None:
        if not isinstance(tarih, dt.date):
            hatalar.append("'son_dogrulama' YYYY-AA-GG biçiminde tarih olmalı")
        elif tarih > bugun:
            hatalar.append("'son_dogrulama' gelecekte bir tarih olamaz")
        elif (bugun - tarih).days > ESKIME_GUN:
            uyarilar.append(f"son doğrulama {(bugun - tarih).days} gün önce; komutlar yeniden kontrol edilmeli")

    satirlar = [s.rstrip() for s in govde.splitlines()]
    konum = -1
    for baslik in ZORUNLU_BASLIKLAR:
        if baslik not in satirlar:
            hatalar.append(f"başlık eksik: {baslik}")
            continue
        yeni = satirlar.index(baslik)
        if yeni < konum:
            hatalar.append(f"başlık sırası yanlış: {baslik}")
        konum = yeni

    if not any(s.startswith("# ") for s in satirlar):
        hatalar.append("birinci düzey başlık (# ...) yok")
    if "```" not in govde:
        hatalar.append("rehberde hiç komut bloğu yok")

    return veri, hatalar, uyarilar


def listeyi_uret(rehberler: list[tuple[Path, dict]]) -> str:
    if not rehberler:
        return LISTE_BASI + "Henüz yayımlanmış rehber yok. İlk rehberler yolda.\n" + LISTE_SONU
    satirlar = [
        "| Araç | Kategori | Platformlar | Zorluk | Son doğrulama |",
        "|---|---|---|---|---|",
    ]
    for yol, veri in sorted(rehberler, key=lambda r: str(r[1]["arac"]).lower()):
        satirlar.append(
            f"| [{veri['arac']}]({yol.name}) | {veri['kategori']} | "
            f"{', '.join(veri['platformlar'])} | {veri['zorluk']} | {veri['son_dogrulama']} |"
        )
    return LISTE_BASI + "\n".join(satirlar) + "\n" + LISTE_SONU


def main() -> int:
    ayristirici = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ayristirici.add_argument("--kontrol", action="store_true", help="listeyi yazma, güncel değilse hata ver")
    secenekler = ayristirici.parse_args()

    bugun = dt.date.today()
    gecerli: list[tuple[Path, dict]] = []
    hata_var = False
    for yol in sorted(REHBER_KLASORU.glob("*.md")):
        if yol == LISTE_DOSYASI:
            continue
        veri, hatalar, uyarilar = rehberi_denetle(yol, bugun)
        goreli = yol.relative_to(KOK)
        for uyari in uyarilar:
            print(f"UYARI {goreli}: {uyari}")
        for hata in hatalar:
            print(f"HATA  {goreli}: {hata}")
        if hatalar:
            hata_var = True
        elif veri is not None:
            gecerli.append((yol, veri))

    if hata_var:
        return 1

    liste = listeyi_uret(gecerli)
    mevcut = LISTE_DOSYASI.read_text(encoding="utf-8") if LISTE_DOSYASI.exists() else ""
    if secenekler.kontrol:
        if mevcut != liste:
            print("HATA  docs/rehberler/index.md güncel değil; 'python scripts/rehber_denetle.py' çalıştır")
            return 1
    elif mevcut != liste:
        LISTE_DOSYASI.write_text(liste, encoding="utf-8")
        print("docs/rehberler/index.md güncellendi")

    print(f"{len(gecerli)} rehber denetlendi, sorun yok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
