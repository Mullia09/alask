# alask
Internal Auditor ISO 45001:2018

## Volunteer Registration App

This repository includes a small command line application to register volunteers. The script is located in `volunteer_app/register.py` and stores data in `volunteer_app/volunteers.csv`.

### Usage

Run the script using Python 3:

```bash
python3 volunteer_app/register.py
```

You will be prompted to add new volunteers or list existing ones.

## Volunteer System CLI

A more complete console application is available in `volunteer_app/main.py`. It supports OTP based registration and login, basic program management and records actions in an audit trail using SQLite.

Initialize the database and start the application:

```bash
python3 -m volunteer_app.main
```

## Awan Kata Kunci

![Awan Kata Kunci](https://quickchart.io/chart?c=%7Btype%3A%22wordCloud%22%2Cdata%3A%7Blabels%3A%5B%22Tapah%22%2C%22Ekonomi%22%2C%22Pelancongan%22%2C%22Pembangunan%22%2C%22Infrastruktur%22%2C%22Komuniti%22%2C%22Warisan%22%2C%22Pendidikan%22%2C%22Industri%22%2C%22Alam%20Sekitar%22%5D%2Cdatasets%3A%5B%7Bdata%3A%5B120%2C95%2C80%2C75%2C70%2C65%2C60%2C55%2C50%2C45%5D%7D%5D%7D%7D)
