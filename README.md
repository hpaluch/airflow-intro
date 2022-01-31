# AirFlow intro DAGs

Here are my basic DAGs to understand how
Apache AirFlow works.

Tested on Ubuntu 18 with Python 3.6.

We use AirFlow 2.2.3 version.

Install at least:
```bash
sudo apt-get install python3-dev make gcc g++ \
   python3-pip git-core curl
```

Then install locally required packages:
```bash
pip3 install -r requirements.txt -c constraints-3.6.txt
```
If you enecounter error:
```
ModuleNotFoundError: No module named 'setuptools_rust'
```
You have to follow: https://github.com/pyca/cryptography/issues/5753
```bash
# upgrade pip3 itself
python3 -m pip install -U pip setuptools
PATH=~/.local/bin:$PATH
pip3 install -r requirements.txt -c constraints-3.6.txt
```

At least once you should run
```bash
airflow standalone
```
To setup database etc - you can then press `Ctrl`-`C` to exit standalone
runner.

Now run tests with:
```bash
./run_tests.sh
```

# Running DAGs directly

Running `bash_template` dag immediately:
```bash
airflow dags test bash_template now
airflow dags test email_template now
```
