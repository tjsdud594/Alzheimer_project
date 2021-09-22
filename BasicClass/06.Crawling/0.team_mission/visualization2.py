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

df = pd.read_excel('./files/youtube_300rank_sub.xlsx')
print(df)

plt.figure(figsize = (30,10))
plt.pie(df['subscriber_sum'], labels=pivot_df['button_sub'], autopct='%1.1f%%')
plt.savefig('./img/save1.png')




