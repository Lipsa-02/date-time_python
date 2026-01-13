#two days difference in string format
from datetime import datetime
dts1="2025/04/23"
dts2="2026-01-14"
dtsstr1= datetime.strptime(dts1,"%Y/%m/%d")
dtsstr2=datetime.strptime(dts2,"%Y-%m-%d")
dfrnc=dtsstr2-dtsstr1
print("Difference :",dfrnc)
