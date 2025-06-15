#!/usr/bin/env python3
"""
🤖 AI Session Update Utility

This script helps AI assistants maintain context between sessions by:
- Logging actions taken
- Updating session history
- Tracking code changes
- Maintaining project state awareness

Usage:
    python ai_session_update.py --action "description" --files "file1,file2"
"""

import argparse
import datetime
import os
import subprocess
from pathlib import Path
from typing import List, Optional


class AISessionTracker:
    """📝 Tracks AI session activities and maintains context files"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.session_log = self.project_root / "AI_SESSION_LOG.md"
        self.codebase_map = self.project_root / "CODEBASE_MAP.md"
    
    def log_action(self, action: str, files_changed: Optional[List[str]] = None, 
                   notes: Optional[str] = None) -> None:
        """
        📝 Log an action taken by an AI assistant
        
        Args:
            action: Description of what was done
            files_changed: List of files that were modified
            notes: Additional notes or observations
        """
        timestamp = datetime.datetime.now().isoformat()
        
        # 🔍 Get current git info if available
        git_info = self._get_git_info()
        
        # 📥 Read current session log
        session_content = self._read_file(self.session_log)
        
        # 🔄 Create new session entry
        new_entry = self._create_session_entry(timestamp, action, files_changed, notes, git_info)
        
        # 📝 Update session log
        updated_content = self._insert_session_entry(session_content, new_entry)
        
        # 💾 Save updated log
        self._write_file(self.session_log, updated_content)
        
        print(f"✅ Session logged: {action}")
    
    def update_file_status(self, file_path: str, status: str, notes: str = "") -> None:
        """
        🔄 Update the status of a specific file in the codebase map
        
        Args:
            file_path: Path to the file
            status: New status (e.g., '✅ Implemented', '🔄 In Progress')
            notes: Additional notes about the file
        """
        # This would update the CODEBASE_MAP.md file
        # Implementation depends on the specific format needed
        print(f"🔄 File status updated: {file_path} -> {status}")
    
    def _get_git_info(self) -> dict:
        """🔍 Get current git status information"""
        try:
            # Get current branch
            branch = subprocess.check_output(
                ["git", "branch", "--show-current"], 
                cwd=self.project_root,
                text=True
            ).strip()
            
            # Get last commit
            last_commit = subprocess.check_output(
                ["git", "log", "-1", "--oneline"],
                cwd=self.project_root,
                text=True
            ).strip()
            
            # Get status
            status = subprocess.check_output(
                ["git", "status", "--porcelain"],
                cwd=self.project_root,
                text=True
            ).strip()
            
            return {
                "branch": branch,
                "last_commit": last_commit,
                "has_changes": bool(status),
                "status": status
            }
        except subprocess.CalledProcessError:
            return {"error": "Not a git repository or git not available"}
    
    def _read_file(self, file_path: Path) -> str:
        """📥 Read file content safely"""
        try:
            return file_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            return ""
    
    def _write_file(self, file_path: Path, content: str) -> None:
        """💾 Write file content safely"""
        file_path.write_text(content, encoding='utf-8')
    
    def _create_session_entry(self, timestamp: str, action: str, 
                            files_changed: Optional[List[str]], 
                            notes: Optional[str], git_info: dict) -> str:
        """📝 Create a new session entry"""
        entry = f"\n### Session Update - {timestamp}\n"
        entry += f"**Action**: {action}\n\n"
        
        if files_changed:
            entry += "**Files Modified**:\n"
            for file in files_changed:
                entry += f"- 📝 `{file}`\n"
            entry += "\n"
        
        if notes:
            entry += f"**Notes**: {notes}\n\n"
        
        if "error" not in git_info:
            entry += f"**Git Status**: {git_info['branch']} - {git_info['last_commit']}\n\n"
        
        return entry
    
    def _insert_session_entry(self, content: str, new_entry: str) -> str:
        """🔄 Insert new session entry in the right place"""
        # Find the session history section and insert the new entry
        lines = content.split('\n')
        insert_index = -1
        
        for i, line in enumerate(lines):
            if "## 🚀 Session History" in line:
                insert_index = i + 2  # Insert after the header
                break
        
        if insert_index > 0:
            lines.insert(insert_index, new_entry)
            return '\n'.join(lines)
        else:
            # If section not found, append to end
            return content + new_entry


def main():
    """🚀 Main CLI interface for AI session tracking"""
    parser = argparse.ArgumentParser(
        description="🤖 AI Session Update Utility",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--action", 
        required=True,
        help="Description of the action taken"
    )
    
    parser.add_argument(
        "--files",
        help="Comma-separated list of files that were changed"
    )
    
    parser.add_argument(
        "--notes",
        help="Additional notes or observations"
    )
    
    parser.add_argument(
        "--project-root",
        default=".",
        help="Path to project root directory"
    )
    
    args = parser.parse_args()
    
    # 🏧 Initialize tracker
    tracker = AISessionTracker(args.project_root)
    
    # 📁 Parse files list
    files_changed = None
    if args.files:
        files_changed = [f.strip() for f in args.files.split(",")]
    
    # 📝 Log the action
    tracker.log_action(
        action=args.action,
        files_changed=files_changed,
        notes=args.notes
    )


if __name__ == "__main__":
    main()

