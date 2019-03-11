SVD分解

线性代数中可知如果一个方正A存在特征值则：
$$
Ax=\lambda x
$$
其中
$$
\lambda 表示方正A的特征值，x表示特征向量 方正A就可以表示成为：A=QW Q^{-1} 其中Q为所有的特征向量组成的
矩阵，W为特征值组成的对角矩阵
$$

$$
其中W^{T}W=E，所以W^{T}=W^{-1}
$$

上面的矩阵分解中要求A必须为方正，无法推广到矩阵 SVD就是对矩阵进行分解 现在假设A是一个mxn的矩阵那么，可以定义svd 为
$$
A=UWV^{T}，其中U是一个mxm的矩阵，其中U中的每一个列向量都是标准正交基，W为一个mxn的矩阵其除了主对角线外
$$
其他的元素都为0，V是一个nxn的矩阵，其中U中的每一个列向量也都是标准正交基，所有
$$
U^{T}U=E，V^{T}V=E
$$
下面求解U，W，V，
$$
A^{T}A是一个n阶方正，对其求特征值(A^{T}A)v=\lambda v 其中特征向量v组成n维的V方正
$$

$$
同样的道理 AA^{T}是一个m阶方正，对其求特征值(AA^{T})u=\lambda u 其中特征向量u组成n维的U方正
$$

证明：
$$
A=UW V^T \Rightarrow A^T=VW^T U^T \Rightarrow A^TA = VW^T U^TUW V^T = VW^2V^T=W^2VV^T，则V是A^TA特征向量组成的矩阵
$$

$$
A=UWV^{T}同乘V\Rightarrow AV=UWV^{T}V\Rightarrow AV=UW\Rightarrow Av=\sigma u\Rightarrow \sigma =Av/u，\sigma为W中主对角线上的值
$$
又由于U是由标准正交基组成的方正，所以
$$
AV=UW\Rightarrow U^{-1}AV=W\Rightarrow U^TAV=W
$$
这样求出了U，W，V

上面的公式推广一下，就可以使用一个k大的奇异值来近似的描述一个矩阵，
$$
A_{m \times n} = U_{m \times m}\Sigma_{m \times n} V^T_{n \times n} \approx U_{m \times k}\Sigma_{k \times k} V^T_{k \times n}
$$
