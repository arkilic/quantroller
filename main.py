from quantroller.valar import *
from prettytable import PrettyTable
start_date = '2008-1-1'
equity_symbols = ['SPY', 'AAPL', 'BP']



df = compose_dataframe(equity_symbols)

df_monthly = resample(df=df, samp_type='M')

vis_data(df_monthly, symbol=equity_symbols[2])

# prepare dataset to be fitted
X = sm.add_constant(df_monthly.iloc[:, 2])
y = df_monthly.iloc[:, 0]

# fit the data using OLS
model = fit(X=X, y=y)
print(model.summary())

beta = model.params[equity_symbols[2]]
alpha = model.params["const"]
rsqr = model.rsquared

x = PrettyTable(["beta", "alpha", "rsqr"])
x.add_row([beta, alpha, rsqr])
print(x)
