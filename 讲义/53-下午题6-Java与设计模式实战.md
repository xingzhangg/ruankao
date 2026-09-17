# 53 · 下午题 6：Java + 设计模式实战

> 真题：观察者模式 2019下·试题六、生成器模式 2017上·试题六、生成器模式 2018上·试题六，三道完整的下午 Java 选做题，题干与代码照录信管网三份「下午案例分析真题文字版」及培训资料扫描件（年份与题号 2026-09-10 核实）｜无计算，五个空全在类图和代码里｜未讲
> 知识点范围：对齐 `外部资源/转录md/15-软件设计师-案例分析专题.md` 第五部分全部（1-1～1-6 Java 语法考点串讲、2 解题技巧与 Q&A、真题 1 观察者、真题 2 生成器）

---

## 定位

**这一课回答**：下午卷那道 Java 选做题的五个空怎么填。

**前后关系**：设计模式各自的意图、分类与适用场景在 28（创建型、结构型）和 29（行为型），类图怎么读在 25 和 51，Java 之外的语言与编译知识在 45；本课只管一件事——照着类图把挖了空的代码补完。48 定了它排答题顺序第 1 位、用时 10 分钟、目标 13 分。

**分值与去向**：15 分、五个空，是全卷性价比最高的一道，因为空几乎全是"从类图上把名字抄下来"，不要求你设计任何东西；零计算。

---

## 开讲：这道题不考你会不会设计，只考你会不会抄

先把这道题为什么值得排第一位说清楚。它给你的东西是**一段业务说明（说明里直接点名用的是哪个设计模式）＋一张类图＋一段挖了五个空的 Java 代码**，让你把空填上。

**设计模式**是前人把"反复出现的同一类设计难题＋已被验证过的解法"整理出来的固定套路，比如"一个对象变了、要通知一堆对象"这件事，对应的套路就叫观察者——23 个套路各自解决什么问题在 28、29 讲过，本课一个都不重讲，只用结论。

关键在于：**题干已经把模式名告诉你了**，所以这道题不是"你能不能想出设计方案"，而是"你能不能照着类图把名字抄进代码"。

类图和代码**一一对应**，同一批类名、方法名在两边各出现一次；补空的动作，本质上就是**在类图上找到对应的那个格子，把里面的名字抄下来**。你是写代码的，读 Java 毫无障碍，这道题对你几乎是白送分——**前提是知道空该往哪个格子抄**。这就是本课要教的全部。

培训资料的口径是：这两道选做题「都是程序填空，原理一模一样」，「只是考基本语法，不涉及算法」，「**完全可以拿满分**」；给零基础的人的建议更直白——「**完全可以从英语角度去理解，根据关键词去联系代码上下文**，都能得出答案，毫无难度，**每个人都能拿满分，要先树立信心**」。

### 一、卷面上有什么

**先说选哪道。** 卷面把这两道排成试题五和试题六，同一个业务场景、同一个设计模式，一道用 C++ 写、一道用 Java 写，任选一道作答。2018 年上半年那套卷面上的原话是：

> 从下列的2道试题(试题五至试题六)中任选1道解答。请在答题纸上的指定位置处将所选择试题的题号框涂黑。若多涂或者未涂题号框,则对题号最小的一道试题进行评分。

注意这句话只说了"两道选做题固定摆在试题五、试题六这两个位置"，**没说哪个位置放哪种语言**。

**两件事要记住。** 第一，**必须动手选**：不涂、或者涂了两个，判的是题号小的那道；如果那年题号小的是 C++ 题，你按 Java 答的那一整道就白写了。机考没有涂题号框这个动作，具体怎么表示"我选这道"官方没有公开说明，考前上官网模拟平台摸界面时（讲义 48 第五节）顺手把这一条也确认掉。第二，**你要选的是题头写着 Java 的那一道，而且认题头不认题号**：常见排法确实是试题五 C++、试题六 Java——2017 上、2017 下、2018 上、2018 下、2019 下这五套卷都是这样——但题号不是铁律，2019 年上半年那套卷整个反过来：**试题五是 Java（类图编号图 5-1），试题六才是 C++（图 6-1）**。所以进考场认的是题头那句"阅读下列说明和 **C++** 代码"还是"阅读下列说明和 **Java** 代码"，不是数题号。本课三道题都是 Java 那一道。

**再说卷面长相。** 这道题**没有小问**，整道题就是一句"将应填入 (n) 处的字句写在答题纸的对应栏内"，代码里挖五个空，标成 `(1)`～`(5)`。15 分五个空，通行的算法是**一空 3 分**——下午题官方不公布评分细则，但它是按点给分（每个空就是一个评分点，填对一个得一个的分），所以五个空互相独立，卡住一个不影响其余四个。

**最后约定类图的纯文本写法**，和讲义 51 用的是同一套，同一个符号全篇只有一种含义，箭头和菱形一律画在它该贴的那一端：

- `A ── B` 关联，一条光实线，两头没记号
- `A ──▶ B` 关联并带导航箭头，箭头贴在**被 A 拿在手里用的那一方**；落到代码上就是"A 里有一个 B 类型的成员变量"
- `子 ──▷ 父` 泛化，也就是继承，空心三角贴**父**那一端；代码上是 `class 子 extends 父`
- `类 ⇢▷ 接口` 实现，虚线加空心三角，三角贴**接口**那一端；代码上是 `class 类 implements 接口`
- `整体 ◇── 部分` 聚合，也就是"整体和它的零件、整体没了零件还在"，空心菱形贴**整体**那一端；两种记号可以叠用，`整体 ◇──▶ 部分` 就是菱形贴整体、箭头贴部分
- 类框里的方法前面那个 `+` 是 public 的意思；**类名或方法名印成斜体＝抽象**，这一条本课后面要用到

### 二、先猜一次：只看类图，你能猜出会挖哪几个空吗

下面是 2019 年下半年那道题的类图（图 6-1），我先只给你图，不给代码。**先别往下看**，看着图想一想：如果出题人要在这份代码里挖五个空，他会挖在哪儿？

```
Subject{ +Attach()  +Detach()  +Notify() }        Observer{ +update() }
OfficeDoc{ }                                       DocExplorer{ }

Subject ──▶ Observer
OfficeDoc ⇢▷ Subject          DocExplorer ⇢▷ Observer
DocExplorer ──▶ OfficeDoc
```

（原图是培训资料上的一张扫描件，线的画法在这里交代清楚，免得你照着上面的纯文本反推错：两条指向 Subject、Observer 的都是**虚线加空心三角**，三角分别贴在 Subject 和 Observer 那一端，是实现关系；Subject 到 Observer、DocExplorer 到 OfficeDoc 是**实线加细箭头**，箭头分别贴在 Observer 和 OfficeDoc 那一端。

Subject 和 Observer 两个框的属性格是空的，OfficeDoc、DocExplorer 两个框的属性格和方法格都是空的。）

图上摆着四个框、四个方法名。**大概率被挖的就是这八个名字里的几个**，因为它们是这道题唯一"有标准答案"的东西——业务逻辑千变万化，名字是死的。往细里猜：

- `Observer` 框里只有一个 `+update()`，而 Observer 一看就是个接口——有一条 `⇢▷`（虚线加空心三角）指着它，这个记号就是"实现"，被指的那一端只能是接口；接口里的方法只有声明没有方法体，**这一行几乎一定被挖**；
- `Subject ──▶ Observer` 这根箭头说明 Subject 那一侧存着一堆 Observer，代码里必然有一个装 Observer 的表，**表里装什么类型**是个天然的空；
- `+Notify()` 是"挨个通知"，方法体里一定有一句"对每个观察者调用 `update()`"，**这句调用**是个天然的空；
- 两条 `⇢▷` 说明代码里有两句 `implements`，`DocExplorer` 要认识它盯着的那个目标，**目标的类型名**是个天然的空。

四条全中——五个空里的四个，只看类图就猜出来了。剩下那一个猜不出来（它藏在代码里，等下会讲），但这已经足够说明本课要你养成的反射：**先读类图，再读代码，读代码时你已经知道每个空该往哪个格子抄了。**

### 三、读这段代码只需要认六件 Java 事

培训资料的 Java 语法串讲一共六小节，逐条对上本课要用的地方，多一个字都不用背：

**① 类里装什么、构造方法长什么样。**「一个类可以包含变量和方法」；「**在创建一个对象的时候，至少要调用一个构造方法。构造方法的名称必须与类同名**，一个类可以有多个构造方法」；没写构造方法时编译器给一个默认的。**构造方法**就是"这个对象刚被造出来时要做的那几件事"，写法是没有返回类型、方法名和类名一模一样，例如 `public OfficeDoc(String name){...}`。本课两道题各有一个空正好落在构造方法里。

**② 怎么造对象。** 关键字 `new`，三步是「声明」「实例化」「初始化」——`Puppy myPuppy = new Puppy("tommy");` 里 `Puppy myPuppy` 是声明、`new Puppy(...)` 是实例化、括号里的参数交给构造方法完成初始化。本课两道题的 `main` 里全是这种句子。

**③ 怎么调方法、怎么访问变量。** 都是一个点号：`myPuppy.setAge(2);`、`myPuppy.puppyAge`。**本课五个空里通常有两三个就是这种一行调用。**

**④ 访问控制修饰符。**「**private：在同一类内可见**」「**public：对所有类可见**」「**protected：对同一包内的类和所有子类可见**」。用到的地方有两处：`protected` 的成员子类里可以直接拿来用，所以生成器那道题的子类方法体里能直接写 `pizza.setParts(...)`；另外「父类中声明为 **public 的方法在子类中也必须为 public**」，所以子类覆盖出来的方法前面必须写 `public`，漏了会编译不过。

**⑤ abstract。**「**抽象类不能用来实例化对象**」「**如果一个类包含抽象方法，那么该类一定要声明为抽象类**」「抽象方法是一种**没有任何实现的方法**，该方法的具体实现由子类提供」「抽象方法的声明以分号结尾」。**抽象方法**就是"只写名字、不写内容，留给子类去写"的方法，写法是 `public abstract void 方法名();`——没有花括号，直接一个分号收尾。类图上印成斜体的那个方法就是它。

**⑥ 继承怎么写。**「继承可以使用 **extends 和 implements** 这两个关键字来实现继承」；`extends` 后面只能跟**一个**类（「类的继承是**单一继承**」），`implements` 后面可以跟**多个**接口、逗号分隔。对应到类图：`──▷` 写成 `extends`，`⇢▷` 写成 `implements`。**接口**就是一张只写方法名、不写方法体的清单，谁 `implements` 了它，谁就必须把清单上的方法一个不落地写出来。

还有一件培训资料没单列、但真题里就有的：**泛型**。`List<Observer> myObs;` 这种尖括号写法，尖括号里写的是"这张表只准装什么类型的东西"，写死了以后往里塞别的类型编译就不过。真题 1 的第二个空正好就在这对尖括号里面。

### 四、跟我做一道真题：文件管理系统的观察者模式

【真题·2019下】（试题六，Java；同场试题五是同一场景的 C++ 版）

**【说明】** 某文件管理系统中定义了类OfficeDoe和DocExplorer。当类OfficeDoe发生变化时，类DocExplorer的所有对象都要更新其自身的状态。现采用观察者(Observer) 设计模式来实现该需求，所设计的类图如图6-1所示。

（说明照录信管网「2019 年下半年软件设计师下午案例分析真题文字版」。说明里的 `OfficeDoe` 是个讹字——同一道题的类图和 Java 代码里都写作 `OfficeDoc`，按后者读。这类讹字在下午卷里不算稀奇，见着别慌。）

**观察者模式**是这么回事：有一个被盯着的目标对象，还有一堆盯着它的观察者；目标一变，所有登记过的观察者自动收到通知、各自刷新——就像一份共享文档被改了，所有打开着它的窗口都要跟着刷新。这里 `OfficeDoc` 是那份文档（目标），`DocExplorer` 是那些窗口（观察者）。类图就是上一节猜过的那张。

**【Java 代码】**（照录培训资料所印版本，五个空标为 `( 1 )`～`( 5 )`）

```java
import java.util.*;
interface Observer{
 public ( 1 );
}

interface Subject{
 public void Attach(Observer obs);
 public void Detach(Observer obs);
 public void Notify();
 public void setStatus(int status);
 public int getStatus();
};

class OfficeDoc implements Subject{
 private Lists< ( 2 ) > myObs;
 private String mySubjectName;
 private int m_status;
 public OfficeDoc(String name) {
    mySubjectName=name;
    this.myObs=new ArrayList< Observer> ();
    m_status=0;
 }
 public void Attach(Observer obs) {this.myObs.add(obs);}
 public void Detach(Observer obs) {this.myObs.remove(obs);}
 public void Notify(){
    for(Observer obs:this.myObs){
      ( 3 );
    }
 }
 public void setStatus(int status){
    m_status=status;
    System.out.println("SetStatus subject["+mySubject.Name+"]status:"+status);
 }
 public int getStatus(){return m_status;}

class DocExplorer implements Observer{
 private String myObsName;
 public DocExplorer(String name, ( 4 ) sub) {
 myObsName=name;
 sub.( 5 );
 }
 public void update() {
   system.out.println("update observer["+myObsName+"]");
 }

class ObserverTest{
  public static void main(String [] args) {
   System.out.println("Hello World!");
   Subject subjectA=new OfficeDoc("subject A");
   Observer oberverA=new DocExplorer("observer A",subjectA);
   SubjectA.setStatus(1);
   SubjectA.Notify();
  }
}
```

**先说这段代码印得毛糙的地方**，免得你以为自己看错了。五处是真会让编译器报错的：`Lists<` 多了个 s（应是 `List<`）；`mySubject.Name` 中间多了个点（应是 `mySubjectName`）；`system.out.println` 的 s 该大写；`SubjectA.setStatus`／`SubjectA.Notify` 首字母该小写（上一行定义的变量叫 `subjectA`）；`OfficeDoc` 和 `DocExplorer` 两个类收尾的花括号没印出来。还有一处看着刺眼、其实无害：`Observer oberverA=...` 里的 `oberverA` 比 `observerA` 少个 s，但它只是个变量名，而且往下再没被用到，原样留着照样编译通过。**这六处没有一处落在五个空上**，照常做题即可——这本身就是一条考场经验：**代码印得毛糙不影响填空，别被吓住。**

**动笔前先做一件事：把类图和代码对一遍。** 类图四个框，代码里除掉最后那个只为跑 `main` 而存在的 `ObserverTest`（它不在类图上，两道题都有这么一个"跑起来看看"的类），正好也是四个类型：`interface Observer`、`interface Subject`、`class OfficeDoc implements Subject`、`class DocExplorer implements Observer`。两条 `⇢▷` 落成两句 `implements`，对上了。剩下两根实线箭头也各有着落：`Subject ──▶ Observer` 就是 `OfficeDoc` 里那个装 Observer 的表，`DocExplorer ──▶ OfficeDoc` 就是 `DocExplorer` 构造方法收进来的那个 `sub`。四个框、四条线，一条不多一条不少。

**空 (1)：`interface Observer{ public ( 1 ); }`。这一步不是推出来的，是照抄的。** 类图 `Observer` 框里只写着一个 `+update()`，格子里没有返回类型，UML 里不写返回类型就是 `void`；接口里的方法只有声明、以分号结尾。所以抄下来就是 **`void update()`**（模板自带那个分号；写成 `void update();` 也照样编得过，Java 允许成员之间多一个分号）。回头验一下：`DocExplorer` 里写着 `public void update() {...}`，签名一模一样，对上了。

**空 (2)：`private Lists< ( 2 ) > myObs;`。先别往下看，猜一个**——尖括号里填 `Observer` 还是 `DocExplorer`？

不少人第一反应填 `DocExplorer`，理由是"实际往里塞的就是 DocExplorer 对象"。

**这个理由本身没错，但答案是 `Observer`**，有两处硬证据：一是同一个类的构造方法里明明白白写着 `this.myObs=new ArrayList< Observer> ();`，声明的类型和赋值的类型必须一致；二是 `Attach(Observer obs)` 往这张表里 `add(obs)`，参数类型是 `Observer`。

填 `DocExplorer` 这两处都编译不过。类图上也是这么画的——箭头从 `Subject` 指向 `Observer`，不是指向 `DocExplorer`。**这就是观察者模式的命门：目标只认那张接口清单，不认具体是谁在盯着它**，这样以后再加一种窗口，`OfficeDoc` 一行都不用改。

**空 (3)：`Notify()` 里 `for(Observer obs:this.myObs){ ( 3 ); }`。** 这是"调用形式"的空——培训资料把这类空描述得很准：「填写函数体，但是这个函数体并不是要写一段真正的程序实现代码，**而是调用形式的**，都有调用函数的，这些调用函数一般在程序中，或者在说明和类图中可以找到」。循环变量 `obs` 的类型是 `Observer`，`Observer` 这张清单上只有一个方法，所以只有一种写法：**`obs.update()`**。语义上也正好是"通知每一个观察者更新"。

**空 (4)：`public DocExplorer(String name, ( 4 ) sub)`。** 参数 `sub` 的类型填什么？类图上 `DocExplorer ──▶ OfficeDoc`，看着像该填 `OfficeDoc`。**这里我卡了一下**，因为往下一行 `sub.( 5 );` 只要求 `sub` 能被调方法，填 `OfficeDoc` 也说得通。**决定性证据在 `main` 里**：`Subject subjectA=new OfficeDoc("subject A");` 把对象声明成了 `Subject` 类型，然后 `new DocExplorer("observer A",subjectA)` 把它传进来——一个声明为 `Subject` 的变量，是塞不进 `OfficeDoc` 类型的参数里的（父类型不能自动当成子类型用），填 `OfficeDoc` 会编译不过。所以 **`Subject`**。这一步的教训是：**类图给的是线索，代码里已经写死的那一行才是判据；两边打架时以代码为准。**

**空 (5)：`sub.( 5 );`。这是全题唯一要靠排除法挑答案的空。** 前面四个空各有一行代码把答案钉死——(1) 有 `DocExplorer` 里同名的 `update()`，(2) 有 `new ArrayList< Observer> ()`，(3) 有"`Observer` 只有一个方法"，(4) 有 `main` 里那句 `Subject subjectA=...`；这一个没有，`Subject` 清单上摆着五个方法（`Attach`／`Detach`／`Notify`／`setStatus`／`getStatus`），得自己挑。怎么排除：

- 这一行在 `DocExplorer` 的**构造方法**里，也就是"这个观察者刚被造出来"的那一刻。`Detach` 是注销，刚出生就注销讲不通；`Notify` 是目标去通知别人，不该由观察者来喊；`setStatus`／`getStatus` 是改和读目标的状态，跟"新来一个观察者"对不上。剩下 `Attach`，字面就是"挂上去"。
- 反过来验一遍更硬：`main` 里从头到尾**没有任何一处**调用过 `Attach`。如果构造方法里不挂，`myObs` 这张表永远是空的，`Notify()` 的循环一次都不会转，`update()` 里那句打印永远不出现——那这段代码就没有任何输出，题目也就没意义了。
- 参数写什么？`Attach(Observer obs)` 要一个 `Observer`，而"要挂上去的观察者"就是正在被构造的这个对象自己，Java 里指代自己的关键字是 `this`。

所以 **`Attach(this)`**。这个动作有个通用叫法：**注册**——观察者主动把自己登记到目标那儿，之后目标一变就会来通知它。

**五个空填回去，整段代码跑一遍**（把上面那五处会报错的毛病改正后编译执行），输出是：

```
Hello World!
SetStatus subject[subject A]status:1
update observer[observer A]
```

三行都对得上：`main` 先打印 Hello World，再 `setStatus(1)` 打印目标改了状态，最后 `Notify()` 触发那唯一一个观察者打印自己更新了。**这一遍"跑一遍看输出对不对"就是你的验算**——考场上跑不了程序，但你可以用眼睛顺着 `main` 走一遍，走通了这五个空就基本没错。

**答案与评分点**：(1) `void update()`　(2) `Observer`　(3) `obs.update()`　(4) `Subject`　(5) `Attach(this)`。五空各 3 分，互相独立。末尾的分号写不写不影响（模板里已经有了，多一个也编得过）；**方法名的大小写必须照抄**——这份代码里 `Attach`、`Detach`、`Notify` 首字母都是大写（不合 Java 惯例，但卷面就这么印的），写成 `attach(this)` 就是另一个方法名了；`(3)` 写成 `obs.update();` 连分号一起写，属于等价写法。

### 五、第二道你自己做：快餐厅的生成器模式

【真题·2017上】（试题六，Java；同场试题五是同一场景的 C++ 版）

**【说明】** 某快餐厅主要制作并出售儿童套餐，一般包括主餐(各类比萨)、饮料和玩具，其餐品种类可能不同，但其制作过程相同。前台服务员 (Waiter) 调度厨师制作套餐。现采用生成器 (Builder) 模式实现制作过程，得到如图 6-1 所示的类图。

**生成器模式**是把"按固定步骤造一个复杂东西"拆成两半：一半是**谁来发号施令、按什么顺序走**，另一半是**每一步具体填什么内容**——同一套流程，换一个生成器就造出不同口味的比萨。这里 `Waiter`（前台服务员）负责发号施令，`PizzaBuilder` 的两个子类负责各自往比萨里填料。

图 6-1 类图（同样转写自扫描件）：

```
（〔斜体〕＝这个名字在原图上印的是斜体）

Waiter{ +construct()  +setPizzaBuilder()  +getPizza() }
PizzaBuilder〔斜体〕{ +createNewPizza()  +buildParts()〔斜体〕  +getPizza() }
HawaiianPizzaBuilder{ +buildParts() }    SpicyPizzaBuilder{ +buildParts() }    Pizza{ }

Waiter ◇──▶ PizzaBuilder
HawaiianPizzaBuilder ──▷ PizzaBuilder      SpicyPizzaBuilder ──▷ PizzaBuilder
HawaiianPizzaBuilder ──▶ Pizza             SpicyPizzaBuilder ──▶ Pizza
```

**图上有一处记号千万别漏**：`PizzaBuilder` 这个类名，以及它框里的 `+buildParts()` 这一行，印的都是**斜体**，而同框的 `+createNewPizza()`、`+getPizza()` 是正体。按第一节的约定，斜体就是抽象——`PizzaBuilder` 是抽象类，`buildParts()` 是抽象方法。这一条直接就是某个空的答案。另外 `Waiter` 和 `PizzaBuilder` 之间是**空心菱形贴在 Waiter 这一端、细箭头贴在 PizzaBuilder 那一端**；两个子类到 `PizzaBuilder` 是**实线加空心三角、三角贴 PizzaBuilder**；两个子类到 `Pizza` 是**实线细箭头、箭头指进 Pizza**。

**【Java 代码】**（照录信管网「2017 年上半年软件设计师下午案例分析真题文字版」）

```java
class Pizza {
private String parts；
public void setParts(String parts) {     this.parts = parts; }
public String toString() {      return this.parts;   }
}

abstract class PizzaBuilder {
protected Pizza pizza;
public Pizza getPizza() { return pizza;  }
public void createNewPizza() {      pizza = new Pizza();     }
public  (1)   ;
}

class HawaiianPizzaBuilder extends PizzaBuilder {
public void buildParts() {     pizza.setParts("cross + mild + ham&pineapp1e”};
}

class SpicyPizzaBuilder extends PizzaBuilder {
public void buildParts() { pizza.setParts("pan baked + hot + pepperoni&salami");          }
}

class Waiter {
private PizzaBuilder pizzaBuilder;
public void setPizzaBuilder(PizzaBuilder pizzaBuilder) {  /*设置构建器*/
( 2 )    ;
}
public Pizza getPizza(){ return pizzaBuilder.getPizza(); }
public void construct() {      /*构建*/
pizzaBuilder.createNewPizza();
( 3 )   ;
}
}

Class FastFoodOrdering {
public static viod mainSting[]args) {
Waiter waiter = new Waiter();
PizzaBuilder hawaiian_pizzabuilder = new HawaiianPizzaBuilder();
( 4 )    ;
( 5 )    ;
System.out.println("pizza: " + waiter.getPizza());
}
}
```

程序的输出结果为：`Pizza:cross + mild + ham&pineapple`

**这份也印得毛糙，四处提前说明**：`private String parts；` 结尾是个全角分号；`ham&pineapp1e”};` 里的 `1` 是数字一、右引号和花括号本该是 `"` 和 `)`，整行应为 `pizza.setParts("cross + mild + ham&pineapple"); }`——末尾那句输出结果里拼的是 `pineapple`，正好替你校对了这个单词；`Class FastFoodOrdering` 的 C 该小写；`public static viod mainSting[]args)` 应是 `public static void main(String[] args)`。**四处仍然一处都不落在五个空上。**

**先别看答案，按第四节的顺序自己走一遍**：先把类图五个框和代码里的五个类型对上号（`FastFoodOrdering` 又是那个只为跑 `main` 而存在、不在类图上的类），再从上往下扫，遇到空就问自己"这个位置该往类图哪个格子抄"。给三条提示，不给答案：

1. 空 (1) 在抽象类 `PizzaBuilder` 里、`public` 后面跟一个分号收尾——回头看类图上哪一行印成了斜体。
2. 空 (2) 在 `setPizzaBuilder(PizzaBuilder pizzaBuilder)` 的方法体里，注意**参数名和成员变量名一模一样**，这不是巧合，是出题人埋的坑。
3. 空 (4)、(5) 在 `main` 里，`Waiter` 只有三个方法，末尾那句 `waiter.getPizza()` 已经用掉一个；两个空的**先后顺序不能反**，想一想 `construct()` 里第一句要用到什么。

**参考答案**（做完再看）：

- **(1) `abstract void buildParts()`。** 类图上 `+buildParts()` 是斜体＝抽象方法，抽象方法只有声明没有方法体、以分号结尾，模板已经给了 `public` 和分号，所以填 `abstract void buildParts()`。返回类型是 `void`，由两个子类里的 `public void buildParts(){...}` 反证。
- **(2) `this.pizzaBuilder=pizzaBuilder`。** 参数名和成员变量名同名时，方法体里光写 `pizzaBuilder` 指的是参数，要指成员变量必须写 `this.`。**漏掉 `this.` 是这道题最狠的坑**：写成 `pizzaBuilder=pizzaBuilder` 语法完全合法、编译照过，但等于自己给自己赋值，成员变量还是空的，程序跑到 `construct()` 就崩（空指针）。
- **(3) `pizzaBuilder.buildParts()`。** `construct()` 的注释写着"构建"，第一句已经 `createNewPizza()` 造了个空比萨，第二句自然是往里填料。`PizzaBuilder` 三个方法里 `createNewPizza` 用过了、`getPizza` 是取结果，只剩 `buildParts`。
- **(4) `waiter.setPizzaBuilder(hawaiian_pizzabuilder)`。** 上一行刚 `new` 了一个夏威夷生成器，它得交给服务员——`Waiter` 里正好有个 `setPizzaBuilder`。**为什么是夏威夷不是香辣？** 末尾那句输出结果是 `cross + mild + ham&pineapple`，正是 `HawaiianPizzaBuilder` 里 `setParts` 填的那串；`SpicyPizzaBuilder` 填的是 `pan baked + hot + pepperoni&salami`，对不上。这就是证据。
- **(5) `waiter.construct()`。** 剩下的那个方法，也是"照着流程做一遍"这个动作本身。
- **顺序为什么不能反**：`construct()` 里第一句就要用 `pizzaBuilder`，而 `pizzaBuilder` 是靠 (4) 那句塞进去的；先 `construct()` 后 `setPizzaBuilder()`，程序一样崩在空指针上。
- **评分点**：五空各 3 分。(2) 写成 `this.pizzaBuilder = pizzaBuilder;` 带分号带空格都等价；(4)(5) 里的变量名必须照抄代码里的 `waiter`、`hawaiian_pizzabuilder`，自己另起名字判不了对。填完通读一遍，输出应当是 `pizza: cross + mild + ham&pineapple`——注意这跟题干印的 `Pizza:cross + mild + ham&pineapple` 大小写和空格对不上，是题干印刷的问题，不影响填空，**你要用它确认的只有一件事：用的是夏威夷那个生成器**。

**两道题对照着看**：业务的皮换了、模式换了，五个空的形态一模一样——一个接口或抽象方法的声明、一个类型名、一到两句"调用别的方法"、`main` 里一两句装配。**这就是这道题能十分钟做完的原因。**

### 六、收口

三步，两道题都是这么做下来的：**① 读说明，记住模式名和角色名；② 扫类图，把每个框、每个方法名、每条线记在心里，斜体标出来的单独记一笔；③ 从上往下扫代码，遇到空先判它属于哪一类，再回类图或代码里抄名字。** 十分钟这么切：读说明和类图 3 分钟，扫代码填空 5 分钟，顺着 `main` 走一遍验算 2 分钟。

几点补充：

- **答案只写答案。** 这道题只要一个标识符或一行语句，不写理由、不写"因为"。带不带末尾分号、空格多少都不影响。
- **大小写必须照抄。** 卷面上的 `Attach`、`Notify` 首字母大写，`buildParts`、`setPizzaBuilder` 是小驼峰，抄错一个字母就是另一个名字。这是这道题唯一会因为"手滑"丢分的地方。
- **五个空互相独立，卡住就跳。** 按点给分，第 (4) 空想不出来不影响 (1)(2)(3)(5) 拿分；十分钟到点还差一个就先翻页，留到机动时间回头补。
- 下午题官方不公布标准答案，市面答案都是老师校对的；这道题的答案是代码，对错比别的题硬，但也别为分号、空格这类出入纠结。培训资料对这道题的要求是「**要求能拿到 12 分以上**」，讲义 48 给的目标是 13 分。

---

## 考试怎么考

五个空翻来覆去只有五种形态，认形态比认模式还管用：

**形态一：接口里的方法声明。** 长相是 `interface X{ public ( n ); }`。解法：去类图上找 `X` 那个框，把方法名连括号抄下来，返回类型图上没写就是 `void`。常见错法是写成带花括号的空方法体 `void update(){}`——接口里的方法不能有方法体。

**形态二：抽象类里的抽象方法声明。** 长相是抽象类里 `public ( n ) ;`。解法：找类图上**印成斜体**的那个方法名，写成 `abstract 返回类型 方法名()`。常见错法是漏掉 `abstract`，那样就成了没有方法体的普通方法，编译不过。

**形态三：类型名。** 出现在三个位置——泛型尖括号里（`List< ( n ) >`）、成员变量声明处、构造方法或普通方法的参数表里。解法：**不要看类图上离得最近的那个框，要看代码里已经写死的赋值语句和调用语句**。真题 1 的 (2) 靠 `new ArrayList<Observer>()` 定死，(4) 靠 `main` 里 `Subject subjectA=...` 定死。常见错法是填具体类（`DocExplorer`、`OfficeDoc`），而设计模式的要害恰恰是**只依赖抽象的那一层**，所以这种空九成填接口名或抽象类名。

**形态四：方法体里的一行调用。** 长相是某个方法体里孤零零一个 `( n );`。解法：看这个方法体里已有的语句用到了哪个对象（循环变量、成员变量、参数），再看那个对象的类型在类图上有哪些方法，把还没用过的那个填上。常见错法是自己去写业务逻辑——培训资料说得很清楚，「这个函数体并不是要写一段真正的程序实现代码，**而是调用形式的**」。

**形态五：赋值，或者 `main` 里的装配句。** 赋值那种要当心**参数名和成员变量同名**，必须写 `this.`；`main` 里那种要当心**先后顺序**，一般是"先把零件塞进去，再让它跑"。这两种错法都有同一个特征：**编译照过，一跑就空指针**，卷面上看不出来，只能靠顺着 `main` 走一遍验算。

至于"认出是哪个模式"——题干每次都直说，所以它不是必要步骤，但**认出来能预判还没读到的代码长什么样**：看见"观察者"就知道会有一张观察者表、一个注册方法、一个遍历通知的循环；看见"生成器"就知道会有一个只管流程的指挥角色和一族只管填内容的生成器。高频的八到十个模式各自的骨架在 28、29。

---

## 练习

**【真题·2018上】**（试题六，Java；同场试题五是同一场景的 C++ 版）

**【说明】** 生成器(Builder)模式的意图是将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示。图6-1所示为其类图。

（图 6-1 本篇没有收录。这正好当成一次加练：**这五个空全部能从代码本身推出来，不看类图也做得出**——做完你就明白，类图是加速器，代码才是判据。）

**【Java代码】**（照录信管网「2018 年上半年软件设计师下午案例分析真题文字版」；该页代码块的空格被整体吞掉了，下面把间隔还原回来，用词与符号一字未动——包括 `ConcreteBuilder1` 后面那个多余的冒号、`∥` 这个本该是 `//` 的注释符、以及 `directorl` 里那个本该是数字 1 的小写 l）

```java
import java.util.*；
class Product{
  private String partA;
  private String partB;
  public Product(){}
  public void setPartA(String s){partA=s;}
  public void setPartB(String s){partB=s;}
}
interface Builder{
  public (1);
  public void buildPartB();
  public (2);
}
class ConcreteBuilder1: implements Builder{
  private Product product;
  public ConcreteBuilder1(){product=new Product();}
  public void buildPartA(){（3）("Component A");}
  public void buildPartB(){（4）("Component B");}
  public Product getResult(){return product;}
}
class ConcreteBuilder2 implements Builder{
  ∥代码省略
}
class Director{
  private Builder builder;
  public Director(Builder builder){this.builder=builder;}
  public void construct(){
    （5）
    ∥代码省略
  }
}
class Test{
  public static void main(String[] args){
    Director director1=new Director(new ConcreteBuilder1());
    directorl.construct();
  }
}
```

将应填入(n)处的字句写在答题纸的对应栏内。

### 参考答案

- **(1) `void buildPartA()`　(2) `Product getResult()`。** 形态一（接口里的方法声明）。`Builder` 是接口，`ConcreteBuilder1` 实现了它，所以接口上的方法必须在 `ConcreteBuilder1` 里全部出现；`ConcreteBuilder1` 里正好三个方法 `buildPartA`／`buildPartB`／`getResult`，接口里已经印出了 `buildPartB`，剩下的两个就是这两个空。返回类型各自去子类那一行抄：`public void buildPartA()` 给出 `void`，`public Product getResult(){return product;}` 给出 `Product`。**这两个空谁填哪一句都算对**——接口里方法的先后顺序在 Java 里没有任何语法含义，公开的答案解析也明说二者可以互换。按代码里的出场顺序填是最省事的写法，不必纠结。
- **(3) `product.setPartA`　(4) `product.setPartB`。** 形态四（方法体里的调用），但只填到方法名为止，因为括号和参数模板里已经给了。判据：这个类里唯一能被调用的对象是成员变量 `product`（构造方法里 `product=new Product();` 造出来的），`Product` 上只有 `setPartA`、`setPartB` 两个方法，按方法名和参数 `"Component A"`／`"Component B"` 一一对上。写成 `this.product.setPartA` 等价。
- **(5) `builder.buildPartA();`。** 形态四。`Director` 手里只有成员变量 `builder`，`construct()` 的职责是"按固定步骤走一遍"，所以填的一定是 `builder.` 加上 `Builder` 上的某个构建方法。**这个空是全题最松的一个**：它后面紧跟着一行"代码省略"，谁也说不准出题人省掉的是哪几句，所以填 `builder.buildPartA();` 或 `builder.buildPartB();` 都算对——按流程第一步走，写 `buildPartA()` 最自然。**这个空要带分号**，因为模板里没给。
- **评分点**：五空各 3 分。(3)(4) 只写 `setPartA`／`setPartB` 而漏掉 `product.` 判不了对——方法体里没有这个名字的局部方法。(5) 漏分号一般不扣，写成 `buildPartA()` 漏掉 `builder.` 则错。
- **四处印刷毛病顺带认一下**：`import java.util.*；` 结尾是全角分号；`ConcreteBuilder1` 后面多了个冒号，同场试题五的 C++ 代码里这一行正是 `class ConcreteBuilder1 : public Builder{`，冒号在 C++ 那边才对，Java 里不该有；`∥` 是注释符 `//`；`directorl.construct()` 里是小写 l，上一行定义的变量叫 `director1`（数字一）。**仍然一处都不落在五个空上**——这是本课第三道字面上磕磕绊绊、却照样能满分的真题了。

---

## 速记

- 两道选做题同场景同模式、一 C++ 一 Java；**认题头"阅读下列说明和 ×× 代码"，别认题号**；必须选定，未选按题号最小的判
- 一道题五个空、各 3 分、互相独立，卡住就跳；十分钟＝读说明与类图 3＋填空 5＋顺 `main` 走一遍 2
- 核心动作：**在类图上找到对应的格子，把名字抄下来**；类图与代码打架时以代码里已写死的那一行为准
- 类图速查：`⇢▷`＝`implements`，`──▷`＝`extends`，`──▶`＝成员变量，`+`＝public，**斜体＝abstract**
- 五种空：接口方法声明／抽象方法声明（记得 `abstract`）／类型名（多半填接口或抽象类，不填具体类）／一行调用（不写业务逻辑）／赋值与 `main` 装配
- 两个"编译过但一跑就崩"的坑：参数与成员同名时漏 `this.`；`main` 里先跑再装配、顺序写反
- 大小写照抄，末尾分号可有可无；只写答案不写理由
