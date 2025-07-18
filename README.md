<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---
BodyWise is a personalized fitness and health guidance web application built with NiceGUI.

BodyWise provides customised
workout and wellness recommendations based on users’ BMI, and — if available — body fat percentage, gender, and
lifestyle data. Whether you’re underweight, overweight, or simply aiming to optimise your physique, BodyWise helps you
make smarter, data-driven decisions for your health and fitness journey.

**PRIVACY NOTICE**
---
This application may require inputting personal information or private data to generate customised suggestions,
recommendations and necessary results. However, please rest assured that the application does **NOT** collect, store, or
transmit your personal information. All processing occurs locally in the browser or runtime environment, and **NO** data
is sent to any external server or third-party service. The entire codebase is open and transparent — you are welcome to
review the code [here](./) at any time to verify how your data is handled.

**BMI EVALUATION STANDARD**
---
The BMI (Body Mass Index) and weight classification in this application are based on the WS/T 428-2003 standard (
Click [here](./assets/WS-T428-2003.pdf) to view the full document) issued by the Chinese Ministry of Health:

- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI < 24.0
- Overweight: 24.0 ≤ BMI < 28.0
- Obese: BMI ≥ 28.0

Reference: WS/T 428-2003 — Criteria of weight for adults (China National Health Standard)

**LICENCE**
---
This application is licensed under the [BSD-3-Clause License](LICENSE). You can click the link to read the licence.

**CREATING THE CHANGELOG**
---

1. Install the required dependencies with the command `pip install git-changelog`.
2. Run the command `pip show git-changelog` to check whether the changelog package has been installed and its version.
3. Prepare the configuration file of `pyproject.toml` at the root of the file.
4. The changelog style is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
5. Run the command `git-changelog`, creating the `Changelog.md` file.
6. Add the file `Changelog.md` to version control with the command `git add Changelog.md` or using the UI interface.
7. Run the command `git-changelog --output CHANGELOG.md` committing the changes and updating the changelog.
8. Push the changes to the remote repository with the command `git push origin main` or using the UI interface.

**USING NICEGUI**
---

1. Install NiceGUI with the command `pip install nicegui`.
2. Run the command `pip show nicegui` to check whether the package has been installed and its version.