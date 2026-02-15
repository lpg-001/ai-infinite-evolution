#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI无限进化系统 - 技能更新脚本
在每次对话结束时自动更新san/SKILL.md和order/SKILL.md
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# 文件路径
BASE_DIR = Path(__file__).parent.parent.parent
SAN_SKILL_FILE = BASE_DIR / "san" / "SKILL.md"
ORDER_SKILL_FILE = BASE_DIR / "order" / "SKILL.md"
FATHER_SKILL_FILE = BASE_DIR / "father" / "SKILL.md"
UPDATE_LOG_FILE = BASE_DIR / "@.cursor" / "skills" / "update_log.json"


class SkillUpdater:
    """技能更新器"""
    
    def __init__(self):
        self.base_dir = BASE_DIR
        self.san_file = SAN_SKILL_FILE
        self.order_file = ORDER_SKILL_FILE
        self.father_file = FATHER_SKILL_FILE
        self.log_file = UPDATE_LOG_FILE
        
    def analyze_conversation(self, user_input: str, ai_response: str) -> Dict:
        """分析对话内容，提取需要更新的规则"""
        analysis = {
            "san_updates": [],
            "order_updates": [],
            "hooks_detected": []
        }
        
        # 检测钩子
        hook_pattern = r'^/(\w+)(?:\s+(.+))?$'
        hook_match = re.match(hook_pattern, user_input.strip())
        if hook_match:
            hook_name = hook_match.group(1)
            hook_params = hook_match.group(2) if hook_match.group(2) else ""
            analysis["hooks_detected"].append({
                "name": hook_name,
                "params": hook_params
            })
            analysis["order_updates"].append({
                "type": "hook_usage",
                "hook": hook_name,
                "params": hook_params
            })
        
        # 分析用户输入语言模式
        user_language_patterns = self._extract_language_patterns(user_input)
        if user_language_patterns:
            analysis["san_updates"].extend(user_language_patterns)
        
        # 分析AI思考规则
        ai_thinking_rules = self._extract_thinking_rules(ai_response)
        if ai_thinking_rules:
            analysis["san_updates"].extend(ai_thinking_rules)
        
        # 分析是否需要order技能更新
        if self._needs_order_update(user_input, ai_response):
            analysis["order_updates"].append({
                "type": "skill_update",
                "reason": "对话涉及特定功能或工具"
            })
        
        return analysis
    
    def _extract_language_patterns(self, text: str) -> List[Dict]:
        """提取用户输入语言模式"""
        patterns = []
        
        # 检测语言类型
        if re.search(r'[\u4e00-\u9fff]', text):
            patterns.append({
                "type": "language_rule",
                "content": "用户使用中文输入",
                "pattern": "中文输入模式"
            })
        
        return patterns
    
    def _extract_thinking_rules(self, text: str) -> List[Dict]:
        """提取AI思考规则"""
        rules = []
        
        # 检测分析方法
        if '分析' in text or 'analyze' in text.lower():
            rules.append({
                "type": "thinking_rule",
                "content": "采用分析方法处理问题",
                "pattern": "分析思维"
            })
        
        return rules
    
    def _needs_order_update(self, user_input: str, ai_response: str) -> bool:
        """判断是否需要更新order技能"""
        order_keywords = [
            '工具', '功能', '脚本', '自动化', '钩子', 'hook',
            'tool', 'function', 'script', 'automation'
        ]
        
        combined_text = (user_input + " " + ai_response).lower()
        return any(keyword in combined_text for keyword in order_keywords)
    
    def read_san_skill(self) -> str:
        """读取san/SKILL.md内容"""
        if self.san_file.exists():
            return self.san_file.read_text(encoding='utf-8')
        return ""
    
    def read_order_skill(self) -> str:
        """读取order/SKILL.md内容"""
        if self.order_file.exists():
            return self.order_file.read_text(encoding='utf-8')
        return ""
    
    def update_san_skill(self, analysis: Dict, conversation_context: Optional[str] = None) -> str:
        """更新san/SKILL.md（必须更新）"""
        current_content = self.read_san_skill()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 提取更新内容
        updates = []
        for update in analysis.get("san_updates", []):
            if update["type"] == "language_rule":
                updates.append(f"- 新增 用户输入语言规则：{update['content']}")
            elif update["type"] == "thinking_rule":
                updates.append(f"- 新增 AI思考规则：{update['content']}")
        
        # 如果没有新内容，也要进行优化性更新
        if not updates:
            updates.append("- 优化 持续学习和改进语言理解能力")
            updates.append("- 优化 持续优化思考规则")
        
        # 构建更新说明
        update_section = f"""**最后更新时间**: {now}（系统自动更新）
**更新内容**: 
{chr(10).join(updates)}"""
        
        # 更新文件内容
        if "**最后更新时间**" in current_content:
            pattern = r'\*\*最后更新时间\*\*:.*?\*\*更新内容\*\*:.*?(?=\n---|\n\*\*|$)'
            new_content = re.sub(pattern, update_section, current_content, flags=re.DOTALL)
        else:
            if current_content.strip().endswith("---"):
                new_content = current_content.rstrip("---").rstrip() + "\n\n" + update_section + "\n\n---"
            else:
                new_content = current_content + "\n\n" + update_section
        
        # 保存文件
        self.san_file.parent.mkdir(parents=True, exist_ok=True)
        self.san_file.write_text(new_content, encoding='utf-8')
        
        return update_section
    
    def update_order_skill(self, analysis: Dict) -> Optional[str]:
        """更新order/SKILL.md（可选更新）"""
        if not analysis.get("order_updates"):
            return None
        
        current_content = self.read_order_skill()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 提取更新内容
        updates = []
        hooks_to_add = []
        
        for update in analysis.get("order_updates", []):
            if update["type"] == "hook_usage":
                hook_name = update["hook"]
                updates.append(f"- 使用 钩子：/{hook_name}")
                if f"/{hook_name}" not in current_content:
                    hooks_to_add.append({
                        "hook": f"/{hook_name}",
                        "description": f"执行{hook_name}相关功能"
                    })
            elif update["type"] == "skill_update":
                updates.append(f"- {update.get('reason', '更新技能')}")
        
        if not updates:
            return None
        
        # 构建更新说明
        update_section = f"""**最后更新时间**: {now}（系统自动更新）
**更新内容**: 
{chr(10).join(updates)}"""
        
        # 更新文件内容
        if "**最后更新时间**" in current_content:
            pattern = r'\*\*最后更新时间\*\*:.*?\*\*更新内容\*\*:.*?(?=\n---|\n\*\*|$)'
            new_content = re.sub(pattern, update_section, current_content, flags=re.DOTALL)
        else:
            if current_content.strip().endswith("---"):
                new_content = current_content.rstrip("---").rstrip() + "\n\n" + update_section + "\n\n---"
            else:
                new_content = current_content + "\n\n" + update_section
        
        # 保存文件
        self.order_file.parent.mkdir(parents=True, exist_ok=True)
        self.order_file.write_text(new_content, encoding='utf-8')
        
        return update_section
    
    def log_update(self, analysis: Dict, san_update: str, order_update: Optional[str]):
        """记录更新日志"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "san_updated": True,
            "order_updated": order_update is not None,
            "san_update_content": san_update,
            "order_update_content": order_update,
            "hooks_detected": analysis.get("hooks_detected", [])
        }
        
        logs = []
        if self.log_file.exists():
            try:
                logs = json.loads(self.log_file.read_text(encoding='utf-8'))
            except:
                logs = []
        
        logs.append(log_entry)
        logs = logs[-100:]
        
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        self.log_file.write_text(json.dumps(logs, ensure_ascii=False, indent=2), encoding='utf-8')
    
    def process_conversation_end(self, user_input: str, ai_response: str) -> Dict:
        """处理对话结束，执行更新"""
        analysis = self.analyze_conversation(user_input, ai_response)
        san_update = self.update_san_skill(analysis)
        order_update = self.update_order_skill(analysis)
        self.log_update(analysis, san_update, order_update)
        
        return {
            "san_updated": True,
            "order_updated": order_update is not None,
            "san_update_content": san_update,
            "order_update_content": order_update,
            "hooks_detected": analysis.get("hooks_detected", [])
        }


if __name__ == "__main__":
    updater = SkillUpdater()
    user_input = "用中文回答，并帮我计算1+1"
    ai_response = "好的，我会用中文回答。1+1=2"
    result = updater.process_conversation_end(user_input, ai_response)
    print("更新结果:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
