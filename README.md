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

## Document Control System

For a minimal digital document control workflow with simple reward points, use
`volunteer_app/doc_control.py`.

```bash
python3 volunteer_app/doc_control.py
```

The script lets you register documents with a generated unique code, list the
stored records and awards a small point value for each registration.
