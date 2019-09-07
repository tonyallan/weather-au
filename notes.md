## Notes to myself

### Manual build and upload

```
cd ~/Documents/GitHub/weather-au
pytest
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```

### Test on repl.it

[https://repl.it/@tony_allan/weather-au](https://repl.it/@tony_allan/weather-au)