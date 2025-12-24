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

## License

MIT
