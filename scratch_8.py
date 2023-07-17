import pd as pandas

data = pd.read_csv(r'C:\Users\Dhanashree Phadke\Documents\Downloads\Placement_Data_Full_Class (1).csv')
print(data)

conditions =[(data['ssc_p']>75)&(data['hsc_p']>70)]
result = ['below average']
data['RESULT-A'] = np.select(conditions,result)

conditions1 = [(data['degree_p']>60)]
result1 = ['average']
data['RESULT-B'] = np.select(conditions1,result1)

conditions2 = [(data['RESULT-A']=='below average')&(data['RESULT-B']=='average')]
result2 = ['above average']
data['RESULT'] = np.select(conditions2,result2)

conditions3 = [(data['status']=='Placed')]
result3 = ['congrats']
data['DISPLAY STATUS'] = np.select(conditions3,result3)

print(data)


