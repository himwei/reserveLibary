import json
import os


def sort_json_by_devName(json_file_path):
    """
    按照devName属性对JSON文件中的对象数组进行升序排序，并将排序后的结果另存为新文件
    :param json_file_path: JSON文件的路径
    """
    file_name, file_extension = os.path.splitext(json_file_path)
    new_file_path = file_name + "_sorted_rev" + file_extension

    try:
        with open(json_file_path, 'r',encoding='utf-8') as file:
            data = json.load(file)

        sorted_data = sorted(data, key=lambda x: x["devName"], reverse=True)

        with open(new_file_path, 'w',encoding='utf-8') as file:
            json.dump(sorted_data, file, indent=4, ensure_ascii=False)

        return sorted_data
    except FileNotFoundError:
        print(f"文件 {json_file_path} 不存在，请检查文件路径是否正确。")
        return []
    except json.JSONDecodeError:
        print(f"文件 {json_file_path} 中的JSON数据格式有误，请检查数据内容。")
        return []


# 示例用法，根据实际情况修改此处的JSON文件路径
json_file_path = "2th_round_reserve_one_seat_clear.json"
sorted_result = sort_json_by_devName(json_file_path)
if sorted_result:
    print(f"排序后的结果已成功保存到 {json_file_path.split('.')[0]}_sorted.json 文件中。")