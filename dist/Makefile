GAME_NAME = DEADBOLT
ARCHIVE_NAME = Українізатор\ $(GAME_NAME)

TRANSLATED = ../translated
STAGES 	= $(wildcard $(TRANSLATED)/stages/*.nc)
DIALOGS = $(wildcard $(TRANSLATED)/dialogs/*.json)
UNX_FILES = $(TRANSLATED)/game.unx
WIN_FILES = $(TRANSLATED)/data.win

UNX_BUILD = ./build/unx
WIN_BUILD = ./build/win

all: win unx

win: $(ARCHIVE_NAME)-Windows.zip

unx: $(ARCHIVE_NAME)-Linux.zip

$(ARCHIVE_NAME)-Linux.zip: $(UNX_FILES) $(DIALOGS) $(STAGES)
	mkdir -p $(UNX_BUILD)/assets/stages/

	for file in $(STAGES);    do cp "$$file" $(UNX_BUILD)/assets/stages/; done
	for file in $(DIALOGS);   do cp "$$file" $(UNX_BUILD)/assets/       ; done
	for file in $(UNX_FILES); do cp "$$file" $(UNX_BUILD)/assets/       ; done

	cd $(UNX_BUILD) && zip -r "$$OLDPWD/$@" .

$(ARCHIVE_NAME)-Windows.zip: $(WIN_FILES) $(DIALOGS) $(STAGES)
	mkdir -p $(WIN_BUILD)/Stages

	for file in $(STAGES);    do cp "$$file" $(WIN_BUILD)/Stages/       ; done
	for file in $(DIALOGS);   do cp "$$file" $(WIN_BUILD)/              ; done
	for file in $(WIN_FILES); do cp "$$file" $(WIN_BUILD)/              ; done

	cd $(WIN_BUILD) && zip -r "$$OLDPWD/$@" .

.IGNORE: clean
.PHONY:  clean
clean:
	rm -r $(UNX_BUILD) $(WIN_BUILD)
	rm "$(ARCHIVE_NAME)-Windows.zip"
	rm "$(ARCHIVE_NAME)-Linux.zip"
