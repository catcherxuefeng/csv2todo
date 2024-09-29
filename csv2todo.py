import csv

'''
使用说明 将csv 转为 todo.txt格式
python3 csv2todo.py todo.csv todo.txt

csv：

任务详情,内容标签,优先级,创建日期,项目标签,截止日期,完成时间,已完成
洗牙,生活,,2024/9/29,,,,
汽车保养,生活,,2024/9/29,汽车,,,
日报,工作,A,2024/9/29,,2024/9/29,2024/9/29,x

结果：

洗牙 @生活 created:2024-9-29
汽车保养 @生活 +汽车 created:2024-9-29
x (A) 日报 @工作 created:2024-9-29 due:2024-9-29 completed:2024-9-29

'''

def format_date(date):
    return date.replace('/', '-')

def convert_csv_to_todo(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过标题行
        
        with open(output_file, mode='w', encoding='utf-8') as outfile:
            for row in reader:
                task, context, priority, created, project, due, completed, is_done = row
                
                todo_line = ""
                
                # 如果任务已完成，在前面加x
                if is_done.strip() == 'x':
                    todo_line += "x "
                
                # 添加优先级
                if priority.strip():
                    todo_line += f"({priority.strip()}) "
                
                # 添加任务详情
                todo_line += f"{task.strip()} "
                
                # 添加内容标签
                if context.strip():
                    todo_line += f"@{context.strip()} "
                
                # 添加项目标签
                if project.strip():
                    todo_line += f"+{project.strip()} "
                
                # 添加创建日期
                if created.strip():
                    formatted_created = format_date(created.strip())
                    todo_line += f"created:{formatted_created} "
                
                # 添加截止日期
                if due.strip():
                    formatted_due = format_date(due.strip())
                    todo_line += f"due:{formatted_due} "
                
                # 添加完成时间
                if completed.strip():
                    formatted_completed = format_date(completed.strip())
                    todo_line += f"completed:{formatted_completed}"
                
                # 去除末尾多余的空格
                todo_line = todo_line.rstrip()
                
                # 写入输出文件
                outfile.write(todo_line + '\n')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_csv_to_todo.py <input.csv> <output.txt>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_csv_to_todo(input_file, output_file)
    print(f"Conversion complete. Output saved to {output_file}")