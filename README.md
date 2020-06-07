## How to Dev

1. Clone repo
2. Create a virtualenv
3. Active virtualenv
4. Install dependences
5. Copy and edit your .env file

```console
git clone https://github.com/dssantos/NumeroPorExtenso.git numeroporextenso
cd numeroporextenso
python -m venv .numeroporextenso
source .numeroporextenso/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
cat .env
```
