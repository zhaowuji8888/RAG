"""
导入入口服务模块，负责识别输入文件类型并初始化导入状态。
"""
from pathlib import Path

from app.shared.runtime.logger import logger, step_log


@step_log("resolve_input_file")
def resolve_input_file(state: dict) -> dict:
    """
    识别导入文件类型并初始化后续节点所需的状态字段。

    Args:
        state: 导入图当前状态，需至少包含 `local_file_path`。

    Returns:
        dict: 补充了文件路径、文件标题及开关字段后的最新状态。
    """
    local_file_path = state.get("local_file_path")
    if not local_file_path:
        logger.warning("节点:node_entry,获取文件输入地址,发现地址为空!直接跳转到END节点")
        return state

    # 识别 Markdown / PDF 两类主流程输入，并打开对应处理开关。
    if local_file_path.endswith(".md"):
        state["md_path"] = local_file_path
        state["is_md_read_enabled"] = True
        state["is_pdf_read_enabled"] = False
    elif local_file_path.endswith(".pdf"):
        state["pdf_path"] = local_file_path
        state["is_pdf_read_enabled"] = True
        state["is_md_read_enabled"] = False
    else:
        logger.warning(f"虽然local_file_path有值{local_file_path},不是md或者pdf类型,所以无法识别,直接跳转到END节点!")
        return state

    state["file_title"] = Path(local_file_path).stem
    return state
