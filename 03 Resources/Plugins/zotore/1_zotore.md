# 1 Zotero与Obsidian双向联动，简单！（含原创精美模板）

## 1.1 最终效果

对于Zotero中的某篇文献条目，可以：

![以这篇文献为例](placeholder.png)

- ✅ **在Ob中自动生成新文档**
  在Obsidian中自动生成一个美观的文档，文档包含Zotero中的所有信息，包括元数据、多色PDF注释、笔记、附件链接等。

  ![Obsidian内的表现](placeholder.png)

- ✅ **Ob一键跳回Zotero和PDF**
  Obsidian文档含链接，能够一键跳转回对应的Zotero文献条目，且能够打开对应的PDF文件。
  对于PDF注释，点击原文还可跳转打开PDF文件的对应上下文位置。

  ![Obsidian内的表现](placeholder.png)

- ✅ **Zotero一键跳转Ob**
  能够在Zotero中，通过右键菜单一键打开对应的Obsidian文档。

  ![Zotero内的表现](placeholder.png)

- ✅ **Ob补充笔记，再次生成不覆盖**
  可在自动生成的Obsidian文档中继续补充笔记，且对相同的文献再次生成文档时，补充笔记不会被覆盖。

- ❌ **Ob补充笔记不可自动导入Zotero**
  在Obsidian文档中补充的笔记，不可再反向自动导入Zotero，但仍可手动复制进Zotero。

## 1.2 安装步骤

安装很简单！

### 1.2.1 安装Zotero插件：Better BibTex和MarkDB-Connect

首先，从官网下载插件安装文件（.xpi）。

- **MarkDB-Connect**: [https://github.com/daeh/zotero-markdb-connect/releases/](https://github.com/daeh/zotero-markdb-connect/releases/)
- **Better BibTex**: [https://github.com/retorquere/zotero-better-bibtex/releases/](https://github.com/retorquere/zotero-better-bibtex/releases/)

然后，在Zotero中打开插件面板。

![Zotero插件面板](placeholder.png)

拖入下载的xpi文件，安装成功！

![安装成功](placeholder.png)

### 1.2.2 配置MarkDB-Connect

Zotero中，打开"设置 → MarkDB-Connect"。

依次输入Ob仓库目录地址、`^.*\.md$`、`citekey`

![配置MarkDB-Connect](placeholder.png)

### 1.2.3 配置Zotero导出格式为IEEE

![配置Zotero导出格式为IEEE](placeholder.png)

### 1.2.4 安装Ob插件：Zotero Integration

![安装Ob插件：Zotero Integration](placeholder.png)

### 1.2.5 新建Ob模板文件

在Ob中新建文件，命名为 `_Template.md`，并粘贴以下代码，保存。

注意复制完整哦！

```markdown
---
citekey: {{citekey}}
Tags: [{% for t in tags %}"{{ t.tag | escape }}"{% if not loop.last %}, {% endif %}{% endfor %}{% if tags.length > 0 %}, {% endif %}"ZoteroIntegration"]
{% if authorsExtended or authors %}Authors: {{authorsExtended | default(authors)}}{% endif %}
{% if DOI %}DOI: {{DOI}}{% endif %}
---
{% set links = "" %}
{%- if itemKey -%}
  {%- set links = "[Zotero](zotero://select/library/items/" ~ itemKey ~ ")" -%}
{%- endif -%}
{%- if pdfLink -%}
  {%- if links != "" -%}
    {%- set links = links ~ " | " -%}
  {%- endif -%}
  {%- set links = links ~ pdfLink -%}
{%- endif -%}
{%- if url -%}
  {%- if links != "" -%}
    {%- set links = links ~ " | " -%}
  {%- endif -%}
  {%- set links = links ~ "[URL](" ~ url ~ ")" -%}
{%- endif -%}
{{ exportDate | format("YYYY-MM-DD HH:mm") }} | {{ links }}

{% persist "Obsidian笔记" %}
{% endpersist %}


{% if notes.length === 0 %}
%%*No Zotero notes found for this item.*%%
{%- elif notes.length === 1 -%}
{%- set firstNote = notes[0] -%}
{%- set lines = firstNote.note.split('\n') -%}
{%- set firstLine = lines[0] | replace("# ", "") -%}
{%- set restOfContent = lines.slice(1).join('\n') -%}
# {{ firstLine }}（Zotero笔记）  
*{{ firstNote.dateModified | format("YYYY-MM-DD HH:mm:ss") }}*{%- for tag in firstNote.tags -%} #{{ tag.tag }}{%- endfor %}
{{ restOfContent | replace("# ", "## ") }}
{% else %}
# Zotero笔记
{%- for note in notes -%}
{%- set lines = note.note.split('\n') -%}
{%- set firstLine = lines[0] | replace("# ", "") -%}
{% set restOfContent = lines.slice(1).join('\n') %}

## {{ firstLine }}（Zotero笔记{{ loop.index }}）  
*{{ note.dateModified | format("YYYY-MM-DD HH:mm:ss") }}*{%- for tag in note.tags -%} #{{ tag.tag }}{%- endfor %}
{{ restOfContent | replace("# ", "### ") }}
{%- endfor -%}
{%- endif %}



{% if annotations.length > 0 %}
{%- set colorMap = {
  "#ffd400": { "name": "yellow", "hex": "#f57f17" },
  "#ff6666": { "name": "red", "hex": "#b71c1c" },
  "#5fb236": { "name": "green", "hex": "#5fb236" },
  "#2ea8e5": { "name": "blue", "hex": "#2ea8e5" },
  "#a28ae5": { "name": "purple", "hex": "#4527a0" },
  "#e56eee": { "name": "carmine", "hex": "#ad1457" },
  "#f19837": { "name": "orange", "hex": "#d84315" },
  "#aaaaaa": { "name": "grey", "hex": "#aaaaaa" }
} -%}
# PDF 注释
*{{importDate | format("YYYY-MM-DD HH:mm:ss")}}*
<section class="annotation-container">
{% for annotation in annotations %}
{% set colorInfo = colorMap[annotation.color] %}
{%- if annotation.annotatedText -%}
<blockquote data-color="{{ colorInfo.name }}" style="--theme-color:{{colorInfo.hex}};border-left-color:color-mix(in srgb, var(--theme-color) 50%, transparent);"><a style="color:var(--theme-color);text-decoration: underline dotted color-mix(in srgb, var(--theme-color) 70%, transparent);" href="zotero://open-pdf/library/items/{{ annotation.attachment.itemKey }}?page={{ annotation.page }}&annotation={{ annotation.id }}">{{ annotation.annotatedText }}</a> <span style="opacity:0.7">(P<sub>{{ annotation.pageLabel }}</sub>)</span>
{%- endif -%}

{% if annotation.comment %}
<p>{{ annotation.comment }}</p>
{%- endif -%}

{%- if annotation.imageRelativePath -%}
  ![[{{ annotation.imageRelativePath }}]]
{% endif %}
</blockquote>
{% endfor %}
</section>
{% else %}
%*未找到任何 PDF 注释。*%
{% endif %}


# 更多信息
## Item Details
Citation: '{{ bibliography | replace(r/^\[\d+\]\s*/, "") }}'
{% if itemType -%}
- **Item Type:** {{itemType}}
{% endif -%}
{% if title -%}
- **Title:** {{title}}
{% endif -%}
{% if authorsExtended or authors -%}
- **Authors:** {{authorsExtended | default(authors)}}
{% endif -%}
{% if editors -%}
- **Editors:** {{editors}}
{% endif -%}
{% if publicationTitle -%}
- **Publication / Journal:** {{publicationTitle}}
{% endif -%}
{% if journalAbbreviation -%}
- **Journal Abbreviation:** {{journalAbbreviation}}
{% endif -%}
{% if volume -%}
- **Volume:** {{volume}}
{% endif -%}
{% if issue -%}
- **Issue:** {{issue}}
{% endif -%}
{% if pages -%}
- **Pages:** {{pages}}
{% endif -%}
{% if series -%}
- **Series:** {{series}}
{% endif -%}
{% if edition -%}
- **Edition:** {{edition}}
{% endif -%}
{% if place -%}
- **Place of Publication:** {{place}}
{% endif -%}
{% if publisher -%}
- **Publisher:** {{publisher}}
{% endif -%}
{% if date -%}
- **Date Published:** {{date | format("YYYY-MM-DD")}}
{% endif -%}
{% if year -%}
- **Year:** {{year}}
{% endif -%}
{% if dateAdded -%}
- **Date Added (to Zotero):** {{dateAdded | format("YYYY-MM-DD HH:mm:ss")}}
{% endif -%}
{% if dateModified -%}
- **Date Modified (in Zotero):** {{dateModified | format("YYYY-MM-DD HH:mm:ss")}}
{% endif %}

## Identifiers & Links
{% if DOI -%}
- **DOI:** [{{DOI}}](https://doi.org/{{DOI}})
{% endif -%}
{% if ISBN -%}
- **ISBN:** {{ISBN}}
{% endif -%}
{% if ISSN -%}
- **ISSN:** {{ISSN}}
{% endif -%}
{% if url -%}
- **URL:** [Link]({{url}})
{% endif -%}
{% if itemKey -%}
- **Zotero Select Link:** [Open in Zotero Library](zotero://select/library/items/{{itemKey}})
{% endif -%}
{% if pdfZoteroLink -%}
- **Zotero Full PDF Link (primary):** {{pdfZoteroLink}}
{% endif %}

## Abstract
{% if abstractNote -%}
{{abstractNote}}
{% endif %}

## Collections & Tags from Zotero
{% if collections and collections.length > 0 -%}
- **Zotero Collections:** {% for c in collections %}{{c.name}}{% if not loop.last %}, {% endif %}{% endfor %}
{% endif -%}
{% if tags and tags.length > 0 -%}
- **Zotero Tags for this Item:**
  {% for t in tags -%}
  - [{{t.tag}}](zotero://select/library/tags/{{t.tag | urlencode}})
  {% endfor -%}
{% endif %}

## Files & Attachments
{% if attachments and attachments | filterby("path") | filterby("contentType", "eq", "application/pdf") | length > 0 or attachments and attachments | filterby("linkMode", "eq", "imported_file") | length > 0 -%}
- **Local File Links (if available):**
    {% for att in attachments -%}
        {% if att.path and (att.contentType == "application/pdf" or att.linkMode == "imported_file") -%}
        - [{{att.title | default("Attachment")}} ({{att.contentType}})](file://{{att.path | urlencode}})
        {% endif -%}
    {% endfor -%}
{% endif -%}
{% if attachments and attachments.length > 0 -%}
- **All Attachments (details):**
    {% for att in attachments -%}
    - **{{att.title | default("Untitled Attachment")}}**
      {% if att.contentType -%}- **Type:** {{att.contentType}}{% endif -%}
      {% if att.path -%}[Open with default](file://{{att.path | replace(" ", "%20")}}){% endif -%}
      {% if att.itemKey or att.key %}  [Open in Zotero](zotero://open-pdf/library/items/{{att.itemKey | default(att.key)}}){% endif -%}
      {% if att.note -%}- **Note:** {{att.note | nl2br}}{% endif -%}
    {% endfor -%}
{% endif %}

## Other Metadata
{% if archive -%}
- **Archive:** {{archive}}
{% endif -%}
{% if archiveLocation -%}
- **Archive Location:** {{archiveLocation}}
{% endif -%}
{% if libraryCatalog -%}
- **Library Catalog:** {{libraryCatalog}}
{% endif -%}
{% if callNumber -%}
- **Call Number:** {{callNumber}}
{% endif -%}
{% if rights -%}
- **Rights:** {{rights}}
{% endif -%}
{% if language -%}
- **Language:** {{language}}
{% endif -%}
{% if shortTitle -%}
- **Short Title:** {{shortTitle}}
{% endif -%}
{% if extra -%}
- **Extra Field:**
  {{extra | nl2br}}
{% endif %}

{% if annotations.length > 0 -%}
<style>
{%- for key, value in colorMap -%}
blockquote[data-color={{ value.name }}] {--theme-color: {{ value.hex }};}
{%- endfor -%}
blockquote{border-left-color:color-mix(in srgb, var(--theme-color) 70%, transparent);}
blockquote a{color:var(--theme-color);text-decoration: underline dotted color-mix(in srgb, var(--theme-color) 70%, transparent);}
</style>
{%- endif -%}
```

### 1.2.6 配置Zotero Integration插件

依次选择：

![配置Zotero Integration插件-1](placeholder.png)
![配置Zotero Integration插件-2](placeholder.png)

依次输入导入样式1、`{{title}}.md`、`{{title}}/`、`image`、`_Template.md`。

![配置Zotero Integration插件-3](placeholder.png)

### 1.2.7 完成！

## 1.3 使用教程

保持Zotero打开，在Obsidian的任意界面，按下 `Ctrl+P`，弹出框中选择"导入样式1"。

![使用教程-1](placeholder.png)

选择论文（一篇或多篇）。

![使用教程-2](placeholder.png)

搞定！

如您有其他问题，欢迎在评论区交流！

![完成](placeholder.png)

## 1.4 留言

> **许翎曦** (美国, 6月28日)
> 为什么你代码，我复制进去报错
>
> > **lzc的碎碎念** (作者, 6月28日)
> > 可以截图报错信息看看吗？
>
> > **许翎曦** (美国, 6月28日)
> > 回复 lzc的碎碎念：谢谢你，发你公众号后台了

> **wxid_g44dgop40v6c22** (上海, 6月9日)
> 太好了，有endnote吗
>
> > **lzc的碎碎念** (作者, 6月9日)
> > 抱歉，还没有endnote的哦

*已无更多数据*
