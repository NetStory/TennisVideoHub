# Business Concepts Sheet — JLZ

## Purpose

本文件用于分析用户故事中涉及的业务概念，并根据设计流程 v1.1 对其进行分类。

当前阶段只判断业务概念属于：

- 实体（Entity）
- 属性（Attribute）
- 关系（Relationship）
- 枚举值（Enum Value）
- 动作（Action）
- 分组或上下文（Context）

---

## Business Concepts


| 业务概念                        | 分类     | 原因                                                                  |
| --------------------------- | ------ | ------------------------------------------------------------------- |
| User                        | 实体     | 用户是系统中需要被独立保存和管理的对象，并且可以拥有多个视频，因此需要拥有独立记录。                          |
| Video                       | 实体     | 视频是视频上传业务中的核心业务对象，需要独立保存视频本身及其相关信息，因此需要拥有独立记录。                      |
| Video File                  | 属性     | 视频文件用于描述某一个 Video，本身目前不需要作为独立业务对象管理。                                |
| Video Title                 | 属性     | 标题用于描述某一个 Video，不需要独立存在。                                            |
| Player Count                | 属性     | 场上人数是对 Video 内容的描述信息，依赖于 Video 存在。                                  |
| Camera Shaking              | 属性     | 用于描述视频拍摄过程中相机是否存在明显晃动，属于 Video 的特征。                                 |
| Camera View                 | 属性     | 用于描述视频的拍摄视角，例如是否为底线视角，属于 Video 的描述信息。                               |
| Video Format                | 属性     | 用于描述上传视频文件的格式，例如 MP4，依附于 Video File / Video。                        |
| Video Size                  | 属性     | 用于描述上传视频文件的大小，用于后续文件验证，不需要独立记录。                                     |
| Video Duration              | 属性     | 视频时长属于 Video 的基础元数据，用于描述视频。                                         |
| Upload Status               | 属性     | 用于描述某个 Video 当前所处的上传或处理状态，例如上传中、上传成功、上传失败。                          |
| Select Video                | 动作     | 用户选择本地视频文件，是用户执行的操作，不是数据库中的独立对象。                                    |
| Fill Video Information      | 动作     | 用户填写视频相关参数，是业务流程中的操作。                                               |
| Validate Video              | 动作     | 系统检查视频格式、大小等是否合法，属于业务逻辑。                                            |
| Upload Video                | 动作     | 将视频提交到系统并存储，是业务操作而不是数据实体。                                           |


---



## Preliminary Entity Candidates

经过本轮业务概念分类，目前 Upload Tennis Video 用户故事中明确需要进一步进入模型设计阶段的实体主要有：

### User

表示 NetStory 用户。

User 本身可能直接使用 Django Authentication System 提供的用户模型，因此未必需要在 `videos` app 中重新创建 User Model。

### Video

Upload Tennis Video 业务中的核心实体。

后续需要围绕 Video 进一步确定：

- 核心属性
- 字段类型
- 必填性
- 默认值
- 验证规则
- 与 User 的关系

---



## Concepts Requiring Further Discussion

以下概念当前暂时判断为属性，但未来随着业务复杂度增加，有可能升级为独立实体：

### Tag

如果 Tag 只是一个简单文本字段，可以暂时作为 Video 属性。

如果未来：

- 多个 Video 可以共享同一个 Tag
- 用户可以搜索 Tag
- 后台需要管理 Tag
- Tag 有自己的名称、描述、创建时间等信息

则 Tag 更适合作为独立实体，并与 Video 建立 Many-to-Many 关系。

### Upload Record

目前一次 Video 上传可以直接由 Video 自己记录状态，因此暂时没有必要创建 UploadRecord。

如果未来需要记录：

- 多次上传尝试
- 上传失败历史
- OSS 请求信息
- 上传进度
- 重试记录

则可以考虑将 UploadRecord 设计为独立实体。

---



## Current Conclusion

对于当前 Video Upload MVP，不应该因为用户故事中出现了一个名词就创建一个 Django Model。

当前分析认为最明确的核心业务实体是：

- User
- Video

其他大部分概念属于：

- Video 的属性
- User 与 Video 的关系
- 有限选项
- 上传流程中的动作
- 系统运行上下文或业务规则

因此下一阶段应围绕 `Video` 实体继续完成字段设计，而不是继续增加新的 Model。

---

Iteration-06 Done