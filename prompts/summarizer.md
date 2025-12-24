# Summarizer Prompt

## Usage
ใช้ prompt นี้เพื่อให้ AI ช่วยสรุปข่าว

## Prompt Template

```
คุณเป็นผู้เชี่ยวชาญในการสรุปข่าว ช่วยสรุปเนื้อหาต่อไปนี้:

## Original Content
[วางเนื้อหาต้นฉบับ หรือ URL]

## Summary Length
[TL;DR: 1-2 sentences / Short: 3-5 sentences / Medium: 1-2 paragraphs]

## Format
[bullet-points / paragraph / key-takeaways]

## Focus On
[ระบุประเด็นที่ต้องการเน้น - optional]

## Language
[Thai / English / Same as original]

## Requirements
- สรุปใจความสำคัญครบถ้วน
- ไม่ใส่ความเห็นส่วนตัว
- รักษา accuracy ของข้อมูล
- ระบุ source ต้นฉบับ
```

## Example

```
คุณเป็นผู้เชี่ยวชาญในการสรุปข่าว ช่วยสรุปเนื้อหาต่อไปนี้:

## Original Content
[วางบทความยาวๆ ที่นี่]

## Summary Length
Short: 3-5 sentences

## Format
key-takeaways

## Language
Thai

## Requirements
- สรุปใจความสำคัญครบถ้วน
- ไม่ใส่ความเห็นส่วนตัว
- รักษา accuracy ของข้อมูล
```

## Output Format

```markdown
## TL;DR
[1-2 ประโยคสรุปสั้นมาก]

## Key Takeaways
1. [ประเด็นสำคัญ 1]
2. [ประเด็นสำคัญ 2]
3. [ประเด็นสำคัญ 3]

## Why It Matters
[ทำไมเรื่องนี้สำคัญ]

## Source
[แหล่งที่มา]
```

## Tips
- ตรวจสอบความถูกต้องหลังได้ผลลัพธ์
- อย่าสรุปสั้นเกินจนขาดข้อมูลสำคัญ
- ระบุถ้ามีข้อมูลที่ไม่แน่ใจ
