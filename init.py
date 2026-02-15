#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI无限进化系统 - 快速初始化脚本
支持所有主流AI助手的快速部署
"""

import os
import shutil
import sys
from pathlib import Path

# AI助手配置映射
AI_ASSISTANTS = {
    'claude': {
        'name': 'Claude Code',
        'rules_file': '.clauderules',
        'description': 'Claude Code AI助手'
    },
    'cursor': {
        'name': 'Cursor',
        'rules_file': '.cursorrules',
        'description': 'Cursor IDE'
    },
    'windsurf': {
        'name': 'Windsurf',
        'rules_file': '.windsurfrules',
        'description': 'Windsurf IDE'
    },
    'antigravity': {
        'name': 'Antigravity',
        'rules_file': '.antigravityrules',
        'description': 'Antigravity AI助手'
    },
    'copilot': {
        'name': 'GitHub Copilot',
        'rules_file': '.copilotrules',
        'description': 'GitHub Copilot'
    },
    'kiro': {
        'name': 'Kiro',
        'rules_file': '.kirorules',
        'description': 'Kiro AI助手'
    },
    'codex': {
        'name': 'Codex CLI',
        'rules_file': '.codexrules',
        'description': 'Codex CLI'
    },
    'qoder': {
        'name': 'Qoder',
        'rules_file': '.qoderrules',
        'description': 'Qoder AI助手'
    },
    'roocode': {
        'name': 'Roo Code',
        'rules_file': '.roocoderules',
        'description': 'Roo Code AI助手'
    },
    'gemini': {
        'name': 'Gemini CLI',
        'rules_file': '.geminirules',
        'description': 'Gemini CLI'
    },
    'trae': {
        'name': 'Trae',
        'rules_file': '.traerules',
        'description': 'Trae AI助手'
    },
    'opencode': {
        'name': 'OpenCode',
        'rules_file': '.opencoderules',
        'description': 'OpenCode AI助手'
    },
    'continue': {
        'name': 'Continue',
        'rules_file': '.continuerules',
        'description': 'Continue AI助手'
    },
    'codebuddy': {
        'name': 'CodeBuddy',
        'rules_file': '.codebuddyrules',
        'description': 'CodeBuddy AI助手'
    },
    'droid': {
        'name': 'Droid (Factory)',
        'rules_file': '.droidrules',
        'description': 'Droid Factory AI助手'
    }
}


def get_template_path(rules_file):
    """获取模板文件路径"""
    script_dir = Path(__file__).parent
    template_path = script_dir / 'templates' / rules_file
    return template_path


def create_rules_file(ai_name, rules_file, project_path):
    """创建规则文件"""
    template_path = get_template_path(rules_file)
    target_path = project_path / rules_file
    
    if template_path.exists():
        shutil.copy(template_path, target_path)
        print(f"✅ 已创建 {rules_file}")
        return True
    else:
        # 如果模板不存在，使用通用模板
        generic_template = get_template_path('.cursorrules')
        if generic_template.exists():
            content = generic_template.read_text(encoding='utf-8')
            # 替换适配信息
            content = content.replace('Cursor规则', f'{ai_name}规则')
            content = content.replace('适配**: Cursor', f'适配**: {ai_name}')
            target_path.write_text(content, encoding='utf-8')
            print(f"✅ 已创建 {rules_file} (使用通用模板)")
            return True
        else:
            print(f"❌ 无法找到模板文件: {rules_file}")
            return False


def init_ai_assistant(ai_name, project_path=None):
    """初始化指定AI助手"""
    if ai_name not in AI_ASSISTANTS:
        print(f"❌ 不支持的AI助手: {ai_name}")
        print(f"支持的AI助手: {", ".join(AI_ASSISTANTS.keys())}")
        return False
    
    if project_path is None:
        project_path = Path.cwd()
    else:
        project_path = Path(project_path).resolve()
    
    if not project_path.exists():
        print(f"❌ 项目路径不存在: {project_path}")
        return False
    
    config = AI_ASSISTANTS[ai_name]
    print(f"\n🚀 正在为 {config['name']} 初始化AI无限进化系统...")
    print(f"📁 项目路径: {project_path}")
    
    # 创建规则文件
    success = create_rules_file(config['name'], config['rules_file'], project_path)
    
    if success:
        print(f"\n✅ {config['name']} 初始化完成！")
        print(f"📝 规则文件: {config['rules_file']}")
        print(f"\n💡 提示: 在 {config['name']} 中打开项目，系统会自动加载规则文件。")
        return True
    else:
        print(f"\n❌ {config['name']} 初始化失败！")
        return False


def init_all_assistants(project_path=None):
    """初始化所有AI助手"""
    if project_path is None:
        project_path = Path.cwd()
    else:
        project_path = Path(project_path).resolve()
    
    if not project_path.exists():
        print(f"❌ 项目路径不存在: {project_path}")
        return False
    
    print(f"\n🚀 正在为所有AI助手初始化AI无限进化系统...")
    print(f"📁 项目路径: {project_path}\n")
    
    success_count = 0
    for ai_name, config in AI_ASSISTANTS.items():
        if create_rules_file(config['name'], config['rules_file'], project_path):
            success_count += 1
    
    print(f"\n✅ 初始化完成！成功创建 {success_count}/{len(AI_ASSISTANTS)} 个规则文件")
    print(f"💡 提示: 根据你使用的AI助手，选择对应的规则文件即可。")
    return success_count == len(AI_ASSISTANTS)


def list_assistants():
    """列出所有支持的AI助手"""
    print("\n📋 支持的AI助手列表:\n")
    for ai_name, config in AI_ASSISTANTS.items():
        print(f"  {ai_name:15} - {config['name']:20} ({config['rules_file']})")
    print()


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='AI无限进化系统 - 快速初始化脚本',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=""
示例:
  python init.py --ai cursor              # 初始化Cursor
  python init.py --ai claude               # 初始化Claude Code
  python init.py --ai all                  # 初始化所有AI助手
  python init.py --list                    # 列出所有支持的AI助手
        """
    )
    
    parser.add_argument(
        '--ai', '-a',
        type=str,
        help='要初始化的AI助手名称 (使用 --list 查看所有选项)'
    )
    
    parser.add_argument(
        '--path', '-p',
        type=str,
        help='项目路径 (默认为当前目录)'
    )
    
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='列出所有支持的AI助手'
    )
    
    args = parser.parse_args()
    
    if args.list:
        list_assistants()
        return
    
    if not args.ai:
        print("❌ 请指定要初始化的AI助手 (使用 --ai <name> 或 --list 查看选项)")
        print("\n快速开始:")
        print("  python init.py --ai cursor    # 初始化Cursor")
        print("  python init.py --ai all       # 初始化所有AI助手")
        print("  python init.py --list         # 查看所有选项")
        return
    
    ai_name = args.ai.lower()
    project_path = args.path
    
    if ai_name == 'all':
        init_all_assistants(project_path)
    else:
        init_ai_assistant(ai_name, project_path)


if __name__ == '__main__':
    main()