# django_pyspark_aws_emr_poc
A Django PySpark application with AWS EMR

```shell
# Project Setup

git clone <this repo>
cd django_pyspark_aws_emr_poc

# Observe dot at tne end of this command
django-admin startproject django_pyspark_aws_emr_poc .

python manage.py runserver

mkdir -p trades_ingest_forex
touch trades_ingest_forex/__init__.py
touch trades_ingest_forex/trades_ingest_facade_impl.py
touch trades_forex_data_generator.py

# Generates Test FOREX datasets
python trades_forex_data_generator

python manage.py runscript run_trades_ingest_forex_to_s3.py

```