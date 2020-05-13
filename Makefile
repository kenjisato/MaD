NBDIR := Jupyter

OUTDIR4SLIDES := Lecture\ Slides/Python
NOTES4SLIDES := $(wildcard $(NBDIR)/week*.ipynb)
BASENAMES4SLIDES := $(basename $(notdir $(NOTES4SLIDES)))
SCRNAMES4SLIDES := $(addsuffix .py, $(BASENAMES4SLIDES))

OUTDIR4TEXT := Lecture\ Notes/Python
NOTES4TEXT := $(wildcard $(NBDIR)/ch*.ipynb)
BASENAMES4TEXT := $(basename $(notdir $(NOTES4TEXT)))
SCRNAMES4TEXT := $(addsuffix .py, $(BASENAMES4TEXT))

TARGET := $(addprefix $(OUTDIR4TEXT)/, $(SCRNAMES4TEXT)) $(addprefix $(OUTDIR4SLIDES)/, $(SCRNAMES4SLIDES)) 
TEMPLATE := $(NBDIR)/simplepython.tpl

all: $(TARGET)

$(OUTDIR4SLIDES)/week%.py: $(NBDIR)/week%.ipynb $(TEMPLATE)
	jupyter nbconvert $< --to python --template $(TEMPLATE) --output-dir $(OUTDIR4SLIDES)

$(OUTDIR4TEXT)/ch%.py: $(NBDIR)/ch%.ipynb $(TEMPLATE)
	jupyter nbconvert $< --to python --template $(TEMPLATE) --output-dir $(OUTDIR4TEXT)
