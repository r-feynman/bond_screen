import QuantLib as ql
import datetime
 
def to_date_vector(int_arr):
    tmpvec = ql.DateVector()
    i = 0
    for intdate in int_arr:
        intdate = int(int_arr[i])
        tmpvec.append(ql.Date(intdate))
        i = i + 1
    return tmpvec
 
def to_real_vector(real_arr):
    tmpvec = ql.DoubleVector()
    i = 0
    for real in real_arr:
        real = float(real_arr[i])
        tmpvec.append(real)
        i = i + 1
    return tmpvec
 
def pythondate_to_excel_date(pythondate):
    temp = datetime.date(1899, 12, 30)
    delta = pythondate - temp
    intdatetime = int(float(delta.days) + (float(delta.seconds) / 86400))
    return intdatetime

def QLOption(args):
    try:
        calcdate = args[0]
        type = args[1]
        expiry = args[2]
        spot = args[3]
        strike = args[4]
        r = args[5]
        div = args[6]
        expirations = args[7]
        strikes = args[8]
        volMatrix = args[9]
        output = args[10]
 
        todaysDate = ql.Date(calcdate.day,calcdate.month,calcdate.year)
        ql.Settings.instance().evaluationDate = todaysDate
        calendar = ql.TARGET()
        dayCounter = ql.ActualActual()
        settlementDate = todaysDate
        riskFreeRate = ql.FlatForward(settlementDate, r, dayCounter)
 
        expirations = to_date_vector(expirations)
        strikes = to_real_vector(strikes)
 
        # surface
        volatilitySurface = ql.BlackVarianceSurface(todaysDate,calendar, expirations, strikes, volMatrix, dayCounter)
        volatilitySurface.enableExtrapolation()
 
        # option parameters
        expint = ql.Date(int(expiry))
        exercise = ql.EuropeanExercise(expint)
        payoff = ql.PlainVanillaPayoff(type, strike)
 
        # market data
        underlying = ql.SimpleQuote(spot)
        dividendYield = ql.FlatForward(settlementDate, div, dayCounter)
 
        process = ql.GeneralizedBlackScholesProcess(ql.QuoteHandle(underlying),
                                            ql.YieldTermStructureHandle(dividendYield),
                                            ql.YieldTermStructureHandle(riskFreeRate),
                                            ql.BlackVolTermStructureHandle(volatilitySurface))
 
        option = ql.EuropeanOption(payoff,exercise)
 
        engine = ql.AnalyticEuropeanEngine(process)
        
        # method: analytic
        option.setPricingEngine(engine)
 
        if (output == "PREMIUM"):
            value = option.NPV()
        elif (output == "DELTA"):
            value = option.delta()
        elif (output == "GAMMA"):
            value = option.gamma()
        elif (output == "DIVRHO"):
            value = option.dividendRho()
        elif (output == "RHO"):
            value = option.rho()
        elif (output == "VEGA"):
            value = option.vega()
        elif (output == "THETA"):
            value = option.theta()
        elif (output == "DPDSTRIKE"):
            value = option.strikeSensitivity()
        elif (output == "THETADAY"):
            value = option.thetaPerDay()
 
        return value
    except Exception:
        return float('NaN')