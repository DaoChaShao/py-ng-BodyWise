<p style="text-align: right;">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**应用简介**
---
**BodyWise** 是一个基于 [NiceGUI](https://nicegui.io) 构建的个性化健身与健康指导网页应用。

BodyWise 可根据用户的 BMI（身体质量指数）、体脂率（如有）、性别及生活方式数据，提供定制化的锻炼与健康建议。无论你是体重偏轻、超重，还是希望优化身材，BodyWise
都能帮助你做出更聪明、数据驱动的健康管理决策。

**隐私声明**
---
本应用可能需要您输入个人信息或隐私数据，以生成定制建议和结果。但请放心，应用程序 **不会**
收集、存储或传输您的任何个人信息。所有计算和数据处理均在本地浏览器或运行环境中完成，**不会** 向任何外部服务器或第三方服务发送数据。

整个代码库是开源透明的 —— 您可以随时点击此处查看代码并验证数据处理方式。

**判定标准** - BMI
---
本应用所使用的 BMI（身体质量指数）和体重分类依据中国卫生部发布的 **WS/T 428-2003 标准
**（点击[这里](./assets/WS-T428-2003.pdf)查看完整文档）：

- **体重过轻**：BMI < 18.5
- **正常体重**：18.5 ≤ BMI < 24.0
- **身体超重**：24.0 ≤ BMI < 28.0
- **身体肥胖**：BMI ≥ 28.0

**参考标准**：WS/T 428-2003 — 《成人体重判定》（中国国家卫生标准）

**许可协议**
---
本应用基于 **BSD-3-Clause 许可证** 开源发布。您可以点击链接阅读完整协议内容：  
👉 [BSD-3-Clause License](./LICENSE)

**日志生成**（CHANGELOG）
---
1. 使用命令 `pip install git-changelog` 安装所需依赖项。
2. 执行 `pip show git-changelog` 检查是否已正确安装该包及其版本。
3. 在项目根目录下准备 `pyproject.toml` 配置文件。
4. 更新日志遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) 提交规范。
5. 执行命令 `git-changelog` 创建 `Changelog.md` 文件。
6. 使用 `git add Changelog.md` 或图形界面将该文件添加到版本控制中。
7. 执行 `git-changelog --output CHANGELOG.md` 提交变更并更新日志。
8. 使用 `git push origin main` 或 UI 工具将变更推送至远程仓库。

**使用NiceGUI**
---
1. 使用命令 `pip install nicegui` 安装 NiceGUI。
2. 执行 `pip show nicegui` 检查是否安装成功及其版本信息。
