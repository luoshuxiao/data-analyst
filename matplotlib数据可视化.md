# 数据可视化：matplotlib
**matplotlib是用于创建出版质量图表的桌⾯绘图包（主要是2D⽅面）**

注意：matplotlib的通常导包是：import matplotlib.pyplot as plt，在Jupyter中运⾏%matplotlib notebook 或在IPython中运⾏ %matplotlib是将画板后台运行，调用画图函数时自动弹出，如果不设置后台运行，需要用画的图调用show()函数展示画板。

## 1. Figure（画板）和Subplot（子画板）
**matplotlib的图像都在figure对象中，可以通过plt.figure创建一个新的figure对象，但是不能直接通过空的figure画图，必须用add_subplot创建一个或多个subplot才行**

	 matplotlib会在最后⼀个⽤过的subplot（如果没有则创建⼀个）上进⾏绘制：
	 fig = plt.figure()  # 创建画板对象
	 ax1 = fig.add_subplot(2, 2, 1) # 创建2x2个subplot子画板，选中第一个（左上角）
	 # 直方图
	 plt.hist(np.random.randn(100), bins=20, color='k', alpha=0.3) # k表示黑色，alpha表示透视度
	 # 散点图
	 ax2 = fig.add_subplot(2, 2, 2)
	 plt.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
	 # 折线图
	 ax3 = fig.add_subplot(2, 2, 3)
	 plt.plot([1.5, 3.5, -2, 1.6])
	 plt.plot(np.random.randn(50).cumsum(), 'k--') # k--是线型选型黑色实线，k-黑色虚线
## 2. 调整subplot周围间距
	默认情况下，matplotlib会在subplot外围留下⼀定的边距，并在subplot之间留下⼀定的间
	距。间距跟图像的⾼度和宽度有关，如果调整了图像⼤⼩（不管是编程还是⼿⼯），间距也会⾃动调整。利⽤Figure的subplots_adjust⽅法可以修改间距,nrows设置subplot行数，ncols表示subplot列数，sharex、sharey表示subplot都使用相同x/y轴刻度。
	 fig, axes = plt.subplots(2, 3) # 创建新的figure，并返回含有已创建的subplot对象Numpy数组axes
	plt.subplots_adjust(wspace=0, hspace=0) # wspace和hspace⽤于控制宽度和⾼度的百分⽐，可以⽤作subplot之间的间距
	fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

## 3. 设置标题、轴标签、刻度以及刻度标签
	改变x轴刻度，最简单的办法是使⽤set_xticks和set_xticklabels。前者告诉matplotlib要将刻度放在数据范围中的哪些位置，默认情况下，这些位置也就是刻度标签。但我们可以通过
	set_xticklabels将任何其他的值⽤作标签
	 plt.xticks([0, 250, 500, 750, 1000], ['one', 'two', 'three', 'four', 
	'five'], rotation=30, fontsize='small')
	 plt.title('My first matplotlib plot')
	 plt.xlabel('Stages')
## 4， 将图标保存在文件
    plt.savefig('figpath.png', dpi=400, bbox_inches='tight')

## 5.seaborn 绘图
### a. 线型图：Series和DataFrame都有⼀个⽤于⽣成各类图表的plot⽅法。默认情况下，它们所⽣成的是线型图
	 s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 
	10))
	 s.plot()
	Series对象的索引会被传给matplotlib，并⽤以绘制X轴。可以通过use_index=False禁⽤该
	功能。X轴的刻度和界限可以通过xticks和xlim选项进⾏调节，Y轴就⽤yticks和ylim
	DataFrame的plot⽅法会在⼀个subplot中为各列绘制⼀条线，并⾃动创建图例

### b.柱状图
	 plot.bar()和plot.barh()分别绘制⽔平和垂直的柱状图。这时，Series和DataFrame的索引将会被⽤作X（bar纵向图）或Y（barh横向图）刻度
	 fig, axes = plt.subplots(2, 1)
	 data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
	 data.plot.bar(ax=axes[0], color='k', alpha=0.7)
	 data.plot.barh(ax=axes[1], color='k', alpha=0.7)
	 对于DataFrame，柱状图会将每⼀⾏的值分为⼀组，并排显示，每一组有相应列数的柱状图，
     设置stacked=True即可为DataFrame⽣成堆积柱状图，这样每⾏的值就会被堆积在⼀起
     df.plot.barh(stacked=True, alpha=0.5)

     import seaborn as sns
	 sns.barplot(x='tip_pct', y='day', data=tips, orient='h')
	 绘制在柱状图上的⿊线代表95%置信区间
### c.直方图和密度图
	直⽅图（histogram）是⼀种可以对值频率进⾏离散化显示的柱状图。数据点被拆分到离散
	的、间隔均匀的⾯元中，绘制的是各⾯元中数据点的数量
      tips[‘tip_pct’].plot.hist(bins=50)
      tips['tip_pct'].plot.density()
      sns.distplot(values, bins=100, color='k')
### d.点图或散布图
	点图或散布图是观察两个⼀维数据序列之间的关系的有效⼿段
	使⽤seaborn的regplot⽅法，它可以做⼀个散布图，并加上⼀条线性回归的线
	sns.regplot('m1', 'unemp', data=trans_data)
	seaborn提供了⼀个便捷的pairplot函数，它⽀持在对⻆线上放置每个变量的直⽅图或密度估
	计
	 sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})

### e.分面网格
	数据集有额外的分组维度, seaborn有⼀个有⽤的内置函数factorplot，可以简化制作多种分⾯
	图
	 sns.factorplot(x='day', y='tip_pct', hue='time', col='smoker',kind='bar', data=tips[tips.tip_pct < 1])
	除了在分⾯中⽤不同的颜⾊按时间分组，我们还可以通过给每个时间值添加⼀⾏来扩展分⾯⽹
	格
	 sns.factorplot(x='day', y='tip_pct', row='time', col='smoker',kind='bar', data=tips[tips.tip_pct < 1])
	factorplot⽀持其它的绘图类型，例如，盒图（它可以显示中位数，四分位
	数，和异常值）就是⼀个有⽤的可视化类型
	sns.factorplot(x='tip_pct', y='day', kind='box',data=tips[tips.tip_pct < 0.5])