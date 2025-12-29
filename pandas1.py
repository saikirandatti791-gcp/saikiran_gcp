

'''import pandas as pd

rr = {
    "c_name": ["wipro", "tcs", "amazon"],
    "salary": [20000, 25000, 30000],
    "experience": [2, 3, 4],
    "dept": ["it", "manager", "hr"]
}

t = pd.DataFrame(rr)

# Correct update using loc
t.loc[1, "salary"] = 30000
print(t)

# Correct update using iloc
t.iloc[0, 1] = 30000
print(t)

# Update department
t.loc[1, "dept"] = "python developer"
print(t)
t.loc[1]=["google",50000,6,"gcp data engineer"]
print(t)

t.loc[0,"c_name"]="geos"
print(t)
t["bonus"]=3000
print(t)
t.iloc[1,4]=4000
print(t)
t.iloc[2,4]=5000
print(t)
t["commision"]=t["salary"]+t["bonus"]
print(t)
row=t.loc[0]
print(row)
row=t.iloc[0]
print(row)
row=t[t["c_name"]=="geos"]
print(row)
new_row={"c_name":"tech1","salary":45000,"experience":5,"dept":"tester","bonus":6000,"commision":55000}
new_row_df=pd.DataFrame([new_row])
print(new_row_df)
t=pd.concat([t,new_row_df],ignore_index=True)
print(


import pandas as pd
ss={
    "name":["sk","sp","ps","pp","sg"],
    "s_no":[1,2,3,4,5],
    "area":["jntu","kphb","gacchibowli","srnagar","charminar"],
    "salary":[25000,35000,45000,55000,65000],
    "country":["uk","america","india","nepal","srilanka"]
}
df=pd.DataFrame(ss)
print(df)
new_row={
    "name":"jon","s_no":6,"area":"eluru","salary":75000,"country":"north_amec"
}
new_row_df=pd.DataFrame([new_row])
print(new_row_df)
t=pd.concat([df,new_row_df],ignore_index=True)
print(t)
t["bonus"]=3000
print(t)
t["new_sal"]=t["salary"]+t["bonus"]
print(t)
row=t[t["name"]=="sk"]
print(row)
t["count"]=[5,6,7,8,9,4]
print(t)
t=t[t["count"]==4]
print(t)
print(t)
t.loc[1,"country"]="south_america"
print(t)'''

import pandas as pd

df={
    'emp_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'first_name': ['John', 'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Mason', 'Mia'],
    'last_name': ['Smith', 'Johnson', 'Brown', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin'],
    'department': ['HR', 'Finance', 'IT', 'Sales', 'IT', 'Marketing', 'Finance', 'HR', 'Sales', 'IT'],
    'salary': [55000, 62000, 75000, 58000, 70000, 64000, 68000, 59000,72000,76000]
}

df1=pd.DataFrame(df)
print(df1)

print(df1.head())
print(df1.tail())

print(df1.info())
print(df1.values)
df3=df1.copy()
print(df3)











