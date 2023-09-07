# Accounting project
An ultra simple Python3 CLI project to account for work done by my kids and other 
events that earn them money.

## How to run
* Clone project
```bash
git clone <project-name>
```

* run app
```bash
cd
```

## Tables
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

