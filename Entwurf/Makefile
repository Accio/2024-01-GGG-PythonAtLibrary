all: py qc_code.png

py: 2024-01-PythonAtLibrary-GGG-Teil2-Entwurf.py 2024-01-PythonAtLibrary-GGG-Teil1-Entwurf.py

2024-01-PythonAtLibrary-GGG-Teil2-Entwurf.py: 2024-01-PythonAtLibrary-GGG-Teil2-Entwurf.ipynb
	jupyter-nbconvert 2024-01-PythonAtLibrary-GGG-Teil2-Entwurf.ipynb --to script

2024-01-PythonAtLibrary-GGG-Teil1-Entwurf.py: 2024-01-PythonAtLibrary-GGG-Teil1-Entwurf.ipynb
	jupyter-nbconvert 2024-01-PythonAtLibrary-GGG-Teil1-Entwurf.ipynb --to script

qc_code.png:
	qrencode -o qc_code.png https://github.com/Accio/2024-01-GGG-PythonAtLibrary
