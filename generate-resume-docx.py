from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "张鸿翔-正式投递版-前端与AI应用-更新版.docx"
BLUE = RGBColor(23, 105, 170)
INK = RGBColor(38, 55, 70)
MUTED = RGBColor(93, 109, 126)


def set_cell_shading(cell, fill):
    props = cell._tc.get_or_add_tcPr()
    shade = OxmlElement("w:shd")
    shade.set(qn("w:fill"), fill)
    props.append(shade)


def set_run_font(run, size=9, bold=False, color=INK):
    run.font.name = "Microsoft YaHei"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def add_text(doc, text, size=9, bold=False, color=INK, align=None, space_after=2):
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.space_after = Pt(space_after)
    paragraph.paragraph_format.line_spacing = 1.05
    if align is not None:
        paragraph.alignment = align
    run = paragraph.add_run(text)
    set_run_font(run, size, bold, color)
    return paragraph


def add_section(doc, title):
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(5)
    paragraph.paragraph_format.space_after = Pt(2)
    paragraph.paragraph_format.keep_with_next = True
    run = paragraph.add_run(title)
    set_run_font(run, 11, True, BLUE)
    p_pr = paragraph._p.get_or_add_pPr()
    border = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "5")
    bottom.set(qn("w:space"), "3")
    bottom.set(qn("w:color"), "DCEAF5")
    border.append(bottom)
    p_pr.append(border)
    return paragraph


def add_bullet(doc, text):
    paragraph = doc.add_paragraph(style="List Bullet")
    paragraph.paragraph_format.left_indent = Inches(0.18)
    paragraph.paragraph_format.first_line_indent = Inches(-0.12)
    paragraph.paragraph_format.space_after = Pt(1)
    paragraph.paragraph_format.line_spacing = 1.02
    run = paragraph.add_run(text)
    set_run_font(run, 8.2, False, INK)
    return paragraph


def add_role(doc, title, date):
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(2)
    paragraph.paragraph_format.space_after = Pt(1)
    paragraph.paragraph_format.keep_with_next = True
    run = paragraph.add_run(title + "　")
    set_run_font(run, 9, True, INK)
    run = paragraph.add_run(date)
    set_run_font(run, 8.2, False, MUTED)
    return paragraph


def add_project(doc, title, tech, intro, bullets):
    add_role(doc, title, "")
    add_text(doc, tech, 8, False, BLUE, space_after=1)
    add_text(doc, intro, 8.2, False, INK, space_after=1)
    for item in bullets:
        add_bullet(doc, item)


doc = Document()
section = doc.sections[0]
section.top_margin = Inches(0.42)
section.bottom_margin = Inches(0.45)
section.left_margin = Inches(0.62)
section.right_margin = Inches(0.62)

normal = doc.styles["Normal"]
normal.font.name = "Microsoft YaHei"
normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
normal.font.size = Pt(8.5)
normal.font.color.rgb = INK

add_text(doc, "张鸿翔", 23, True, INK, WD_ALIGN_PARAGRAPH.CENTER, 1)
add_text(doc, "求职方向：Web 前端开发工程师（AI 应用方向）", 10.5, False, BLUE, WD_ALIGN_PARAGRAPH.CENTER, 3)
add_text(doc, "电话：17870172591　｜　邮箱：839159219@qq.com　｜　学历：大专", 8.3, False, MUTED, WD_ALIGN_PARAGRAPH.CENTER, 7)

add_section(doc, "个人简介")
add_text(doc, "3 年以上前端开发经验，主要使用 Vue 2/Vue 3、TypeScript，具备 React/Redux 数据大屏、UniApp 小程序及工业管理平台开发经历。熟悉数据可视化、WebSocket 实时通信、业务组件封装和权限路由。近期通过个人项目“团队知识库助手”使用 Node.js/Fastify 构建后端 API，连接 PostgreSQL 和模型 SDK，完成文档检索、带来源问答、流式交互及人工确认型待办工作流。", 8.4, space_after=2)

add_section(doc, "专业技能")
for item in [
    "前端开发：Vue 2/Vue 3、JavaScript ES6+、TypeScript；具备 React、Redux 项目经验，熟悉 Vue Router、Pinia、Vuex。",
    "业务与多端：Element、Ant Design Vue、Vant、uView、UniApp 微信/支付宝小程序、腾讯地图 API、响应式页面开发。",
    "可视化与通信：ECharts 图表与数据大屏、Vis.js 网络拓扑、WebSocket 心跳保活及实时数据展示。",
    "工程化：Vite、Webpack、组件化、路由懒加载、资源优化、Git/SVN 协作及浏览器兼容问题排查。",
    "后端与 AI 应用实践：具备 Node.js/Fastify 后端应用开发实践，使用 PostgreSQL 和 OpenAI 兼容 SDK 实现文档检索、流式问答、来源引用、会话存储、用户级数据隔离和待办确认流程。",
]:
    add_bullet(doc, item)

add_section(doc, "工作经历")
add_role(doc, "熊猫车邦（厦门）信息有限公司｜前端开发工程师", "2024.12—2026.08")
for item in [
    "根据产品需求和设计稿完成页面及通用业务组件开发，参与 React 实时数据大屏和 UniApp 自助洗车小程序建设。",
    "参与前端代码规范和结构调整，抽取可复用组件，处理浏览器兼容及页面交互问题。",
    "使用 Git/SVN 进行版本管理和分支协作，配合产品、设计和后端推进功能交付。",
]:
    add_bullet(doc, item)
add_role(doc, "厦门集恩图造科技有限公司｜Web 前端开发工程师", "2022.11—2024.11")
for item in [
    "使用 Vue、Vant、Element 等技术开发业务页面及地图交互、表单、列表等模块。",
    "配合后端完成接口联调、数据交互和问题定位，参与版本迭代与线上功能维护。",
    "修复业务缺陷和浏览器兼容问题，参与组件复用及前端资源优化。",
]:
    add_bullet(doc, item)

add_section(doc, "项目经历")
add_project(doc, "团队知识库助手｜个人实践项目", "Vue 3、TypeScript、Vite、Node.js、Fastify、PostgreSQL、OpenAI 兼容 SDK", "面向制度和流程资料的知识库应用，使用 Node.js/Fastify 提供后端 API，支持资料导入、带来源问答，以及用户确认后创建待办。本项目为个人实践，不属于公司商业项目或已部署的生产系统。", [
    "完成登录、文本/Markdown 导入、资料检索、流式问答、来源原文展开及历史恢复，并连接模型服务和 PostgreSQL。",
    "实现文档分段、词项匹配和有限同义扩展检索，保存回答对应的原文快照；无匹配资料时由后端直接拒答。",
    "在服务端管理模型密钥，使用 HttpOnly Cookie 会话和用户过滤保护资料、消息与待办，并补充输入校验、请求来源校验和限流。",
    "实现“生成草稿—用户确认/拒绝—创建待办”固定流程；通过事务、行锁和幂等请求号避免重复创建。",
    "建立固定离线评测和数据库集成测试；小型离线题库通过数由 7/8 提升至 8/8。",
])
add_project(doc, "宏发质检平台", "Vue 3、TypeScript、Pinia、Vue Router、Ant Design Vue、ECharts、WebSocket、Vite", "工业质检管理平台，面向历史质检数据查询、设备采集和控制器管理等业务场景。", [
    "从零搭建 Vue 3、TypeScript、Pinia 和 Vue Router 项目骨架，划分页面路由、业务模块和公共组件，完成历史数据、采集器及控制器管理模块。",
    "使用 WebSocket 心跳保活对接服务端实时数据，处理连接状态、消息解析和页面销毁，推动实时数据进入 ECharts 图表并同步更新页面状态。",
    "抽取查询条件、表格、图表和状态提示等可复用组件；通过按需引入、路由懒加载、图片本地化和生产日志清理控制资源与构建产物。",
])

doc.add_page_break()
add_section(doc, "项目经历（续）")
add_project(doc, "网络感知系统", "Vue 3、TypeScript、Vuex、Ant Design Vue、Vis.js、TailwindCSS", "网络运维管理平台，覆盖网络拓扑、观测、配置、告警和系统管理等模块。", [
    "使用 Vis.js 开发网络拓扑图，将节点、连线和设备状态映射为可交互视图，支持节点增删改查、选中定位及拓扑信息展示。",
    "参与观测中心、配置中心、告警中心和系统管理模块开发，完成表单、列表、详情、筛选和状态反馈等管理场景。",
    "结合路由守卫与动态路由实现角色页面访问控制，统一接口数据类型和页面状态处理，并拆分拓扑、列表及复杂表单组件。",
])
add_project(doc, "熊猫车邦实时数据大屏与自助洗车小程序", "React、TypeScript、Redux、ECharts、UniApp、Vuex、uView、腾讯地图 API", "", [
    "参与实时数据大屏的页面和图表开发，使用 React、Redux 管理共享筛选与展示状态，使用 ECharts 封装趋势、统计和状态类图表，并适配大屏尺寸。",
    "对接后端接口和实时数据，处理加载、空数据、异常和刷新状态，展示关键业务指标和实时变化。",
    "使用 UniApp 开发微信、支付宝小程序页面，完成首页、个人中心及门店相关功能，处理多端组件和基础 API 差异。",
    "集成腾讯地图 API 实现门店定位、地图展示和路线导航，将地图调用与业务页面分离，便于维护。",
])

add_section(doc, "教育经历")
add_text(doc, "江西应用工程职业技术学院｜计算机网络技术｜大专｜2022 年 7 月毕业", 8.4, space_after=2)
add_section(doc, "求职补充说明")
add_text(doc, "2026 年 8 月结束上一段工作后，持续进行个人 AI 应用项目实践和岗位准备。知识库助手属于个人实践项目，Docker 生产部署尚未完成实机验收。", 8.2, space_after=2)

doc.save(OUTPUT)
print(OUTPUT)
