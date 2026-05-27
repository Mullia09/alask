# Naming Convention — SM-OS Strategic Core

Standar ini digunakan untuk menjaga konsistensi nama file/folder agar mudah dicari, diaudit, dan diotomasi.

## 1) Aturan Umum

- Gunakan huruf kecil semua (`lowercase`).
- Gunakan pemisah `-` (kebab-case), bukan spasi atau underscore.
- Hindari karakter khusus selain `-` dan `.`.
- Nama file harus deskriptif dan singkat (maksimal ±60 karakter bila memungkinkan).

## 2) Format Penamaan File

### A. Dokumen Umum

`<topik>-<jenis>.md`

Contoh:
- `growth-strategy-brief.md`
- `pricing-decision-memo.md`
- `ops-risk-register.md`

### B. Dokumen Bertanggal

`<topik>-<jenis>-<yyyy-mm>.md` atau `<topik>-<jenis>-<yyyy-mm-dd>.md`

Contoh:
- `kpi-summary-2026-04.md`
- `weekly-dashboard-2026-04-09.md`
- `milestone-review-2026-04.md`

### C. Versi Draft/Revisi

`<topik>-<jenis>-v<major>.<minor>.md`

Contoh:
- `okr-framework-v1.0.md`
- `okr-framework-v1.1.md`

> Jika dokumen sudah final, pindahkan ke nama final tanpa suffix versi bila memungkinkan.

## 3) Prefix yang Direkomendasikan per Domain

- `01_IDENTITY`: `vision-`, `mission-`, `positioning-`, `persona-`
- `02_DOCTRINE`: `principle-`, `policy-`, `sop-`, `operating-model-`
- `03_PROGRAMS`: `roadmap-`, `program-`, `milestone-`, `owner-`
- `04_WAR_ROOM`: `priority-`, `decision-log-`, `blocker-`, `action-tracker-`
- `05_DATA_FIELD`: `kpi-`, `metric-`, `experiment-`, `insight-`
- `06_TEMPLATES`: `template-`, `checklist-`
- `07_OUTPUTS`: `report-`, `deck-`, `playbook-`, `announcement-`
- `08_DASHBOARD`: `dashboard-`, `okr-status-`, `risk-monitor-`, `health-check-`

## 4) Standar Folder Tambahan (Opsional)

Untuk folder dengan volume tinggi, gunakan struktur:

- `YYYY/` lalu `YYYY-MM/` (contoh: `2026/2026-04/`), atau
- `active/`, `archive/` untuk pemisahan cepat.

## 5) Larangan (Anti-Pattern)

Hindari nama seperti:
- `Final FINAL report.md`
- `new doc (2).md`
- `Dashboard Update Terbaru Banget.md`
- `kpi_summary_april.md` (gunakan `kpi-summary-2026-04.md`)

## 6) Checklist Validasi Nama

Sebelum commit, pastikan:
- [ ] Sudah kebab-case.
- [ ] Tidak ada spasi/karakter khusus.
- [ ] Mengandung konteks topik + jenis dokumen.
- [ ] Menggunakan format tanggal ISO bila bertanggal.
- [ ] Konsisten dengan prefix domain terkait.
