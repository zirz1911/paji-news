---
title: "Claude Code เปิดตัว Custom Slash Commands ช่วยเพิ่มประสิทธิภาพการทำงาน"
date: 2025-12-24
category: breaking
tags: [AI, Claude, Developer Tools, Productivity]
author: paji-news
---

## Headline
Claude Code เปิดตัว Custom Slash Commands ช่วยเพิ่มประสิทธิภาพการทำงาน

## Lead
Anthropic ได้เพิ่มฟีเจอร์ Custom Slash Commands ใน Claude Code CLI tool ทำให้นักพัฒนาสามารถสร้างคำสั่งลัดส่วนตัวเพื่อเพิ่มประสิทธิภาพ workflow ได้

## Key Points
- สร้าง custom commands ได้ง่ายๆ ด้วยไฟล์ Markdown
- รองรับทั้ง project-level และ global commands
- ใช้ YAML frontmatter กำหนด description และ allowed-tools
- รองรับ arguments และ bash command execution

## Details
Claude Code ซึ่งเป็น CLI tool อย่างเป็นทางการของ Anthropic สำหรับการทำงานกับ Claude AI ได้เพิ่มความสามารถในการสร้าง custom slash commands ทำให้นักพัฒนาสามารถกำหนด workflow ที่ใช้บ่อยเป็นคำสั่งสั้นๆ ได้

### วิธีการสร้าง Custom Command

สร้างไฟล์ `.md` ใน folder ที่กำหนด:
- **Global**: `~/.claude/commands/` - ใช้ได้ทุก project
- **Project**: `.claude/commands/` - ใช้ได้เฉพาะ project นั้น

### ตัวอย่าง Command

```markdown
---
description: สร้าง commit message อัตโนมัติ
allowed-tools: Bash
---

# Auto Commit

วิเคราะห์ git diff และสร้าง commit message ที่เหมาะสม
```

## Impact
ฟีเจอร์นี้ช่วยให้นักพัฒนาสามารถ:
- ลดเวลาในการพิมพ์คำสั่งซ้ำๆ
- สร้าง workflow ที่เป็นมาตรฐานสำหรับทีม
- แชร์ best practices ผ่าน git repository

## Source
- [Claude Code Documentation](https://docs.anthropic.com/claude-code)

---
*Published: 2025-12-24 16:30 GMT+7*
