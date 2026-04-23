# README Sistem — SM-OS Strategic Core

Dokumen ini adalah panduan sistem untuk menjalankan **SM-OS Strategic Core** secara konsisten lintas tim.

## 1) Tujuan Sistem

SM-OS Strategic Core dipakai untuk:
- menyatukan arah strategis,
- menerjemahkan strategi ke program eksekusi,
- menjaga ritme operasional,
- menutup loop keputusan berbasis data,
- menstandarkan output dan pelaporan.

## 2) Struktur Inti

1. `01_IDENTITY/` — identitas strategis (visi, misi, positioning).
2. `02_DOCTRINE/` — prinsip kerja, kebijakan, SOP.
3. `03_PROGRAMS/` — roadmap, backlog, milestone.
4. `04_WAR_ROOM/` — prioritas mingguan, keputusan cepat, blocker.
5. `05_DATA_FIELD/` — KPI, sumber data, eksperimen, insight.
6. `06_TEMPLATES/` — template baku dokumen.
7. `07_OUTPUTS/` — output final (report, deck, playbook).
8. `08_DASHBOARD/` — ringkasan performa dan health check.

## 3) Siklus Operasi (Cadence)

### Harian
- Perbarui `04_WAR_ROOM/action-tracker.md`.
- Catat blocker baru dan owner mitigasi.

### Mingguan
- Tetapkan 3 prioritas minggu berjalan di `04_WAR_ROOM/weekly-priorities.md`.
- Review kemajuan program di `03_PROGRAMS/milestones.md`.
- Sinkronkan KPI utama di `08_DASHBOARD/kpi-summary.md`.

### Bulanan
- Review outcome terhadap objective di `08_DASHBOARD/okr-status.md`.
- Rekap insight dari `05_DATA_FIELD/insights.md`.
- Publikasikan hasil ke `07_OUTPUTS/reports/`.

## 4) Standar Penamaan File

Ringkasan aturan ada di bawah ini.
Gunakan pola:
- `kebab-case` untuk nama file, contoh: `risk-monitor.md`.
- tanggal ISO jika time-based, contoh: `report-2026-04.md`.
- awali dokumen keputusan dengan konteks, contoh: `pricing-decision-2026-04.md`.


Lihat detail lengkap di `06_TEMPLATES/naming-convention.md`.

## 5) Definisi Minimal Selesai (Definition of Done)

Sebuah artefak dianggap selesai jika:
1. memiliki owner,
2. memiliki tanggal update terakhir,
3. memiliki keputusan/next action yang jelas,
4. tertaut ke objective/KPI terkait,
5. tersimpan di folder domain yang benar.

## 6) Aturan Tata Kelola

- **Single source of truth**: satu dokumen utama per topik.
- **Traceability**: keputusan harus tercatat di `decision-log`.
- **Evidence-based**: klaim strategis wajib punya data pendukung.
- **Reviewability**: perubahan mayor direview minimal 1 owner lintas fungsi.

## 7) Alur Implementasi Cepat (Quick Start)

1. Isi `01_IDENTITY` dan `02_DOCTRINE` terlebih dulu.
2. Turunkan inisiatif aktif ke `03_PROGRAMS`.
3. Jalankan ritme eksekusi lewat `04_WAR_ROOM`.
4. Ukur dan validasi lewat `05_DATA_FIELD` + `08_DASHBOARD`.
5. Gunakan `06_TEMPLATES` sebelum mempublikasikan ke `07_OUTPUTS`.

## 8) RACI Ringkas (Contoh)

- **Responsible**: Program Owner per stream di `03_PROGRAMS/owners.md`.
- **Accountable**: Strategic Lead.
- **Consulted**: Data Lead, Ops Lead, Product/Business Lead.
- **Informed**: Stakeholder eksekutif dan tim pelaksana.

## 9) Checklist Audit Bulanan

- [ ] Semua objective punya status terbaru.
- [ ] Semua KPI inti punya angka bulan berjalan.
- [ ] Semua keputusan besar tercatat dengan alasan.
- [ ] Semua program memiliki milestone berikutnya.
- [ ] Semua output penting terarsip rapi di `07_OUTPUTS`.


## Navigasi Cepat

- Lihat `INDEX.md` untuk peta navigasi seluruh dokumen.
