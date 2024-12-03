def read_user_txt(knox_id):
    result = {}
    with open('D:/Tool/Test/user.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            items = line.split('\t')
            if items[0].strip() == knox_id.strip():
                result['knox_id'] = items[0].strip()
                result['start'] = items[1].strip()
                result['end'] = items[2].strip()
    return result
