import pandas as pd
import glob

path = r'C:\data/names/' 
all_files = glob.glob(os.path.join(path , "/*.csv"))

liste = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    liste.append(df)

frame = pd.concat(liste, axis=0, ignore_index=True)

sutun_isimleri = ['name','sex', 'births','year']

veriseti = pd.DataFrame(data=veri, columns=sutun_isimleri)
print(veriseti)


df.female_name.value_counts()
df.female_name.nunique()

df['male_name'].value_counts().idxmax()
df['male_name'].mode()

df['births'].groupby([df.births.dt.year, df.birthdate.dt.month]).agg('count')

births_male = (df["sex"] == "male")
birth_woman_age = (df["births"] > 30)
birth_rate = birth_woman_age < 35
birth_rate.count()


births_male2 = (df["sex"] == "male")
birth_woman_age2 = (df["births"] > 25)
birth_rate2 = birth_woman_age2 < 30
birth_rate2


df1['diff'] = df1['len(female_name)'] - df1['len(male_name)']
print("\nDifference of female name and male name :\n", df1)


p['age'] = (datetime.date.today() - p['births']) // datetime.timedelta(days=365.25)