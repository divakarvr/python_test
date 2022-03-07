import time
ct= time.time()
totalsec= int(ct)
cs= totalsec % 60
ttm = totalsec // 60
cm = ttm % 60
th = ttm // 60
ch = th % 24
print("Current time is", ch, ":",
 cm, ":", cs, "GMT")
