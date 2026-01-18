all: win unx

win: Українізатор\ DEADBOLT-Windows.zip

unx: Українізатор\ DEADBOLT-Linux.zip

TRANSLATED = ../translated
STAGES 	= $(wildcard $(TRANSLATED)/stages/*.nc)
DIALOGS = $(wildcard $(TRANSLATED)/dialogs/*.json)
UNX_FILES = $(TRANSLATED)/game.unx
WIN_FILES = $(TRANSLATED)/data.win

UNX_BUILD = ./build/unx
WIN_BUILD = ./build/win

Українізатор\ DEADBOLT-Linux.zip: $(UNX_FILES) $(DIALOGS) $(STAGES)
	mkdir -p $(UNX_BUILD)/assets/stages/
	for file in $(STAGES);    do cp "$$file" $(UNX_BUILD)/assets/stages/; done
	for file in $(DIALOGS);   do cp "$$file" $(UNX_BUILD)/assets/       ; done
	for file in $(UNX_FILES); do cp "$$file" $(UNX_BUILD)/assets/       ; done

	cd $(UNX_BUILD) && zip -r "$$OLDPWD/$@" .

Українізатор\ DEADBOLT-Windows.zip: $(WIN_FILES) $(DIALOGS) $(STAGES)
	mkdir -p $(WIN_BUILD)/Stages
	for file in $(STAGES);    do cp "$$file" $(WIN_BUILD)/Stages/       ; done
	for file in $(DIALOGS);   do cp "$$file" $(WIN_BUILD)/              ; done
	for file in $(WIN_FILES); do cp "$$file" $(WIN_BUILD)/              ; done

	cd $(WIN_BUILD) && zip -r "$$OLDPWD/$@" .

.IGNORE: clean
.PHONY:  clean
clean:
	rm -r $(UNX_BUILD) $(WIN_BUILD)
	rm "Українізатор DEADBOLT-Windows.zip"
	rm "Українізатор DEADBOLT-Linux.zip"
