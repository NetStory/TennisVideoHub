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