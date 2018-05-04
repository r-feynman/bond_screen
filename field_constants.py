import pandas as pd

def get_fields(df):
   
   numeric_fields = ['Coupon Rate (%)', 'Offering Amount ($USDmm, Historical rate)', "Amount Outstanding ($USDmm, Today's rate)", 'Yield to Worst (%) [Latest]',
                     'Duration [Latest]', 'Net Debt/EBITDA [LTM] [Issuer]', 'Net Debt/(EBITDA-CAPEX) [LTM] [Issuer]', 'Next Call Price', 'No of Analysts (Latest) [Issuer]',
                     'No of Analysts (Latest) [Ultimate Parent]', '% Price Change (%) [3 Months]', 'Price [Latest]', 'Amount Outstanding ($USDmm, Historical rate)',
                     'Offering Price ($USD, Historical rate)', 'Offering Yield (%)', 'Principal Amount ($USD, Historical rate)', 'Benchmark Spread (bps)', 'Gross Spread (bps)',
                     'Convexity [Latest]', 'Conversion Price ($)', 'Conversion Security Price ($)', 'Conversion Premium', 'EBITDA Margin % [LTM] [Issuer]', 'EBITDA Margin % [LTM] [Ultimate Parent]',
                     'Total Debt/Capital % [Latest Quarter] [Issuer]', 'Total Debt/Capital % [Latest Quarter] [Ultimate Parent]', 'EBITDA [LTM] ($USDmm, Historical rate) [Issuer]',
                     'EBITDA [LTM] ($USDmm, Historical rate) [Ultimate Parent]', 'Total Enterprise Value [My Setting] [Latest] ($USDmm, Historical rate) [Issuer]',
                     'Total Enterprise Value [My Setting] [Latest] ($USDmm, Historical rate) [Ultimate Parent]', 'Est. Annual Revenue Growth - 2 Yr % - Capital IQ [Latest] [Issuer]',
                     'Est. Annual Revenue Growth - 2 Yr % - Capital IQ [Latest] [Ultimate Parent]', 'EBITDA - Capital IQ [NTM] ($USDmm, Historical rate) [Issuer]',
                     'EBITDA - Capital IQ [NTM] ($USDmm, Historical rate) [Ultimate Parent]', 'Est. Annual EBITDA Growth - 2 Yr % - Capital IQ [Latest] [Issuer]',
                     'Est. Annual EBITDA Growth - 2 Yr % - Capital IQ [Latest] [Ultimate Parent]', 'EBITDA, 1 Yr Growth % [LTM] (%) [Issuer]', 'EBITDA, 1 Yr Growth % [LTM] (%) [Ultimate Parent]',
                     'Net Debt [Latest Quarter] ($USDmm, Historical rate) [Issuer]', 'Net Debt [Latest Quarter] ($USDmm, Historical rate) [Ultimate Parent]']
   
   column_names = list(df.columns)
   
   short_column_names = ['Maturity Date',
                        'Issuer',
                        'Exchange:Ticker',
                        'Security Type',
                        'Seniority',
                        'Coupon',
                        'Coupon Type',
                        'Offering Date',
                        'Offering Amount',
                        "Amount Outstanding",
                        'Rating (Local Currency)',
                        'Rating Date (Local Currency)',
                        'Parent Name',
                        'YTW',
                        'Duration',
                        'Net Debt/EBITDA',
                        'Net Debt/(EBITDA-CAPEX)',
                        'Next Call Date',
                        'Next Call Price',
                        'Industry Classifications',
                        'Sector',
                        'Sector (Parent)',
                        'No of Analysts',
                        'No of Analysts (Parent)',
                        'Price Change (3m %)',
                        'Price',
                        'Country (Issuer)',
                        'Country (Parent)',
                        'Amount Outstanding ($USDmm, Historical rate)',
                        'Rating (Foreign Currency)',
                        'Rating Date (Foreign Currency)',
                        'Security ID',
                        'Offering Price',
                        'Offering Yield',
                        'Principal Amount',
                        'Spread',
                        'Gross Spread',
                        'Payment Frequency',
                        'Evaluation Date',
                        'Convexity',
                        'Conversion Security',
                        'Conversion Price',
                        'Conversion Security Price',
                        'Conversion Premium',
                        'Bondholder Protective',
                        'Issuer Restrictive',
                        'Subsidiary Restrictive',
                        'EBITDA Margin',
                        'EBITDA Margin (Parent)',
                        'Security Tickers (Issuer)',
                        'Security Tickers (Parent)',
                        'Country of Incorporation',
                        'Total Debt/Capital',
                        'Total Debt/Capital (Parent)',
                        'EBITDA',
                        'EBITDA (Parent)',
                        'EV',
                        'EV (Parent)',
                        'Currency',
                        'Primary Industry',
                        '2y Fwd Revenue Growth',
                        '2y Fwd Revenue Growth (Parent)',
                        'NTM EBITDA',
                        'NTM EBITDA (Parent)',
                        '2y FWD EBITDA Growth',
                        '2y FWD EBITDA Growth (Parent)',
                        'LTM EBITDA Growth',
                        'LTM EBITDA Growth (Parent)',
                        'Net Debt',
                        'Net Debt (Parent)',
                        'Excel Company ID']

   column_mapping = dict(zip(column_names, short_column_names))

   bond_id_columns = ['Maturity Date', 'Issuer', 'Security Type','Seniority','Coupon','Coupon Type','Offering Date','Offering Amount','Country of Incorporation']

   ratings_sorted = ['AAA', 'AA+', 'AA', 'AA-', 'A+', 'A', 'A-', 'BBB+', 'BBB', 'BBB-', 'BB+', 'BB', 'BB-', 'B+', 'B', 'B-', 'CCC+', 'CCC', 'CCC-', 'CC+', 'CC', 'CC-', 'CCD', 'D', 'NR', '-', '']

   numeric_fields_mapped = [column_mapping[field] for field in numeric_fields]

   group_categories = ['Bond ID', 'Pricing', 'Financials', 'Other']

   sorted_results_mapping = {
       'Bond ID':
       [
       'Exchange:Ticker',
       'Security ID',
       'Evaluation Date',
       'Issuer',
       'Parent Name',
       'Maturity Date',
       'Years to Maturity',
       'Coupon',
       'Coupon Type',
       'Security Type',
       'Seniority',
       'Amount Outstanding',
       'Currency',
       'Rating',
       'Next Call Date',
       'Years to Next Call',
       'Next Call Price',
       'Sector',
       'Sector (Parent)',
       'Country (Issuer)',
       'Country (Parent)',
       'Primary Industry',
       ],
       'Pricing':
       [
       'YTW',
       'Price',
       'Price Change (3m %)',
       'Call Premium',
       'Spread',
       'Duration',
       'Convexity',
       ],
       'Financials':
       [
       'Net Debt/EBITDA',
       'Net Debt/(EBITDA-CAPEX)',
       'Net Debt/EBITDA Fwd (Parent)',
       'Total Debt/Capital',
       'Total Debt/Capital (Parent)',
       'EBITDA Margin',
       'EBITDA Margin (Parent)',
       'EV/EBITDA Fwd (Parent)',
       'LTM EBITDA Growth',
       'LTM EBITDA Growth (Parent)',
       '2y Fwd Revenue Growth',
       '2y Fwd Revenue Growth (Parent)',
       '2y FWD EBITDA Growth',
       '2y FWD EBITDA Growth (Parent)',
       'EBITDA',
       'EBITDA (Parent)',
       'NTM EBITDA',
       'NTM EBITDA (Parent)',
       'EV',
       'EV (Parent)',
       'Net Debt',
       'Net Debt (Parent)',
       ],
       'Other':
       [
       'Conversion Security',
       'Conversion Price',
       'Conversion Security Price',
       'Conversion Premium',
       'Industry Classifications',
       'Bondholder Protective',
       'Issuer Restrictive',
       'Subsidiary Restrictive',    
       'No of Analysts',
       'No of Analysts (Parent)',
       'Excel Company ID',
       'YTW_predicted',
       'YTW_diff',
       'Leverage'
       ]
   }

   sorted_results_columns = [y for x in [sorted_results_mapping[grp] for grp in group_categories] for y in x]

   return numeric_fields, short_column_names, column_mapping, bond_id_columns, \
          ratings_sorted, numeric_fields_mapped, group_categories, \
          sorted_results_mapping, sorted_results_columns