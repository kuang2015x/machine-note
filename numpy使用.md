# numpy使用

## 1 numpy基本操作

numpy生成数组或矩阵方法

```python
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
```

numpu使用shape，ndim，size等方法获取矩阵的形状，维度，元素个数

```python
a = np.array([1, 2, 3])
print(a.shape)
print(a.ndim)
print(a.size)
#输出结果
(3,) #当数组是一维时 shape就是输出元素的个数
1
3
```

```python
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(b.ndim)
print(b.size)
#输出结果为：
(2, 3)
2
6
```

由上面的输出结果可以看出矩阵的维度可以从最左边的连续的左中括号的个数得出。

### 1.1 numpy创建矩阵或数组

除了上面的创建矩阵外还有以下几种方法：

```python
# 指定数据的类型
a = np.array([1, 2, 3], dtype=np.int32)
print(a)
print(a.dtype)

# 生成一个全部为0的矩阵
b = np.zeros((2, 3))
print(b)

# 生成一个全1的矩阵,也可以通过dtype 指定数据的类型
d = np.ones((2, 3))
print(d)

#生成一个有序的数其中可以指定开始值，结束值，以及步长
#生成一个10到20之间的数
e = np.arange(10,20)
print(e)
#生成一个10到20之间的数，步长为2
f = np.arange(10,20,2)
print(f)

#reshape 改变一个矩阵的形状,如：将10到20一维矩阵转成2行5列的矩阵
g = np.arange(10,20).reshape((2,5))
print(g)

#将一个2行5列的矩阵拉成一个向量
k = g.ravel()
#生成一个随机矩阵
h = np.random.random((2,3))
```

### 1.2 numpy的基础运算

矩阵的元素的加减乘除，矩阵的乘法

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 矩阵相加减乘除，矩阵中对应的位置的元素相加减乘除
print(a + b)
print(a * b)
print(a / b)

# 矩阵的平方，矩阵中的每一个元素平方
print(a ** 2)

# 矩阵可以直接使用<,>,==等判断符，判断矩阵中的每一个元素是否满足给定的条件
print(a < 3)

# 当需要使用矩阵的乘法法则时需要用 dot

c = np.dot(a, b)
print(c)
# 也可所以使用如下方法运算矩阵的乘法
d = a.dot(b)
print(d)

# 对一个矩阵中的所有元素进行求和使用sum
print(np.sum(a))
# 求矩阵中最大的一个元素
print(np.max(a))
# 求矩阵中的最小的一个元素
print(np.min(a))

# 如果要求每一行或每一列的和或最大值，最小值时需要使用参数axis,
# 当axis值为0时表示对列进行操作，为1时表示对行进行操作
print(np.sum(a, axis=0))
print(np.max(a, axis=1))
print(np.min(a, axis=0))
```

其余的一些运算

```python
a = np.array([[1, 2, 3], [6, 5, 4]])
# 获取元素最大值的索引
print(np.argmax(a))
# 获取元素最小值的索引
print(np.argmin(a))

# 获取矩阵的平均值
print(np.mean(a))
# 或者
print(a.mean())
# 或者
print(np.average(a))

# 获取中位数
print(np.median(a))
# 逐步累加
print(np.cumsum(a))
# 每行中相邻的两个数的差
print(np.diff(a))

# 输入矩阵中非0的行，列索引
print(np.nonzero(a))

# 矩阵的每一行进行排序
print(np.sort(a))

# 矩阵进行转置
print(a.T)

# 将矩阵中小于3的元素置为3，大于5的元素置为5
print(np.clip(a, 3, 5))

#也可以使用如下方法将a中小于3的元素设置为3
print(a[a<3]=3)
```

## 2 numpy索引

```python
a = np.array([[1, 2, 3], [6, 5, 4], [7, 8, 9]])

# 矩阵的索引
# 取出某第一行第二列的一个元素
print(a[0][1])
# 也可以为
print(a[0, 1])
# 取出第二行所有的元素
print(a[1])
# 也可以为
print(a[1, :])
# 取出第二行中第一二列的元素
print(a[1, 0:2])
# 取出第二列的所有元素
print(a[:, 1])
# 取出第一二行的第二列元素
print(a[0:2, 1])

#按行迭代矩阵
for raw in a:
    print(raw)
#如果要按列进行迭代只需进行转置即可

#迭代矩阵中每一个元素
for item in a.flat:
    print(item)

#将矩阵变成一个一维数组
print(a.flatten())

a = np.array([[1, 2, 3], [6, 5, 4], [7, 8, 9]])

# array类型的比较如 找出a中那些数等于5
# b是一个和a的维度相同的矩阵，且b中元素的值为a中元素的值和5的比较
# 如果a中的元素的值等于5则b中对应的位置为true，否则为false
# 即b为一个true或false组成的矩阵
b = a == 5
print(b)

# 也可以通过一个true，false矩阵作为索引取出另一个矩阵中对应的特定的行或列
# 如取出b中true所对应的行列在a中的元素
print(a[b])

# 取出b中true所在的行对应在a中所在的行
# 注意此时a中传入的参数索引必须为一维的矩阵
# 本例是将b中true所在的行取出作为一个向量如果想在矩阵中取出一行或一列必须传入的参数为
# 向量，再将此向量作为索引传入到a中
# 取出true所在的行
print(a[b[1, :], :])
# 取出true所在的列
print(a[:, b[1, :]])
```

#### 2.1矩阵的拼接和切分

```python

d = np.floor(10 * np.random.random((3, 3)))
print(d)

# 将两个矩阵进行拼接方法有hstack((a,b))和vstack((a,b))两种方法
# hstack是将两个矩阵进行横着并在一起即将b矩阵拼在a矩阵的右边
#此时a,b的行数必须相同
print(np.hstack((a,d)))

#vstack((a,b))是将b矩阵拼接在a矩阵的下方，此时它们的列必须相同
print(np.vstack((a,d)))

a = np.floor(10*np.random.random((3,4)))
#有了拼接就有切分的方法hsplite(a,n)和vsplite(a,n)
#hsplite是将矩阵a按照左右切成n个矩阵，其中切分后的每一个矩阵行数
#和a矩阵相同，就是对矩阵进行竖着切，其实是按照a矩阵的列数除以n就是切分后每一个矩阵的列数
#如果a除以n不为整则报错
print(np.hsplit(a,4))

#相对的vsplite(a,n)就是横着对a进行均分，其中切分后的矩阵列数和a相同
#每一个矩阵的行数就是a除以n
print(np.vsplit(a,3))

a = np.floor(10*np.random.random((6,10)))
#hsplite和vsplite除了上面的传入一个数值将矩阵均等切分之外还能传入一个tuple
#并按照tuple中的数值进行切分，如将矩阵在第3列，4列，6列分别切开可以使用
#hstack(a,(3,4,6))
print(np.hsplit(a,(3,4,6)))

#也可以按照行切vstack,如将矩阵在第二行和第四行进行切分
print(np.vsplit(a,(2,4)))
```

#### 2.2矩阵的复制

numpy矩阵或者python 列表，字典，元组中如果使用“=”将它们赋值给另一个变量，则它们会同时指向这一块内存，如现在有一个矩阵或列表a，做了赋值操作 a=b，此时a，b同时指向a指向的内存，如果此时对b进行操作如改变b中的值，则a中的值也会改变

```python
a = np.arange(12)

b = a

b.shape = 3,4
#此时a也变成了3x4的矩阵
print(a)

print(id(a)) #变量的id
print(id(b))
```

如果要将a的值拷贝一份给b 需要使用可以使用copy

```python
a = np.arange(12)

c=a.copy()
c.shape = 3,4
print(a)
```

对矩阵进行扩展除了上面的方法外还可以使用title

```python
a = np.arange(0,40,10)
print(a)

#title(a,tuple)其中a为要扩展的矩阵，tuple为一个元组，表示行和列要复制几次
b = np.tile(a,(2,3)) #表示将a复制两份列复制三分作为新的矩阵
print(b)
```