# "Budowa i działanie witryn internetowych" - laboratorium 2

## Pobieranie i inicjowanie środowiska:

1. Otwórz okno linii poleceń.
2. Pobierz repozytorium z GitHub'a: `git clone https://github.com/WojciechThomas/bdwi2021-2.git`
3. Wejdź do pobranego folderu: `cd bdwi2021-2`
4. Utwórz wirtualne środowisko Pythona: `python -m venv venv`
5. Aktywuj wirtualne środowisko Pythona (przejrzyj Uwagi poniżej): `.\venv\Scripts\activate.bat`
6. Zaktualizuj instalator pip: `python -m pip install --upgrade pip`
7. Zainstaluj wszystkie potrzebne biblioteki: `pip install -r requirements.txt`

### Uwagi:

- Jeśli używasz systemu MacOS lub Linux w punkcie 5. użyj polecenia `/venv/Scripts/activate`
- Jeśli używasz okna Powershell w systemie Windows:
  - po otwarciu nowego okna uruchom polecenie `Set-ExecutionPolicy RemoteSigned -Scope Process`
  - w punkcie 5. użyj polecenia `.\venv\Scripts\Activate.ps1`
- Nie używaj do pracy z Pythonem okna Git Bash w systemie Windows.

## Uruchamianie aplikacji

Możesz przetestować swoją instalację wpisując: `python app1.py`

Jeśli wszystko jest poprawnie zainstalowane na ekranie powinny pojawić się komunikaty:

```
 * Serving Flask app "app1" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
 
 Po wpisaniu w oknie przeglądarki internetowej podanego adresu (`http://127.0.0.1:5000` lub `http://localhost:5000`) przeglądarka 
 powinna wyświetlić stronę aplikacji Flask. Działanie aplikacji zakończysz naciskając w oknie konsoli `Ctrl-C`.
 
 Powodzenia!

