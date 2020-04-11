# 设计文稿

## 给项目起个名字

就叫它 `jpnblog`(jupyter notebook blog) 吧!

## 目录结构初始版本

> 需求分析
> - 内容的结构化管理
> - 图片的结构化管理
> - 草稿的结构化管理

目录结构设计
- _draft 未发布的草稿文件
- _posts 确定发布的正式文件
- _site 无需手动修改
- _material 存储图片动图等素材
- _template 模板仓库(暂时未启用)
- index.html 主页
- index.ipynb
- jpnblog.py 项目主要脚本

## 结构修改第二版

> 测试中GitHub page好像不能连接到`_`开始的文件名  
> 测试了:
> - `site`,可以访问
> - `_site`,不可以访问
> - `__site`,不可以访问

所以做全新设计:
- _draft 未发布的草稿文件
- _posts 确定发布的正式文件
- _material 存储图片动图等素材
- _template 模板仓库(暂时未启用)
- blogs 无需手动修改自动生成
- index.html 主页
- index.ipynb
- jpnblog.py 项目主要脚本
