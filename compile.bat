#!/usr/bin/env bash

pip install -r src/requirements.txt
pyinstaller --onefile --noconsole src/circuit.py
cp dist/circuit.exe .
rm -rf build/
rm -rf dist/
