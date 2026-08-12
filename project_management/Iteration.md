# Iteration-01

## Observations

目前啥都没有，需要搭建网站地基才可以开始。

## Decision

跟着 P2 的教程和经验 搭建网站的地基

## Goal

创建一个能启动，能连接数据库，知道以后把 “上传功能” 放在哪里的网站空架子

## Change & Deliverable

1.创建Django项目:生成了manage.py、settings.py、总路由等网站基础设施

1. 创建了 `videos` 应用：给视频业务准备了模型、视图、后台和测试文件
2. 注册 `videos`：在 `INSTALLED_APPS` 中告诉 Django 这个网站包含 videos 功能，请在启动和操作数据库时加载它
3. 配置数据库：使用 SQLite，通过迁移创建用户、权限、后台等基础数据表
4. 配置访问根目录时候的路由：
5. 设置上海时区

Why:
项目开始时啥都没有，所以先用mdn Django P2 的教程把骨架搭好：能启动、能连 SQLite、并把视频相关功能统一放到 `videos` 应用里。这样 Iteration-01 先解决“能不能跑、东西放哪”的问题，为后续上传功能开发打好基础。

## Review

@JLZ，下次做完可以把TODO这个格式删掉

Iteration-01 done. 2026-08-07

---

# Iteration-02

## Observation

当前目标及意义：
1. 定义出models.py，意义是确定videos核心业务所需要的数据结构

当前情况：
1. 网站地基已建好
2. 根据教程P3，现在要做的事情是定义models.py，也就是定义模型。

当前卡点：
1. 我不知道我应该怎么把我这个应用都需要哪些模型找出来你懂吗，我不知要要遵循什么步骤才能把需要什么模型找出来，完全不知道

## Decision

调查出 设计出一个应用的models.py 需要经历哪些步骤

## Deliverable

设计models.py 所需要的步骤(v1.0)：

1. 写出主要用户故事（目前只需要上传）
2. 从用户故事中抽取名词（Video、User、Comment、Tag等等）
3. 为每个实体列出核心属性（title, file, duration, status类似的）
4. 标记出实体之间的关系（一对多，多对多等等）
5. 产出模型草案 videos/models_design.md
6. 通过评审
7. 实现videos/models.py
8. Django迁移

## Review & Next Step

今天的工作主要是定下了设计models.py SOP（Standard Operation Protocol）的第一版，也就是到底要怎么一步步把models.py真正设计和最后实现出来。

下一步会是写出主要用户故事。

Iteration-02 done. 2026-08-07

---

# Iteration-03

## Observation

当前目标及意义：
1. 定义出models.py，意义是确定videos核心业务所需要的数据结构

当前情况：
1. 已确认第一步为写出 上传视频 功能的主要用户故事

当前卡点：
啥是用户故事？这词在软件工程范式中靠谱吗

## Decision

获得用户故事的定义和模板

## Deliverable

用户故事回答的是：谁，想完成什么，以及为什么要完成。

常见格式：
> 作为 [某类用户]，我希望 [完成某件事]， 从而 [获得某种价值]

TennisVideoHub-上传功能用户故事v1.0：

作为已登录用户，我希望能上传一个网球视频，并且填写关于这个视频的基本信息，从而能够在网站中保存和观看该视频。

其中基本信息包括：
1. 场上人数（视频画面中切实参与击球的人数，数字框）
2. 相机是否晃动（拍摄过程中只要不是固定视角，稍微晃动也算晃动，是或否）
3. 底线视角（单选，地板视角，支架视角，高位摄像机视角）
4. 标签（拉球，比赛，多球练习，目前就这三个，我希望这个之后我还可以扩展）

## Review

今日写完了用户故事，明天将是在用户故事中抽取名词。

Iteration-03 done. 2026-08-10

---

# Iteration-04

status now: open

## Observation

当前目标及意义：
1. 定义出models.py，意义是确定videos核心业务所需要的数据结构

当前情况：
1. 已经写出用户故事，及其上传视频所需要的基本信息明细

当前卡点：
我们需要写出一个关于用户故事中名词的文档，具体参考 Iteration-02: 从用户故事中抽取名词（Video、User、Comment、Tag等等）

## Decision

JLZ和THN各自写出一个用户故事的名词抽取报告，以供之后合并

## Deliverable

JLZ：
- [x] $root/docs/user_story_noun_analysis_jlz.md

THN:
- [x] $root/docs/user_story_noun_analysis_thn.md


Iteration-04 done. 2026-08-12

---

# Iteration-05

## Observation

当前目标及意义：
1. 定义出models.py，意义是确定videos核心业务所需要的数据结构

当前情况：
目前THN和JLZ已完成各自user_story_noun_analysis

当前卡点：
这个提取名词的步骤有点太宽泛了 到底要提取什么名词？难道是个名词就要提取吗？

## Judge

设计models.py 所需要的步骤(v1.0) 的 第二步 和 第三步之间 差了一步，也就是：

> 判断提取出来的概念中，哪些是真正的实体。

## Decision

1. 更新 设计models.py 所需要的步骤 协议 至 v1.1
2. 给出业务概念分类表
3. 给出业务概念表清单模板

## Deliverable

设计 models.py 所需要的步骤(v1.1)：

1. 写出主要用户故事（目前只需要上传）
2. 从用户故事中提取**业务概念** 
3. 对业务概念进行分类，区分实体、属性、关系、枚举值、动作和上下文，确定业务概念表清单
4. 为每个实体列出核心属性，并确定字段类型、必填性、默认值和验证规则
    - 实体判断标准：这个东西要不要在数据库中拥有属于自己的“一行记录”？
5. 标记实体之间的关系（一对一、一对多、多对多）
6. 产出模型草案 `videos/models_design.md`
7. 通过评审
8. 实现 `videos/models.py`
9. 创建并执行 Django 迁移

业务概念分类表(v1.0)：

| 分类 | 含义 | 常见实现 |
|---|---|---|
| 实体 | 需要独立保存和管理的对象 | Django Model |
| 属性 | 用来描述某个实体的信息 | Model Field |
| 关系 | 一个实体和另一个实体之间的联系 | `ForeignKey`、`ManyToManyField` |
| 枚举值 | 某个属性可以选择的有限选项 | `TextChoices` |
| 动作 | 用户或系统执行的操作 | View、Service、业务逻辑 |
| 分组或上下文 | 帮助人理解，但不需要存进数据库 | 不实现 |

业务概念表清单模板：

| 业务概念 | 分类 | 原因 |

## Review

之前写出的 user_story_noun_analysis仍然有价值，但是第二步需要重新走一遍：2. 从用户故事中提取业务概念

这确实会让项目变得更加清楚，这个信息的引入是值得的

## Next

和JLZ通气Iteration-05 对于 设计 models.py 所需要的步骤(v1.1) 的改变，准备升级原名词分析文档为业务概念文档。

Iteration-05 done. 2026-08-12

---