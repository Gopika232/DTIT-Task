
import pandas as pd

df = pd.read_csv("data.csv")

result = df[df["Age"] > 22]

print(result)

####        OUTPUT   #####

#    ID       Name  Age Department  Salary         City
# 0   1       John   25         IT   50000      Chennai
# 1   2      Alice   28         HR   45000   Coimbatore
# 3   4       Emma   30    Finance   60000        Salem
# 4   5      David   27         IT   52000       Trichy
# 5   6     Sophia   24         HR   48000        Erode
# 6   7    Michael   35    Finance   75000      Vellore
# 7   8     Olivia   29         IT   65000      Chennai
# 8   9      James   23  Marketing   40000  Tirunelveli
# 9  10  Charlotte   26  Marketing   47000    Thanjavur