# TennisVideoHub

TennisVideoHub 当前提供第一条本地产品流程：登录用户上传一个小型 MP4 网球视频，填写基本信息和标签，然后在详情页播放。

## 开发环境

项目当前使用以下 Conda 环境：

```text
C:\Users\lance\scoop\apps\anaconda3\current\App\envs\django
```

在仓库根目录打开 PowerShell：

```powershell
$djangoPython = 'C:\Users\lance\scoop\apps\anaconda3\current\App\envs\django\python.exe' # 这里换成你本机的django环境
& $djangoPython -m pip install -r requirements.txt
& $djangoPython TennisVideoHub\manage.py migrate
& $djangoPython TennisVideoHub\manage.py create_test_admin
& $djangoPython TennisVideoHub\manage.py runserver
```

首次使用时运行一次 `create_test_admin`。它会创建或重置以下本地测试管理员：

```text
用户名：testadmin
密码：TennisTest-001!
```

该账号仅用于本机 `DEBUG=True` 的开发与验收环境，不能用于生产部署，也不要复用这个密码。

服务启动后打开：

```text
http://127.0.0.1:8000/accounts/login/
```

登录后访问上传页面：

```text
http://127.0.0.1:8000/videos/upload/
```

## 当前上传边界

- 只接受 `.mp4` 文件；
- 文件必须大于 0 且不超过 50 MB；
- 场上人数为 1 至 4；
- 视频保存在本地 `TennisVideoHub/media/`；
- 本地媒体服务只用于开发，不代表生产环境的私有文件授权方案。

## 检查与测试

```powershell
$djangoPython = 'C:\Users\lance\scoop\apps\anaconda3\current\App\envs\django\python.exe'
& $djangoPython TennisVideoHub\manage.py check
& $djangoPython TennisVideoHub\manage.py test videos
```

## 项目协作

- 产品与工程职责见 `project_management/COLLABORATION_PROTOCOL.md`。
- 当前工作见 `project_management/bets/BET-001-upload-and-play.md`。
