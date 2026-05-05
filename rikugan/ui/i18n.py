"""Simplified i18n module for Rikugan UI strings.

This module provides a simple translation lookup mechanism for UI strings.
It is designed to be lightweight and avoid Qt signal cross-thread issues.

Supported languages:
    en  – English (default)
    zh  – Simplified Chinese (中文)

Usage:
    from rikugan.ui.i18n import t
    
    # Translate a string key
    label = t("settings.provider")  # Returns "LLM Provider" or "LLM 提供商"
"""

from __future__ import annotations

_TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        # Settings dialog
        "settings.title": "Rikugan Settings",
        "settings.provider_tab": "Provider",
        "settings.skills_tab": "Skills",
        "settings.mcp_tab": "MCP",
        "settings.profiles_tab": "Profiles",
        "settings.provider_group": "LLM Provider",
        "settings.provider_label": "Provider:",
        "settings.api_key_label": "API Key:",
        "settings.api_key_placeholder": "sk-... or leave empty for auto-detect",
        "settings.api_base_label": "API Base:",
        "settings.model_label": "Model:",
        "settings.generation_group": "Generation",
        "settings.temperature_label": "Temperature:",
        "settings.max_tokens_label": "Max Output Tokens:",
        "settings.context_window_label": "Context Window:",
        "settings.behavior_group": "Behavior",
        "settings.auto_context": "Auto-inject binary context into system prompt",
        "settings.auto_save": "Auto-save sessions",
        "settings.exploration_turns": "Exploration turn limit:",
        "settings.normal_turns": "Normal turn limit:",
        "settings.api_retries": "API retry attempts:",
        "settings.silent_retry": "Show loading indicator instead of error messages during retries",
        "settings.preserve_context": "Preserve full context (disable tool result truncation)",
        "settings.encrypt_keys": "Encrypt API keys with password",
        "settings.language_label": "Language:",
        # Dependency warnings
        "settings.warnings_prefix": "Warnings: ",
        # Tool buttons
        "settings.add_provider": "Add custom OpenAI-compatible connection",
        "settings.remove_provider": "Remove custom connection",
        "settings.fetch_models": "Refresh",
        # Add provider dialog
        "settings.add_provider_dialog.title": "Add Custom Connection",
        "settings.connection_name_label": "Connection Name:",
        "settings.api_base_url_label": "API Base URL:",
        "settings.name_required": "Name is required",
        "settings.name_exists": "'{name}' already exists",
        "settings.base_url_required": "API Base URL is required",
        # Auth status messages
        "settings.auth_claude_setup": "run claude setup-token to acquire your oauth",
        "settings.type_model_manually": "Type model name manually",
        "settings.models_found": "{count} models",
        # Chat UI input area
        "chat.mode_chat": "Chat",
        "chat.input_placeholder.ask": "Ask about this binary... (/ for skills, /modify to patch)",
        "chat.input_placeholder.thinking": "Rikugan is thinking...",
        # Chat UI approve/reject (generic)
        "chat.approve": "Approve",
        "chat.reject": "Reject",
        "chat.allow": "Allow",
        "chat.deny": "Deny",
        # Plan view
        "plan.header": "Plan",
        "plan.approve_execute": "Approve & Execute",
        "plan.reject": "Reject",
        # Agent messages
        "agent.running": "Agent is running...",
        "agent.cancelled": "Agent cancelled",
        "agent.error": "Error: {error}",
        "agent.unknown_error": "Unknown error",
        "agent.queued": "[queued]",
        # Message widgets — role labels
        "message.you": "You",
        "message.rikugan": "Rikugan",
        "message.thinking": "Thinking",
        "message.thinking_progress": "Thinking\u2026",
        "message.error_header": "Error",
        "message.question_header": "Rikugan asks:",
        # Mutation log
        "mutation.title": "Mutation Log",
        "mutation.undo_last": "Undo Last",
        "mutation.count": "{n} mutation{'s' if n != 1 else ''}",
        # Tools panel
        "tools.title": "Tools",
        "tools.renamer_tab": "Renamer",
        "tools.agents_tab": "Agents",
        "tools.not_loaded": "Not loaded",
        # Context menu actions (IDA/Binary Ninja)
        "action.send_to": "Analyze the function {name} at 0x{ea:x}",
        "action.send_to_addr": "Analyze the code at 0x{ea:x}",
        "action.explain": "Explain the function {_name} at 0x{_ea}. Decompile it and provide a detailed analysis.",
        "action.rename": "Analyze the function {_name} at 0x{_ea}. Based on its behavior, suggest better names for the function and its local variables. Apply the renames.",
        "action.deobfuscate": "Deobfuscate the function {_name} at 0x{_ea}. Identify obfuscation patterns (opaque predicates, junk code, control-flow flattening, encrypted strings) and explain them. If possible, apply {_term} optimizations to clean the output.",
        "action.vuln_audit": "Audit the function {_name} at 0x{_ea} for security vulnerabilities. Check for buffer overflows, format strings, integer overflows, use-after-free, command injection, and other memory-safety issues. List each finding with severity and evidence.",
        "action.suggest_types": "Analyze the function {_name} at 0x{_ea} and infer types. Examine pointer dereference patterns to suggest structs, identify enum-like constants, and propose proper parameter types. Apply the type changes.",
        "action.annotate": "Annotate the function {_name} at 0x{_ea} with comments. Add a function-level comment summarizing its purpose, and add inline comments to key basic blocks explaining the logic.",
        "action.clean": "Clean the {_term} for {_name} at 0x{_ea}. Read the {_term}, identify junk or obfuscated instructions, NOP or patch them if needed, then redecompile to verify.",
        "action.xref_analysis": "Perform a deep cross-reference analysis on {_name} at 0x{_ea}. Trace all callers and callees, identify data references, and map out the call graph around this function.",
        # Context menu action labels & tooltips (IDA/Binary Ninja)
        "action.send_to_label": "Send to Rikugan",
        "action.send_to_tooltip": "Send selection or address to Rikugan input",
        "action.explain_label": "Explain this",
        "action.explain_tooltip": "Explain the current function with Rikugan",
        "action.rename_label": "Rename with Rikugan",
        "action.rename_tooltip": "Analyze and rename the current function",
        "action.deobfuscate_label": "Deobfuscate with Rikugan",
        "action.deobfuscate_tooltip": "Deobfuscate the current function",
        "action.vuln_audit_label": "Find vulnerabilities",
        "action.vuln_audit_tooltip": "Audit the current function for security bugs",
        "action.suggest_types_label": "Suggest types",
        "action.suggest_types_tooltip": "Infer and apply types for the current function",
        "action.annotate_label": "Annotate function",
        "action.annotate_tooltip": "Add comments to the current function",
        "action.clean_mcode_label": "Clean microcode",
        "action.clean_mcode_tooltip": "Clean the microcode for the current function",
        "action.xref_label": "Xref analysis",
        "action.xref_tooltip": "Deep cross-reference analysis on the current function",
        # Binary Ninja-specific action labels & tooltips
        "action.clean_il_label": "Clean IL",
        "action.clean_il_tooltip": "Clean IR IL for the current function",
        "action.smart_patch_label": "Smart Patch",
        "action.smart_patch_tooltip": "Modify function behavior with natural language and apply binary patches",
        # General actions (menu)
        "action.open_tools_label": "Open Tools",
        "action.open_tools_tooltip": "Open the Rikugan Tools panel",
        "action.send_to_bulk_rename_label": "Send to Bulk Rename",
        "action.send_to_bulk_rename_tooltip": "Send function to Rikugan Bulk Renamer",
        # execute_python approval
        "execute_python.approve_header": "Approve execute_python?",
        "execute_python.code_info": "Python code - {lines} line{'s' if lines != 1 else ''}",
        "execute_python.always_allow": "Always Allow",
        "execute_python.allowed": "Allowed",
        "execute_python.always_allowed": "Always Allowed",
        "execute_python.denied": "Denied",
        # Profile settings
        "profile.denied_tools": "Denied Tools",
        "profile.error_title": "Error",
        "profile.name_exists": "Profile '{name}' already exists.",
        "profile.name_required": "Name is required",
        "profile.description_required": "Description is required — it helps the AI agent follow your constraints",
        # Thinking phrases (animated indicator)
        "thinking.analyzing_structure": "analyzing binary structure...",
        "thinking.examining_flow": "examining control flow...",
        "thinking.tracing_xrefs": "tracing cross-references...",
        "thinking.inspecting_disassembly": "inspecting disassembly...",
        "reading_signatures": "reading function signatures...",
        "correlating_refs": "correlating data references...",
        "mapping_call_graph": "mapping call graph...",
        "evaluating_types": "evaluating type patterns...",
        "scanning_strings": "scanning string references...",
        "deobfuscating_logic": "deobfuscating logic...",
        "checking_imports": "checking import table...",
        "inferring_vars": "inferring variable types...",
        "analyzing_stack": "analyzing stack layout...",
        "tracing_data_flow": "tracing data flow...",
        "examining_vtables": "examining vtable references...",
        "decoding_values": "decoding encoded values...",
        # Bulk renamer widget
        "renamer.filter_placeholder": "Filter by name or address...",
        "renamer.filter_all": "All Functions",
        "renamer.filter_auto_named": "Auto-named Only",
        "renamer.filter_user_renamed": "User-renamed",
        "renamer.filter_imports": "Imports",
        "renamer.selection_count": "{n} / {total} selected",
        "renamer.header_checkbox": "",
        "renamer.header_address": "Address",
        "renamer.header_current_name": "Current Name",
        "renamer.header_length": "Length",
        "renamer.header_new_name": "New Name",
        "renamer.header_status": "Status",
        "renamer.mode_label": "Mode:",
        "renamer.mode_quick": "Quick",
        "renamer.mode_deep": "Deep",
        "renamer.batch_label": "Batch:",
        "renamer.batch_tooltip": "Quick: functions per LLM prompt. Deep: ignored (1 agent per function).",
        "renamer.jobs_label": "Jobs:",
        "renamer.jobs_tooltip": "Max parallel agents/requests running at the same time",
        "renamer.btn_start": "Start",
        "renamer.btn_stop": "Stop",
        "renamer.btn_pause": "Pause",
        "renamer.btn_resume": "Resume",
        "renamer.btn_undo_all": "Undo All",
        "renamer.progress_label": "{n} / {total}",
        "renamer.subagents_count": "\u2022 {n} subagent{'s' if n != 1 else ''}",
        "renamer.batch_count": "\u2022 {n} batch(es)",
        # Agent tree widget
        "agent_tree.btn_kill_selected": "Kill Selected",
        "agent_tree.btn_clean": "Clean",
        "agent_tree.clean_tooltip": "Remove selected finished agents (or all finished if none selected)",
        "agent_tree.filter_all": "All Agents",
        "agent_tree.filter_general": "General",
        "agent_tree.filter_bulk_rename": "Bulk Rename",
        "agent_tree.status_label": "{n} running / {m} completed",
        "agent_tree.tree_header_name": "Name",
        "agent_tree.tree_header_type": "Type",
        "agent_tree.tree_header_status": "Status",
        "agent_tree.tree_header_turns": "Turns",
        "agent_tree.tree_header_time": "Time",
        "agent_tree.preview_placeholder": "Select an agent to preview its output...",
        "agent_tree.no_output_yet": "(no output yet)",
        # Context bar labels
        "context.addr_label": "Addr:",
        "context.func_label": "Func:",
        "context.model_label": "Model:",
        "context.tokens_label": "Tokens:",
        # Message widgets
        "message.high_relevance": "High relevance",
        # Mutation log tooltips
        "mutation.reversible_tooltip": "Reversible",
        "mutation.not_reversible_tooltip": "Not reversible",
        # Tool widgets
        "tool.result_header": "Result:",
        "tool.tools_called_label": "{n} tool{'s' if n != 1 else ''} called",
        # Chat view save approval options
        "chat.save_all": "Save All",
        "chat.discard_all": "Discard All",
        # Session controller tab labels
        "session.new_chat": "New Chat",
        # Panel core action buttons & dialogs
        "panel.btn_send": "Send",
        "panel.btn_stop": "Stop",
        "panel.btn_new": "New",
        "panel.btn_export": "Export",
        "panel.btn_settings": "Settings",
        "panel.btn_mutations": "Mutations",
        "panel.export_title": "Rikugan — Encrypted API Keys",
        "panel.decrypt_prompt": "Enter password to decrypt API keys:",
        "panel.decrypt_placeholder": "Password",
        "panel.wrong_password_title": "Wrong Password",
        "panel.wrong_password_message": "Incorrect password. Please try again.",
        "panel.export_options_title": "Export Options",
        "panel.export_include_subagents": "Include subagent logs ({n} subagent runs)",
        "panel.export_chat_title": "Export Chat",
        "panel.new_chat_dialog_title": "New Chat",
        "panel.new_chat_dialog_message": "Start a new chat? Current conversation will be saved.",
        "panel.context_usage": "Context usage: {pct}%",
        "panel.yes_button": "Yes",
        "panel.yes_clear_context": "Yes, clear context ({pct}% used)",
        "panel.no_button": "No",
        "panel.subagent_status": "Subagent \u201c{name}\u201d {status}",
        "panel.subagent_completed": "[Subagent \u201c{name}\u201d completed ({turns} turns, {elapsed}s)]",
        "panel.input_placeholder_thinking": "Rikugan is thinking... press Enter (or Queue) to queue a follow-up.",
        # Settings dialog additional strings
        "settings.add_provider_name_placeholder": "e.g. minimax, deepseek, local-vllm",
        "settings.oauth_checkbox": "Use OAuth from Claude Code (macOS Keychain)",
        "settings.oauth_tooltip": "Auto-load your Claude Code OAuth token from the macOS Keychain.\nRequires accepting Anthropic's credential use policy.",
        "settings.custom_endpoint_placeholder": "Custom endpoint URL (optional)",
        "settings.api_base_form_label": "API Base:",
        "settings.model_form_label": "Model:",
        "settings.exploration_turns_tooltip": "Maximum turns the agent spends in the exploration phase before forcing a transition (or reporting an error if findings are insufficient).",
        "settings.normal_turns_tooltip": "Maximum turns the agent spends in normal mode before stopping.",
        "settings.api_retries_tooltip": "Number of retry attempts when the API returns a rate-limit or transient error.",
        "settings.silent_retry_tooltip": "When enabled, rate-limit retries show a subtle text indicator instead of red error messages.",
        "settings.preserve_context_tooltip": "Disables tool result truncation and message trimming. Enable for deep RE sessions where losing decompilation context is worse than higher token cost.",
        "settings.encrypt_keys_tooltip1": "Encrypt all stored API keys with a password.\nYou must enter this password each time Rikugan starts.",
        "settings.encrypt_keys_tooltip2": "Requires the 'cryptography' package (pip install cryptography).",
        "settings.lang_english": "English",
        "settings.lang_chinese": "中文",
        "settings.api_key_placeholder_oauth": "sk-... or leave empty for OAuth auto-detect",
        "settings.api_key_placeholder_local": "Not required for local Ollama",
        "settings.api_key_placeholder_endpoint": "API key for the endpoint",
        "settings.api_key_placeholder_generic": "API key",
        "settings.password_placeholder": "Password",
        "settings.confirm_password_placeholder": "Confirm password",
    },
    "zh": {
        # Settings dialog
        "settings.title": "六眼设置",
        "settings.provider_tab": "提供商",
        "settings.skills_tab": "技能",
        "settings.mcp_tab": "MCP",
        "settings.profiles_tab": "配置",
        "settings.provider_group": "LLM 提供商",
        "settings.provider_label": "提供商：",
        "settings.api_key_label": "API 密钥：",
        "settings.api_key_placeholder": "sk-... 或留空以自动检测",
        "settings.api_base_label": "API 地址：",
        "settings.model_label": "模型：",
        "settings.generation_group": "生成设置",
        "settings.temperature_label": "温度：",
        "settings.max_tokens_label": "最大输出 Token 数：",
        "settings.context_window_label": "上下文窗口：",
        "settings.behavior_group": "行为设置",
        "settings.auto_context": "自动注入二进制上下文到系统提示词",
        "settings.auto_save": "自动保存会话",
        "settings.exploration_turns": "探索轮数限制：",
        "settings.normal_turns": "正常模式轮数限制：",
        "settings.api_retries": "API 重试次数：",
        "settings.silent_retry": "重试时显示加载指示器而非错误消息",
        "settings.preserve_context": "保留完整上下文（禁用工具结果截断）",
        "settings.encrypt_keys": "使用密码加密 API 密钥",
        "settings.language_label": "语言：",
        # Dependency warnings
        "settings.warnings_prefix": "警告： ",
        # Tool buttons
        "settings.add_provider": "添加自定义 OpenAI 兼容连接",
        "settings.remove_provider": "移除自定义连接",
        "settings.fetch_models": "刷新",
        # Add provider dialog
        "settings.add_provider_dialog.title": "添加自定义连接",
        "settings.connection_name_label": "连接名称：",
        "settings.api_base_url_label": "API 基础 URL：",
        "settings.name_required": "名称不能为空",
        "settings.name_exists": "'{name}' 已存在",
        "settings.base_url_required": "API 基础 URL 不能为空",
        # Auth status messages
        "settings.auth_claude_setup": "运行 claude setup-token 获取 OAuth 令牌",
        "settings.type_model_manually": "手动输入模型名称",
        "settings.models_found": "{count} 个模型",
        # Chat UI input area
        "chat.mode_chat": "聊天",
        "chat.input_placeholder.ask": "关于此二进制文件输入消息...（/ 使用技能，/modify 进行修补）",
        "chat.input_placeholder.thinking": "六眼正在思考...",
        # Chat UI approve/reject (generic)
        "chat.approve": "批准",
        "chat.reject": "拒绝",
        "chat.allow": "允许",
        "chat.deny": "拒绝",
        # Plan view
        "plan.header": "计划",
        "plan.approve_execute": "批准并执行",
        "plan.reject": "拒绝",
        # Agent messages
        "agent.running": "代理正在运行...",
        "agent.cancelled": "代理已取消",
        "agent.error": "错误：{error}",
        "agent.unknown_error": "未知错误",
        "agent.queued": "[排队中]",
        # Message widgets — role labels
        "message.you": "你",
        "message.rikugan": "六眼",
        "message.thinking": "思考中",
        "message.thinking_progress": "思考\u2026",
        "message.error_header": "错误",
        "message.question_header": "六眼提问：",
        # Mutation log
        "mutation.title": "变更日志",
        "mutation.undo_last": "撤销上次",
        "mutation.count": "{n} 次变更",
        # Tools panel
        "tools.title": "工具",
        "tools.renamer_tab": "重命名器",
        "tools.agents_tab": "代理",
        "tools.not_loaded": "未加载",
        # Context menu actions (IDA/Binary Ninja)
        "action.send_to": "分析函数 {name}（地址 0x{ea:x}）",
        "action.send_to_addr": "分析地址 0x{ea:x} 处的代码",
        "action.explain": "解释函数 {_name}（地址 0x{_ea}）。反编译它并提供详细分析。",
        "action.rename": "分析函数 {_name}（地址 0x{_ea}）。根据其行为，为函数及其局部变量建议更好的名称。应用这些重命名。",
        "action.deobfuscate": "去混淆函数 {_name}（地址 0x{_ea}）。识别混淆模式（不透明谓词、垃圾代码、控制流扁平化、加密字符串）并解释它们。如果可能，应用 {_term} 优化来清理输出。",
        "action.vuln_audit": "审计函数 {_name}（地址 0x{_ea}）的安全漏洞。检查缓冲区溢出、格式字符串、整数溢出、释放后使用、命令注入和其他内存安全问题。列出每个发现及其严重程度和证据。",
        "action.suggest_types": "分析函数 {_name}（地址 0x{_ea}）并推断类型。检查指针解引用模式以建议结构体，识别类似枚举的常量，并提出适当的参数类型。应用这些类型更改。",
        "action.annotate": "为函数 {_name}（地址 0x{_ea}）添加注释。添加一个总结其用途的函数级注释，并为关键基本块添加内联注释来解释逻辑。",
        "action.clean": "清理 {_name}（地址 0x{_ea}）的 {_term}。读取 {_term}，识别垃圾或混淆指令，必要时 NOP 或修补它们，然后重新反编译以验证。",
        "action.xref_analysis": "对 {_name}（地址 0x{_ea}）执行深度交叉引用分析。追踪所有调用者和被调用者，识别数据引用，并绘制该函数周围的调用图。",
        # Context menu action labels & tooltips (IDA/Binary Ninja)
        "action.send_to_label": "发送到 Rikugan",
        "action.send_to_tooltip": "将选中内容或地址发送到 Rikugan 输入框",
        "action.explain_label": "解释此函数",
        "action.explain_tooltip": "用 Rikugan 解释当前函数",
        "action.rename_label": "用 Rikugan 重命名",
        "action.rename_tooltip": "分析并重命名当前函数",
        "action.deobfuscate_label": "用 Rikugan 去混淆",
        "action.deobfuscate_tooltip": "去混淆当前函数",
        "action.vuln_audit_label": "查找漏洞",
        "action.vuln_audit_tooltip": "审计当前函数的安全漏洞",
        "action.suggest_types_label": "建议类型",
        "action.suggest_types_tooltip": "推断并应用当前函数的类型",
        "action.annotate_label": "注释函数",
        "action.annotate_tooltip": "为当前函数添加注释",
        "action.clean_mcode_label": "清理微码",
        "action.clean_mcode_tooltip": "清理当前函数的微码",
        "action.xref_label": "交叉引用分析",
        "action.xref_tooltip": "对当前函数执行深度交叉引用分析",
        # Binary Ninja-specific action labels & tooltips
        "action.clean_il_label": "清理 IL",
        "action.clean_il_tooltip": "清理当前函数的 IL",
        "action.smart_patch_label": "智能修补",
        "action.smart_patch_tooltip": "用自然语言修改函数行为并应用二进制补丁",
        # General actions (menu)
        "action.open_tools_label": "打开工具面板",
        "action.open_tools_tooltip": "打开 Rikugan 工具面板",
        "action.send_to_bulk_rename_label": "发送到批量重命名",
        "action.send_to_bulk_rename_tooltip": "将函数发送到 Rikugan 批量重命名器",
        # execute_python approval
        "execute_python.approve_header": "批准执行 execute_python？",
        "execute_python.code_info": "Python 代码 - {lines} 行",
        "execute_python.always_allow": "始终允许",
        "execute_python.allowed": "已允许",
        "execute_python.always_allowed": "始终允许",
        "execute_python.denied": "已拒绝",
        # Profile settings
        "profile.denied_tools": "禁用工具",
        "profile.error_title": "错误",
        "profile.name_exists": "配置 '{name}' 已存在。",
        "profile.name_required": "名称不能为空",
        "profile.description_required": "描述不能为空——它帮助 AI 代理遵循你的约束",
        # Thinking phrases (animated indicator)
        "thinking.analyzing_structure": "分析二进制结构...",
        "thinking.examining_flow": "检查控制流...",
        "thinking.tracing_xrefs": "追踪交叉引用...",
        "thinking.inspecting_disassembly": "检查反汇编代码...",
        "reading_signatures": "读取函数签名...",
        "correlating_refs": "关联数据引用...",
        "mapping_call_graph": "映射调用图...",
        "evaluating_types": "评估类型模式...",
        "scanning_strings": "扫描字符串引用...",
        "deobfuscating_logic": "去混淆逻辑...",
        "checking_imports": "检查导入表...",
        "inferring_vars": "推断变量类型...",
        "analyzing_stack": "分析栈布局...",
        "tracing_data_flow": "追踪数据流...",
        "examining_vtables": "检查虚函数表引用...",
        "decoding_values": "解码编码值...",
        # Bulk renamer widget
        "renamer.filter_placeholder": "按名称或地址过滤...",
        "renamer.filter_all": "全部函数",
        "renamer.filter_auto_named": "仅自动命名",
        "renamer.filter_user_renamed": "用户重命名",
        "renamer.filter_imports": "导入函数",
        "renamer.selection_count": "{n} / {total} 已选中",
        "renamer.header_checkbox": "",
        "renamer.header_address": "地址",
        "renamer.header_current_name": "当前名称",
        "renamer.header_length": "长度",
        "renamer.header_new_name": "新名称",
        "renamer.header_status": "状态",
        "renamer.mode_label": "模式：",
        "renamer.mode_quick": "快速",
        "renamer.mode_deep": "深度",
        "renamer.batch_label": "批次：",
        "renamer.batch_tooltip": "快速模式：每次 LLM 请求处理的函数数。深度模式：忽略（每个函数一个代理）。",
        "renamer.jobs_label": "任务：",
        "renamer.jobs_tooltip": "同时运行的最大并行代理/请求数",
        "renamer.btn_start": "开始",
        "renamer.btn_stop": "停止",
        "renamer.btn_pause": "暂停",
        "renamer.btn_resume": "恢复",
        "renamer.btn_undo_all": "全部撤销",
        "renamer.progress_label": "{n} / {total}",
        "renamer.subagents_count": "\u2022 {n} 个代理",
        "renamer.batch_count": "\u2022 {n} 批",
        # Agent tree widget
        "agent_tree.btn_kill_selected": "终止选中",
        "agent_tree.btn_clean": "清理",
        "agent_tree.clean_tooltip": "移除选中的已完成代理（或未选中时移除所有已完成代理）",
        "agent_tree.filter_all": "全部代理",
        "agent_tree.filter_general": "通用",
        "agent_tree.filter_bulk_rename": "批量重命名",
        "agent_tree.status_label": "{n} 运行中 / {m} 已完成",
        "agent_tree.tree_header_name": "名称",
        "agent_tree.tree_header_type": "类型",
        "agent_tree.tree_header_status": "状态",
        "agent_tree.tree_header_turns": "轮数",
        "agent_tree.tree_header_time": "耗时",
        "agent_tree.preview_placeholder": "选择代理以预览其输出...",
        "agent_tree.no_output_yet": "(暂无输出)",
        # Context bar labels
        "context.addr_label": "地址：",
        "context.func_label": "函数：",
        "context.model_label": "模型：",
        "context.tokens_label": "Token：",
        # Message widgets
        "message.high_relevance": "高相关性",
        # Mutation log tooltips
        "mutation.reversible_tooltip": "可撤销",
        "mutation.not_reversible_tooltip": "不可撤销",
        # Tool widgets
        "tool.result_header": "结果：",
        "tool.tools_called_label": "{n} 个工具已调用",
        # Chat view save approval options
        "chat.save_all": "全部保存",
        "chat.discard_all": "全部丢弃",
        # Session controller tab labels
        "session.new_chat": "新聊天",
        # Panel core action buttons & dialogs
        "panel.btn_send": "发送",
        "panel.btn_stop": "停止",
        "panel.btn_new": "新建",
        "panel.btn_export": "导出",
        "panel.btn_settings": "设置",
        "panel.btn_mutations": "变更日志",
        "panel.export_title": "六眼 — 加密 API 密钥",
        "panel.decrypt_prompt": "输入密码以解密 API 密钥：",
        "panel.decrypt_placeholder": "密码",
        "panel.wrong_password_title": "密码错误",
        "panel.wrong_password_message": "密码不正确，请重试。",
        "panel.export_options_title": "导出选项",
        "panel.export_include_subagents": "包含代理日志（{n} 次代理运行）",
        "panel.export_chat_title": "导出聊天记录",
        "panel.new_chat_dialog_title": "新聊天",
        "panel.new_chat_dialog_message": "开始新聊天？当前对话将被保存。",
        "panel.context_usage": "上下文使用：{pct}%",
        "panel.yes_button": "是",
        "panel.yes_clear_context": "是，清除上下文（已用 {pct}%）",
        "panel.no_button": "否",
        "panel.subagent_status": "代理「{name}」{status}",
        "panel.subagent_completed": "[代理「{name}」已完成（{turns} 轮，{elapsed}s）]",
        "panel.input_placeholder_thinking": "六眼正在思考... 按 Enter（或排队）以发送后续消息。",
        # Settings dialog additional strings
        "settings.add_provider_name_placeholder": "例如 minimax、deepseek、local-vllm",
        "settings.oauth_checkbox": "使用 Claude Code OAuth（macOS 钥匙串）",
        "settings.oauth_tooltip": "从 macOS 钥匙串自动加载 Claude Code OAuth 令牌。\n需要接受 Anthropic 的凭据使用策略。",
        "settings.custom_endpoint_placeholder": "自定义端点 URL（可选）",
        "settings.api_base_form_label": "API 地址：",
        "settings.model_form_label": "模型：",
        "settings.exploration_turns_tooltip": "代理在探索阶段花费的最大轮数，之后强制转换（或报告错误）。",
        "settings.normal_turns_tooltip": "代理在正常模式下花费的最大轮数，之后停止。",
        "settings.api_retries_tooltip": "API 返回速率限制或临时错误时的重试次数。",
        "settings.silent_retry_tooltip": "启用后，速率限制重试显示微妙的文本指示器而非红色错误消息。",
        "settings.preserve_context_tooltip": "禁用工具结果截断和消息修剪。在深度逆向工程会话中启用，丢失反编译上下文比更高的 Token 成本更糟糕。",
        "settings.encrypt_keys_tooltip1": "使用密码加密所有存储的 API 密钥。\n每次六眼启动时都必须输入此密码。",
        "settings.encrypt_keys_tooltip2": "需要安装 'cryptography' 包（pip install cryptography）。",
        "settings.lang_english": "English",
        "settings.lang_chinese": "中文",
        "settings.api_key_placeholder_oauth": "sk-... 或留空以使用 OAuth 自动检测",
        "settings.api_key_placeholder_local": "本地 Ollama 不需要密钥",
        "settings.api_key_placeholder_endpoint": "端点的 API 密钥",
        "settings.api_key_placeholder_generic": "API 密钥",
        "settings.password_placeholder": "密码",
        "settings.confirm_password_placeholder": "确认密码",
    },
}

# Thinking phrase keys in order — used by the animated indicator
_THINKING_KEYS = [
    "thinking.analyzing_structure",
    "thinking.examining_flow",
    "thinking.tracing_xrefs",
    "thinking.inspecting_disassembly",
    "reading_signatures",
    "correlating_refs",
    "mapping_call_graph",
    "evaluating_types",
    "scanning_strings",
    "deobfuscating_logic",
    "checking_imports",
    "inferring_vars",
    "analyzing_stack",
    "tracing_data_flow",
    "examining_vtables",
    "decoding_values",
]


def set_language(language: str) -> None:
    """Set the current UI language.

    Args:
        language: Language code ("en" or "zh"). Defaults to "en" if unknown.
    """
    # No global state to update — translations are looked up on demand.
    pass


def t(key: str, **kwargs) -> str:
    """Translate a string key to the current language.

    Args:
        key: Translation key (e.g., "settings.provider_group").
        **kwargs: Format arguments for string interpolation.

    Returns:
        Translated string, falling back to English then the key itself.
    """
    lang = "en"  # Always default to English as fallback
    
    # Try to detect current language from config if available
    try:
        from ..core.config import RikuganConfig
        cfg = RikuganConfig.load_or_create()
        lang = cfg.language if cfg.language in _TRANSLATIONS else "en"
    except Exception:
        pass
    
    lang_translations = _TRANSLATIONS.get(lang, _TRANSLATIONS["en"])
    
    # Look up the translation
    value = lang_translations.get(key)
    if value is None:
        # Fall back to English
        en_value = _TRANSLATIONS["en"].get(key)
        if en_value is not None:
            value = en_value
        else:
            # Return the key itself as last resort
            return key
    
    # Apply format arguments
    if kwargs:
        try:
            value = value.format(**kwargs)
        except (IndexError, KeyError, AttributeError):
            pass
    
    return value


def is_chinese() -> bool:
    """Check if the current language is Chinese.

    Returns:
        True if the current language is Simplified Chinese.
    """
    try:
        from ..core.config import RikuganConfig
        cfg = RikuganConfig.load_or_create()
        return cfg.language == "zh"
    except Exception:
        return False


def get_thinking_phrases() -> list[str]:
    """Return the list of thinking phrase strings for the current language.

    Returns:
        List of 16 thinking phrases in the current language.
    """
    result = []
    for key in _THINKING_KEYS:
        result.append(t(key))
    return result
