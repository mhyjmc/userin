# 张鸿翔求职材料

## 文件说明

- `张鸿翔-正式投递版-前端与AI应用.pdf`：适合上传招聘网站或发送给招聘人员。
- `张鸿翔-正式投递版-前端与AI应用.docx`：可编辑的正式投递版，适合按岗位修改。
- `张鸿翔-正式投递版-前端与AI应用-更新版.docx`：最新更新版，补充了 Node.js/Fastify 后端应用实践表述。
- `17-张鸿翔-正式投递版简历.md`：正式投递版源文件，后续修改内容后需要重新生成 PDF。
- `16-张鸿翔-前端与AI应用开发-改写版.md`：带修改说明和投递建议的版本。
- `15-前端与AI应用开发工程师简历.md`：简历草稿版本。
- `18-张鸿翔-简历面试题库.md`：面试题、参考答案和学习清单。
- `张鸿翔- web前端.pdf`：之前的原始简历，仅作为版式和内容对照。
- `generate-resume-pdf.py`：重新生成正式投递 PDF 的脚本。
- `generate-resume-docx.py`：重新生成可编辑 Word 文档的脚本。

## 重新生成 PDF

在 Windows PowerShell 中运行：

```powershell
$python = 'C:\Users\win10-\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $python '.\generate-resume-pdf.py'
```

PDF 使用 Windows 中文字体生成，建议只在当前电脑或安装了相同字体的环境中重新生成。

## 使用建议

投递前确认电话、邮箱、工作日期和项目描述准确；面试时不要把个人实践项目说成公司商业项目，也不要把尚未完成 Docker 实机验收说成已经上线。
