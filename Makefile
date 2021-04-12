# Prefices
ch := ch
sld := sld

# Destination Directories
book := Book
vpath $(ch)%.pdf $(book)
vpath all.pdf $(book)

slides := Slides
vpath $(sld)%.pdf $(slides)

# Source Directories
lyx := Manuscripts
vpath all.lyx $(lyx)
vpath $(ch)%.lyx $(lyx)
vpath $(sld)%.lyx $(lyx)

inc := $(lyx)/Include
vpath %.tex $(inc)
vpath %.sty $(inc)

refs := $(lyx)/References
vpath %.bib $(refs)

python := $(lyx)/Python
vpath $(ch)%.py $(python)
vpath $(sld)%.py $(python)

jupyter := $(lyx)/Jupyter
vpath $(ch)%.ipynb $(jupyter)
vpath $(sld)%.ipynb $(jupyter)
CONFIG := $(jupyter)/cfg.py

diagrams := $(lyx)/Diagrams
vpath %.drawio $(diagrams)

figures := $(lyx)/Figures
images := $(lyx)/Images
knitr := $(lyx)/Knitr


# Lists of manuscripts and outputs
chapter_lyx = $(notdir $(wildcard $(lyx)/$(ch)*.lyx))
chapter_pdf = $(addprefix $(book)/,$(chapter_lyx:.lyx=.pdf))
slides_lyx = $(notdir $(wildcard $(lyx)/$(sld)*.lyx))
slides_pdf = $(addprefix $(slides)/,$(slides_lyx:.lyx=.pdf))
chapter_ipynb = $(notdir $(wildcard $(jupyter)/$(ch)*.ipynb))
chapter_py = $(chapter_ipynb:.ipynb=.py)
slides_ipynb = $(notdir $(wildcard $(jupyter)/$(sld)*.ipynb))
slides_py = $(slides_ipynb:.ipynb=.py)

aux = $(wildcard $(refs)/*.bib $(knitr)/* $(inc)/*)
ch_only_aux = $(wildcard $(refs)/$(ch)*.bib $(knitr)/$(ch)* $(inc)/$(ch)*)
sld_only_aux = $(wildcard $(refs)/$(sld)*.bib $(knitr)/$(sld)* $(inc)/$(sld)*)
chapter_aux = $(filter-out $(sld_only_aux),$(aux))
slides_aux = $(filter-out $(ch_only_aux),$(aux))

dia_drawio = $(wildcard $(diagrams)/*.drawio)
dia_pdf = $(dia_drawio:.drawio=.pdf)
img_ext = $(wildcard $(images)/*)

# LyX app
lyxapp := $(shell if type lyx >/dev/null 2>&1; then echo lyx; fi)
ifeq ($(lyxapp),)
	lyxapp := /Applications/LyX.app/Contents/MacOS/lyx
endif
lyxapp.opts := --export-to pdf5

# draw.io app
drawio := $(shell if type drawio >/dev/null 2>&1; then echo drawio; fi)
ifeq ($(drawio),)
	drawio := /Applications/draw.io.app/Contents/MacOS/draw.io
endif
drawio.opts := -x -f pdf --crop

# Rules

.PHONY: all
all:
	@echo Compilation takes very long time. What do you want to do?
	@echo ------------------------------------------------------
	@echo make book			: Compile the complete book.
	@echo make chapters	: Compile all chapters separately.
	@echo make slides		: Compile all slides.
	@echo make full			: Do all the above.
	@echo make ch02			: Compile Chapter 2, etc.
	@echo make week02		: Compile slides for Week 2, etc.
	@echo ------------------------------------------------------
	@echo make clean				: Remove .lyx~ files.
	@echo make clean-cache	: Remove knitr cache.
	@echo make clean-all		: Do the above two.
	@echo make destlean			: Remove PDF files.

# Compilation.
.SECONDEXPANSION:

full: book chapters

book all.pdf: $(book)/all.pdf;
$(book)/all.pdf: all.lyx $(chapter_aux) $(chapter_py) diagrams $(img_ext)
	$(lyxapp) $(lyxapp.opts) $@ $<

chapters: $(chapter_pdf);
$(ch)%: $(book)/$(ch)%.pdf;
$(book)/$(ch)%.pdf: $(ch)%.lyx $(chapter_aux) \
		$$(subst .ipynb,.py,$$(filter $$(notdir $$(wildcard $(jupyter)/$(ch)$$**.ipynb)),$(chapter_ipynb))) \
		$$(subst .drawio,.pdf,$$(filter $$(wildcard $(diagrams)/$(ch)$$**.drawio),$(dia_drawio))) \
		$$(filter $$(wildcard $(imgages)/$(ch)$$**.*),$(img_ext))
	$(lyxapp) $(lyxapp.opts) $@ $<

slides: $(slides_pdf);
$(sld)%: $(slides)/$(sld)%.pdf;
$(slides)/$(sld)%.pdf: $(sld)%.lyx $(slides_aux) \
		$$(subst .ipynb,.py,$$(filter $$(notdir $$(wildcard $(jupyter)/$(sld)$$**.ipynb)),$(slides_ipynb))) \
		$$(subst .drawio,.pdf,$$(filter $$(wildcard $(diagrams)/$(sld)$$**.drawio),$(dia_drawio))) \
		$$(filter $$(wildcard $(imgages)/$(sld)$$**.*),$(img_ext))
	$(lyxapp) $(lyxapp.opts) $@ $<

# Jupyter to PYTHON
nbconvert: $(chapter_py) $(slides_py);

$(chapter_py) $(slides_py): %.py: %.ipynb $(CONFIG)
	jupyter nbconvert $< --to script --config $(CONFIG) --output-dir $(python)

# Draw.io diagrams
diagrams: $(dia_pdf);
$(diagrams)/%.pdf: %.drawio
	$(drawio) $(drawio.opts) $<

# Cleaning.

.PHONY: clean-all
clean-all: clean clean-cache destclean

.PHONY: clean
clean:
	rm -rf .ipynb_checkpoints
	rm -f $(lyx)/*.lyx~
	find . -type f -name '.DS_Store' -delete

.PHONY: clean-cache
clean-cache:
	rm -rf $(lyx)/cache
	rm -rf $(python)/__pycache__

.PHONY: destclean
destclean:
	rm $(book)/*.pdf
	rm $(slides)/*.pdf
	rm $(diagrams)/*.pdf
	rm -rf $(python)/*
	rm -rf $(figures)/*
