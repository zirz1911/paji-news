# paji-news

News Content Repository - AI-powered news articles and infographics

## Overview

`paji-news` เป็น repository สำหรับจัดเก็บและจัดการเนื้อหาข่าวในรูปแบบ Markdown โดยใช้ AI ช่วยสร้างเนื้อหา

## Features

- **Text/Article** - บทความข่าว ข้อความ
- **Image/Infographic** - รูปภาพ กราฟิกข่าว
- **AI-Powered** - ใช้ AI ช่วยเขียนและสร้างเนื้อหา
- **Templates** - มี templates สำเร็จรูปสำหรับข่าวประเภทต่างๆ

## Structure

```
paji-news/
├── README.md              # Project overview
├── CLAUDE.md              # AI Guidelines
├── templates/             # Templates สำหรับข่าวประเภทต่างๆ
│   ├── breaking-news.md
│   ├── feature-article.md
│   ├── summary.md
│   └── infographic.md
├── articles/              # บทความข่าว
│   └── YYYY-MM/           # จัดเก็บตามเดือน
├── assets/                # รูปภาพ, กราฟิก
│   └── YYYY-MM/
└── prompts/               # AI Prompts สำหรับสร้างข่าว
    ├── article-writer.md
    ├── summarizer.md
    └── infographic-ideas.md
```

## Quick Start

1. เลือก template ที่ต้องการจาก `templates/`
2. ใช้ AI prompt จาก `prompts/` ช่วยสร้างเนื้อหา
3. บันทึกบทความใน `articles/YYYY-MM/`
4. เก็บรูปภาพใน `assets/YYYY-MM/`

## Templates

| Template | ใช้สำหรับ |
|----------|----------|
| `breaking-news.md` | ข่าวด่วน ข่าวสั้น |
| `feature-article.md` | บทความเชิงลึก |
| `summary.md` | สรุปข่าว |
| `infographic.md` | Brief สำหรับสร้าง Infographic |

## AI Prompts

| Prompt | หน้าที่ |
|--------|--------|
| `article-writer.md` | ช่วยเขียนบทความข่าว |
| `summarizer.md` | สรุปข่าวให้กระชับ |
| `infographic-ideas.md` | สร้างไอเดีย Infographic |

## How to Write News (Workflow)

### Workflow Diagram
```
┌─────────────────────────────────────────────────────────┐
│                    NEWS WRITING WORKFLOW                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. CHOOSE TYPE          2. USE TEMPLATE                │
│  ┌──────────────┐       ┌──────────────┐               │
│  │ Breaking?    │──────▶│ breaking-    │               │
│  │ Feature?     │       │ news.md      │               │
│  │ Summary?     │       │ feature-     │               │
│  │ Infographic? │       │ article.md   │               │
│  └──────────────┘       └──────────────┘               │
│         │                      │                        │
│         ▼                      ▼                        │
│  3. AI ASSIST            4. WRITE & EDIT               │
│  ┌──────────────┐       ┌──────────────┐               │
│  │ Use prompts/ │──────▶│ Fill template│               │
│  │ article-     │       │ Review & edit│               │
│  │ writer.md    │       │ Add sources  │               │
│  └──────────────┘       └──────────────┘               │
│         │                      │                        │
│         ▼                      ▼                        │
│  5. SAVE                 6. COMMIT                      │
│  ┌──────────────┐       ┌──────────────┐               │
│  │ articles/    │──────▶│ git add      │               │
│  │ YYYY-MM/     │       │ git commit   │               │
│  │ filename.md  │       │ git push     │               │
│  └──────────────┘       └──────────────┘               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Step-by-Step Guide

#### Step 1: เลือกประเภทข่าว
| ประเภท | เมื่อไหร่ใช้ |
|--------|------------|
| Breaking News | ข่าวด่วน เหตุการณ์ใหม่ ต้องการความรวดเร็ว |
| Feature Article | บทความเชิงลึก วิเคราะห์ มีหลาย sections |
| Summary | สรุปข่าวจากแหล่งอื่น ต้องการความกระชับ |
| Infographic | ต้องการสร้าง visual content |

#### Step 2: Copy Template
```bash
cp templates/[type].md articles/$(date +%Y-%m)/$(date +%Y-%m-%d)-title-slug.md
```

#### Step 3: ใช้ AI ช่วยเขียน
1. เปิดไฟล์ `prompts/article-writer.md`
2. ใส่ข้อมูล: Topic, Type, Tone, Key Information
3. ให้ AI generate draft
4. Review และ edit

#### Step 4: ตรวจสอบก่อน Publish
- [ ] Headline ดึงดูดและตรงประเด็น
- [ ] Lead สรุปใจความสำคัญครบ
- [ ] ข้อมูลถูกต้อง มี source
- [ ] ไม่มี typos
- [ ] Format ถูกต้องตาม template

#### Step 5: Save & Commit
```bash
git add articles/
git commit -m "article: [headline]"
git push
```

### File Naming Convention
```
articles/YYYY-MM/YYYY-MM-DD-title-slug.md

ตัวอย่าง:
articles/2024-12/2024-12-24-ai-trends-2025.md
articles/2024-12/2024-12-24-breaking-tech-news.md
```

### Tips
- ใช้ภาษาที่เข้าใจง่าย หลีกเลี่ยงศัพท์เทคนิคที่ไม่จำเป็น
- ใส่ source/reference เสมอ
- Review อย่างน้อย 1 รอบก่อน commit
- ใช้ tags ที่เกี่ยวข้องเพื่อง่ายต่อการค้นหา

## License

MIT
