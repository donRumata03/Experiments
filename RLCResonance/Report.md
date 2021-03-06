# Резонанс в RLC-цепи

> ​													**Владимир Латыпов && Серёжа Онищенко**



#### Методика

Рассмотрим резонансную кривую, для этого промерим непустое множество точек в районе «ROI» — Region Of Interest, в именно — вокруг пика.

Подключим щупы осциллографа к резистору, собрав схему:

![image-20210212233442831](D:\Projects\Experiments\RLCResonance\scheme.png)

Затем, крутя ручку генератора и записывая его частоту, будем также замечать амплитуду, которую показывает осциллограф. Был ещё вариант записывать всё на видео, но мы посчитали его нецелесообразным, например, потому что он мешает оценивать нашу работу в реальном времени и, соответственно, не даёт достаточной обратной связи.

#### Теоретическое обоснование

Напряжение на катушке и на конденсаторе противоположны по фазе, то есть сумма векторов — просто разность модулей. Проекции этой суммы, напряжения на резисторе и на источнике должны давать ноль, следовательно, 
$$
U_0^2=U_{0R}^2+(U_{0L}-U_{0C})^2\\
U_0^2=(RI)^2+(L\frac{d^2q}{dt^2}-\frac{q}{C})^2
$$
Так как
$$
I_0 cos(wt)=\frac{dq}{dt}=\frac{d(CU_c)}{dt}=C\frac{dU_c}{dt}\\
\frac{dU_c}{dt} = \frac{1}{C}I_0 cos(wt)\\
U_C = \frac{1}{wC}I_0 sin(wt)\\
U_{0C}=\frac{1}{wC}
$$
Аналогично для катушки
$$
L\frac{d^2q}{dt^2}=U_{L}\\
L\frac{d(I_0·cos(wt))}{dt}=U_L\\
U_L = LwI_0·sin(wt)\\
U_{0L} = Lw·I_0
$$
Тогда 
$$
\label{current_formula}
U_0^2 = I^2R^2+(\frac{1}{wC}-wL)^2I^2\\
I_0 =\frac{ε}{\sqrt{R^2+(\frac{1}{wC}-wL)^2}}
$$

##### Резонанс

Найдём частоту, при которой достигается максимальный ток в цепи, а значит — и напряжение на резисторе. Понятно, что если мы рассматриваем зависимость от частоты, то наша задача — минимизировать слагаемое в знаменателе амплитуды $(\frac{1}{wC}-wL)^2$, тогда минимум при $\frac{1}{wC}=wL; w =\sqrt{\frac{1}{LC}}$



#### Измерения

Примерно так проходил процесс получения экспериментальных данных.

> Репортаж с места съёмок:

<img src="D:\Projects\Experiments\RLCResonance\images\measuring.png" alt="image-20210212221421996" style="zoom:50%;" />

#### Экспериментальные данные

Серия измерений состоит из нескольких точек, для которых на осциллографе были выставлены одинаковые диапазоны значений по обеим осям. Записываются частоты и количества делений вместе с ценой деления по вертикали. 

*Примерно так выглядит типичный $json$ с описанием эксперимента:*

<img src="D:\Projects\Experiments\RLCResonance\images\json.png" alt="image-20210212222244340" style="zoom: 67%;" />

*Так выглядит график, построенный по измеренным точкам:*

![image-20210212221538840](D:\Projects\Experiments\RLCResonance\images\scatter.png)

Добавим обозначение теоретического максимума, полученного из измеренных параметров элементов $\left( \nu_{opt} = \frac{1}{\sqrt{LC} \cdot 2 \pi} \approx 1206. ~ Hz\right)$

![image-20210212231654555](D:\Projects\Experiments\RLCResonance\images\scatter_with_peak.png)

Теперь аппроксимируем этот график указанной в методике функцией $\left( I_0 =\frac{ε}{\sqrt{R^2+(\frac{1}{wC}-wL)^2}} \right)$:

![image-20210212230910310](D:\Projects\Experiments\RLCResonance\images\approx.png)

В задании было сказано «посмотреть, где в измерениях есть какие-то систематические ошибки и чем они были вызваны», однако точки легли почти идеально, так что нет никаких проблем!

# ***OMG***

​						😎😎😎😎😎😎😎																							😎😎😎😎😎

​			😎												😎					😎							😎					😎						😎

​	😎															😎				😎	😎			😎   😎				😎								😎

😎																	😎			😎		😎	😎		😎				😎

😎																	😎			😎			😎			  😎				😎

​	😎																😎			😎							  😎				😎						  

​		😎														😎				😎							  😎				😎						😎😎😎				😎											😎					😎							  😎					😎							😎😎

​						😎😎😎😎😎😎😎😎						   😎							 😎							😎😎😎😎😎😎😎



### Вывод

Всё фантасмагорически замечательно. 

![Image](https://pbs.twimg.com/media/EAvMpNHXsAEKQLI?format=png&name=900x900)

