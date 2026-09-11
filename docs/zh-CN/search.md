# 论文检索指南

[首页](../../README.zh-CN.md) · [English](../en/search.md) · [全部论文速览](paper-list.md) · [研究导读](research-guide.md)

在仓库根目录使用 Python 3.10+ 检索三个分类。无需安装依赖、联网或维护独立数据库：结果直接读取双语 Markdown 表格。

## 示例

```bash
python3 scripts/search_index.py Godot --status Open --lang zh-CN
python3 scripts/search_index.py --category interactive-worlds --year 2026 --lang zh-CN
python3 scripts/search_index.py "reinforcement learning" --category pcg --lang zh-CN
python3 scripts/search_index.py --lang zh-CN --json
```

## 参数

| 参数 | 行为 |
| --- | --- |
| 关键词 | 无论输出语言是什么，均同时匹配中英文文本。多个关键词须全部命中；完整短语请加引号。匹配忽略大小写并进行 Unicode 规范化。 |
| `--category` | 限定分类为 `end-to-end`、`pcg` 或 `interactive-worlds`。 |
| `--status` | 匹配 `Open`、`Partial` 或 `Closed`，解读方式见下方说明。 |
| `--year` | 匹配记录中明确列出的年份，包括修订年份。 |
| `--lang` | 输出描述与来源位置可选 `en`（默认）或 `zh-CN`；不限制关键词的匹配语言。 |
| `--json` | 输出结构化 JSON，而不是简短文本结果。不加筛选时导出整个索引。 |
| `--help` | 显示命令内置帮助。 |

可以组合关键词和筛选条件缩小结果范围。不提供关键词或筛选条件时，命令返回全部记录。

## 读取结果

文本结果包含记录 ID、标题、列出的年份、工件标签、论文主链接和源文件行号。打开对应源文件行，可查看任务说明、评测细节与工件限制。

JSON 结果还包含标题单元格的完整链接（`paper_urls`）、描述单元格（`details`）、保留链接的工件 Markdown（`artifacts`），以及来源底稿路径（`evidence`）。源文件和行号定位完整公开记录；底稿使用相同的分类与条目编号。

`pcg:12` 这类 ID 对应当前分类与行号，不是永久论文标识，重新排序后可能变化。需要长期引用时，请使用论文一手来源 URL。

## 解读筛选条件

- **年份：** 一条记录可能列出多个年份，例如首次发布和修订年份。命中某年不表示全部关联工件都在该年发布或核验。
- **工件标签：** 筛选会匹配任一版本的标签。标记为 `Partial / Closed` 的记录会同时命中 `--status Partial` 和 `--status Closed`；不同版本的情况请查看工件列。
- **可用性：** `Open` 不意味着许可证无限制、开箱即用或已独立复现成功。标签描述已核验的官方发布情况，详见[标签定义](../../README.zh-CN.md#工件标签)。

## 查找 Benchmark

可先看[端到端生成](end-to-end.md#1-生成-benchmark10-条)和[交互世界](interactive-worlds.md#2-交互世界生成-benchmark4-条)中的 benchmark 分区。PCG 混合收录方法与 benchmark，需查看 [PCG 分类表](pcg.md)中每条记录的任务与评测列。

[研究导读](research-guide.md)对比不同评测设置。准备动手时，[实验起点](../../research/experiment-entry-points-2026-09-08.md)保留安装要求和固定版本工件证据；这些是配置建议，不是复现成功报告。
