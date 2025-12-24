# CLAUDE.md - paji-news AI Guidelines

## Project Overview

`paji-news` เป็น repository สำหรับสร้างและจัดเก็บเนื้อหาข่าวโดยใช้ AI ช่วย

## Content Types

### 1. Text/Article
- บทความข่าว
- ข่าวด่วน (Breaking News)
- บทความเชิงลึก (Feature Article)
- สรุปข่าว (Summary)

### 2. Image/Infographic
- Infographic briefs
- Image descriptions
- Visual content ideas

## Writing Guidelines

### Tone & Style
- เขียนตรงประเด็น กระชับ
- ใช้ภาษาที่เข้าใจง่าย
- หลีกเลี่ยงศัพท์เทคนิคที่ไม่จำเป็น
- รองรับทั้งภาษาไทยและอังกฤษ

### Article Structure
1. **Headline** - หัวข้อดึงดูดความสนใจ
2. **Lead** - สรุปใจความสำคัญ 1-2 ประโยค
3. **Body** - รายละเอียดข่าว
4. **Conclusion** - สรุป/ผลกระทบ

### File Naming Convention
```
articles/YYYY-MM/YYYY-MM-DD-title-slug.md
assets/YYYY-MM/YYYY-MM-DD-image-name.png
```

## AI Usage

### When Writing Articles
1. ใช้ prompt จาก `prompts/article-writer.md`
2. ระบุ topic, tone, และ target audience
3. Review และ edit ก่อน publish

### When Summarizing
1. ใช้ prompt จาก `prompts/summarizer.md`
2. ระบุ source และ desired length
3. ตรวจสอบความถูกต้องของข้อมูล

### When Creating Infographics
1. ใช้ prompt จาก `prompts/infographic-ideas.md`
2. ระบุ data points และ key message
3. สร้าง brief สำหรับ designer

## Voice Notification | แจ้งเตือนด้วยเสียง

**ทุกครั้งที่ทำงานเสร็จ** ให้ใช้ `say` command แจ้งเตือน (English):

```bash
say "Task completed. [Brief description of what was done]."
```

**ตัวอย่าง:**
```bash
say "Task completed. Article created and pushed to GitHub."
say "Task completed. Retrospective saved."
say "Task completed. Year updated in all articles."
```

---

## Quality Checklist

Before publishing:
- [ ] ตรวจสอบความถูกต้องของข้อมูล
- [ ] Headline ดึงดูดและตรงประเด็น
- [ ] Lead สรุปใจความสำคัญครบ
- [ ] ไม่มี typos หรือ grammatical errors
- [ ] มี source/reference ถ้าจำเป็น
- [ ] รูปภาพมี alt text

## Short Codes

| Code | Action |
|------|--------|
| `write [topic]` | เขียนบทความใหม่ |
| `summarize [url/text]` | สรุปข่าว |
| `infographic [topic]` | สร้าง infographic brief |

## Folder Structure

```
paji-news/
├── templates/         # ใช้เป็น base สำหรับเขียน
├── articles/          # บทความที่เสร็จแล้ว
├── assets/            # รูปภาพและ media
└── prompts/           # AI prompts
```

---
**Last Updated**: 2025-12-24
**Version**: 1.0.0
