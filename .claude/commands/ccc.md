---
description: Create Context & Compact - บันทึก session context เป็น GitHub Issue แล้วแจ้งให้ compact conversation
allowed-tools: Bash, Read, Glob, Grep
---

# Create Context & Compact (ccc)

เมื่อ user พิมพ์ `/ccc` ให้ทำตามขั้นตอนนี้:

## Step 1: Gather Information

รันคำสั่งเหล่านี้พร้อมกันเพื่อรวบรวมข้อมูล:

```bash
# Git status
git status --porcelain

# Recent commits
git log --oneline -5

# Current branch
git branch --show-current

# Check for uncommitted changes
git diff --stat
```

## Step 2: Create GitHub Context Issue

สร้าง GitHub Issue ด้วย `gh issue create` โดยใช้ template นี้:

```bash
gh issue create --title "context: [Session Context] - $(date +%Y-%m-%d %H:%M)" --body "$(cat <<'TEMPLATE'
## Session Context

**Date**: $(date +%Y-%m-%d)
**Time**: $(TZ='Asia/Bangkok' date +%H:%M) GMT+7
**Branch**: [current branch]

## Current State

### Git Status
```
[paste git status output]
```

### Recent Commits
```
[paste git log output]
```

## Changed Files
- [ ] file1
- [ ] file2

## Key Discoveries
<!-- สิ่งที่ค้นพบระหว่าง session -->
1.
2.
3.

## Current Progress
<!-- กำลังทำอะไรอยู่ -->


## Next Steps
<!-- ต้องทำอะไรต่อ -->
- [ ]
- [ ]
- [ ]

## Notes
<!-- หมายเหตุเพิ่มเติม -->


---
*Context saved by /ccc command*
TEMPLATE
)"
```

## Step 3: Report & Compact

หลังสร้าง Issue แล้ว:

1. แสดง Issue URL ให้ user
2. แจ้ง user ว่า:
   ```
   Context saved!
   Issue: [URL]

   กรุณารัน /compact เพื่อ compact conversation
   ```

## Important Notes

- ใช้ Time Zone GMT+7 (Bangkok) เสมอ
- Issue title ต้องขึ้นต้นด้วย `context:` เพื่อแยกจาก issue ประเภทอื่น
- รวบรวมข้อมูลจาก conversation ปัจจุบันใส่ใน Key Discoveries และ Current Progress
- อย่าลืมแจ้งให้ user รัน `/compact` หลังเสร็จ
