# 53 · 下午题 6：Java + 设计模式实战（最该拿满分的一题）

> 真题：观察者、生成器两道完整真题（外部资料，年份待核实）｜阶段B（高频模式类图骨架）｜未讲（09-04 补缺课）

---

## 第 0 层 · 定位

**这一课回答**：下午题 6（Java + 设计模式，15 分，与 C++ 二选一）怎么拿满：Java 语法够用部分、题干点名的模式怎么填类名/方法名/调用。

**前后关系**：28/29 是知识底座；48 定了它排第 1 位、10 分钟、目标 13–15 分。

**分值与去向**：15 分，全卷唯一「应该拿满」的题，只考基本语法不涉及算法；高频模式类图骨架要默得出，阶段B。

---

## 第 1 层 · 理解

### 一句话

> 下午题 6 给你**一个设计模式的类图 + 一份挖了 5 个空的 Java 代码**，让你把空填上。**题干会明说用的是哪个模式**，所以它考的不是"你能不能想出设计方案"，而是**「你能不能照着类图，把接口方法声明和对象调用语句写对」**。

### 痛点："我不会 Java" —— 这是本题最大的误解

很多零基础的人看到 Java 代码就放弃，实际上：

- **这题不考 Java 特性**。没有泛型通配符、没有 Lambda、没有并发、没有 Stream。用到的语法只有：`class`、`interface`、`implements`、`extends`、`abstract`、`new`、`for` 循环、方法调用。
- **五个空里通常有三个是"照抄类图"**：类图上写着 `+update()`，代码里 `interface Observer{ public ( 1 ); }` 的空就是 `void update();`。这不需要懂 Java，只需要认得类图。
- **另外两个空是"照抄调用形式"**：函数体里不是写真正的业务逻辑，而是**调用另一个已经存在的方法**——那个方法名在类图或代码别处一定出现过。

外部资料的原话说得很直白：
> 这一题**完全可以从英语角度去理解，根据关键词去联系代码上下文**，都能得出答案，毫无难度，**每个人都能拿满分，要先树立信心**。

### 一条主线

```
题干直接告诉你：现采用【XX 设计模式】实现该需求，类图如图 6-1
   ↓ 所以第一步不是读代码，是【回忆这个模式的骨架】
   ↓
   高频八个模式的骨架（讲义 28/29 已讲，本课只需能默画）：
     观察者 → Subject(Attach/Detach/Notify) + Observer(update)
     生成器 → Director/Waiter(construct) + Builder(buildParts/getResult)
     策略   → Context + Strategy(algorithm)
     工厂方法 → Creator(factoryMethod) + Product
     ...
   ↓ 第二步：把类图和代码对应起来
   ↓
   五个空必然属于两类之一：
   ┌─【类型A·纯定义】接口方法声明、抽象方法声明、类型名
   │    解法 = 照抄类图上的方法签名
   │    例：类图写 +update()  → 代码填 void update();
   └─【类型B·调用形式】函数体，但不是真业务逻辑，是调用别的方法
        解法 = 在类图/代码里找那个被调用的方法名，写成调用语句
        例：Notify() 的函数体 → obs.update();
   ↓ 第三步：注意 Java 的三个小语法点
        implements 接口 / extends 类 / abstract 方法以分号结尾
```

**一句话收口**：`题干告诉你模式 → 回忆骨架 → 五个空按"抄类图"和"写调用"两类分别处理。`

---

## 第 2 层 · 考点：考试怎么问

### 考点① Java 语法：本题只需要这些（够用即可）

**（1）类与构造方法**
```java
public class Puppy{
    int puppyAge;                          // 成员变量
    public Puppy(String name){             // 构造方法：名称必须与类同名，无返回值
        System.out.println("小狗的名字是 : " + name);
    }
    public void setAge(int age){ puppyAge = age; }
    public int  getAge(){ return puppyAge; }
}
```
- **构造方法的名称必须与类同名**；
- 如果没有显式定义构造方法，**Java 编译器会提供一个默认构造方法**；
- 一个类**可以有多个构造方法**（重载）。

**（2）创建对象三步**
> **声明 → 实例化（new）→ 初始化（调构造方法）**
```java
Puppy myPuppy = new Puppy("tommy");
```

**（3）访问控制修饰符**

| 修饰符 | 可见范围 | 能修饰什么 |
|---|---|---|
| **private** | **同一类内** | 变量、方法（**不能修饰外部类**） |
| **public** | **对所有类可见** | 类、接口、变量、方法 |
| **protected** | **同一包内的类 + 所有子类** | 变量、方法（**不能修饰外部类**） |

**方法继承规则**（上午题也考）：
- 父类中声明为 **public 的方法，子类中也必须为 public**；
- 父类中声明为 **protected 的方法，子类中要么 protected 要么 public，不能 private**；
- 父类中声明为 **private 的方法，不能被继承**。

**（4）abstract 抽象类与抽象方法**
```java
public abstract class SuperClass{
    abstract void m();                 // 抽象方法：没有方法体，以分号结尾
}
class SubClass extends SuperClass{
    void m(){ ......... }              // 子类必须实现
}
```
- **抽象类不能用来实例化对象**，声明抽象类的唯一目的是为了将来对该类进行扩充；
- **如果一个类包含抽象方法，该类一定要声明为抽象类**；
- **抽象类可以不包含抽象方法**（反向不成立）；
- **任何继承抽象类的子类必须实现父类的所有抽象方法**，除非该子类也是抽象类；
- **抽象方法的声明以分号结尾**：`public abstract void sample();`

**（5）extends 与 implements**

| 关键字 | 用途 | 数量限制 |
|---|---|---|
| **extends** | 继承**类** | **单一继承，只能继承一个类** |
| **implements** | 实现**接口** | **可以同时实现多个接口**（逗号分隔），变相实现多继承 |

```java
public interface A { public void eat(); public void sleep(); }
public interface B { public void show(); }
public class C implements A, B { ... }        // 实现多个接口
public class Penguin extends Animal { ... }   // 继承一个类
```

---

### 考点② 认出设计模式（题干会直说，但要能默画骨架）

**题干的原话形式**：
> 现采用**观察者 (Observer) 设计模式**来实现该需求，所设计的类图如图 6-1 所示。
> 现采用**生成器 (Builder) 模式**实现制作过程，得到如图 6-1 所示的类图。

**高频模式子集**（`计划/00-总体计划.md`「W4 面向对象」节）：**观察者 / 策略 / 工厂方法 / 装饰器 / 适配器 / 外观 / 享元 / 单例**。加上真题实际出现过的**生成器**，共九个。

> ⚠️ **补充**：计划文件「W4 面向对象」节的**已核实真题清单**【真题·2021上/2022下/2024上/2025上】里还有 **责任链、命令、状态、代理** 四个，它们**有明确年份背书却不在上面的九个里**。本课已把这四个的骨架一并列入下表，**不要漏练**。

**必须能默画的骨架（本课核心记忆项）**：

| 模式 | 骨架（角色 + 关键方法） |
|---|---|
| **观察者 Observer** | `Subject`（Attach / Detach / Notify）+ `ConcreteSubject`（setStatus / getStatus + 观察者列表）+ `Observer`（update）<br>⚠️ GoF 里 setState/getState 属 ConcreteSubject；本题真题把它们提到了接口上 |
| **生成器 Builder** | 四角色：`Director/Waiter`（construct / setBuilder）+ `Builder`（createNew / **buildParts** 抽象）+ `ConcreteBuilder`（实现 buildParts、getResult）+ **`Product`**（本题的 Pizza） |
| **策略 Strategy** | `Context`（持有 Strategy 引用）+ `Strategy`（algorithm）+ 具体策略 |
| **工厂方法 Factory Method** | `Creator`（factoryMethod）+ `Product`；子类决定实例化哪个类 |
| **适配器 Adapter** | `Target` + `Adapter` + `Adaptee`；**继承 Adaptee = 类适配器，组合持有 = 对象适配器**（Java 多用后者） |
| **装饰 Decorator** | `Component` + `ConcreteComponent` + `Decorator`（持有 Component）+ 具体装饰 |
| **外观 Facade** | `Facade` 对外统一接口，内部持有多个子系统 |
| **单例 Singleton** | 私有构造 + 私有静态实例 + 公有静态 getInstance |
| **享元 Flyweight** | `FlyweightFactory`（共享池）+ `Flyweight`；**区分内部状态（可共享）与外部状态（不可共享）** |
| **责任链 Chain** | `Handler`（handleRequest + 持有 successor）+ 具体 Handler；沿链传递直到有人处理 |
| **命令 Command** | `Invoker` + `Command`（execute）+ `Receiver`；把请求封装成对象，支持撤销/日志 |
| **状态 State** | `Context`（持有 State 引用）+ `State`（handle）+ 具体状态类；状态改变则行为改变 |
| **代理 Proxy** | `Subject` + `Proxy`（持有 RealSubject）+ `RealSubject`；控制对目标的访问 |

**陷阱**：
- ⚠️ **题干明说了模式名，不要自己另判一个**。有时你觉得"这更像策略模式"，但题干说是状态模式——**以题干为准**。
- ⚠️ 上午题会考"**判断分类归属**"（生成器属创建型、享元属结构型），下午题不考分类，只考骨架。

---

### 考点③ 填空类型 A：纯定义（照抄类图）

**外部资料的原话**：
> 面向对象的程序填空分为两类，**一个是考察纯定义**，如接口类，抽象类，接口类中的函数定义等，这些根据程序代码可以快速判断出。

**长什么样**：
```java
interface Observer{
    public ( 1 );        // ← 填 void update();
}
```

**怎么解**：
1. 看**类图**上这个接口/抽象类有哪些方法；
2. 照着写方法签名（**返回类型 + 方法名 + 参数列表 + 分号**）。

**关键细节**：
- 接口里的方法**没有方法体，以分号结尾**；
- 抽象方法同理：`abstract void buildParts();`
- 类图上 `+update()` 的 `+` 表示 public，`-` 表示 private，`#` 表示 protected；
- 类图上如果方法名是**斜体**，表示这是**抽象方法**。

**陷阱**：
- ⚠️ **别忘了分号**。接口方法/抽象方法末尾必须有 `;`，写成 `{}` 就错了。
- ⚠️ **返回类型别漏**。类图上 `+update()` 没写返回类型时，默认 `void`。

---

### 考点④ 填空类型 B：调用形式（在代码里找被调用的方法）

**外部资料的原话**：
> 另一类，就是**关于设计的，填写函数体，但是这个函数体并不是要写一段真正的程序实现代码，而是调用形式的**，都有调用函数的，**这些调用函数一般在程序中，或者在说明和类图中可以找到**，考察的是调用形式。

**长什么样**：
```java
public void Notify(){
    for(Observer obs : this.myObs){
        ( 3 );                     // ← 填 obs.update();
    }
}
```

**怎么解（三步）**：
1. **看这个方法叫什么名字**——`Notify()` 的语义是"通知所有观察者"；
2. **看循环变量/上下文对象是什么**——`obs` 是 `Observer` 类型；
3. **在类图或代码里找 Observer 有什么方法**——只有 `update()` → 填 `obs.update();`

**再看一例**：
```java
public void construct(){       /*构建*/
    pizzaBuilder.createNewPizza();
    ( 3 );                     // ← 填 pizzaBuilder.buildParts()
}
```
1. 方法名 `construct` = 生成器模式里 Director 的"指挥构建"；
2. 上一行已经调了 `pizzaBuilder.createNewPizza()`；
3. 类图上 PizzaBuilder 的方法有 `createNewPizza()`、`buildParts()`、`getPizza()`——按生成器骨架，创建完就该**建造各部分** → 填 `pizzaBuilder.buildParts()`。

**陷阱**：
- ⚠️ **别写真正的业务实现**。看到 `buildParts()` 要填，不要去写"设置芝士、设置火腿"的具体代码——**填的是调用语句**。
- ⚠️ **注意调用者是谁**：是 `this.xxx()`、`obs.xxx()` 还是 `waiter.xxx()`？看上下文的变量名。

---

## 完整算例

### 算例 A：观察者模式（五空全解）

【真题·年份待核实】（来源：外部培训资料"历年典型真题 1"）

#### 【说明】

某文件管理系统中定义了类 **OfficeDoc** 和 **DocExplorer**。**当类 OfficeDoc 发生变化时，类 DocExplorer 的所有对象都要更新其自身的状态**。现采用**观察者 (Observer) 设计模式**来实现该需求，所设计的类图如图 6-1 所示。

![真题 1：图 6-1 观察者模式类图](../外部资源/转录md/images/fig_d15_s094.png)

**类图要点**：`Subject` 有 `+Attach()`、`+Detach()`、`+Notify()`；`Observer` 有 `+update()`；`OfficeDoc` 实现 Subject，`DocExplorer` 实现 Observer。

> 📌 **注意**：类图上 `DocExplorer` 的关联箭头指向的是具体类 **`OfficeDoc`**（不是 `Subject`）；而代码里为了面向接口编程，构造参数用的是 `Subject`。**空 (4) 的真正依据不在类图，在 main 里**——见下文。

#### 【Java 代码】

![真题 1：Java 代码（第一部分）](../外部资源/转录md/images/fig_d15_s095.png)

![真题 1：Java 代码（第二部分）](../外部资源/转录md/images/fig_d15_s096.png)

代码骨架（五个空）：
```java
import java.util.*;

interface Observer{
    public ( 1 );                              // ← 空(1)
}

interface Subject{
    public void Attach(Observer obs);
    public void Detach(Observer obs);
    public void Notify();
    public void setStatus(int status);
    public int  getStatus();
}

class OfficeDoc implements Subject{
    private List<( 2 )> myObs;                 // ← 空(2)
    private String mySubjectName;
    private int m_status;

    public OfficeDoc(String name){
        mySubjectName = name;
        this.myObs = new ArrayList<Observer>();
        m_status = 0;
    }
    public void Attach(Observer obs){ this.myObs.add(obs); }
    public void Detach(Observer obs){ this.myObs.remove(obs); }
    public void Notify(){
        for(Observer obs : this.myObs){
            ( 3 );                             // ← 空(3)
        }
    }
    public void setStatus(int status){
        m_status = status;
        System.out.println("SetStatus subject["+mySubjectName+"]status:"+status);
    }
    public int getStatus(){ return m_status; }
}

class DocExplorer implements Observer{
    private String myObsName;
    public DocExplorer(String name, ( 4 ) sub){    // ← 空(4)
        myObsName = name;
        sub.( 5 );                                 // ← 空(5)
    }
    public void update(){
        System.out.println("update observer["+myObsName+"]");
    }
}
```

> ⚠️ **本课对外部转录代码做了三处订正**（原图为 PPT 截图，有排版讹误）：`Lists<` → `List<`、`system.out` → `System.out`、`mySubject.Name` → `mySubjectName`。**订正后整份代码 `javac` 编译通过并正常运行**，输出 `SetStatus subject[...]status:...` / `update observer[...]`。

#### 分步解

**空 (1)｜类型 A（纯定义）**
- 看类图：`Observer` 接口只有一个方法 `+update()`；
- 接口方法无方法体，以分号结尾；
- 返回类型：类图未标，且 `DocExplorer.update()` 的实现里没有 return → `void`。
- → **(1) = `void update();`**

**空 (2)｜类型 A（类型名）**
- `private List<( 2 )> myObs;` 是主题持有的**观察者列表**；
- 下一行构造方法里已经写了 `this.myObs = new ArrayList<Observer>();`——**答案在代码里直接给出了**；
- → **(2) = `Observer`**

> 💡 这就是"捷径 B"的典型：不需要懂观察者模式，只需要看下一行。

**空 (3)｜类型 B（调用形式）**
- 方法名 `Notify()` = 通知所有观察者；
- 循环变量 `obs` 是 `Observer` 类型；
- `Observer` 只有一个方法 `update()`；
- → **(3) = `obs.update();`**

**空 (4)｜类型 A（类型名）**
- `public DocExplorer(String name, ( 4 ) sub)` 是构造方法的第二个参数类型；
- **决定性依据在测试类**：main 里写的是 `Subject subjectA = new OfficeDoc("subject A");` 然后 `new DocExplorer("observer A", subjectA)`——实参 `subjectA` 的**声明类型就是 `Subject`**，形参若写成 `OfficeDoc` 会**编译不过**；
- （类图上 DocExplorer 关联的是 OfficeDoc，但代码面向接口，以 main 的声明类型为准）
- → **(4) = `Subject`**

**空 (5)｜类型 B（调用形式）**
- 上下文：观察者在**构造时把自己注册到主题**上；
- `Subject` 接口里负责注册的方法是 `Attach(Observer obs)`；
- 要注册的是"自己" → `this`；
- → **(5) = `Attach(this);`**

**答案**：
- (1) `void update();`
- (2) `Observer`
- (3) `obs.update();`
- (4) `Subject`
- (5) `Attach(this);`

> 💡 **复盘**：五个空里，(2) 直接抄下一行，(1)(4) 抄类图，(3)(5) 靠"方法名语义 + 接口里有哪些方法"推断。**全程没有用到任何 Java 高级特性。**

---

### 算例 B：生成器模式（五空全解）

【真题·年份待核实】（来源：外部培训资料"历年典型真题 2"）

#### 【说明】

某快餐厅主要制作并出售儿童套餐，一般包括主餐（各类比萨）、饮料和玩具，**其餐品种类可能不同，但其制作过程相同**。前台服务员 (**Waiter**) 调度厨师制作套餐。现采用**生成器 (Builder) 模式**实现制作过程，得到如图 6-1 所示的类图。

![真题 2：图 6-1 生成器模式类图](../外部资源/转录md/images/fig_d15_s098.png)

**类图要点**：`Waiter` 有 `+construct()`、`+setPizzaBuilder()`、`+getPizza()`；`PizzaBuilder` 有 `+createNewPizza()`、`+buildParts()`（斜体 = 抽象）、`+getPizza()`；`HawaiianPizzaBuilder` 和 `SpicyPizzaBuilder` 继承 PizzaBuilder，各自实现 `+buildParts()`；PizzaBuilder 关联 `Pizza`。

> 💡 **注意"其餐品种类可能不同，但其制作过程相同"**——这句话就是生成器模式的定义（"将一个复杂类的表示与其构造相分离，使得相同的构建过程能够得出不同的表示"）。

#### 【Java 代码】

![真题 2：Java 代码（含 5 处填空）](../外部资源/转录md/images/fig_d15_s099.png)

代码骨架：
```java
class Pizza {
    private String parts;
    public void setParts(String parts){ this.parts = parts; }
    public String toString(){ return this.parts; }
}

abstract class PizzaBuilder {
    protected Pizza pizza;
    public Pizza getPizza(){ return pizza; }
    public void createNewPizza(){ pizza = new Pizza(); }
    public ( 1 );                                    // ← 空(1)
}

class HawaiianPizzaBuilder extends PizzaBuilder {
    public void buildParts(){ pizza.setParts("cross + mild + ham&pineapple"); }
}
class SpicyPizzaBuilder extends PizzaBuilder {
    public void buildParts(){ pizza.setParts("pan baked + hot + pepperoni&salami"); }
}

class Waiter {
    private PizzaBuilder pizzaBuilder;
    public void setPizzaBuilder(PizzaBuilder pizzaBuilder){   /*设置构建器*/
        ( 2 );                                       // ← 空(2)
    }
    public Pizza getPizza(){ return pizzaBuilder.getPizza(); }
    public void construct(){                          /*构建*/
        pizzaBuilder.createNewPizza();
        ( 3 );                                        // ← 空(3)
    }
}

class FastFoodOrdering {
    public static void main(String[] args){
        Waiter waiter = new Waiter();
        PizzaBuilder hawaiian_pizzabuilder = new HawaiianPizzaBuilder();
        ( 4 );                                        // ← 空(4)
        ( 5 );                                        // ← 空(5)
        System.out.println("pizza: " + waiter.getPizza());
    }
}
```
程序的输出结果为：`Pizza:cross+mild+ham&pineapple`

#### 分步解

**空 (1)｜类型 A（抽象方法声明）**
- `PizzaBuilder` 是 `abstract class`；
- 类图上 `buildParts()` 是**斜体**（抽象方法）；
- 两个子类都实现了 `public void buildParts()`，所以父类必须声明这个抽象方法；
- 抽象方法**以分号结尾**；
- → **(1) = `abstract void buildParts();`**

**空 (2)｜类型 B（赋值）**
- 方法名 `setPizzaBuilder(PizzaBuilder pizzaBuilder)` = 典型 setter；
- 参数名和成员变量同名，需要用 `this` 区分；
- → **(2) = `this.pizzaBuilder = pizzaBuilder`**

**空 (3)｜类型 B（调用形式）**
- 方法名 `construct()` = 生成器模式里 Director 的"指挥构建"；
- 上一行已 `pizzaBuilder.createNewPizza();`（新建一个空 Pizza）；
- 按生成器骨架，接下来要**建造各部分**；
- → **(3) = `pizzaBuilder.buildParts()`**

**空 (4)｜类型 B（调用形式）**
- main 里已创建 `waiter` 和 `hawaiian_pizzabuilder`；
- 要让 waiter 用这个 builder → 调 `setPizzaBuilder`；
- → **(4) = `waiter.setPizzaBuilder(hawaiian_pizzabuilder)`**

**空 (5)｜类型 B（调用形式）**
- 设置好 builder 后，要真正开始构建，最后 `waiter.getPizza()` 才有东西；
- → **(5) = `waiter.construct()`**

**验算**：按 (4)(5) 的顺序执行 → waiter 用 HawaiianPizzaBuilder → construct() 先 createNewPizza() 再 buildParts() → parts = "cross + mild + ham&pineapple" → 输出内容与题干给的结果**一致** ✓

**答案**：
- (1) `abstract void buildParts();`
- (2) `this.pizzaBuilder = pizzaBuilder`
- (3) `pizzaBuilder.buildParts()`
- (4) `waiter.setPizzaBuilder(hawaiian_pizzabuilder)`
- (5) `waiter.construct()`

> 💡 **复盘**：本题的 (4)(5) 有一个隐藏的**顺序陷阱**——必须先 `setPizzaBuilder` 再 `construct`，反了就会空指针。**题干给的"程序输出结果"就是用来验算顺序的**。

---

### 算例 C：两道真题的共同套路

| | 真题 1（观察者） | 真题 2（生成器） |
|---|---|---|
| 空 (1) | 接口方法声明 `void update();` | 抽象方法声明 `abstract void buildParts();` |
| 空 (2) | 泛型类型名 `Observer`（下一行有答案） | setter 赋值 `this.x = x` |
| 空 (3) | 循环内调用 `obs.update();` | 委托调用 `pizzaBuilder.buildParts()` |
| 空 (4) | 参数类型名 `Subject` | main 里的调用 `waiter.setPizzaBuilder(...)` |
| 空 (5) | 构造中注册 `Attach(this);` | main 里的调用 `waiter.construct()` |

**规律**：
- **前两个空基本是"定义类"**（方法声明、类型名）；
- **后三个空基本是"调用类"**（对象.方法()）；
- **答案几乎都能在类图或代码别处找到原型**。

---

## 速记

**1. 选题**
> **选试题 6（Java），不选试题 5（C++）。两题同场景同模式，只练 Java 一门**

**2. 做题顺序**
> **全卷第一个做，10 分钟，目标满分**

**3. 五个空的两种类型**
> **类型A 纯定义 → 照抄类图的方法签名（接口/抽象方法末尾加分号）**
> **类型B 调用形式 → 在类图/代码别处找被调用的方法名，写成调用语句**

**4. Java 三个关键语法**
> **extends 继承类（单一）；implements 实现接口（可多个，逗号分隔）**
> **abstract 方法无方法体、以分号结尾；含抽象方法的类必须是抽象类**
> **构造方法与类同名、无返回值**

**5. 访问修饰符**
> **private 同类内；public 所有类；protected 同包 + 所有子类**
> **private 和 protected 不能修饰外部类**

**6. 高频九模式的骨架**
> **观察者 Attach/Detach/Notify + update**
> **生成器 construct/setBuilder + createNew/buildParts/getResult**
> **策略 Context + algorithm；工厂方法 Creator.factoryMethod**
> **适配器 Target/Adapter/Adaptee；装饰 Component + Decorator**
> **外观统一接口；单例私有构造 + getInstance；享元共享池**

**7. 验算手段**
> **题干给的"程序输出结果"是用来验算填空顺序的**——比对的是**拼装内容**（选了哪个 Builder、先 set 后 construct），**不是逐字符比对大小写和空格**（真题原件的输出常有排版差异）。

**8. 心态**
> **完全可以从英语角度理解，根据关键词联系上下文，每个人都能拿满分**

---

## 自测练习

**练习 1【模拟·下午题型】** 阅读下列说明、类图和 Java 代码，将应填入 (n) 处的字句写在答题纸的对应栏内。

**【说明】**
某图形绘制系统需要支持多种图形（圆形 Circle、矩形 Rectangle）的绘制。系统希望**在不修改已有图形类的前提下，动态地为图形添加边框、阴影等附加效果**。现采用**装饰器 (Decorator) 设计模式**实现，类图如下：

```
        <<interface>> Shape
        + draw()
              △
       ┌──────┼──────────┐
    Circle  Rectangle   ShapeDecorator (abstract)
                         # decoratedShape : Shape   （# = protected）
                         + draw()
                              △
                        ┌─────┴─────┐
                 BorderDecorator  ShadowDecorator
                    + draw()         + draw()
```

**【Java 代码】**
```java
interface Shape {
    public ( 1 );
}

class Circle implements Shape {
    public void draw(){ System.out.println("Shape: Circle"); }
}

class Rectangle implements Shape {
    public void draw(){ System.out.println("Shape: Rectangle"); }
}

abstract class ShapeDecorator implements Shape {
    protected ( 2 ) decoratedShape;
    public ShapeDecorator(Shape decoratedShape){
        ( 3 );
    }
    public void draw(){
        decoratedShape.draw();
    }
}

class BorderDecorator extends ShapeDecorator {
    public BorderDecorator(Shape decoratedShape){
        super(decoratedShape);
    }
    public void draw(){
        ( 4 );
        System.out.println("Border added");
    }
}

public class DecoratorDemo {
    public static void main(String[] args){
        Shape circle = new Circle();
        Shape borderedCircle = new BorderDecorator( ( 5 ) );
        borderedCircle.draw();
    }
}
```
程序的输出结果为：
```
Shape: Circle
Border added
```

---

### 参考答案

**(1) = `void draw();`**
- 类型 A（纯定义）。类图上 `Shape` 接口只有 `+draw()`；接口方法无方法体、以分号结尾；两个实现类的 `draw()` 都是 `public void`，无返回值 → `void draw();`

**(2) = `Shape`**
- 类型 A（类型名）。类图上 `ShapeDecorator` 的成员 `- decoratedShape : Shape` 已直接标出类型；构造方法的参数也是 `Shape decoratedShape` → `Shape`

**(3) = `this.decoratedShape = decoratedShape`**
- 类型 B（赋值）。构造方法把参数存进成员变量，参数名与成员名相同，必须用 `this` 区分。

**(4) = `super.draw();`**（或 `decoratedShape.draw();`）
- 类型 B（调用形式）。装饰器的核心是"**先执行被装饰对象的原有行为，再加上自己的附加行为**"。
- 从输出结果验算：先打印 `Shape: Circle`（原有行为），再打印 `Border added`（附加行为）→ 空 (4) 必须先调用被装饰对象的 draw。
- 父类 `ShapeDecorator.draw()` 里正是 `decoratedShape.draw();` → 调 `super.draw();` 等价，两种写法均可。
> ⚠️ **「均可」是有前提的**：字段声明为 **`protected`**（子类可见）。**若类图上写成 `-`（private），则子类只能写 `super.draw();`**，`decoratedShape.draw();` 会编译不过。本题类图标的是 `#`（protected），故两种都行。

**(5) = `circle`**
- 类型 B（调用形式）。main 里已创建 `Shape circle = new Circle();`，要给它加边框 → 把 circle 传进装饰器构造方法。
- 验算：`new BorderDecorator(circle).draw()` → 先 `circle.draw()` 输出 "Shape: Circle"，再输出 "Border added"，与题干给的输出结果**内容一致** ✓（题干印的是 `Pizza:cross+mild+ham&pineapple`，实际运行输出 `pizza: cross + mild + ham&pineapple`——**大小写与空格的差异来自真题原件排版，不影响验算**）

**得分复盘**：五个空里 (1)(2) 直接抄类图，(3) 是标准 setter 写法，(4)(5) 靠"输出结果倒推执行顺序"。**全题不需要理解装饰器模式的设计哲学，只需要认类图 + 读输出。**

---

## 考题回顾

| # | 出处 | 考点 | 状态 |
|---|---|---|---|
| 1 | 下午题 6·观察者模式（外部资料"历年典型真题 1"） | 接口方法声明、泛型类型名、循环内调用、构造中注册 | 已作为算例 A 五空全解，**年份待核实** |
| 2 | 下午题 6·生成器模式（外部资料"历年典型真题 2"） | 抽象方法声明、setter、委托调用、main 中调用顺序 | 已作为算例 B 五空全解，**年份待核实** |

> ⚠️ **本课练习尚未作答**，需在课堂检验环节收题批改后回填。
> ⚠️ **真题储备不足**：目前只有 2 道完整 Java 设计模式真题，覆盖观察者、生成器两个模式。`计划/00-总体计划.md`「W4 面向对象」节列出的高频子集有 8 个模式，**建议补充 6 道真题**覆盖策略、工厂方法、装饰器、适配器、外观、单例。
