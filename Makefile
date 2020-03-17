NBDIR := Jupyter
OUTDIR := Lecture\ Notes/Python
NOTES := $(wildcard $(NBDIR)/*.ipynb)
NOTES := $(filter-out $(NBDIR)/README.ipynb, $(NOTES))
BASENAMES := $(basename $(notdir $(NOTES)))
SCRNAMES := $(addsuffix .py, $(BASENAMES))
TARGET := $(addprefix $(OUTDIR)/, $(SCRNAMES))
TEMPLATE := Jupyter/simplepython.tpl
all: $(TARGET)
$(OUTDIR)/%.py: $(NBDIR)/%.ipynb $(TEMPLATE)
	jupyter nbconvert $< --to python --template $(TEMPLATE) --output-dir $(OUTDIR)
