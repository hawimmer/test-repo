test-repo
=========

My first Repo!
H. Wimmer

## Excel GUI App

Dieses Repository enthält ein einfaches Beispiel `excel_gui_app.py`, das
mit `tkinter` eine kleine Oberfläche zum Öffnen und Speichern von Excel-Dateien
bereitstellt. Für die Verarbeitung von Excel-Dateien wird `openpyxl` benötigt.
Installiere die Abhängigkeit z. B. mit:

```bash
pip install openpyxl
```

Starte die Anwendung mit:

```bash
python excel_gui_app.py
```

Nach dem Öffnen einer Excel-Datei wird diese bearbeitet (im Beispiel wird die
Zelle `A1` auf den Wert `"Verarbeitet"` gesetzt) und kann unter einem neuen
Dateinamen gespeichert werden.
