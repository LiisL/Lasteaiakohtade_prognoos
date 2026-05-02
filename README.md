# Rakvere valla sündivuse ja rände trendide analüüs lasteaia kohtade vajaduse hindamiseks

## Uurimisküsimus

Kuidas on muutunud Rakvere valla sündivus ja ränne ning mida see tähendab lasteaia kohtade vajaduse jaoks lähiaastatel?

---

## Projekti eesmärk

Projekti eesmärk on luua **täielik ETL-pipeline**, mis:

* loeb Statistikaameti API-st rahvastiku-, sündide-, surmade- ja rändeandmeid
* puhastab ja teisendab need analüüsitavaks kujuks
* salvestab tulemused PostgreSQL andmebaasi
* võimaldab tulemusi visualiseerida Apache Supersetis

---

## Arhitektuur

```text
Statistikaameti API
        ↓
Python ETL (Lasteaiakohad.py)
        ↓
CSV väljundfailid (Outputs/)
        ↓
PostgreSQL (etl/load_to_postgres.py)
        ↓
Apache Superset
        ↓
Dashboard ja visualiseeringud
```

---

## Andmeallikad

Statistikaameti API tabelid:

* RV0240 – rahvastik soo, vanuse ja elukoha järgi
* RV112U – elussündinud soo ja haldusüksuse järgi
* RV49U – surnud soo ja haldusüksuse järgi
* RV172 – sündimuse vanuskordajad
* RVR02 – rände saldo haldusüksuse järgi
* RVR03 – rände saldo vanuserühma järgi

---

## Projekti struktuur

```text
.
├── Outputs/                     # genereeritud CSV ja pildid
├── etl/
│   └── load_to_postgres.py     # Load: CSV → PostgreSQL
├── docker/
│   └── superset/
│       └── Dockerfile          # Superset + PostgreSQL driver
├── Lasteaiakohad.py            # ETL + prognoos + graafikud
├── docker-compose.yml          # PostgreSQL + Superset
├── requirements.txt
└── README.md
```

---

## Projekti käivitamine

### 1. Paigalda Python sõltuvused

```bash
pip install -r requirements.txt
```

---

### 2. Käivita PostgreSQL ja Superset

```bash
docker compose up -d
```

---

### 3. Käivita ETL pipeline

```bash
python Lasteaiakohad.py
```

See samm:

* laeb andmed API-st
* teeb transformatsioonid
* arvutab prognoosid
* salvestab CSV failid ja graafikud kausta `Outputs/`

---

### 4. Laadi andmed PostgreSQL-i

```bash
python etl/load_to_postgres.py
```

---

### 5. Ava Superset

Brauseris:

```
http://localhost:8088
```

**Login:**

* kasutaja: `admin`
* parool: `admin`

---

### 6. Lisa PostgreSQL ühendus Supersetis

Connection string:

```text
postgresql://postgres:postgres@postgres:5432/lasteaiakohad
```

NB:

* Superseti sees on host `postgres`
* Kui ühendud otse arvutist, kasuta porti `5433`

---

## PostgreSQL tabelid

ETL loob järgmised tabelid:

* `population_forecast`
* `birth_forecast`
* `kinder_need`
* `summary`
* `yearly_kinder_compare`
* `population_compare`
* `migration_history`
* `birth_death_history`
* `population_pyramid`

---

## Visualiseerimine (Superset)

Dashboard sisaldab:

* Rahvaarvu prognoos (2026–2035)
* Sündide ja surmade trendid
* Rände saldo
* Lasteaiakohtade vajadus
* Rahvastikupüramiid

---


## Peamised järeldused

* Rahvaarv väheneb enamikus stsenaariumites
* Loomulik iive on negatiivne
* Ränne mõjutab tulevikuprognoosi oluliselt
* Lasteaiakohtade vajadus pigem väheneb

---

## Piirangud

* Prognoos põhineb eeldustel ja ajaloolistel trendidel
* Rände vanuseline jaotus on lihtsustatud
* Ei eristata era- ja munitsipaallasteaedu
* Laste osalemismäärad on hinnangulised

---

## Kasutatud tehnoloogiad

* Python (pandas, numpy, requests, matplotlib)
* SQLAlchemy
* PostgreSQL
* Docker Compose
* Apache Superset

---

## Autorid

Jaak Ilves, Kata Metsar, Liis Lille, Miina Voltri
Andmetehnika projekt