# Lecture Notes
NotesDir := LectureNotes
vpath ch%.pdf $(NotesDir)
vpath ch%.lyx $(NotesDir)
vpath _main.pdf $(NotesDir)
vpath _main.lyx $(NotesDir)
vpath ch%.py $(NotesDir)/Python

ChapterLyx = $(shell ls $(NotesDir)/ch*.lyx)
ChapterPdf = $(notdir $(ChapterLyx:.lyx=.pdf))

# Lecture Slides
SlidesDir := LectureSlides
vpath week%.pdf $(SlidesDir)
vpath week%.lyx $(SlidesDir)
vpath week%.py $(SlidesDir)/Python

SlidesLyx = $(shell ls $(SlidesDir)/week*.lyx)
SlidesPdf = $(notdir $(SlidesLyx:.lyx=.pdf))

# Jupyter Notebooks
JupyterDir := Jupyter
vpath %.ipynb $(JupyterDir)

Nb4Book = $(notdir $(shell ls $(JupyterDir)/ch*.ipynb))
Nb4Slides = $(notdir $(shell ls $(JupyterDir)/week*.ipynb))

Py4Book = $(notdir $(Nb4Book:.ipynb=.py))
Py4Slides = $(notdir $(Nb4Slides:.ipynb=.py))
CONFIG := $(JupyterDir)/cfg.py

# LaTeX and LyX
vpath %.tex $(NotesDir)/Include
LYX := /Applications/LyX.app/Contents/MacOS/lyx

# Rules

.PHONY: all
all: chapters slides

.PHONY: clean
clean:
	rm -f $(NotesDir)/*.lyx~
	rm -f $(SlidesDir)/*.lyx~

python: $(Py4Book) $(Py4Slides)
chapters: $(ChapterPdf)
slides: $(SlidesPdf)

book: _main.lyx 
	$(LYX) --export pdf3 $<

ch%.pdf: ch%.lyx ch%.py
	$(LYX) --export pdf3 $<
	
week%.pdf: week%.lyx week%.py
	$(LYX) --export pdf3 $<

week%.py: week%.ipynb $(CONFIG)
	jupyter nbconvert $< --to script --config $(CONFIG) --output-dir $(SlidesDir)/Python

ch%.py: ch%.ipynb $(CONFIG)
	jupyter nbconvert $< --to script --config $(CONFIG) --output-dir $(NotesDir)/Python
	

