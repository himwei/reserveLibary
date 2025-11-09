import json
import os
from pathlib import Path

def sort_json_by_devName(json_file_path):
    """
    按照 devName 属性对 JSON 文件中的对象数组进行降序排序（reverse=True），
    并将排序后的结果另存为新文件（文件名后加 _sorted_rev）。
    :param json_file_path: JSON 文件的路径
    :return: 排序后的数据列表，若出错则返回空列表
    """
    file_name, file_extension = os.path.splitext(json_file_path)
    new_file_path = file_name + "_sorted_rev" + file_extension

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 确保 data 是一个列表
        if not isinstance(data, list):
            print(f"警告：{json_file_path} 的顶层结构不是数组，跳过排序。")
            return []

        sorted_data = sorted(data, key=lambda x: x.get("devName", ""), reverse=True)

        with open(new_file_path, 'w', encoding='utf-8') as file:
            json.dump(sorted_data, file, indent=4, ensure_ascii=False)

        print(f"✅ 已处理: {json_file_path} → {new_file_path}")
        return sorted_data

    except FileNotFoundError:
        print(f"❌ 文件 {json_file_path} 不存在，请检查路径。")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式错误（{json_file_path}）: {e}")
        return []
    except KeyError as e:
        print(f"❌ 某个对象缺少 'devName' 字段（{json_file_path}）: {e}")
        return []
    except Exception as e:
        print(f"❌ 处理 {json_file_path} 时发生未知错误: {e}")
        return []


def main():
    # 获取当前目录
    current_dir = Path(".")
    # 查找所有以 _clear.json 结尾的文件
    clear_files = list(current_dir.glob("*_clear.json"))

    if not clear_files:
        print("⚠️  当前目录下没有找到以 '_clear.json' 结尾的文件。")
        return

    print(f"🔍 找到 {len(clear_files)} 个待处理文件：")
    for f in clear_files:
        print(f"  - {f}")

    print("\n🔄 开始处理...")
    for file_path in clear_files:
        sort_json_by_devName(str(file_path))

    print("\n✅ 所有文件处理完成！")


if __name__ == "__main__":
    main()