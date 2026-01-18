import json
import os

target_files = [
  "./source/strings/strings-unx.json",
  "./source/strings/strings-win.json"
]

translations_file = "./translated/translations.json"

with open(translations_file, "r") as file:
  translations = json.load(file)

#print(json.dumps(translations, indent=2, ensure_ascii=False))

for target_file in target_files:
  with open(target_file, "r") as file:
    target = json.load(file)

  for i, string in enumerate(target["Strings"]):
    if string in translations:
      target["Strings"][i] = translations[string]

  with open(f"translated/strings/{os.path.basename(target_file)}", "w", encoding="utf-8") as file:
      json.dump(target, file, ensure_ascii=False, indent=4)
