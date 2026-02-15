#!/bin/bash
# AI无限进化系统 - 快速初始化脚本 (Shell版本)
# 支持所有主流AI助手的快速部署

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# AI助手配置
declare -A AI_ASSISTANTS=(
    ["claude"]="Claude Code:.clauderules"
    ["cursor"]="Cursor:.cursorrules"
    ["windsurf"]="Windsurf:.windsurfrules"
    ["antigravity"]="Antigravity:.antigravityrules"
    ["copilot"]="GitHub Copilot:.copilotrules"
    ["kiro"]="Kiro:.kirorules"
    ["codex"]="Codex CLI:.codexrules"
    ["qoder"]="Qoder:.qoderrules"
    ["roocode"]="Roo Code:.roocoderules"
    ["gemini"]="Gemini CLI:.geminirules"
    ["trae"]="Trae:.traerules"
    ["opencode"]="OpenCode:.opencoderules"
    ["continue"]="Continue:.continuerules"
    ["codebuddy"]="CodeBuddy:.codebuddyrules"
    ["droid"]="Droid (Factory):.droidrules"
)

# 获取脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATES_DIR="$SCRIPT_DIR/templates"

# 显示帮助信息
show_help() {
    echo "AI无限进化系统 - 快速初始化脚本"
    echo ""
    echo "用法:"
    echo "  ./init.sh --ai <assistant_name>    # 初始化指定AI助手"
    echo "  ./init.sh --ai all                  # 初始化所有AI助手"
    echo "  ./init.sh --list                    # 列出所有支持的AI助手"
    echo ""
    echo "示例:"
    echo "  ./init.sh --ai cursor               # 初始化Cursor"
    echo "  ./init.sh --ai claude               # 初始化Claude Code"
    echo "  ./init.sh --ai all                  # 初始化所有AI助手"
    echo ""
}

# 列出所有支持的AI助手
list_assistants() {
    echo -e "${BLUE}📋 支持的AI助手列表:${NC}\n"
    for key in "${!AI_ASSISTANTS[@]}"; do
        IFS=':' read -r name rules_file <<< "${AI_ASSISTANTS[$key]}"
        printf "  %-15s - %-20s (%s)\n" "$key" "$name" "$rules_file"
    done
    echo ""
}

# 创建规则文件
create_rules_file() {
    local ai_name=$1
    local rules_file=$2
    local project_path=$3
    
    local template_path="$TEMPLATES_DIR/$rules_file"
    local target_path="$project_path/$rules_file"
    
    if [ -f "$template_path" ]; then
        cp "$template_path" "$target_path"
        echo -e "${GREEN}✅ 已创建 $rules_file${NC}"
        return 0
    else
        echo -e "${RED}❌ 无法找到模板文件: $rules_file${NC}"
        return 1
    fi
}

# 初始化指定AI助手
init_ai_assistant() {
    local ai_name=$1
    local project_path=${2:-$(pwd)}
    
    if [ ! -d "$project_path" ]; then
        echo -e "${RED}❌ 项目路径不存在: $project_path${NC}"
        return 1
    fi
    
    if [ -z "${AI_ASSISTANTS[$ai_name]}" ]; then
        echo -e "${RED}❌ 不支持的AI助手: $ai_name${NC}"
        echo -e "${YELLOW}支持的AI助手: ${!AI_ASSISTANTS[*]}${NC}"
        return 1
    fi
    
    IFS=':' read -r display_name rules_file <<< "${AI_ASSISTANTS[$ai_name]}"
    
    echo -e "\n${BLUE}🚀 正在为 $display_name 初始化AI无限进化系统...${NC}"
    echo -e "${BLUE}📁 项目路径: $project_path${NC}\n"
    
    if create_rules_file "$display_name" "$rules_file" "$project_path"; then
        echo -e "\n${GREEN}✅ $display_name 初始化完成！${NC}"
        echo -e "${GREEN}📝 规则文件: $rules_file${NC}"
        echo -e "\n${YELLOW}💡 提示: 在 $display_name 中打开项目，系统会自动加载规则文件。${NC}"
        return 0
    else
        echo -e "\n${RED}❌ $display_name 初始化失败！${NC}"
        return 1
    fi
}

# 初始化所有AI助手
init_all_assistants() {
    local project_path=${1:-$(pwd)}
    
    if [ ! -d "$project_path" ]; then
        echo -e "${RED}❌ 项目路径不存在: $project_path${NC}"
        return 1
    fi
    
    echo -e "\n${BLUE}🚀 正在为所有AI助手初始化AI无限进化系统...${NC}"
    echo -e "${BLUE}📁 项目路径: $project_path${NC}\n"
    
    local success_count=0
    local total_count=${#AI_ASSISTANTS[@]}
    
    for key in "${!AI_ASSISTANTS[@]}"; do
        IFS=':' read -r display_name rules_file <<< "${AI_ASSISTANTS[$key]}"
        if create_rules_file "$display_name" "$rules_file" "$project_path"; then
            ((success_count++))
        fi
    done
    
    echo -e "\n${GREEN}✅ 初始化完成！成功创建 $success_count/$total_count 个规则文件${NC}"
    echo -e "${YELLOW}💡 提示: 根据你使用的AI助手，选择对应的规则文件即可。${NC}"
    
    return $([ $success_count -eq $total_count ] && echo 0 || echo 1)
}

# 主函数
main() {
    local ai_name=""
    local project_path=""
    
    # 解析参数
    while [[ $# -gt 0 ]]; do
        case $1 in
            --ai|-a)
                ai_name="$2"
                shift 2
                ;;
            --path|-p)
                project_path="$2"
                shift 2
                ;;
            --list|-l)
                list_assistants
                exit 0
                ;;
            --help|-h)
                show_help
                exit 0
                ;;
            *)
                echo -e "${RED}❌ 未知参数: $1${NC}"
                show_help
                exit 1
                ;;
        esac
    done
    
    if [ -z "$ai_name" ]; then
        echo -e "${RED}❌ 请指定要初始化的AI助手 (使用 --ai <name> 或 --list 查看选项)${NC}"
        echo ""
        echo "快速开始:"
        echo "  ./init.sh --ai cursor    # 初始化Cursor"
        echo "  ./init.sh --ai all       # 初始化所有AI助手"
        echo "  ./init.sh --list         # 查看所有选项"
        exit 1
    fi
    
    ai_name=$(echo "$ai_name" | tr '[:upper:]' '[:lower:]')
    
    if [ "$ai_name" = "all" ]; then
        init_all_assistants "$project_path"
    else
        init_ai_assistant "$ai_name" "$project_path"
    fi
}

# 运行主函数
main "$@"