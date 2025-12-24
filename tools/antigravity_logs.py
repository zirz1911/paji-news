#!/usr/bin/env python3
"""
Antigravity Log Reader
อ่านและวิเคราะห์ logs จาก Antigravity (Google AI Coding Assistant)

Usage:
    python antigravity_logs.py              # Show latest logs
    python antigravity_logs.py --tail 100   # Show last 100 lines
    python antigravity_logs.py --errors     # Show only errors
    python antigravity_logs.py --analyze    # Analyze log patterns
    python antigravity_logs.py --sessions   # List all sessions
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
from collections import Counter

# Antigravity logs location
LOGS_BASE = Path.home() / "Library/Application Support/Antigravity/logs"

def get_latest_session():
    """Get the most recent session folder."""
    if not LOGS_BASE.exists():
        print("❌ Antigravity logs folder not found")
        return None

    sessions = sorted([d for d in LOGS_BASE.iterdir() if d.is_dir()])
    if not sessions:
        print("❌ No sessions found")
        return None

    return sessions[-1]

def get_main_log_path(session_path):
    """Get the main Antigravity.log path from a session."""
    log_path = session_path / "window1/exthost/google.antigravity/Antigravity.log"
    if log_path.exists():
        return log_path
    return None

def get_app_info():
    """Get Antigravity app information."""
    app_support = Path.home() / "Library/Application Support/Antigravity"

    info = {
        "name": "Antigravity",
        "developer": "Google",
        "type": "VS Code-based IDE",
        "extensions": []
    }

    # Get latest session to find extensions
    session = get_latest_session()
    if session:
        exthost_path = session / "window1/exthost"
        if exthost_path.exists():
            for item in exthost_path.iterdir():
                if item.is_dir() and not item.name.startswith("output_"):
                    info["extensions"].append(item.name)

    return info

def show_app_info():
    """Display app information."""
    info = get_app_info()

    print("🖥️  Application Info")
    print("=" * 50)
    print(f"App Name:    {info['name']}")
    print(f"Developer:   {info['developer']}")
    print(f"Type:        {info['type']}")
    print(f"Logs Path:   {LOGS_BASE}")
    print()
    print("📦 Installed Extensions:")
    print("-" * 50)
    for ext in sorted(info['extensions']):
        if 'claude' in ext.lower():
            print(f"  🟣 {ext}")
        elif 'google' in ext.lower() or 'antigravity' in ext.lower():
            print(f"  🔵 {ext}")
        elif 'github' in ext.lower():
            print(f"  ⚫ {ext}")
        elif 'python' in ext.lower():
            print(f"  🟡 {ext}")
        else:
            print(f"  ⚪ {ext}")
    print("=" * 50)

def list_sessions():
    """List all available sessions."""
    if not LOGS_BASE.exists():
        print("❌ Antigravity logs folder not found")
        return

    sessions = sorted([d for d in LOGS_BASE.iterdir() if d.is_dir()])

    # Show app info first
    show_app_info()
    print()

    print("📁 Antigravity Sessions")
    print("=" * 50)

    for session in sessions:
        # Parse timestamp from folder name (e.g., 20251224T162423)
        try:
            name = session.name
            date_str = f"{name[:4]}-{name[4:6]}-{name[6:8]} {name[9:11]}:{name[11:13]}"
            log_path = get_main_log_path(session)
            status = "✅" if log_path and log_path.exists() else "⚠️"

            # Get log size
            if log_path and log_path.exists():
                size = log_path.stat().st_size
                size_str = f"{size / 1024:.1f} KB"
            else:
                size_str = "N/A"

            print(f"{status} {date_str} | {session.name} | {size_str}")
        except:
            print(f"⚠️ {session.name}")

    print("=" * 50)
    print(f"Total: {len(sessions)} sessions")

def read_logs(lines=50, errors_only=False):
    """Read latest logs."""
    session = get_latest_session()
    if not session:
        return

    log_path = get_main_log_path(session)
    if not log_path:
        print(f"❌ Log file not found in session: {session.name}")
        return

    print(f"📄 Reading: {log_path}")
    print(f"📅 Session: {session.name}")
    print("=" * 60)

    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        all_lines = f.readlines()

    if errors_only:
        # Filter for errors and warnings
        filtered = [l for l in all_lines if '[error]' in l.lower() or '[warn]' in l.lower() or 'failed' in l.lower()]
        display_lines = filtered[-lines:]
        print(f"🔴 Showing {len(display_lines)} errors/warnings (of {len(filtered)} total)")
    else:
        display_lines = all_lines[-lines:]
        print(f"📝 Showing last {len(display_lines)} lines (of {len(all_lines)} total)")

    print("=" * 60)

    for line in display_lines:
        # Colorize output
        if '[error]' in line.lower() or 'failed' in line.lower():
            print(f"🔴 {line.rstrip()}")
        elif '[warn]' in line.lower():
            print(f"🟡 {line.rstrip()}")
        elif '[info]' in line.lower():
            print(f"🔵 {line.rstrip()}")
        else:
            print(f"   {line.rstrip()}")

def analyze_logs():
    """Analyze log patterns."""
    session = get_latest_session()
    if not session:
        return

    log_path = get_main_log_path(session)
    if not log_path:
        print(f"❌ Log file not found in session: {session.name}")
        return

    print(f"📊 Analyzing: {log_path}")
    print(f"📅 Session: {session.name}")
    print("=" * 60)

    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        all_lines = f.readlines()

    # Count log levels
    levels = Counter()
    patterns = Counter()

    for line in all_lines:
        # Count levels
        if '[error]' in line.lower():
            levels['error'] += 1
        elif '[warn]' in line.lower():
            levels['warning'] += 1
        elif '[info]' in line.lower():
            levels['info'] += 1

        # Count common patterns
        if 'truncated' in line.lower():
            patterns['truncated'] += 1
        if 'failed' in line.lower():
            patterns['failed'] += 1
        if 'supercomplete' in line.lower():
            patterns['supercomplete'] += 1
        if 'trajectory' in line.lower():
            patterns['trajectory'] += 1

    # Get time range
    first_time = None
    last_time = None
    for line in all_lines:
        if line.startswith('2025-'):
            try:
                time_str = line[:23]
                if not first_time:
                    first_time = time_str
                last_time = time_str
            except:
                pass

    print("\n📈 Log Analysis")
    print("-" * 40)
    print(f"Total Lines: {len(all_lines)}")
    print(f"Time Range: {first_time} → {last_time}")

    print("\n📊 Log Levels")
    print("-" * 40)
    print(f"🔵 Info:     {levels['info']}")
    print(f"🟡 Warning:  {levels['warning']}")
    print(f"🔴 Error:    {levels['error']}")

    print("\n🔍 Common Patterns")
    print("-" * 40)
    for pattern, count in patterns.most_common(10):
        print(f"  {pattern}: {count}")

    print("\n" + "=" * 60)

def read_terminal_history(lines=30):
    """Read terminal command history from Antigravity."""
    global_storage = Path.home() / "Library/Application Support/Antigravity/User/globalStorage/state.vscdb"

    if not global_storage.exists():
        print("❌ Global storage not found")
        return

    try:
        import sqlite3
        import json

        conn = sqlite3.connect(str(global_storage))
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM ItemTable WHERE key='terminal.history.entries.commands'")
        result = cursor.fetchone()
        conn.close()

        if not result:
            print("❌ No terminal history found")
            return

        data = json.loads(result[0])
        entries = data.get('entries', [])

        print("📜 Antigravity Terminal Command History")
        print("=" * 70)
        print(f"Showing last {min(lines, len(entries))} of {len(entries)} commands")
        print("-" * 70)

        for i, entry in enumerate(entries[-lines:], 1):
            cmd = entry.get('key', '').strip()
            shell = entry.get('value', {}).get('shellType', 'unknown')

            # Color code by shell type
            if shell == 'python':
                shell_icon = "🐍"
            elif shell == 'node':
                shell_icon = "📦"
            elif shell == 'zsh' or shell == 'bash':
                shell_icon = "💻"
            else:
                shell_icon = "⚪"

            if cmd:
                # Truncate long commands
                cmd_display = cmd[:60] + "..." if len(cmd) > 60 else cmd
                print(f"{i:3}. {shell_icon} [{shell:7}] {cmd_display}")

        print("=" * 70)

    except Exception as e:
        print(f"❌ Error reading terminal history: {e}")

def main():
    parser = argparse.ArgumentParser(description='Antigravity Log Reader')
    parser.add_argument('--tail', '-n', type=int, default=50, help='Number of lines to show')
    parser.add_argument('--errors', '-e', action='store_true', help='Show only errors')
    parser.add_argument('--analyze', '-a', action='store_true', help='Analyze log patterns')
    parser.add_argument('--sessions', '-s', action='store_true', help='List all sessions')
    parser.add_argument('--info', '-i', action='store_true', help='Show app info')
    parser.add_argument('--terminal', '-t', action='store_true', help='Show terminal command history')

    args = parser.parse_args()

    if args.info:
        show_app_info()
    elif args.sessions:
        list_sessions()
    elif args.analyze:
        analyze_logs()
    elif args.terminal:
        read_terminal_history(lines=args.tail)
    else:
        read_logs(lines=args.tail, errors_only=args.errors)

if __name__ == '__main__':
    main()
