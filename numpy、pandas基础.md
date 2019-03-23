# 数据分析基础知识点 -- numpy and Pandas 
## 1.numpy: 适合处理统一的数值数组数据 -- numpy.array
## 2. pandas: 专门处理表格和混杂数据设计的 -- pandas.Series/pandas.DataFrame
  **两个主要的数据结构：Series和DataFrame**
### a. Series -- 类似一维数组对象，由一组数据和一组与之相关的数据标签（索引）组成；
	   1)创建Series带有一个可以对各个数据点进行标记的索引，比如下面的对象：
	     obj = pd.Series([1,2,4,5], index=['a','b','c','d'])
	     当然也可以使用默认的数字索引，即0,1,2,3,4...
	       obj['a'] 等同于obj[0]
	   2)Series看成是一个定长的有序的字典对象，可以通过字典直接创建Series对象,
            key为索引，value为数据
	      sdata = {'a':1,'b':2,'c':3}
	      obj1 = pd.Series(sdata)
	   3）通过已有的Series对象，创建新的Series对象
	      obj2 = pd.Series(sdata,index=['a','b','d','g'])
	      原有的索引对应的值复制到新建的对象，原来没有的索引对应的值为NaNt
	      NaN（not a number） -- 表示缺失或者NA值
	   4）Series最重要的一个功能是根据运算的索引自动对齐数据进行运算
	       obj3 = obj1 + obj2  （必须对应位置上两个对象都有值才相加，
                                 其中一个为NaN，结果为NaN）
	       obj3输出为：
		        a  2
				b  4
				c  NaN
				d  NaN
				g  NaN
	    pd.isnull(obj) -- 检测是否缺失数据（每个数据对应返回bool值，缺失则返回True）
	    pd.notnull(obj) -- 检测是否缺失数据（每个数据对应返回bool值，不缺失则返回True）
	    obj.name = 'obj_name' -- 给Series对象的数据name属性赋值
	    obj.index.name = 'index_name' -- 给Series对象的索引的name属性赋值
	    obj.index = ['bob','steve','jeff','ryan'] -- 直接修改索引的名字

### b. DataFrame -- 表格型的数据结构，含有一组有序的列，每一列可以是不同的值类型（数值，字符串，布尔值等等），DataFrame既有行索引也有列索引
    生成dataframe对象：
     data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
			 'year': [2000, 2001, 2002, 2001, 2002, 2003],
			 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
	 frame = pd.DataFrame(data)   # 用python数据类型字典生成
		In [46]: frame.head()  # 查看前五个数据
		Out[46]: 
		  pop state year
		0 1.5 Ohio 2000
		1 1.7 Ohio 2001
		2 3.6 Ohio 2002
		3 2.4 Nevada 2001
        4 2.9 Nevada 2002
     # 用已有的dataframe生成
	 frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],    
	 ....:                 index=['one', 'two', 'three', 'four',
	 ....:                 'five', 'six'])
     其中columns表示列索引，index表示行索引
     Index对象是不可变的，因此⽤户不能对其进⾏修改

     frame2.columns         # 获取列索引（类似mysql里面的字段名）
     frame2['state']        #  获取某一列的值  （值的类型是Series）
     frame2.year            # 获取year那一列  （值的类型是Series）
     frame2.loc['three']    # 获取行索引名是three的那一行  （这个行索引是用户自定义的）
     frame2.iloc[0]         # 通过下标索引获取下标为0的那一行（这个下标是pandas默认的行索引）
     frame2['debt'] = 16.5  # 将debt那一列所有的值赋为16.5
     del frame2['eastern']  # 删除eastern这一列
     frame3.T               # 转置 （交换行和列）

    其中： iloc表示自带的下标行索引，loc表示index行索引名索引，这两种索引Series和DataFrame都
          能用，但是直接通过索引名索引只对Series有效（obj['b']与obj.loc['b']等同），
          DateFrame只能用obj.loc['b'],不能直接用obj['b']


    如果嵌套字典传给DataFrame，pandas就会被解释为：外层字典的键作为列，内层键则作为⾏索引：
	In [65]: pop = {'Nevada': {2001: 2.4, 2002: 2.9},
	....: 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
	In [66]: frame3 = pd.DataFrame(pop)
	In [67]: frame3
	Out[67]: 
	  Nevada Ohio
	2000 NaN 1.5
	2001 2.4 1.7
	2002 2.9 3.6

    pandas对象的⼀个重要⽅法是reindex，其作⽤是创建⼀个新对象，它的数据符合新的行索引或者列索引。
    只能生成新的对象，不会改变原来对象的index，因为index是不可变得

       obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])  # 行索引顺序是dbac
       obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])  # 将行的排列顺序按新的顺序排列,行索引顺序变成abcde
       states = ['Texas', 'Utah', 'California']
       frame.reindex(columns=states)
     data.drop(['Colorado', 'Ohio'])  # 删除行索引为Colorado和Ohio的两行数据（默认行索引）
     data.drop(['two', 'four'], axis='columns')  # 删除列索引为two和four的列所有的值
     data.drop(['two', 'four'], axis=1)   # 删除列索引为two和four的列所有的值
     
     获取行数据：
     obj.take([1,2])        # 获取行索引下标为1和2的行数据
	 obj['b']               # 获取行索引为b的行数据 （Series能用，DataFrame需要用obj.loc['b']）
	 obj[1]                 # 获取下标为1也就是第二行的行数据
	 obj[2:4]               # 获取下标为2到4的行数据（不包含4）
	 obj[['b', 'a', 'd']]   # 获取行索引为b,a,d的行数据
	 obj[[1, 3]]            # 获取下标为1和3的行数据
	 obj[obj < 2]           # 获取数据小于2的行数据（obj<2结果是逻辑值，bool，再通过逻辑值取行数据）
	 obj['b':'c']           # 获取行索引为b到行索引为c的行数据（与下标不同的是，此方法包括c）

     dataframe 获取行列数据：
     data['b']  # 默认获取列数据
     data.iloc[2, [3, 0, 1]]  # 获取下标为2的行，下标为3，0，1的列的数据
     data.iloc[[1, 2], [3, 0, 1]]  # 获取下标为1，2的行，下标为3，0，1的列的数据
     data.loc['Colorado', ['two', 'three']] # 获取索引名为Colorado的行，索引名为two，three的列的数据
     data.iloc[:, :3]  # 获取所有行，列从下标0到3的数据（不包含3）

     算数运算：
     不管是Series还是DataFrame，在进行算术运算时，都会进行数据对齐，对应的数据进行算术运算，对应位置其中一个
     数据没有或者为空，结果也会为空（NaN）
     
      
     df1.add(df2, fill_value=0)  # 将df1和df2数据相加，df1中的数据把df2中有df1中没有的合并到df2中，
                                     df1中对应位置没有数据的地方用0表示
     frame.sub(series3, axis='index')  # frame - series3 ,以行的index对应每一列对应数据相减
     np.abs(frame)  # 对frame每一个数据取绝对值

     f = lambda x: x.max() - x.min()  
     obj.apply(f)   # 将f函数映射到obj的每一行（得出列索引对应的每一列中行最大值减去行最小值的值）
     obj.apply(f, axis='columns')  # 将f函数映射到obj每一列
     
     obj.sort_index()  # 根据行索引排序
     obj.sort_index(axis=1) # 根据列索引排序
     obj.sort_index(axis=1, ascending=False) # 降序排列
     obj.sort_values()  # 按Series的值进行排序（当其中有NaN时，不管升序降序，空值都会放在最后）
     obj.sort_values(by='b') # 按照columns索引名为b的列的值大小来对行进行重新排序（默认升序）
     obj.sort_values(by=['a', 'b'])  # 先按照columns索引名为a的排序，拍完过后有相同的值，对相同的值在用b排序
     obj.rank()  # 对obj中的元素进行排名，按行排名，输出排名数据
     obj.rank(axis='columns') # 每一行按列进行排名，输出排名的数据
     obj.index.is_unique  # 判断行索引是否具有唯一性 （有重复的返回False,没有就返回True）
     obj.sum()  # 对每一列，求所有行的和，输出一个索引是列，值是和的Series数据结构
     obj.sum(axis=1)或者obj.sum(axis='columns')  # 对每一行，求所有列的和
     obj.mean()  # 求平均（传入参数也可以求行平均）
     obj.unique()  # 对Series进行去重处理，返回一个没有重复值的新的Series
     obj.value_counts()  # 计算各个值出现的频率（Series）
     obj.isin(['b', 'c']) # 判断Series每个值是不是在传入的参数集合当中（返回一个是bool值的Series）
     pd.isnull(obj)  # 判断obj中所有数据是否是空（返回一个逻辑DataFrame）
     data.apply(pd.value_counts).fillna(0) # 输出dataframe中每个值在每一列中出现的次数，data的
                                            列索引不变，行索引是去重后的数据值
### c. 从文件中读取数据
  读取文件的函数：read_csv/read_table/read_json/read_html/read_excel等等，大部分函数的参数都很多， read_csv的参数超过50个(下面代码为一部分参数的作用)

	   df = pd.read_csv('examples/ex1.csv')  
	   df = pd.read_csv('examples/ex2.csv', header=None) # 不加文件中自带的列索引
	   df = pd.read_table('examples/ex1.csv', sep=',') # sep是指定数据分隔符
	   df = pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])  # 将names作为列索引
	   df = pd.read_csv('examples/ex2.csv', names=['a','b','message'], index_col='message')  # 将某一列的值作为行索引
	   df = pd.read_csv('examples/csv_mindex.csv',index_col=['key1', 'key2']) # 将key1的值作为外层行索引，key2的值作为内层行索引
	   result = pd.read_table('examples/ex3.txt', sep='\s+') # 有些文件是很多空格或者其他字符分隔符，可以传入正则表达式去匹配分隔符
	   df = pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3]) # 忽略掉第一行，第三行，第四行，也就是说不读取这些行的值
	   
	   df = sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
	   df = pd.read_csv('examples/ex5.csv', na_values=sentinels)  # 将message列下的所有foo,NA变为NaN，something下的two变为NaN
	   df =  pd.read_csv('examples/ex6.csv', nrows=5) # 只读取前五行数据
	   chunker = pd.read_csv('examples/ex6.csv', chunksize=1000) # 逐块读取（每一块1000行数据），结果是一个迭代对象，可遍历
       data = pd.read_json('examples/example.json') # 将特定格式的json读取出来
       tables = pd.read_html('examples/fdic_failed_bank_list.html') # 基于lxml和beatifulsoup读取网页中的表格，转为dataframe(网页可以是在线的也可以是本地的)
       pd.read_pickle('examples/frame_pickle') # 读取二进制文件，转为dataframe
       frame = pd.read_excel('examples/ex1.xlsx', 'Sheet1') # 读取Microsoft Excel⽂件
### d. 将DataFrame数据存入文件中（空值默认是空字符串，数据间默认分隔符为逗号，行列索引默认一起写入）
	  sys.stdout标准输出 -- 表示输出在显示屏上
	  data.to_csv('examples/out.csv') # 将data写入到参数中的路径文件中
	  data.to_csv(sys.stdout, sep='|') # 将data输出到显示屏，以 | 分隔数据
	  data.to_csv(sys.stdout, na_rep='NULL') # 将data输出到显示屏，空值用NULL代替
	  data.to_csv(sys.stdout, index=False, header=False) # 去掉行和列索引
	  data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c']) # 指定列的顺序
	  data.to_json() # 输出json数据 
	  data.to_pickle('examples/frame_pickle') # 将data以二进制存入磁盘文件
	  data.to_excel('examples/ex2.xlsx') # 将data写⼊为Excel格式

### e. 与数据库的交互
	 从数据库读取数据转为dataframe：
	   import sqlalchemy as sqla
	   db= sqla.create_engine('mysql+pymysql://root:123456@127.0.0.1/taobao?charset=utf8')
	   pd.read_sql('select * from product', db)
	 将dataframe数据写入数据库：
		connect_db = create_engine('mysql+pymysql://root:123456@127.0.0.1/movie_db?charset=utf8')
          上句代码是连接mysql数据库，用户是root,密码是123456，本地连接，数据库名叫movie_db
		data.to_sql('rating', connect_db, if_exists='append', index=False)
          上句代码中rating是写入movie_db的rating表，append表示将数据添加在表后面，index=False表示不将行索引写入
        注意：如果用if_exists = 'replace'，会先删除原表，再创建新表字段，所以新建的数据表与原来不同（字段的数据类型），append参数不会改变原来字段的数据类型，会在原表下添加数据，最好用append，对添加约束外键等操作有利

### f. 数据清理

     删除缺省值数据（空值数据nan）：
		from numpy import nan as NA
		data = pd.Series([1, NA, 3.5, NA, 7])
		data.dropna()   # 默认丢弃掉任何有缺失值的行，等同于： data[data.notnull()]
        data.dropna(how='all') # 将只丢弃全为NA的那些行
        data.dropna(axis=1, how='all') # 只丢弃全为NA的那些列
        data.dropna(thresh=2)  # 保留少于2个NA的行，丢弃大于等于2个NA的行
        df.fillna({1: 0.5, 2: 0})  # 对下标索引为1的列中的NA赋值0.5，下标索引为2的列下的NA赋值0
        df.fillna(0, inplace=True) # 将df中的NA变为0，对df本身进行修改，不产生新的dataframe对象
        df.fillna(method='ffill')  # 将缺省值NA前一行的值填充NA值
        df.fillna(method='ffill', limit=2) # 将缺省值NA前一行的值填充NA值，如果在列方向有连续的NA，只填充两个
    删除重复行：
		 data.duplicated()  # 返回一个逻辑值Series（重复的行值为True，不重复的为False）
		 data.drop_duplicates() # 直接删除重复的行（默认保留第一个出现的行）
         data.drop_duplicates(['k1']) # 将k1列作为去重的判断条件
         data.drop_duplicates(['k1', 'k2'], keep='last') # 将k1/k2作为去重的判断条件，（保留最后一个出现的行）

### g. 用函数或映射进行数据转换

	 data['food'].str.lower() # 将data中的food一列的所有字母转换为小写（str.lower()是Series的方法）
	 data.replace(-999, np.nan)  # 将data中值为-999的数据替换为nan
	 data.replace([-999, -1000], np.nan) # 将data中的-999，-1000都替换为nan
	 data['food'].map(lambda x: meat_to_animal[x.lower()]) # 将data中的food列中的数据都进行lambda函数处理得到一个Series
	 data.index = data.index.map(lambda x: x[:4].upper()) # 将data行索引保留前四个字符并全变成大写字母（生成新的index再替换原来的）
	
	 data.rename(index=str.title, columns=str.upper) # 重命名索引名
	 data.rename(index={'OHIO': 'INDIANA'},columns={'three': 'peekaboo'}) # 重命名索引名（将行索引OHIO变为INDIANA，列索引three变为peekaboo）
	 data.rename(index={'OHIO': 'INDIANA'}, inplace=True) # 传入inplace=True参数就地修改

### h. 离散化和面元化分（cut和qcut）
	ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
	bins = [18, 25, 35, 60, 100]
	cats = pd.cut(ages, bins)  # 传入列表bins表示面元边界划分生成面元对象 （默认有边界为封闭区间）
	pd.value_counts(cats)  # 统计每个面元中包含的数据个数
	cats.codes  # 查看ages每个数据对应的面元区间
	cats.categories # 查看面元区间
	pd.cut(ages, [18, 26, 36, 61, 100], right=False) # 将面元右边界改为开区间
	pd.cut(ages, bins, labels= ['Youth', 'YoungAdult']) # 传递列表或数组设置面元名称
	pd.cut(data, 4, precision=2) # 传入整数4表示面元数量，precision表示小数点位数（cut是根据数据的最大最小值计算等长面元）
	cats = pd.qcut(data, 4) # （qcut表示根据data的数据个数平均分为4组）

### i. 检测、过滤异常值
	 data.describe()  # 输出每一列数据的总体情况，count,mean,std,min,25%,50%,75%,max
	 data[np.abs(data[2]) > 3] # 输出data第三列绝对值大于3的数据
	 np.sign(data)  # 输出data中数据的正负号（1代表正数，-1代表负数，0代表0）

### j. 排列和随机采样
       对数据进行行重新随机排序：
	 df = pd.DataFrame(np.arange(20).reshape((5, 4)))
	 sampler = np.random.permutation(5)  # 生成0到4整数，排序随机
	 df.take(sampler)  # 取下标为sampler的行数据
	
	 df.sample(n=3)、df.sample(3)  # 随机获取3行数据（可以直接传整数3）
	 df.sample(n=3，replace=True)  # 传入replace=True可以随机生成超过df总行数的数据

### k. 计算指标/哑变量

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})
pd.get_dummies(df['key'])

	  a b c
	0 0 1 0
	1 0 1 0
	2 1 0 0
	3 0 0 1
	4 1 0 0
	5 0 1 0      # 将key作为指标，data1作为数据，0行a列无数据计为0，有则计为1

### l. 矢量化字符串函数

	通过data.map，所有字符串和正则表达式⽅法都能被应⽤于（传⼊lambda表达式或其他函
	数）各个值，但是如果存在NA（null）就会报错。为了解决这个问题，Series有⼀些能够跳过
	NA值的⾯向数组⽅法，进⾏字符串操作。通过Series的str属性即可访问这些⽅法。例如，我
	们可以通过str.contains检查各个电⼦邮件地址是否含有"gmail"：
	
	 data.str.contains('gmail')  # 返回bool值，但是NaN无法识别
	 pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})' 
	 data.str.findall(pattern, flags=re.IGNORECASE)
	 matches = data.str.match(pattern, flags=re.IGNORECASE)  # 返回bool值，但是NaN无法识别
	 data.str[:5]  # 截取字符串