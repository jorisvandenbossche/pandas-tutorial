# EuroScipy 2015 Pandas Tutorial

This repository contains the material (notebooks, data) for the pandas tutorial at EuroScipy 2015.

## Installation notes

This tutorial requires the following packages:

- Python version 2.6-2.7 or 3.3-3.4
- `pandas` version 0.15.2 or later: http://pandas.pydata.org/
- `numpy` version 1.7 or later: http://www.numpy.org/
- `matplotlib` version 1.3 or later: http://matplotlib.org/
- `ipython` version 3.x with notebook support, or `ipython 4.x` combined with `jupyter`: http://ipython.org
- `seaborn` (this is used for some plotting, but not necessary to follow the tutorial): http://stanford.edu/~mwaskom/software/seaborn/

I recommend to use the [conda](https://store.continuum.io/) environment manager to install all the requirements 
(you can install [miniconda](http://conda.pydata.org/miniconda.html) or install the (very large) Anaconda software
distribution, found at http://continuum.io/downloads).

Once this is installed, the following command will install all required packages in your Python environment:
```
$ conda install numpy pandas scipy matplotlib jupyter seaborn
```

But of course, using another distribution (e.g. Enthought Canopy) or pip is good as well, as long
as you have the above packages installed.


## Downloading the tutorial materials

I would highly recommend using git (not only for this tutorial, but just because it makes your life
easier). Once git is installed, you can get the material in this tutorial by cloning this repo:

    git clone https://github.com/jorisvandenbossche/2015-EuroScipy-pandas-tutorial.git

As an alternative, you can download it as a zip file:
https://github.com/jorisvandenbossche/2015-EuroScipy-pandas-tutorial/archive/master.zip.
I will probably make some changes until the start of the tutorial, so best to download
the latest version then (or do a `git pull` if you are using git).


## Content
