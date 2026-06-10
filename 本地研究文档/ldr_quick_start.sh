#!/bin/bash
# Local Deep Research 快速启动脚本
# 使用 tmux 在后台运行，断开 SSH 后服务不中断
#
# 用法:
#   bash quick_start.sh                  # 默认端口 5000 启动
#   bash quick_start.sh -p 8080          # 指定端口启动
#   bash quick_start.sh --stop           # 停止
#   bash quick_start.sh --stop -p 8080   # 停止指定端口
#   bash quick_start.sh --restart -p 8080

SESSION_NAME="ldr"
DEFAULT_PORT=5000
PORT="$DEFAULT_PORT"

# ── 参数解析 ─────────────────────────────────────────────────────────────
ACTION="start"
while [[ $# -gt 0 ]]; do
    case "$1" in
        --stop)    ACTION="stop"; shift ;;
        --restart) ACTION="restart"; shift ;;
        -p)
            PORT="$2"; shift 2
            if ! [[ "$PORT" =~ ^[0-9]+$ ]] || [ "$PORT" -lt 1 ] || [ "$PORT" -gt 65535 ]; then
                echo "错误: 端口范围 1-65535, 当前: $PORT"
                exit 1
            fi
            ;;
        -h|--help)
            echo "用法: bash quick_start.sh [选项]"
            echo ""
            echo "  -p PORT       指定端口 (默认: $DEFAULT_PORT)"
            echo "  --stop        停止服务"
            echo "  --restart     重启服务"
            echo "  -h, --help    显示帮助"
            exit 0
            ;;
        *)
            echo "未知参数: $1, 使用 -h 查看帮助"
            exit 1
            ;;
    esac
done

# ── 停止服务 ─────────────────────────────────────────────────────────────
stop_service() {
    echo "正在停止 LDR (端口 $PORT)..."
    tmux kill-session -t "$SESSION_NAME" 2>/dev/null || true
    pid=$(lsof -ti :"$PORT" 2>/dev/null) || true
    [ -n "$pid" ] && kill -9 $pid 2>/dev/null || true
    echo "LDR 已停止。"
}

if [ "$ACTION" = "stop" ]; then
    stop_service
    exit 0
fi

if [ "$ACTION" = "restart" ]; then
    stop_service
    sleep 1
fi

# ── 已在运行 ─────────────────────────────────────────────────────────────
if tmux has-session -t "$SESSION_NAME" 2>/dev/null; then
    echo "LDR 已在运行中 (tmux session: $SESSION_NAME)"
    echo "进入会话: tmux attach -t $SESSION_NAME"
    exit 0
fi

# ── 启动服务 ─────────────────────────────────────────────────────────────
tmux new-session -d -s "$SESSION_NAME" \
    "source /data/miniforge/etc/profile.d/conda.sh && conda activate ldr && LDR_WEB_PORT=$PORT ldr-web; exec bash"

echo "=========================================="
echo "  LDR 已启动!"
echo "=========================================="
echo ""
echo "  访问地址: http://10.10.20.21:$PORT"
echo ""
echo "  进入会话:     tmux attach -t $SESSION_NAME"
echo "  退出会话:     Ctrl+B 然后按 D"
echo "  停止服务:     bash quick_start.sh --stop"
echo "  重启服务:     bash quick_start.sh --restart"
echo "=========================================="
