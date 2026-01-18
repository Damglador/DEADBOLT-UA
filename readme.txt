
Щоб інтегрувати переклад у гру:
- Взяти game.unx або data.win
- Відкрити їх у UndertaleModTool
- Експортувати всі рядки як JSON
  - Зберегти до ./source/strings/strings-(win/unx).json
- Переконатися що у translated/translations.json всі рядки правильні
- Запустити apply-translations.py
- Імпортувати вивід у ./translated/strings/strings-(win/unx).json у UndertaleModTool
- Імпортувати шрифти з ./assets/fonts
- У Embedded textures замість Texture 0 та Texture 1 імпортувати свої текстурки
