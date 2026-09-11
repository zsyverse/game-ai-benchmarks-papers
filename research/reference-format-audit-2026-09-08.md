# 高 Star 论文收集仓库格式核查与采用方案

核查日期：2026-09-08。目的：为本仓库的双语首页、分类导航与论文条目寻找可借鉴的组织方式，不借样本的热度证明本仓库或论文的学术质量。

本记录检查五个样本的官方 GitHub 元数据与实际 README，并针对部分样本读取分类页和贡献说明。发现路径包括 GitHub 官方仓库搜索（`awesome papers stars:>1000 in:name,description`，按 star 降序）和已知主题型清单；不纳入只因热度高而缺乏论文组织结构的泛课程/工具合集。样本不是全站最高 star 排名，也不是维护活跃度排名。

Star 为 2026-09-08 GitHub API 返回的快照，会持续变化。README 固定版本用于复查当时的结构，不把仓库 `pushed_at`、默认分支提交时间或本次读取时间混同为论文核验日期。未克隆仓库、未运行其代码，亦未重新核验其收录论文。

## 样本与来源快照

| 仓库 | 当日 Stars | 默认分支与入口 | 固定版本 |
| --- | ---: | --- | --- |
| [eugeneyan/applied-ml](https://github.com/eugeneyan/applied-ml) | 30,117 | `main` / `README.md` | [`d58606b`](https://github.com/eugeneyan/applied-ml/tree/d58606b6ec039e9cc242f43fd64d16af71cd1297) |
| [terryum/awesome-deep-learning-papers](https://github.com/terryum/awesome-deep-learning-papers) | 26,185 | `master` / `README.md` | [`1a0a9df`](https://github.com/terryum/awesome-deep-learning-papers/tree/1a0a9dfb1ee27f74a1ab47ed1273694ec4778ae7) |
| [diff-usion/Awesome-Diffusion-Models](https://github.com/diff-usion/Awesome-Diffusion-Models) | 12,370 | `main` / `README.md` | [`01be334`](https://github.com/diff-usion/Awesome-Diffusion-Models/tree/01be334d2e258b0150093761d77ab55b789e88d3) |
| [MrNeRF/awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) | 8,869 | `main` / `README.md` | [`daabf89`](https://github.com/MrNeRF/awesome-3D-gaussian-splatting/tree/daabf8909a13e6f9ea12235bde2ac8c960cafc83) |
| [DeepGraphLearning/LiteratureDL4Graph](https://github.com/DeepGraphLearning/LiteratureDL4Graph) | 3,102 | `master` / `README.rst` | [`0de0b5d`](https://github.com/DeepGraphLearning/LiteratureDL4Graph/tree/0de0b5d0383ea0e63b9838af02107cd8dd3dabb1) |

Stars 与默认分支来源：[applied-ml 官方 API](https://api.github.com/repos/eugeneyan/applied-ml)、[LiteratureDL4Graph 官方 API](https://api.github.com/repos/DeepGraphLearning/LiteratureDL4Graph)。默认分支顶端提交来源：[applied-ml commit API](https://api.github.com/repos/eugeneyan/applied-ml/commits/main)、[LiteratureDL4Graph commit API](https://api.github.com/repos/DeepGraphLearning/LiteratureDL4Graph/commits/master)。

其余三个样本的元数据来源：[经典深度学习清单 API](https://api.github.com/repos/terryum/awesome-deep-learning-papers)、[扩散模型清单 API](https://api.github.com/repos/diff-usion/Awesome-Diffusion-Models)、[3DGS 清单 API](https://api.github.com/repos/MrNeRF/awesome-3D-gaussian-splatting)。相应默认分支顶端提交日期为 2018-10-19、2023-11-05、2026-09-03；这些日期不表示论文链接经过重新核验。

## 1. applied-ml：轻量首页、按读者问题分类、紧凑单行条目

### 实际结构

- 首页先用一句话限定为生产环境中的数据科学与机器学习资料，再说明读者能得到什么：问题如何定义、哪些方法有效、为何有效、取得了哪些实际结果。它是论文、文章与技术博客的混合清单，并非只收论文。来源：[README 开头](https://github.com/eugeneyan/applied-ml/blob/d58606b6ec039e9cc242f43fd64d16af71cd1297/README.md#applied-ml)。
- `Table of Contents` 提供 31 个主题锚点，从 `Data Quality`、`Data Engineering`、`Recommendation` 到 `Generation`、`Practices`、`Fails`。分类先服务阅读问题，不按机构或发表年份构成主树。来源：[README 目录](https://github.com/eugeneyan/applied-ml/blob/d58606b6ec039e9cc242f43fd64d16af71cd1297/README.md#applied-ml)。
- 各主题使用编号列表，常见条目是“链接标题 + 可选 Paper / Code / Video 链接 + 行内代码样式的机构与年份”，不是宽表格。例如 `Data Quality` 可见标题与额外 `Paper`，`Data Discovery` 可见独立 `Code`；年份与附加链接并非每项都有。来源：[Data Quality](https://github.com/eugeneyan/applied-ml/blob/d58606b6ec039e9cc242f43fd64d16af71cd1297/README.md#data-quality)、[Data Discovery](https://github.com/eugeneyan/applied-ml/blob/d58606b6ec039e9cc242f43fd64d16af71cd1297/README.md#data-discovery)。
- 首页提供 contributions welcome 徽章，链接到独立的 `CONTRIBUTING.md`。贡献说明要求先查是否重复，也欢迎给旧条目补充链接，并给出可复制的 Markdown 最小模板。来源：[Contribution Guide](https://github.com/eugeneyan/applied-ml/blob/d58606b6ec039e9cc242f43fd64d16af71cd1297/CONTRIBUTING.md#contribution-guide)。
- 已检查的 README 没有独立的更新日志或“全部条目核验日期”字段；贡献入口是 PR。默认分支顶端提交时间为 2024-05-02，而仓库 API 的 `pushed_at` 为 2024-07-18，二者不是同一含义，也不能当成论文链接最近核验日期。来源：[固定 README](https://github.com/eugeneyan/applied-ml/blob/d58606b6ec039e9cc242f43fd64d16af71cd1297/README.md)、[贡献说明](https://github.com/eugeneyan/applied-ml/blob/d58606b6ec039e9cc242f43fd64d16af71cd1297/CONTRIBUTING.md)、[仓库 API](https://api.github.com/repos/eugeneyan/applied-ml)、[默认分支提交](https://github.com/eugeneyan/applied-ml/commit/d58606b6ec039e9cc242f43fd64d16af71cd1297)。

### 适合本仓库的借鉴

1. 首页先回答“收什么、从哪里读”，把完整审计解释留到专门页面；读者首先看到游戏生成、PCG、交互世界三条路径。
2. 把论文、代码、项目页的链接标签保持简短且一致，方便扫描；代码发布状态仍需另行解释。
3. 把去重要求和条目模板放进贡献指南，并让首页有清晰入口。

这些是针对本仓库的设计建议，不是该样本作者声称经过用户研究证明的最佳实践。

### 不照搬的部分

- 不照搬其混合收录博客、报道、失败案例等内容的范围；本仓库仍只正式计入符合生成任务范围的方法与基准。
- 不把全部 203 条双语记录塞进一个长 README，也不为模仿单行列表而删除生成输出、评测边界和材料可用性信息。首页可以轻量，分类正文与证据档案仍应保留层次。
- 不把机构标签变成论文质量标签，不用访问量徽章代替质量核查，也不把 GitHub 的更新时间当成研究复查时间。

## 2. LiteratureDL4Graph：主题与发表场所双入口、分层分类、稳定元数据

### 实际结构

- 文件是 reStructuredText 的 `README.rst`，而非 `README.md`。开头只有标题与一句范围介绍，随后提供 `Sort by topic` 和 `Sort by venue` 两个入口；主题页用 `contents` 与 `sectnum` 指令设置两级目录和编号。来源：[主题页开头](https://github.com/DeepGraphLearning/LiteratureDL4Graph/blob/0de0b5d0383ea0e63b9838af02107cd8dd3dabb1/README.rst)。
- `Node Representation Learning` 下分 `Unsupervised Node Representation Learning`、`Node Representation Learning in Heterogeneous Graphs`、`Node Representation Learning in Dynamic Graphs`；其他主节包括 `Knowledge Graph Embedding`、`Graph Neural Networks` 和 `Applications of Graph Deep Learning`。应用节再按 NLP、CV、推荐、图生成等细分。来源：[主题页](https://github.com/DeepGraphLearning/LiteratureDL4Graph/blob/0de0b5d0383ea0e63b9838af02107cd8dd3dabb1/README.rst)。
- 单篇条目使用“标题及论文链接 + authors + venue（含年份）+ 可选 keywords”的多行格式。`DeepWalk` 例如有作者、`KDD 2014` 和 `Node classification, Random walk, Skip-gram` 关键词。来源：[Node Representation Learning](https://github.com/DeepGraphLearning/LiteratureDL4Graph/blob/0de0b5d0383ea0e63b9838af02107cd8dd3dabb1/README.rst#node-representation-learning)。
- `BYVENUE.rst` 也提供双入口，但正文先按年份、再按发表场所分层，例如 `2019` 下有 `WSDM`、`ICLR`、`AAAI`、`ICML` 等，目录深度为四级；这不是另一个全然不同的主题清单。来源：[Sort by venue 页面](https://github.com/DeepGraphLearning/LiteratureDL4Graph/blob/0de0b5d0383ea0e63b9838af02107cd8dd3dabb1/BYVENUE.rst)。
- 代码并不是统一独立字段：已检查主题页有代码 URL 放在 `keywords` 的个例，以及系统条目自身指向 GitHub 的情况；不能把该格式描述成“每篇都有 Paper / Code”。来源：[主题页原始文件](https://raw.githubusercontent.com/DeepGraphLearning/LiteratureDL4Graph/0de0b5d0383ea0e63b9838af02107cd8dd3dabb1/README.rst)、[Graph Representation Learning Systems](https://github.com/DeepGraphLearning/LiteratureDL4Graph/blob/0de0b5d0383ea0e63b9838af02107cd8dd3dabb1/README.rst#graph-representation-learning-systems)。
- 核查时根目录只有 `README.rst`、`BYVENUE.rst`、`LICENSE`；两个列表中未发现单独贡献指南、更新日志或全量核验日期。默认分支顶端提交为 2020-01-02，仓库 `pushed_at` 为 2020-12-20。Stars 较多不表示列表近期仍有内容维护。来源：[根目录 API](https://api.github.com/repos/DeepGraphLearning/LiteratureDL4Graph/contents/)、[默认分支提交](https://github.com/DeepGraphLearning/LiteratureDL4Graph/commit/0de0b5d0383ea0e63b9838af02107cd8dd3dabb1)、[仓库 API](https://api.github.com/repos/DeepGraphLearning/LiteratureDL4Graph)。

### 适合本仓库的借鉴

1. 主分类保留输出类型，分类页内部增加清晰的段落导航或二级主题索引，尤其帮助读者进入 120 条的 PCG 集合。
2. 提供不重复维护正文的第二检索入口。本仓库已有年份和类别搜索，可以将其作为时间视角入口；不必为模仿另复制一份按年份排列的 203 条双语目录。
3. 用统一的年份、论文入口和方法关键词帮助扫读，但生成产物与评测限制不能被关键词替代。

### 不照搬的部分

- 不为了样式切换到 reStructuredText；现有 Markdown、双语链接与校验工具应保留。
- 不单纯按顶会或发表场所决定阅读优先级，也不暗示预印本与已发表论文证据等价。
- 不把代码链接混入关键词，更不凭代码链接存在就标成可复现；继续保留 `Open / Partial / Closed` 的明确含义。
- 不直接照抄它包含 systems、datasets 的收录边界；本仓库的独立数据集与纯基础设施仍按现有范围规则处理。

## 3. awesome-deep-learning-papers：有限阅读集、按主题分类、单行文献

- 开头明确聚焦 2012–2016 年的经典高引论文，另有停止维护通知；中间是选录条件、贡献入口与 `Contents`，再按 Generalization、Optimization、Generative Models、CNN、NLP/RNN 等主题展开。来源：[固定 README](https://github.com/terryum/awesome-deep-learning-papers/blob/1a0a9dfb1ee27f74a1ab47ed1273694ec4778ae7/README.md)。
- 实际条目是“**论文标题**（年份），作者，`pdf` 链接”的紧凑列表，例如 `Distilling the knowledge in a neural network`。并不是每篇都有代码或详细实验表。来源：[Understanding / Generalization / Transfer](https://github.com/terryum/awesome-deep-learning-papers/blob/1a0a9dfb1ee27f74a1ab47ed1273694ec4778ae7/README.md#understanding--generalization--transfer)。
- 借鉴：给初读者一个数量有限、按问题分类的阅读入口，使用一致的标题、年份和资源链接。**不照搬** Top 100、高引阈值或停止增补的规则；本仓库的六篇阅读起点不是按引用数或 stars 排名，也不取代完整 203 条索引。开头较长的历史背景也不适合作为本仓库首页模板。

## 4. Awesome-Diffusion-Models：资源与论文分层、稳定的链接标签

- 首页先给一句范围和独立网站入口，再以两级目录区分 `Resources` 和 `Papers`；论文内部按 Vision、Audio、Natural Language、Graph 等领域及其任务再分层。来源：[固定 README](https://github.com/diff-usion/Awesome-Diffusion-Models/blob/01be334d2e258b0150093761d77ab55b789e88d3/README.md)。
- 实际文献条目为加粗标题、斜体作者、venue/year 与 `Paper` 链接、日期的多行形式。例如 `DiffEnc: Variational Diffusion with a Learned Encoder` 位于 `Vision → Generation`。`Resources → Introductory Papers` 与主体论文也分开；并非所有条目都提供 `Code`。来源：[Vision / Generation](https://github.com/diff-usion/Awesome-Diffusion-Models/blob/01be334d2e258b0150093761d77ab55b789e88d3/README.md#vision)、[Introductory Papers](https://github.com/diff-usion/Awesome-Diffusion-Models/blob/01be334d2e258b0150093761d77ab55b789e88d3/README.md#introductory-papers)。
- 借鉴：先有研究任务的大类，再有方法/基准分区；初读材料与完整清单分层；资源标签统一。**不照搬**超长单页、多级分类的全部复杂度，也不自动把综述和教程计入本仓库论文总数。官方 README API 首次读取不完整，后通过固定提交的 raw README 成功读取并复核，不以失败响应推测格式。

## 5. awesome-3D-gaussian-splatting：入口型首页、论文数据库与资源表分离

- 核查时首页以短定位和 `Browse the Paper List / Contribute` 等快捷入口开场，`Contents` 靠前；完整论文导向独立可搜索数据库，而 README 还分类列出实现、引擎支持、工具与学习资料。来源：[固定 README](https://github.com/MrNeRF/awesome-3D-gaussian-splatting/blob/daabf8909a13e6f9ea12235bde2ac8c960cafc83/README.md)。
- `Community Implementations` 的表头是 Implementation / Language / License / Description，其他资源多用“名称链接 + 一句说明”的列表；该表是实现对照表，不能误说成论文的统一格式。来源：[实现区](https://github.com/MrNeRF/awesome-3D-gaussian-splatting/blob/daabf8909a13e6f9ea12235bde2ac8c960cafc83/README.md#implementations)。
- 借鉴：首页负责导航，长列表与深读资料分层；比较多字段时保留表格，轻量阅读入口使用列表。**不照搬**产品推广、单独网站部署或资源大杂烩。本仓库已经有离线检索和分类页，此次不引入第二套数据库或网站构建流程。独立论文数据库本身未进行内容审计。

## 对本仓库的采用方案

| 页面层级 | 应借鉴的组织方式 | 应保留的本仓库特性 |
| --- | --- | --- |
| 首页 | 一句话定位、简洁导航、按读者任务给入口、清晰贡献链接 | 中英文互链；严格范围；最后全量核查与局部更新分开 |
| 分类页 | 明显的章节锚点、统一链接标签与年份字段、适量关键词导航 | 一篇一个规范记录；方法与基准区分；生成产物和评测限制 |
| 深读页面 | 将阅读说明与大清单分开，提供另一种找论文的路径 | 研究导读、原始证据档案、未收录候选和不确定性 |
| 维护说明 | 去重提醒、条目模板、贡献入口前置 | 双语对应、官方材料可用性核查、结构测试但不冒充实验复现 |

总体建议是借鉴成熟清单的“易进入、易跳转、字段一致”，而不是复制它们的内容、领域范围或全部技术实现。本记录不改变任何论文的收录状态，也不对样本仓库的学术完整性作评级。

本轮具体落地：

1. 双语首页改为短定位、核查日期、目录、三类索引、六篇阅读起点；阅读条目采用“标题 + 年份 + Paper / Code + 一句话说明”，关键运行/材料限制仍保留。
2. 六个分类页增加章节锚点、研究导读和来源底稿入口，把历史覆盖记录移至核查说明。全部 canonical 表格行、ID、计数标题和外部 URL 次序保持不变。
3. 详细范围继续由 `SCOPE.md` 承载；来源证据与待定线索继续保存在 `research/`，不为首页简化而丢弃研究依据。
4. 贡献指南增加可复制的证据条目模板和仓库层级说明；不增加虚假的 Awesome 认证、热度徽章或未核验的作者/venue 元数据。

来源支持的是上述仓库的实际组织方式；这些布局能否提高本仓库的阅读效率属于设计判断，尚未进行用户测试。

## 本轮验证结果

- 六个分类页的所有表格行、表头、ID、计数标题和外部 URL 顺序与本轮编辑前一致；双语首页的 13 个外部 URL 也完全同序。
- 按 Git 跟踪文件及未忽略文件限定 Markdown 扫描范围后，索引校验通过：38 + 120 + 45 = 203 条。原始校验命令会额外扫描 `.git/info/exclude` 已排除的 `output/pdf/game-generation-review-2026-09-08/`，其中 PDF 草稿存在图片相对路径和表格错误；没有为本任务修改这些构建产物或校验脚本。
- 38 份项目 Markdown 的 lint、6 项检索回归测试和 `git diff --check` 通过。
- 11 份本轮编辑文档通过 Pandoc 的 GFM 解析，51 个本地页内跳转目标有效；这是渲染结构与锚点检查，不是 GitHub 实际页面的视觉验收或外链全量活性检查。

## 后续格式优化：全量速览与首页收敛

第一轮的详细分类表仍较宽，因此继续借鉴样本的紧凑文献列表，增加 [English](../docs/en/paper-list.md) / [中文全部论文速览](../docs/zh-CN/paper-list.md)。它从现有 203 条规范记录和对应编号的证据标题自动生成，不是第二份手工维护的目录；分区沿用原表，分区内按所列最新年份倒序（含修订年份），同年按原编号排列。

速览使用“完整年份 + 论文标题链接 + 含限定词的工件状态 + 精确证据入口”。仅标题单元格的第一个来源作为主论文，避免把前驱、后续论文或附加材料误标为本论文；官方代码、评测和局限保留在直达的证据块中，不推断某个 GitHub 链接就是本论文的实现。

双语首页进一步减少重复语言列和范围说明；详细检索语义迁至 [English](../docs/en/search.md) / [中文检索指南](../docs/zh-CN/search.md)。`build_paper_list.py --check` 和回归测试检查派生视图是否过期，贡献流程与 CI 增加该检查。此次仍不改变原始条目、收录范围或论文核验日期。
