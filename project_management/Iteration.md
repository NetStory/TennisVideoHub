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
