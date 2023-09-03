setup:
	python3 -m venv
	pip install -r requirements.txt

run:
  python detectorColisao.py
  python sensors.py

clean:
  rm -rf venv
