#!/usr/bin/env python
# coding: utf-8

#---- ch00/versions/noinc
import platform
import numpy
import scipy
import sympy
import pandas
import matplotlib
import statsmodels

#---- ch00/installpdr/dnr
conda install pandas-datareader#---- ch00/pipinstallpdr/dnr
python -m pip install pandas-datareader
#---- ch00/importpdr/noinc
import pandas_datareader


#---- ch00/gentable/noinc
versions = pandas.DataFrame({
    "Version": ([platform.python_version()] + 
                [pkg.__version__ 
                 for pkg in [numpy, scipy, sympy, pandas, 
                             matplotlib, statsmodels,
                             pandas_datareader]])
}, index=["Python", "NumPy", "SciPy", "SymPy", 
          "Pandas", "Matplotlib", "statsmodels", 
          "pandas-datareader"])

versions


#---- ch00/showtable
print(versions.to_latex())




