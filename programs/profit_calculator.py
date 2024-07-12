#this program is to find the gst and profit amount of your selling and cost price
sp = eval(input('Enter the selling price of your product = '))
cp = eval(input('Enter the cost price of your product = '))
app_gst = eval(input('Enter the gst bracket = '))

app_gst = app_gst / 100

gstsp = sp * app_gst
gstcp = cp * app_gst

totalsp = gstsp + sp
totalcp = gstcp + cp

profit = totalsp - totalcp

print('The profit earned after gst is =', format(profit, ".2f"))