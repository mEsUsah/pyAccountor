# Accounting project
Ultra simple Python 3 project to account for work done by my kids and other 
events that earn them money.

## How to run:
* Clone project
```bash
git clone git@github.com:mEsUsah/pyaccountor.git
```

* run CLI app
```bash
cd pyaccountor
python3 cli_app.py
```

## Tables:
* accounts
    * id (INTEGER) <--- Primary key
    * name (TEXT)

* transactions
    * id (INTEGER) <---- Primary key
    * date (TEXT)
    * account_id (INTEGER) <--- foreign key
    * debit_account_id (INTEGER) <---- foreign key, nullable
    * debit_amount (INTEGER)
    * credit_account_id (INTEGER) foreign key, nullable
    * credit_amount (INTEGER)
    * forfilled (INTEGER)

