# bond_screen

See the bond_screen_v3.ipynb Jupyter Notebook file for the walktrhough.

Attempt to run a simple linear regression on a population of bonds downloaded from [Capital IQ](https://www.capitaliq.com/) to detect outliers and screen for relative value opportunities to identify where to focus a deeper dive work.

The Excel files contain ~70 columns, containing bond-specific descriptive fields, such as coupon, maturity, covenants, etc., as well as company fundamental metrics, such as Net Debt/EBITDA, EV/EBITDA, EBITDA margin, Debt/Capital ratio, etc. The files need to be combined in a Pandas dataframe, which will be cleaned up and used to run a multiple linear regression on the data, targeting YTW as an independent variable. This is just a proof of concept - eventually the independent variable should be either spread-to-worst or option-adjusted-spread.
