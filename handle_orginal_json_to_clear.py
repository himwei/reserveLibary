import os
import json

def process_json_files(keep_keys):
    """
    处理当前目录下的所有JSON文件，保留指定属性，处理后文件以原文件名+_clear.json保存
    """
    # 获取当前目录（脚本所在目录，与待处理文件同级）
    current_dir = os.path.dirname(os.path.abspath(__file__)) if __file__ else os.getcwd()
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_dir):
        # 只处理JSON文件，且跳过已处理过的_clear文件
        if not filename.endswith(".json") or "_clear.json" in filename:
            continue
        
        file_path = os.path.join(current_dir, filename)
        print(f"开始处理文件: {filename}")
        
        try:
            # 读取JSON文件
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"  ❌ JSON解析错误: {e}，跳过该文件")
                    continue
            
            # 检查是否为JSON数组
            if not isinstance(data, list):
                print(f"  ❌ 文件内容不是JSON数组，跳过该文件")
                continue
            
            # 处理每个对象，保留指定属性
            processed_data = []
            for item in data:
                if isinstance(item, dict):
                    # 只保留指定键，不存在的键会被过滤（不设为None）
                    processed_item = {key: item[key] for key in keep_keys if key in item}
                    processed_data.append(processed_item)
                else:
                    print(f"  ⚠️ 数组中存在非对象元素，已跳过")
            
            # 生成输出文件名（原文件名+_clear.json）
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}_clear{ext}"
            output_path = os.path.join(current_dir, output_filename)
            
            # 写入处理后的JSON
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, ensure_ascii=False, indent=4)
            
            print(f"  ✅ 处理完成，保存为: {output_filename}")
            
        except Exception as e:
            print(f"  ❌ 处理文件时出错: {e}，跳过该文件")


if __name__ == "__main__":
    # 需要保留的属性列表（与示例一致）
    KEEP_KEYS = [
        "devId", "devSn", "devName", "kindId", "kindName",
        "roomId", "roomName", "labName", "labId"
    ]
    
    # 执行处理
    process_json_files(KEEP_KEYS)
    print("所有文件处理完毕！")