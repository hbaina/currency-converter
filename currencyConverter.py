print('========SEE HOW MUCH YOU GET IF YOU SELL OR BUY========')
currencyOption1 = input('Select Your Currency:' 
'\n' '[''NGN, ' 'GBP , ' 'USD , ''EUR ' ']:' )
amount = float(input('Enter Amount To Sell: '))
currencyOption2 = input('Select Currency To Buy:' 
'\n' '[''NGN, ' 'GBP , ' 'USD , ''EUR ' ']:' )
#EXCHAGE RATE CURRENCY TRADING: NGN><USD><GBP><EUR
import currencyConverterModule
if currencyOption1 == 'NGN' and currencyOption2 == 'USD':
    print('=','NGN', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.NGN_USD(amount),'USD')
elif currencyOption1 == 'USD' and currencyOption2 == 'NGN':
    print('=','USD', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.USD_NGN(amount),'NGN')
elif currencyOption1 == 'NGN' and currencyOption2 == 'GBP':
    print('=','NGN', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.NGN_GBP(amount),'GBP')
elif currencyOption1 == 'GBP' and currencyOption2 == 'NGN':
    print('GBP', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.GBP_NGN(amount),'NGN')
elif currencyOption1 == 'NGN' and currencyOption2 == 'EUR' :  
    print('=','NGN','%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.NGN_EUR(amount),'EUR')
elif currencyOption1 == 'EUR' and currencyOption2 == 'NGN':
    print('=','EUR', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.EUR_NGN(amount),'NGN')
elif currencyOption1 == 'USD' and currencyOption2 == 'GBP':
    print('=','USD', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.USD_GBP(amount),'GBP')
elif currencyOption1 == 'GBP' and currencyOption2 == 'USD':
    print('=','GBP', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.GBP_USD(amount),'USD')
elif currencyOption1 == 'USD' and currencyOption2 == 'EUR':
    print('=','USD', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.USD_EUR(amount),'EUR')
elif currencyOption1 == 'EUR' and currencyOption2 == 'USD':
    print('=','EUR','%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.EUR_USD(amount),'USD')
elif currencyOption1 == 'GBP' and currencyOption2 == 'EUR' :  
    print('=','GBP','%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.GBP_EUR(amount),'EUR')
elif currencyOption1 == 'EUR' and currencyOption2 == 'GBP':
    print('=','EUR', '%.2f' % amount, 'buys', '%.2f' % + currencyConverterModule.EUR_GBP(amount),'GBP')

    