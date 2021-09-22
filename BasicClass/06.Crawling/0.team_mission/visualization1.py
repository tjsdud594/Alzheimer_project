import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform



if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')

df = pd.read_excel('./files/youtube_rank.xlsx')

df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
df['replaced_view(단위:만)'] = df['view'].str.replace('억', '')
df['replaced_view(단위:만)'] = df['replaced_view(단위:만)'].str.replace('만', '')

print(df)
sub_num = ''
def range_sep(num):
    if num >= 10000000:
        sub_num = 'diamond button'
    elif num >= 500000:
        sub_num = 'gold button'
    elif num >= 100000:
        sub_num = 'silver button'
    else :
        sub_num = 'under_silver'
    return sub_num

df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
df['replaced_view(단위:만)'] = df['replaced_view(단위:만)'].astype('int')
df['button_sub'] = df['replaced_subscriber'].apply(range_sep) 
pivot_df = df.pivot_table(index = 'button_sub', values = 'replaced_subscriber', aggfunc = ['sum','count'])
pivot_df.columns = ['subscriber_sum', 'category_count']
pivot_df = pivot_df.reset_index()

pivot_df2 = df.pivot_table(index = 'button_sub', values = 'replaced_view(단위:만)', aggfunc=['sum','mean'])
pivot_df2.columns = ['view_sum', 'view_mean']
pivot_df2 = pivot_df2.reset_index()

print(pivot_df)
print(pivot_df2)

plt.figure(figsize = (30,10))
plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['button_sub'], autopct='%1.1f%%')
plt.savefig('./img/save1.png')

plt.figure(figsize = (30,10))
plt.pie(pivot_df2['view_sum'], labels=pivot_df['button_sub'], autopct='%1.1f%%')
plt.savefig('./img/save2.png')