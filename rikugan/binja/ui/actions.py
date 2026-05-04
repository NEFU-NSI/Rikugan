"""Prompt-generating command handlers for Binary Ninja UI actions."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from ...ui.action_handlers import (
    handle_annotate,
    handle_clean,
    handle_deobfuscate,
    handle_explain,
    handle_rename,
    handle_send_to,
    handle_suggest_types,
    handle_vuln_audit,
    handle_xref_analysis,
)
from ...ui.i18n import t


def build_context(
    bv: Any,
    ea: int,
    get_function_at: Callable[[Any, int], Any],
    get_function_name: Callable[[Any], str],
) -> dict[str, Any]:
    ctx: dict[str, Any] = {
        "ea": int(ea),
        "func_ea": None,
        "func_name": None,
        "selected_text": "",
    }
    func = get_function_at(bv, ea)
    if func is not None:
        ctx["func_ea"] = int(getattr(func, "start", ea))
        ctx["func_name"] = get_function_name(func)
    return ctx


# Binary Ninja uses "IL" terminology
def handle_deobfuscate_bn(ctx: dict[str, Any]) -> str:
    return handle_deobfuscate(ctx, optimizer_term="IL")


def handle_clean_il(ctx: dict[str, Any]) -> str:
    return handle_clean(ctx, ir_term="IL")


def handle_smart_patch(ctx: dict[str, Any]) -> str:
    name = ctx["func_name"] or f"sub_{ctx['ea']:x}"
    ea = ctx["func_ea"] or ctx["ea"]
    return _t(
        "action.smart_patch",
        _name=name,
        _ea=ea,
        _fallback=f"/smart-patch-binja Patch function {name} at 0x{ea:x}.\nDesired behavior: ",
    )


def _t(key: str, **kwargs) -> str:
    """Translate a key using the current UI language."""
    try:
        from .i18n import t as _t_func
        return _t_func(key, **kwargs)
    except Exception:
        return kwargs.get("_fallback", key)


ACTION_DEFS: tuple[tuple[str, str, Callable[[dict[str, Any]], str], bool], ...] = (
    (
        t("action.send_to_label"),
        t("action.send_to_tooltip"),
        handle_send_to,
        False,
    ),
    (t("action.explain_label"), t("action.explain_tooltip"), handle_explain, True),
    (
        t("action.rename_label"),
        t("action.rename_tooltip"),
        handle_rename,
        True,
    ),
    (
        t("action.deobfuscate_label"),
        t("action.deobfuscate_tooltip"),
        handle_deobfuscate_bn,
        True,
    ),
    (
        t("action.vuln_audit_label"),
        t("action.vuln_audit_tooltip"),
        handle_vuln_audit,
        True,
    ),
    (
        t("action.suggest_types_label"),
        t("action.suggest_types_tooltip"),
        handle_suggest_types,
        True,
    ),
    (
        t("action.annotate_label"),
        t("action.annotate_tooltip"),
        handle_annotate,
        True,
    ),
    (t("action.clean_il_label"), t("action.clean_il_tooltip"), handle_clean_il, True),
    (
        t("action.xref_label"),
        t("action.xref_tooltip"),
        handle_xref_analysis,
        True,
    ),
    (
        t("action.smart_patch_label"),
        t("action.smart_patch_tooltip"),
        handle_smart_patch,
        False,
    ),
)
